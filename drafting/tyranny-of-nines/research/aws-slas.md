# AWS SLA Snapshot

Retrieved 2026-07-12 from AWS's official SLA pages. These are current inputs for a
worked example, not claims about the historical Twilio architecture or contract.

## Comparison

| Service/configuration | Current commitment | Scope and important definition | Article use |
|---|---:|---|---|
| EC2 Region-Level | 99.99% | Requires running instances concurrently deployed across 2+ AZs in one Region. `Unavailable` means all those instances concurrently lack external connectivity. | Establishes the named four-nines Regional compute commitment. |
| Single EC2 instance | 99.5% | Applies to an individual instance. | Shows that architecture is required even to obtain the Region-Level commitment. |
| Multi-AZ ALB | 99.99% | Load balancer enabled in 2+ AZs with at least one healthy target; unavailable when it has no external connectivity and connection attempts fail. | Required ingress dependency for candidate paths. |
| Single-AZ load balancer | 99.9% | Applies to a load balancer deployed in one AZ. | Configuration contrast; do not silently assume Multi-AZ. |
| Multi-AZ ElastiCache, current generation | 99.99% | Valkey: automatic failover enabled, primary+replica per shard across 2+ AZs. Redis OSS additionally requires v6.2+ created or engine-updated on/after 2023-01-13 with the Multi-AZ setting enabled. Serverless ElastiCache (Valkey, Redis OSS, Memcached) carries the same 99.99%. | Dropped from the worked example (D14); reference only. |
| ElastiCache Cross-AZ (Memcached) and Previous Generation Multi-AZ (Redis OSS) | 99.9% | Two named configurations share this tier: Memcached deployed across 2+ AZs, and Redis OSS Multi-AZ clusters that miss the v6.2+/2023-01-13 gate. Re-verified against the live SLA page 2026-07-12. | Dropped from the worked example (D14); reference only. |
| Single-AZ ElastiCache | 99.5% | Applies to qualifying single-AZ Valkey, Memcached, or Redis OSS configuration. | Configuration contrast. |
| Multi-AZ RDS instance or cluster | 99.95% | Unavailable when all connection requests fail during a one-minute interval. | Lowest commitment on the core ALB/EC2/RDS path. |
| Single RDS DB instance | 99.5% | Separate instance-level commitment. | Configuration contrast. |
| S3 Standard and most requests | 99.9% | Monthly uptime is based on average request error rates for each five-minute interval in the affected Region. | Demonstrates both a lower published number and a different denominator. |
| S3 Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant Retrieval | 99.0% | Separate storage-class commitment. | Storage class matters; never write simply `S3 = X` without qualifying it. |
| Route 53 authoritative hosted zone (commercial Regions) | 100% | Hosted zone unavailable only if all four assigned name servers fail to answer all queries throughout a minute. API and console are excluded. | Potential global routing dependency for multi-Region discussion. |

## Exact editorial distinctions

### EC2 has a Region-Level SLA; AWS does not have one universal Region SLA

Safe wording:

> EC2's Region-Level SLA supports a qualifying Multi-AZ compute deployment at 99.99%
> within a Region.

Unsafe wording:

> AWS guarantees every service in a Region at 99.99%.

ALB, ElastiCache, RDS, S3, and Route 53 each have separate agreements, thresholds,
definitions, exclusions, and remedies.

### A commitment is not a maximum

AWS promises commercially reasonable efforts and service credits below the stated
threshold. The threshold is not a claim that the service cannot or will not perform
better. In this article, `cap` should mean the level of a downstream promise directly
supported by the supplier's contract—not a physical ceiling on observed uptime.

### AWS does not guarantee the calculated composite

Multiplying the values in this table produces a theoretical engineering model. AWS
applies each SLA individually. Differences in measurement units make the product even
less suitable as literal contract arithmetic.

## Configuration questions — resolved 2026-07-12

See DECISIONS D14–D16 and `story-notes.md`:

- ElastiCache: historically Redis, Multi-AZ; dropped from the worked example (D14).
- RDS, compute, ALB: the platform was Multi-AZ overall (D16); the worked example assumes the modern Multi-AZ configurations in this table.
- S3: S3 Standard assumed; modeled as a degraded-mode dependency after the hard-path math (D15).
- The platform was single-Region at the time (D16).

The worked example remains an assumed modern Multi-AZ configuration, not a claim about the historical Twilio deployment's exact contracts.
