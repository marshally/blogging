# Research leads for the lesson brainstorm

Created 2026-10-10 for the 100-item [lesson menu](../lesson-ideas.md). This is a source map for ideation. The titles and demonstrations are proposals, not author quotations or approved lessons. Source keys mean “investigate this connection,” not “this author made this exact agentic-coding claim.”

## Evidence status

Existing primary research supports only the specific claims recorded in its linked entries. Newly inspected book-skill entrypoints are secondary syntheses, often reconstructed from training knowledge. Their candidate book attributions and technical teaching claims are **unsubstantiated for publication** until checked against primary passages. The broad menu deliberately retains those ideas for selection rather than silently upgrading their evidence.

The selected skill entrypoint introductions and concept/scorecard sections were inspected in the local software-engineering plugin. They supplied topic leads only. The lesson-specific agent applications are original synthesis. No performance gain, token saving, optimal size, or universal architectural prescription is established by this brainstorm.

## Source key

| Key | Starting point | Scope and status |
|---|---|---|
| MODEL | [Series model and original applications](../DECISIONS.md) | Original proposals. Technical demonstrations and claims of improved outcomes remain unsubstantiated until tested. |
| CONTEXT | [Context engineering, delegation, and skills](sources.md) | Primary starting points C03–C07. Specific lesson applications are proposals. |
| OUSTERHOUT | [A Philosophy of Software Design](sources.md#c02-deep-modules-and-information-hiding) | Primary support for depth and information hiding. Other concepts require passage verification. |
| METZ | [Metz on interfaces and testing](metz-interfaces-and-tests.md) | Primary support for the scoped claims in M01–M03. Recursive agent applications are synthesis. |
| PHOENIX | [Chad Fowler on replaceable implementations](replaceable-modules.md) | Primary support for the scoped claims R02–R04. No claim of guaranteed correctness. |
| PRAGMATIC | [The Pragmatic Programmer](book-skill-inventory.md#b02-hunt-and-thomas-and-orthogonality) | Partial primary support for orthogonality. Broader concepts remain secondary leads. |
| TDD | [Test Driven Development by Example](book-skill-inventory.md#b03-beck-and-incremental-tdd) | Primary author clarification of incremental TDD. Specific agent demonstrations are proposals. |
| TIDY | [Tidy First?](book-skill-inventory.md#b05-beck-and-separating-kinds-of-change) | Primary author essay on separating changes. Verify detailed book treatments before drafting. |
| LEGACY | [Working Effectively with Legacy Code](book-skill-inventory.md#b04-feathers-and-seams) | Primary support for seams. Characterization and sprout-method details remain research leads. |
| REFACTOR | [Refactoring](book-skill-inventory.md#b09-fowler-and-behavior-preserving-refactoring) | Secondary skill lead. Selected transformations need primary verification. |
| EXPLORE | [Explore It!](book-skill-inventory.md#b06-hendrickson-and-exploratory-charters) | Primary support for exploratory charters. Agent-review applications are synthesis. |
| DEBUG | [Debug It!](book-skill-inventory.md#b07-butcher-and-experimental-debugging) | Primary support for experimental diagnosis. Other techniques need passage verification. |
| OBSERVABILITY | [Observability Engineering](book-skill-inventory.md#b11-majors-fong-jones-and-miranda-and-observability) | Secondary skill lead. Agent-run telemetry application is synthesis. |
| DDD | [Domain-Driven Design](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-domain-driven-design/SKILL.md) | Secondary skill lead: domain language, model boundaries, entities, values, aggregates. |
| IDDD | [Implementing Domain-Driven Design](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-implementing-domain-driven-design/SKILL.md) | Secondary skill lead: consistency boundaries, events, integration, and application services. |
| GOOS | [Growing Object-Oriented Software, Guided by Tests](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-growing-object-oriented-software/SKILL.md) | Secondary skill lead: interface discovery, feedback loops, collaborator boundaries, and walking skeletons. |
| TESTING | [Effective Software Testing](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-mauricio-aniche-effective-software-testing/SKILL.md) | Secondary skill lead: specification-derived cases, partitions, properties, and testability. Mutation-testing attribution needs separate verification. |
| RELEASE | [Release It!](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-release-it/SKILL.md) | Secondary skill lead: timeouts, failure isolation, circuit breakers, resources, and deployment safety. |
| DATA | [Designing Data-Intensive Applications](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-designing-data-intensive-applications/SKILL.md) | Secondary skill lead: transactions, consistency, schema evolution, and distributed failure semantics. |
| EVOLUTION | [Building Evolutionary Architectures](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-building-evolutionary-architectures/SKILL.md) | Secondary skill lead: fitness functions, incremental change, and architectural constraints. Verify edition and authors before publication. |
| DELIVERY | [Accelerate](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-accelerate/SKILL.md) | Secondary skill lead: delivery outcomes, capabilities, batch size, and system-level measurement. Recheck current metric terminology if used. |
| HISTORY | [Your Code as a Crime Scene](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-adam-tornhill-your-code-as-a-crime-scene/SKILL.md) | Secondary skill lead: hotspots and change coupling. No causal claims from Git history alone. |
| PLATFORM | [Platform Engineering](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-platform-engineering/SKILL.md) | Secondary skill lead: platforms as products, useful defaults, adoption, and ownership. |
| PATTERNS | [Design Patterns](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-design-patterns/SKILL.md) | Secondary skill lead: composition and encapsulating variation. No claim that agents require OO patterns. |
| CLEAN | [Clean Code](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-clean-code/SKILL.md) | Secondary skill lead: names, abstraction levels, and design heuristics. Preserve disagreements with other authors. |
| HARDPARTS | [Software Architecture: The Hard Parts](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-software-architecture-the-hard-parts/SKILL.md) | Secondary skill lead: decomposition tradeoffs, communication, data ownership, and coordination. |
| ENTERPRISE | [Patterns of Enterprise Application Architecture](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-patterns-of-enterprise-application-architecture/SKILL.md) | Secondary skill lead: domain logic, persistence, layering, and complexity fit. |

## Verification before a lesson becomes an outline

Select the original concept, verify the author and source passage, and specify a small demonstration. Record which behavior should improve and how to check it. A candidate about an agent failure needs either an explicitly hypothetical example or evidence from an actual run. Keep the distinction between an author's original idea and this series' application visible.

## Folklore and exclusions

No new quotation is proposed. Do not invent book quotations or chapter numbers, present consensus where authors disagree, equate a bounded context with a token window, or claim that passing tests or multiple agreeing agents establish comprehensive correctness. “Mutation testing” and the practical handling of uncertain writes remain independent technical research leads unless a specific book attribution is verified.
