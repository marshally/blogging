# Worked Example

All calculations use current public SLA commitments as rough probability inputs. They
are checked arithmetic, not an AWS-backed composite SLA and not a historical claim
about Twilio.

## Assumed component values

```text
Multi-AZ ALB                         0.9999
EC2 Region-Level                    0.9999
Multi-AZ ElastiCache (Redis/Valkey) 0.9999
Multi-AZ RDS                        0.9995
S3 Standard                         0.9990
```

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

## Candidate operation 2: cache hit

```text
client -> ALB -> EC2 -> ElastiCache
```

```text
0.9999 x 0.9999 x 0.9999
= 0.999700029999
= 99.9700029999%
```

Approximate theoretical annual unavailability: 157.66 minutes, or about 2 hours 38
minutes.

This path is only valid if a cache hit does not synchronously require RDS.

## Candidate operation 3: cache miss backed by RDS

```text
client -> ALB -> EC2 -> ElastiCache -> RDS
```

```text
0.9999 x 0.9999 x 0.9999 x 0.9995
= 0.9992001799840007
= 99.9200179984%
```

Approximate theoretical annual unavailability: 420.39 minutes, or about 7 hours.

Question for the draft: if ElastiCache is unavailable, can the application bypass it
and use RDS directly? If so, ElastiCache is not a simple hard dependency and this path
needs a conditional/degraded model instead of serial multiplication.

## Deliberately naive inventory calculation

If every named AWS service were required for every operation:

```text
ALB x EC2 x ElastiCache x RDS x S3

0.9999 x 0.9999 x 0.9999 x 0.9995 x 0.999
= 0.9982009798040167
= 99.8200979804%
```

Approximate theoretical annual unavailability: 945.57 minutes, or about 15 hours 46
minutes.

Use this only to expose the mistake of multiplying an inventory. Follow it immediately
with request-path analysis.

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
