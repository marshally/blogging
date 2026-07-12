# Multi-Region Research

## Core claim

If the availability requirement includes continued operation through loss of an AWS
Region, the workload must be capable of serving without that Region. Multi-Region is
necessary for that failure mode.

It is not sufficient for a stronger customer-facing SLA. The whole customer operation
must have a working alternative, not merely a second collection of resources.

## Why the topology changes the math

Within one Region, the request's hard dependencies are usually a series (`ALL`)
relationship. A fully independent second Region can turn regional deployments into a
parallel (`ANY`) relationship:

```text
ALL within a Region: multiply availability
ANY across Regions:  multiply unavailability, then subtract from one
```

The gain comes from needing both regional alternatives to fail simultaneously. It does
not come from the word `multi-Region` in a diagram.

## Requirements hidden inside `either Region can work`

### Complete runtime dependency graph

Each Region must have every service, internal API, certificate, key, secret, parameter,
network path, and third-party dependency needed for the customer operation. AWS
Prescriptive Guidance recommends no runtime dependency from the standby Region back to
the primary Region.

### Capacity

The surviving Region must already have or reliably acquire enough capacity. Static
stability is stronger than assuming control planes will provision replacement capacity
during an impairment.

### Data

Cross-Region distance imposes replication latency. Asynchronous replication improves
availability and latency but creates possible data loss/inconsistency at failover.
Synchronous designs increase latency and can turn an inter-Region network partition into
an availability failure. RPO and consistency semantics belong beside the uptime target.

### Detection and routing

The design needs external health measurement, a decision rule, and a traffic-shift
mechanism. Route 53 authoritative DNS currently carries a 100% hosted-zone SLA under a
narrow definition, but DNS caching, health checks, client behavior, and the failover
mechanism still affect observed recovery.

### Deployment and operations

Deploying the same bad release to both Regions creates a shared failure mode. AWS
guidance recommends deploying one Region at a time, monitoring customer experience
outside each Region, and testing failover/failback regularly with the same runbook used
for real events.

## Correlated failures that eat the theoretical gain

- The same application defect or configuration error.
- A simultaneous multi-Region deployment.
- Shared CI/CD, identity, certificate, secret, feature-flag, or configuration systems.
- A database or replication error propagated to both copies.
- Global traffic management or DNS dependencies.
- Third-party dependencies common to both Regions.
- Operator action with global scope.
- Insufficient standby capacity.
- A failover procedure that has not been exercised under load.

AWS Builders Library material explicitly warns that correlated failures reduce the
benefit of redundancy and identifies common infrastructure, DNS, operator action, and
identical behavior/resource limits as examples.

## Active-active is not the only model

- **Backup/restore:** cheapest, long RTO; not an availability alternative in the normal
  probability sense.
- **Pilot light:** core data/services exist, compute is provisioned during recovery;
  control-plane and time dependencies dominate.
- **Warm standby:** full stack exists at reduced capacity; failover and scale-up consume
  time.
- **Hot standby:** complete capacity is ready but normally passive; closest to the
  `either can work` model if promotion/routing is fast.
- **Active-active:** both Regions serve; minimizes modal failover behavior but makes data
  semantics and coordination harder.

AWS's 2025 multi-Region fundamentals guide says most workloads can meet resilience goals
in one Region, that hot standby commonly doubles workload cost, and that a poorly built
multi-Region architecture can reduce availability.

## The discontinuous cost of another nine

The title's `tyranny` is partly economic. Availability improvement is not always a
smooth sequence of tuning changes:

```text
single instance -> multi-instance / Multi-AZ -> multi-Region
```

Crossing a fault-domain boundary duplicates infrastructure and introduces new software,
data, deployment, testing, and organizational obligations. A higher SLA can force a
qualitatively different system.

## Wording guardrails

Prefer:

> To survive Regional failure, the service must operate from another Region.

Avoid:

> Two Regions automatically provide eight nines.

Prefer:

> Under independence and perfect failover, two four-nines alternatives produce a
> theoretical 99.999999% infrastructure layer.

Avoid:

> AWS guarantees our multi-Region service at eight nines.
