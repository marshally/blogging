# Decision Log

Settled choices from the design conversation. Do not relitigate without new
information.

## D1. Narrative frame: Sean changes the question

The post is a partially remembered teaching story in the tradition of *The Goal* and
*The Phoenix Project*. Marshall begins by calculating an SLA from downtime his own team
expects to cause. Sean Kilgore changes the boundary of the analysis: even a perfect
application still depends on infrastructure with its own availability commitments.

Sean is a real software architect/staff-plus engineer who taught Marshall a great deal
about leading large teams from the IC chair while they built platform tools at Twilio.
The staff-plus lesson is secondary but real: architectural leadership often consists
of asking the question that reveals everyone has been solving the wrong problem.

## D2. No invented transcript

Marshall does not remember exact quotations from the conversation. The current house
style also requires personal anecdotes to be reported without embellishment. Therefore:

- Do not put polished invented sentences in Sean's mouth.
- Do not invent a conference room, whiteboard, meeting, deadline, customer, gesture,
  reaction, or chronology.
- Dialogue may be described in indirect speech or clearly introduced as the shape of
  the remembered lesson, never as a verbatim transcript.
- The piece should disclose that memory has compressed the exchange and that the exact
  words are not recoverable.

## D3. The central mnemonic

The most important lesson is:

> **For components that must all work, multiply their availability. For redundant
> systems where either can work, multiply their unavailability.**

The computationally complete second half adds `then subtract from one`. The post should
state the lesson several times in different forms: plain English, equations, an
architecture diagram, worked numbers, and the conclusion.

Canonical compact version:

> **ALL multiplies availability. ANY multiplies unavailability.**

## D4. Use the real service inventory, not a serverless substitute

The Twilio platform used EC2, Application Load Balancer, ElastiCache, RDS, and S3. Use
those services in the worked example. Do not imply that every service was a hard
dependency of every request. Draw customer-visible request paths first; calculate only
the services that a particular operation requires.

*Amended by D14 (2026-07-12): ElastiCache is dropped from the worked example.*

## D5. Separate historical truth from the current worked example

The remembered lesson happened at Twilio. The numerical example uses AWS's currently
published SLAs. Unless historical architecture and contract details are confirmed, do
not claim that the current figures or assumed Multi-AZ configurations describe the
Twilio system at that time.

## D6. The Region is the second boundary

EC2 currently offers a 99.99% Region-Level SLA when the qualifying compute deployment
spans at least two Availability Zones. A single-Region architecture cannot be designed
to remain available through loss of that Region. If the customer promise must survive
a Regional failure, a second Region is necessary.

Multi-Region is necessary for that failure mode, not sufficient for the final SLA. The
full regional stack, routing, data replication, capacity, failover behavior, shared
dependencies, software, and operations remain in the calculation.

## D7. Four nines in parallel is the memorable inversion

For two independent, instantly interchangeable regional deployments, each available
at 99.99%:

```text
1 - (1 - 0.9999)^2 = 0.99999999 = 99.999999%
```

The idealized model turns two four-nines alternatives into eight nines. Use this to
show that the same percentages behave differently when topology changes from `ALL` to
`ANY`. Immediately afterward, examine the independence and perfect-failover assumptions.

## D8. SLA is a contract, not a physical maximum

Avoid saying that a public SLA is the maximum availability a service can achieve. It
is a contractual service commitment, typically with credits as the remedy, and actual
performance may be better. Preferred claim:

> The public SLAs bound the customer promise that the supplier contracts directly
> support. Promising more means engineering redundancy, accepting the uncovered risk,
> or both.

## D9. Repetition is deliberate

Repeating the ALL/ANY lesson is a pedagogical feature. Each repetition must add a new
representation or consequence rather than merely restating the same paragraph.

## D10. The teaching story is the frame; no extended metaphor

Resolves the open metaphor question. This piece uses no borrowed extended metaphor: the remembered teaching story (D1) carries the structure, and the mathematics is the star. The register is earnest — humor only where it sharpens the math, no irreverence quota. Not every piece requires an extended metaphor; `/docs/writing-style.md` now reflects this.

## D11. The anchor operation is the database request

The worked example anchors on the database operation:

```text
client -> ALB -> EC2 -> RDS
```

Use the same architecture in every calculation so the reader follows one system throughout: the serial product, the budget conversion, and the per-Region stack that gets duplicated in the multi-Region sections. The cache and S3 paths appear only as contrast when introducing hard versus soft dependencies; they are not the anchor, and their open historical questions stay open.

## D12. Let the reader make the naive multiplication first

Present the full service inventory with its SLA numbers and invite the seductive mistake — multiply everything — before request-path analysis breaks it. The naive five-service product (~99.82%) is the hook that motivates hard-versus-soft dependency analysis, not a callback after the lesson has been taught.

## D13. The price of the next nine is brainpower, not hosting bills

Multi-Region is much harder than 2x from an engineering and operations perspective, and a properly autoscaled multi-Region deployment does not cost 2x in hosting. Never use `hot standby ≈ 2x workload cost` as the punchline: engineer brainpower is generally much more expensive than hosting bills. The cost beat presents a step function — crossing a fault-domain boundary buys new classes of engineering and operational obligation, not a second copy of the same bill.

Framing (settled): the beat combines two devices — quasi-math compression that states and then corrects the naive expectation (`Cost(next nine) = 2 x hosting` becomes `ΔEngineering + ΔOperations + ΔNew failure modes`), followed by the prose punchline `you don't buy a second copy; you buy a distributed-systems problem`.

## D14. Drop ElastiCache from the worked example

Amends D4 with Marshall's authorization. The historical cache was Redis ElastiCache, Multi-AZ, but no anchor calculation needs it: the database operation is the anchor (D11) and S3 carries the soft-dependency arithmetic (D15). The worked example uses four services — ALB, EC2, RDS, S3. The draft may spend one honest clause noting the real platform also ran a Multi-AZ Redis cache, omitted because it is not load-bearing.

## D15. S3 enters as a degraded-mode dependency, with the arithmetic shown

After the hard-path math and budget conversion, add S3 to the operation and show the degraded-mode arithmetic. Hard S3 multiplies in: `99.930011% x 99.9% = 99.830081%` (~14 h 53 m theoretical annual downtime, 2.77 nines). A degraded mode that counts as success removes the factor: `A = A(hard chain) x [A(S3) + (1 - A(S3)) x f]`; at `f = 1` the operation returns to 99.930011% (3.16 nines), recovering roughly S3's entire ~8 h 45 m downtime budget.

Exploit the built-in coincidence: the four-service naive inventory product equals the all-four-hard product, so the naive multiplication was correct arithmetic for the wrong question. The repetition form this beat adds (D9): a dependency you can degrade around gives its failure chances back.

## D16. Story anchors: SLO adoption, circa 2020, Multi-AZ but single-Region

Marshall's spreadsheet served the team's first adoption of internal SLOs, in the tradition of the Google SRE book — the piece may say so and link the book's Service Level Objectives chapter. The conversation was probably in 2020; prose hedges as `around 2020`. The platform was Multi-AZ but not multi-Region, which makes the Region-boundary section concrete rather than hypothetical: Multi-AZ was already earning the compute commitment, and the Region was the shared box the platform actually lived in. Precise SLO/SLA targets remain unremembered; keep them out.
