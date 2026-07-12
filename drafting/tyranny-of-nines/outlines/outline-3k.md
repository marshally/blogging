# Outline: The Tyranny of Nines (~3,000 words)

Public essay. A remembered staff-plus teaching moment carries a practical probability
lesson. The outline repeats one rule through story, diagram, equation, worked example,
and conclusion:

> **ALL multiplies availability. ANY multiplies unavailability.**

## 1. I had a spreadsheet (~300 words)

Open at Twilio while Marshall and Sean Kilgore were building platform tools. Marshall
is trying to construct an SLA from the inside out: expected deployment disruption,
maintenance, database changes, incidents, recovery time, and other team-controlled
downtime. The work is careful and intuitively reasonable.

Do not invent the immediate setting or business trigger. Establish Sean in one clause:
software architect/staff-plus engineer; one of the people who taught Marshall how to
lead large teams from an IC chair.

Narrative turn: Sean changes the boundary. Paraphrase the remembered challenge rather
than fabricate a quote: suppose the application and team were perfect; what availability
could the infrastructure underneath them support?

Loaded guns:

- `perfect` returns when application reliability is added back to the model.
- `inside out` becomes `outside in` in the conclusion.
- The spreadsheet survives, but moves to the end of the calculation.

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

## 3. What has to work? (~550 words)

Put the real service inventory on the page: ALB, EC2, ElastiCache, RDS, S3. Then reject
the naive inventory multiplication. Membership in the architecture does not make a
service a hard dependency of every request.

Draw candidate paths:

```text
Database operation: ALB -> EC2 -> RDS
Cache hit:          ALB -> EC2 -> ElastiCache
Object operation:  ALB -> EC2 -> S3 [and perhaps RDS]
Cache miss:         ALB -> EC2 -> ElastiCache -> RDS
```

The exact anchor path remains open pending Marshall's choice. Introduce hard versus soft
dependencies. A required synchronous dependency belongs in the chain. A dependency the
service can bypass, defer, cache, queue, or degrade around may not.

First canonical statement:

> **If every component must work, multiply their availability.**

Equation:

```text
A(ALL) = A1 x A2 x ... x An
```

Use the current Multi-AZ ALB + Region-Level EC2 + Multi-AZ RDS example:

```text
99.99% x 99.99% x 99.95% = 99.930011%
```

Each component looks better than the system. The arrows, not the boxes, create the
tyranny.

## 4. Why did the vendor numbers eat my budget? (~400 words)

Show a compact current-SLA table, carefully labeled as a present-day worked example,
not the historical Twilio contract:

- EC2 Region-Level, qualifying Multi-AZ deployment: 99.99%
- Multi-AZ ALB: 99.99%
- Multi-AZ ElastiCache for Redis OSS/Valkey: 99.99%
- Multi-AZ RDS: 99.95%
- S3 Standard: 99.9%

If all five were truly required in series, the theoretical product would be about
99.820098%, or roughly 15 hours 46 minutes of expected annual unavailability. This is
an intentionally suspicious result: it demonstrates why request paths matter and why
public SLA multiplication is a rough engineering model, not a new contract AWS signed.

Return to Marshall's spreadsheet. It was not wrong; it started too late. Supplier and
architecture risk consume the budget before deployments, bugs, and recovery do.

Repeat in a different form:

> Every hard dependency is another chance for the request to fail.

## 5. What happens when the box is the Region? (~500 words)

Move through fault-domain boundaries:

```text
instance -> Availability Zone -> Region
```

EC2's 99.99% Region-Level SLA requires instances concurrently deployed across two or
more AZs in one Region. Multi-AZ is therefore already part of obtaining the four-nines
compute commitment. But every service in the example can still share the Regional
boundary.

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

## 6. Did we really get eight nines? (~450 words)

Complicate the clean model once it has landed. The eight-nines result assumes:

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

## 7. So how should I calculate my SLA? (~300 words)

Give the reader a reusable procedure:

1. Define the customer-visible operation and how availability is measured.
2. Draw only its runtime dependencies.
3. Mark each relationship `ALL` or `ANY`.
4. Label each component with the correct SLA for its actual configuration.
5. Calculate serial and parallel groups from the inside out.
6. Challenge independence and identify shared failure modes.
7. Add routing, replication, application, deployment, detection, and recovery behavior.
8. Set the customer SLA below the modeled SLO with an explicit safety margin—or accept
   that the company is self-insuring the difference.

Repeat as a decision rule:

> Need all of them? Multiply success. Need any of them? Multiply failure and subtract
> from one.

## 8. What did Sean actually teach me? (~200 words)

Return to leadership from the IC chair. Sean did not make the original spreadsheet more
precise. He reframed the system so the spreadsheet answered the right question. Its
internal downtime estimates now spend what remains after the dependency graph and
architecture establish the boundary.

Final repetition should be short enough to remember:

> **ALL multiplies availability. ANY multiplies unavailability.**

Kicker territory (do not lock prose yet): the nines were never hiding in the rows of
the spreadsheet; they were hiding in the arrows between boxes. Circle back to `inside
out` versus `outside in` and the tyranny named in the title.

**Estimated total: ~3,050 words.**
