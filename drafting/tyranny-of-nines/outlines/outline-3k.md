# Outline: The Tyranny of Nines (~3,600 words)

Public essay. A remembered staff-plus teaching moment carries a practical probability
lesson. The outline repeats one rule through story, diagram, equation, worked example,
and conclusion:

> **ALL multiplies availability. ANY multiplies unavailability.**

## 1. I had a spreadsheet (~300 words)

Open at Twilio, around 2020 (hedged; D16), while Marshall and Sean Kilgore were building platform tools and the team was adopting internal SLOs for the first time, in the tradition of the Google SRE book. Marshall is trying to construct the target from the inside out: expected deployment disruption, maintenance, database changes, incidents, recovery time, and other team-controlled downtime. The work is careful and intuitively reasonable.

Do not invent the immediate setting or business trigger. Establish Sean in one clause:
software architect/staff-plus engineer; one of the people who taught Marshall how to
lead large teams from an IC chair.

Narrative turn: Sean changes the boundary. Paraphrase the remembered challenge rather
than fabricate a quote: suppose the application and team were perfect; what availability
could the infrastructure underneath them support?

Place the D2 disclosure here, one sentence: the lesson is real, but memory has compressed the exchange and the exact words are not recoverable.

Loaded guns:

- `perfect` returns when application reliability is added back to the model.
- `inside out` becomes `outside in` in the conclusion.
- The spreadsheet survives, but moves to the end of the calculation.
- The spreadsheet's `rows` against the diagram's `arrows`, planting the kicker's arrows-between-boxes image in the opening.

## 2. What exactly are we promising? (~350 words)

Define terms early:

- **Availability:** proportion of valid work successfully served, or proportion of time
  the service meets its defined availability condition.
- **SLO:** the operator's internal target.
- **SLA:** a contractual service commitment, including its measurement rules and remedy.
- **Error/downtime budget:** the amount of unavailability compatible with a target.

State the contractual caveat without derailing the lesson: AWS SLAs are not observed
failure probabilities or physical ceilings. They are the supplier commitments directly
supporting our downstream promise. Actual performance can exceed them; we can promise
more only by adding architecture or accepting risk AWS does not reimburse.

Define availability for one customer operation before drawing architecture. A service
does not have one meaningful composite availability until `available` and the unit of
work are specified.

The definitions are also story: the team was adopting SLOs for the first time, so SLO versus SLA is precisely the distinction Marshall was living inside. Link the Google SRE book's Service Level Objectives chapter here (D16).

## 3. What has to work? (~550 words)

Put the worked example's service inventory on the page with its current SLA numbers, carefully labeled as a present-day model, not the historical Twilio contract. One honest clause may note the real platform also ran a Multi-AZ Redis cache, omitted because nothing in the analysis needs it (D14).

- Multi-AZ ALB: 99.99%
- EC2 Region-Level, qualifying Multi-AZ deployment: 99.99%
- Multi-AZ RDS: 99.95%
- S3 Standard: 99.9%

Invite the seductive mistake before correcting it (D12): the diagram lists four services, so multiply four numbers.

```text
0.9999 x 0.9999 x 0.9995 x 0.999 = 99.830081%
```

Roughly 14 hours 53 minutes of theoretical annual unavailability. Let it sit as the answer for a beat — then break it: the method assumed every box is a hard dependency of every request. Membership in the architecture does not make it so.

Draw candidate paths:

```text
Database operation: ALB -> EC2 -> RDS
Object operation:   ALB -> EC2 -> RDS + S3
```

Introduce hard versus soft dependencies. A required synchronous dependency belongs in the chain. A dependency the service can bypass, defer, cache, queue, or degrade around may not. The object path returns in section 5; the anchor operation for every later calculation is the database request (D11).

First canonical statement:

> **If every component must work, multiply their availability.**

Equation:

```text
A(ALL) = A1 x A2 x ... x An
```

Apply it to the anchor path:

```text
99.99% x 99.99% x 99.95% = 99.930011%
```

Each component looks better than the system. Dismantle the proverb: everyone knows a chain is only as strong as its weakest link. The math is crueler — a chain of components is *weaker* than its weakest link (`A(ALL) <= min(A_i)`, strictly less under independence). The arrows, not the boxes, create the tyranny.

## 4. Why did the vendor numbers eat my budget? (~350 words)

Convert the anchor path's 99.930011% into intuition: roughly 6 hours 8 minutes of theoretical annual unavailability, spent before the team's own software, deployments, and incidents consume anything.

State the model's limits without derailing it: multiplying public SLAs is a rough engineering model, not a new contract AWS signed. AWS applies each SLA separately, the measurement units differ (S3 counts request error rates; RDS counts connection-failure minutes), and actual performance often exceeds the commitment.

Return to Marshall's spreadsheet. It was not wrong; it started too late. Supplier and architecture risk consume the budget before deployments, bugs, and recovery do.

Repeat in a different form:

> Every hard dependency is another chance for the request to fail.

## 5. Do we really need S3 every time? (~300 words)

Bring the object operation back (D15). If S3 is a hard dependency, all four services multiply, and the product is exactly section 3's naive number:

```text
99.930011% x 99.9% = 99.830081%
```

Point at the coincidence deliberately: the naive inventory multiplication was correct arithmetic for the wrong question — it assumed everything is always required.

Now give the application a degraded mode: when S3 is unavailable, the operation still succeeds without the object payload, and the availability definition from section 2 counts that as success. With `f` the probability the degraded path works:

```text
A = 99.930011% x [99.9% + 0.1% x f]

f = 0: 99.830081%  (2.77 nines, ~14 h 53 m/yr)
f = 1: 99.930011%  (3.16 nines, ~6 h 8 m/yr)
```

