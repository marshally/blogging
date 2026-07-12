# Availability Math

## Definitions

Let:

- `A` = availability, expressed as a probability between 0 and 1.
- `Q = 1 - A` = unavailability or failure probability.
- `A_i` = availability of component or subsystem `i`.
- `Q_i = 1 - A_i` = unavailability of component or subsystem `i`.

Basic time-based availability:

```text
A = uptime / (uptime + downtime)
```

For request-based services, availability is often better defined as successfully
processed valid requests divided by total valid requests. The unit and measurement
window must be defined before combining numbers.

## Rule 1: ALL (series dependencies)

If an operation succeeds only when every required component succeeds, the system is a
series system.

Under statistical independence:

```text
A_all = product(A_i)
```

Example:

```text
0.9999 x 0.9999 x 0.9995 = 0.999300109995
                              = 99.9300109995%
```

Exact statement without assuming independence:

```text
A_all = P(component 1 up AND component 2 up AND ...)
A_all <= min(A_i)
```

The product requires independence (or a specified joint distribution). If only the
marginal availability figures are known, a conservative lower bound is:

```text
A_all >= max(0, 1 - sum(Q_i))
```

This is the complement of the union bound. For high availabilities, the independent
product and `1 - sum(Q_i)` are numerically close, but they mean different things.

## Rule 2: ANY (parallel redundancy)

If an operation succeeds when any one of several interchangeable alternatives works,
the system fails only when all alternatives fail.

Under statistical independence:

```text
Q_all_fail = product(Q_i)
A_any      = 1 - product(Q_i)
```

For two identical alternatives with availability `A`:

```text
A_any = 1 - (1 - A)^2
```

For two independent four-nines alternatives:

```text
A     = 0.9999
Q     = 0.0001
A_any = 1 - (0.0001)^2
      = 0.99999999
      = 99.999999%
```

This is the origin of the article's mnemonic:

> **ALL multiplies availability. ANY multiplies unavailability.**

The full `ANY` computation always subtracts the product from one.

## Correlation: why redundancy gains disappear

Independence is the load-bearing assumption in the simple parallel formula.

- If two Regions fail independently, multiply their failure probabilities.
- If the two deployments fail together because of shared code, deployment tooling,
  credentials, data, control planes, routing, or operator action, the joint failure
  probability can be much higher.
- With perfect positive correlation, two 99.99% copies can still provide only 99.99%.

The architecture must make `either can work` operationally true. Two deployed copies
are not automatically two independent alternatives.

## Public SLAs are not clean probability inputs

Treat SLA composition as a planning model, not literal contract algebra:

1. An SLA is a service commitment with definitions, exclusions, and remedies, not a
   direct forecast of future outages.
2. Actual service availability often exceeds the public SLA.
3. Different AWS SLAs use different units. EC2, ELB, and RDS largely use unavailable
   minutes; S3 uses average request error rates over five-minute intervals.
4. Monthly commitments do not automatically become annual probability distributions.
5. AWS applies its service SLAs separately. It does not sign the composite percentage
   calculated by a customer.
6. The customer's own software, deployment, capacity, recovery, and measurement rules
   remain part of customer-visible availability.

AWS's own availability whitepaper calls the product of dependency SLAs a theoretical
maximum/rough order-of-magnitude calculation and notes that workloads often outperform
it because dependencies exceed their public commitments.

## Approximate annual downtime table

Using a 365-day year (525,600 minutes) solely for intuition:

| Availability | Approximate downtime/year |
|---:|---:|
| 99.5% | 43 h 48 m |
| 99.9% | 8 h 45 m 36 s |
| 99.95% | 4 h 22 m 48 s |
| 99.99% | 52 m 33.6 s |
| 99.999% | 5 m 15.36 s |
| 99.9999% | 31.536 s |
| 99.99999% | 3.1536 s |
| 99.999999% | 0.31536 s |

Do not present this table as AWS's credit calculation. AWS evaluates each SLA over its
specified monthly billing cycle and its own definition of unavailability.

## Five-minute failover sanity check

One five-minute service interruption in an otherwise perfect 365-day year yields:

```text
A = 1 - (5 / 525600)
  = 99.9990487%
```

Therefore an architecture claiming the theoretical eight nines from two Regions cannot
tolerate even a single ordinary failover delay. Detection, routing, and data readiness
must appear in the model.
