# Worked Example

All calculations use current public SLA commitments as rough probability inputs. They
are checked arithmetic, not an AWS-backed composite SLA and not a historical claim
about Twilio.

## Assumed component values

```text
Multi-AZ ALB                        0.9999
EC2 Region-Level                    0.9999
Multi-AZ RDS                        0.9995
S3 Standard                         0.9990
```

ElastiCache (historically Redis, Multi-AZ) is dropped from the worked example per D14; nothing in the analysis requires it.

## Candidate operation 1: database request

```text
client -> ALB -> EC2 -> RDS
```

All three must work:

```text
0.9999 x 0.9999 x 0.9995
= 0.999300109995
= 99.9300109995%
```

Approximate theoretical annual unavailability: 367.86 minutes, or about 6 hours 8
minutes.

## Candidate operation 2: object-serving request, S3 hard

```text
client -> ALB -> EC2 -> RDS + S3 (all required)
```

```text
0.9999 x 0.9999 x 0.9995 x 0.999
= 0.998300809885
= 99.8300809885%
```

Approximate theoretical annual unavailability: 893.09 minutes, or about 14 hours 53 minutes. By construction this equals the naive inventory product below: naive multiplication is correct arithmetic only for an operation that hard-requires everything.

## Candidate operation 3: object-serving request with a degraded mode (D15)

Let `f` be the probability the degraded path succeeds when S3 is down, with the degraded response counting as success under the operation's availability definition (see Rule 3 in `availability-math.md`):

```text
A = 0.999300109995 x [0.999 + 0.001 x f]

f = 0:   99.8300809885%  (~14 h 53 m/yr, 2.77 nines)
f = 0.5: 99.8800459940%  (~10 h 30 m/yr, 2.92 nines)
f = 1:   99.9300109995%  (~6 h 8 m/yr, 3.16 nines)
```

At `f = 1` the degraded mode recovers about 525 minutes (~8 h 45 m) annually — essentially S3's entire downtime budget.

## Deliberately naive inventory calculation

If every service in the worked example were required for every operation:

```text
ALB x EC2 x RDS x S3

0.9999 x 0.9999 x 0.9995 x 0.999
= 0.998300809885
= 99.8300809885%
```

Approximate theoretical annual unavailability: 893.09 minutes, or about 14 hours 53 minutes.

Use this only to expose the mistake of multiplying an inventory. Follow it immediately with request-path analysis. It coincides with candidate operation 2 on purpose: the naive method is only right when everything really is hard.

## Simplified two-Region teaching calculation

Assume two regional compute deployments, each at the EC2 Region-Level commitment of
99.99%. Assume either can serve the request, failures are independent, capacity is
ready, data is available, and failover is instantaneous:

```text
Q(region)      = 1 - 0.9999 = 0.0001
Q(both regions)= 0.0001 x 0.0001 = 0.00000001
A(either)      = 1 - 0.00000001
               = 0.99999999
               = 99.999999%
```

Approximate theoretical annual unavailability: 0.31536 seconds.

This is the cleanest demonstration of `ANY`; it is not the final service SLA.

## Two complete regional database paths

If each Region independently contains the three-component database path above, and
either Region can serve:

```text
A(region) = 0.999300109995
A(either) = 1 - (1 - 0.999300109995)^2
          = 0.999999510153981
          = 99.9999510154%
```

Approximate theoretical annual unavailability: 15.45 seconds.

This more honest example shows why a regional *stack* should not automatically inherit
EC2's 99.99% Region-Level number.

## Formula implementation notes

These values were checked with direct floating-point arithmetic. Keep more precision
during calculation than the prose displays; round only at the final presentation step.

The annual conversions use 525,600 minutes. Do not imply AWS evaluates these SLAs
annually; AWS uses the measurement window and rules in each service agreement.