Full degradation hands back roughly S3's entire ~8 h 45 m annual downtime budget. This is the first escape from the tyranny, and it is architectural, not contractual: demote the dependency instead of shrinking the promise.

Repeat in a new form:

> A dependency you can degrade around gives its failure chances back.

Transition: degrading shortens the `ALL` chain. The other escape is adding alternatives — turning `ALL` into `ANY`.

## 6. What happens when the box is the Region? (~500 words)

Move through fault-domain boundaries:

```text
instance -> Availability Zone -> Region
```

EC2's 99.99% Region-Level SLA requires instances concurrently deployed across two or
more AZs in one Region. Multi-AZ is therefore already part of obtaining the four-nines
compute commitment. But every service in the example can still share the Regional
boundary.

Now a usable fact rather than a hypothetical (D16): the platform itself was Multi-AZ but single-Region. Multi-AZ was already earning the compute commitment; the Region was the shared box the whole platform lived in.

The key architecture claim:

> If the customer SLA must survive loss of the Region, the service must be able to
> operate without that Region.

Draw the second copy:

```text
             +-> Region A -+
customer ----|              |----> successful operation
             +-> Region B -+
```

Now the topology is `ANY`, not `ALL`.

Second canonical statement:

> **If either independent alternative can work, multiply their unavailability, then
> subtract from one.**

```text
A(ANY) = 1 - [(1 - A1) x (1 - A2) x ... x (1 - An)]
```

For two idealized independent four-nines regional compute deployments:

```text
1 - (0.0001 x 0.0001) = 99.999999%
```

Same number on each box; radically different result because the relationship changed.

## 7. Did we really get eight nines? (~500 words)

First make the model honest about what is inside each Region. Section 6's idealization paralleled compute alone; each Region actually contains the whole anchor stack from section 3, which multiplied out to 99.930011%. Parallel the path product, not the best box's SLA:

```text
A(region stack) = 0.999300109995
A(either)       = 1 - (1 - 0.999300109995)^2
                = 99.9999510154%
```

About 15.45 seconds of theoretical annual unavailability — six and a half nines, not eight. A regional stack does not inherit EC2's Region-Level number.

Then complicate the clean model. Even the honest version assumes:

- failures between Regions are independent;
- either Region has sufficient live capacity;
- traffic detects and routes around failure;
- the required data is available and sufficiently current;
- certificates, secrets, configuration, and dependencies exist in both Regions;
- failover is automatic and fast enough;
- deployments and operator actions cannot break both copies together.

Use a concrete budget shock: eight nines permits only about 0.315 seconds of expected
unavailability per year. One five-minute failover event implies only about 99.99905%
annual availability before counting any other failure. The theoretical eight nines are
not a customer promise until the recovery path earns them.

Name correlated failure as the villain: shared code, shared data, shared control planes,
DNS/routing, simultaneous deployment, and human action. Two copies with shared fate are
two copies, not two independent alternatives.

AWS itself warns that an incorrectly built multi-Region architecture can reduce overall
availability. Multi-Region is a topology change plus an operating model, not a checkbox.

## 8. What does the next nine cost? (~250 words)

Name the economic half of the tyranny: availability does not improve along a smooth slope. Crossing a fault-domain boundary (`instance -> Multi-AZ -> multi-Region`) is a step function that buys a qualitatively different system.

Guardrail (D13): do not frame the step as `2x the hosting bill`. A properly autoscaled multi-Region deployment does not double hosting costs — and hosting is the cheap part. The price is paid in engineering and operations: replication semantics and RPO decisions, one-Region-at-a-time deploys, failover drills that must actually be run, capacity audits, an on-call rotation that reasons about two of everything. Engineer brainpower is generally much more expensive than hosting bills.

Close the beat with AWS's own warning: an incorrectly built multi-Region architecture can reduce overall availability — it is possible to pay the full price and receive fewer nines.

Framing (settled, D13): combine the distributed-systems-problem frame with the quasi-math compression. Open with the naive expectation and correct the equation — the house step-by-step quasi-math move:

```text
Cost(next nine) = 2 x hosting            <- the naive expectation
Cost(next nine) = ΔEngineering + ΔOperations + ΔNew failure modes
```

Then land the punch in prose: **you don't buy a second copy; you buy a distributed-systems problem** — a new class of failure modes that did not exist in one Region. The equation states the structure; the sentence makes it memorable. Exact prose not locked.

## 9. So how should I calculate my SLA? (~300 words)

Give the reader a reusable procedure:

1. Define the customer-visible operation and how availability is measured.
2. Draw only its runtime dependencies.
3. Mark each relationship `ALL`, `ANY`, or soft — degradable, with an honest `f`.
4. Label each component with the correct SLA for its actual configuration.
5. Calculate serial and parallel groups from the inside out.
6. Challenge independence and identify shared failure modes.
7. Add routing, replication, application, deployment, detection, and recovery behavior.
8. Set the customer SLA below the modeled SLO with an explicit safety margin—or accept
   that the company is self-insuring the difference.

Repeat as a decision rule:

> Need all of them? Multiply success. Need any of them? Multiply failure and subtract
> from one.

## 10. What did Sean actually teach me? (~200 words)

Return to leadership from the IC chair. Sean did not make the original spreadsheet more
precise. He reframed the system so the spreadsheet answered the right question. Its
internal downtime estimates now spend what remains after the dependency graph and
architecture establish the boundary.

Final repetition should be short enough to remember:

> **ALL multiplies availability. ANY multiplies unavailability.**

Kicker territory (do not lock prose yet): the nines were never hiding in the rows of
the spreadsheet; they were hiding in the arrows between boxes. Circle back to `inside
out` versus `outside in` and the tyranny named in the title.

**Estimated total: ~3,600 words.**
