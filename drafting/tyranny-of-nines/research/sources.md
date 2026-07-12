# Sources

Primary sources retrieved 2026-07-12 unless otherwise noted.

## Load-bearing AWS SLA pages

- [Amazon Compute Service Level Agreement](https://aws.amazon.com/compute/sla/)
  — EC2 Region-Level SLA (99.99% with qualifying deployment across 2+ AZs),
  Instance-Level SLA (99.5%), definitions of unavailability, exclusions, and credits.
  Last updated 2022-05-25.
- [Amazon Elastic Load Balancing Service Level Agreement](https://aws.amazon.com/elasticloadbalancing/sla/)
  — Multi-AZ load balancer (99.99%), Single Load Balancer (99.9%), healthy-target and
  connectivity definitions. Last updated 2022-07-25.
- [Amazon ElastiCache Service Level Agreement](https://aws.amazon.com/elasticache/sla/)
  — current Serverless/Multi-AZ (99.99%), Cross-AZ/previous-generation Multi-AZ
  (99.9%), and Single-AZ (99.5%) commitments; engine/topology distinctions. Last
  updated 2024-10-16.
- [Amazon RDS Service Level Agreement](https://aws.amazon.com/rds/sla/)
  — Multi-AZ DB instance/cluster (99.95%), Single DB instance (99.5%), one-minute
  connection-failure definition. Last updated 2024-01-22.
- [Amazon S3 Service Level Agreement](https://aws.amazon.com/s3/sla/)
  — S3 Standard and most requests (99.9%), selected storage classes (99.0%),
  five-minute request-error-rate calculation. Last updated 2023-11-28.
- [Amazon Route 53 Service Level Agreement](https://aws.amazon.com/route53/sla/)
  — 100% commitment for authoritative hosted zones in commercial Regions, narrow
  all-four-name-servers definition, API/console exclusion. Last updated 2025-04-16.

## Availability math

- AWS, [Understanding availability](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/understanding-availability.html)
  — availability definition, MTBF/MTTR relationship, and `failure = 1 - availability`.
- AWS, [Availability with dependencies](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-dependencies.html)
  — hard/soft dependencies; theoretical product for components that must all operate;
  explicit warning that public SLA composition is only a rough model and dependencies
  commonly outperform their SLA.
- AWS, [Availability with redundancy](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html)
  — redundant alternatives fail only when all fail; product of independent failure
  probabilities; cost and complexity of sparing.
- AWS, [Measuring availability](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/measuring-availability.html)
  — customer-visible units of work, server/client viewpoints, partial failures, and why
  `availability of the whole workload` requires an explicit definition.

## Fault isolation, correlation, and multi-Region design

- AWS Builders Library, [Minimizing correlated failures in distributed systems](https://aws.amazon.com/builders-library/minimizing-correlated-failures-in-distributed-systems/)
  — why correlation destroys redundancy gains; infrastructure, DNS, deployments,
  operator actions, and identical limits as shared failure modes.
- AWS Builders Library, [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)
  — provision capacity before impairment; avoid control-plane dependencies during
  recovery; Multi-AZ active-active and active-standby patterns.
- AWS Prescriptive Guidance, [AWS multi-Region fundamentals](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.html)
  — Regions as isolation boundaries, use cases, and warning that a badly built
  multi-Region design can lower availability. Published/updated 2025.
- AWS Prescriptive Guidance, [Fundamental 1: Understanding the requirements](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-1.html)
  — multi-Region for exceptional availability/continuity requirements, cost and RTO/RPO
  tradeoffs, hot standby cost near 2x.
- AWS Prescriptive Guidance, [Fundamental 2: Understanding the data](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-2.html)
  — replication latency, consistency/availability tradeoffs, and active-active versus
  other patterns.
- AWS Prescriptive Guidance, [Fundamental 3: Understanding workload dependencies](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-3.html)
  — each Region must operate without runtime dependence on the other; enumerate AWS,
  internal, third-party, network, certificate, key, secret, and parameter dependencies.
- AWS Prescriptive Guidance, [Fundamental 4: Operational readiness](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-4.html)
  — one-Region-at-a-time deployments, external monitoring, replication-lag metrics,
  regular failover/failback tests, and dependency-graph failover.
- AWS Well-Architected Framework, [REL10-BP01: Deploy the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)
  — Multi-AZ baseline, Regions as stronger isolation, duplicate complete workload
  components, and avoid cross-Region runtime coupling.
- AWS whitepaper, [Increasing dependency MTBF](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/increasing-mtbf.html)
  — when a Regional service's designed availability does not support the workload goal,
  consider a multi-Region approach as a spare/isolated instantiation.

## Source-use cautions

- AWS is both the vendor and the source of the SLAs and architectural guidance. The SLA
  pages are authoritative for contract text; the whitepapers are vendor guidance, not
  independent empirical proof of achieved availability.
- Recheck every SLA page immediately before publication. Values, definitions, supported
  engines, and configuration requirements can change.
- Do not use AWS marketing `designed for` availability numbers in place of contractual
  SLA commitments.
- Avoid long quotations. Paraphrase and link; the equations and computed examples are
  the article's own exposition.
