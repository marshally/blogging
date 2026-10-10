# Software engineering fundamentals for agentic coding

Series planning brief, 2026-10-10. Marshall's argument: software-engineering fundamentals become more important when agents do the coding. Teach the agent operating model first, then connect individual engineering principles to concrete improvements in how agents understand, change, and verify software. Each lesson becomes one short post and one video. Later, assemble them into the course described in [D6](DECISIONS.md#d6-eventual-course).

The audience proposed here is working developers who already use coding agents and want more reliable results. This brief uses an internal planning register. Episode order, examples, and exercises are suggestions for discussion. [DECISIONS.md](DECISIONS.md) records Marshall's actual selections.

The [100-lesson brainstorm](lesson-ideas.md) expands the options across context, agent coordination, contracts, design, domain modeling, testing, legacy changes, review, reliability, and delivery. Its [source map](research/lesson-source-leads.md) identifies book and research leads for later development.

## The foundational model

**Give each agent one coherent outcome, enough context to achieve it, and a clear way to prove it is done.** That is the proposed operating rule for the series. A coordinator understands the overall objective and dependencies. Workers load the detail needed for their assignments and return useful results with evidence. The coordinator owns integration and the check that the combined result satisfies the original objective. This applies the context-management and delegation ideas in [C03–C05](research/sources.md#c03-progressive-disclosure-and-sufficient-context) using the proposed ownership model in [A02](research/sources.md#a02-focused-ownership-with-explicit-handoffs).

Marshall anticipates humans doing much of the steering at module boundaries: which modules exist, where they communicate, and what behavior is observable at those seams. Humans carefully review the public-interface tests as an executable contract. A calling agent should be able to load the interface file and its behavioral documentation to use the component, without opening the implementation. That compact description must reflect the contract expressed in the tests ([D8](DECISIONS.md#d8-human-steering-centers-on-modules-seams-and-contracts), [R06](research/replaceable-modules.md#r06-recursive-modules-and-human-reviewed-behavioral-contracts)).

```mermaid
flowchart TD
    G[User goal and acceptance criteria] --> H[Humans steer modules, seams, and observable behavior]
    H --> C[Coordinator owns task scope and integration]
    H --> K[Indexed context and reviewed module contracts]
    C --> A[Agent A owns one outcome]
    C --> B[Agent B owns a separable outcome]
    K -. Load detail as needed .-> A
    K -. Load detail as needed .-> B
    A --> E[Results, evidence, and unresolved dependencies]
    B --> E
    E --> I[Integrate and verify the whole result]
    I --> R[Focused review of a specific risk]
    R --> D[Accept or revise]
```

This is a teaching model, not a fixed roster of agents. Keep tightly coupled work together. Parallelize work whose outputs can be reconciled. A researcher, implementer, or reviewer is a possible assignment, not a mandatory agent for every task. The evidence supports selective delegation and also documents coordination and token costs ([C05](research/sources.md#c05-multi-agent-gains-depend-on-task-structure-and-cost)).

The proposed assignment contract contains the desired outcome, relevant shared constraints, owned scope, an initial context packet, pointers to deeper material, acceptance criteria, and the expected return format. A useful return contains the result or artifact, evidence, assumptions, unresolved dependencies, and locations for further detail. Any constraint that can invalidate the result belongs in the contract even when implementation detail stays behind a reference. This delegation agreement is distinct from the module's behavioral contract, which persists across individual agent assignments.

### Progressive disclosure

Teach three levels: a small map of what exists and when to consult it, the selected task's instructions and contracts, then the source, examples, or tool results needed for the next decision. Important shared constraints arrive up front. Detailed investigation expands only as needed. The agent must be able to discover missing context and revisit its scope when a dependency appears. This is the practical application of [C03](research/sources.md#c03-progressive-disclosure-and-sufficient-context) and the skill-loading example in [C06](research/sources.md#c06-skills-offer-a-concrete-disclosure-mechanism).

### The budget

Marshall's targets are **under 150,000 total tokens per agent task where practical, with a ceiling below 250,000** ([D3](DECISIONS.md#d3-token-targets-and-accounting-scope)). These count cumulative work across calls. Active context occupancy is a separate measurement ([C07](research/sources.md#c07-capacity-occupancy-and-cumulative-usage-differ)).

For demonstrations, define the runtime's input, output, reasoning, and cached-token accounting explicitly so categories are not double-counted. Preserve a logical task's identity across resumptions. Report each agent's consumption, coordinator consumption, combined run consumption, elapsed time, and acceptance results. Several workers can each meet their budget while the combined cost rises.

The proposed response to an approaching ceiling is to inspect scope, dependencies, repeated discovery, and failed attempts, then change the work plan. Keep the acceptance criteria intact. The targets are a design constraint to investigate, not evidence that every task should require that many tokens or that crossing the number causes failure ([A03](research/sources.md#a03-the-proposed-150000--250000-token-budget)).

## Proposed opening sequence

Alternate agent mechanics with the books that help explain them. Each row is one self-contained lesson. The agent applications are proposals, with research links identifying the underlying concepts and their evidence limits.

| Order | Lesson | Source | Concrete teaching move |
|---|---|---|---|
| 1 | Give an agent a problem it can finish | [Focused-agent model](research/sources.md#a02-focused-ownership-with-explicit-handoffs) | Turn an open-ended request into an outcome, context map, budget, and acceptance check. Show who owns integration. |
| 2 | Make context discoverable | [Progressive disclosure](research/sources.md#c03-progressive-disclosure-and-sufficient-context) | Show an index leading to a contract, then to the relevant implementation. |
| 3 | Deep modules organize context at every level | [Ousterhout and composed abstractions](research/replaceable-modules.md#r01-ousterhouts-abstraction-supports-composition) | Show a compact public contract over composed internal domains, then follow one task into the relevant inner module. |
| 4 | Write interface tests that leave room for replacement | [Metz on interfaces and tests](research/metz-interfaces-and-tests.md) | Preserve the outer behavioral contract while changing inner collaborators. Show which tests belong at each boundary. |
| 5 | Package a skill behind a useful interface | [Skills and disclosure](research/sources.md#c06-skills-offer-a-concrete-disclosure-mechanism) | Show discovery metadata, task instructions, and supporting resources. Distinguish a reusable skill from the agent executing it. |
| 6 | Divide work along independent changes | [Hunt and Thomas, The Pragmatic Programmer](research/book-skill-inventory.md#b02-hunt-and-thomas-and-orthogonality) | Compare a split by filenames with a split by responsibilities and dependencies. Full book treatment still needs verification. |
| 7 | Give the agent a feedback loop | [Beck, Test Driven Development by Example](research/book-skill-inventory.md#b03-beck-and-incremental-tdd) | Demonstrate one behavior through a failing test, implementation, and a passing check. |
| 8 | Find a seam before changing the system | [Feathers, Working Effectively with Legacy Code](research/book-skill-inventory.md#b04-feathers-and-seams) | Substitute one troublesome dependency to make the relevant behavior testable. |
| 9 | Separate structural and behavioral changes | [Beck, Tidy First](research/book-skill-inventory.md#b05-beck-and-separating-kinds-of-change) | Make a useful preparation independently reviewable, then implement the feature. |
| 10 | Give adversarial review a question to investigate | [Hendrickson, Explore It](research/book-skill-inventory.md#b06-hendrickson-and-exploratory-charters) | Ask a reviewer to investigate one risk and supply a reproducible counterexample. Keep access to requirements and context. |
| 11 | Diagnose before patching | [Butcher, Debug It](research/book-skill-inventory.md#b07-butcher-and-experimental-debugging) | Show an observation, competing explanations, and an experiment that distinguishes them. |

Later candidates from the same skill inventory: Fowler on named refactorings, Evans on shared domain language, and Majors, Fong-Jones, and Miranda on observability. Their proposed applications and outstanding source work are in [B09–B11](research/book-skill-inventory.md#secondary-leads-for-later-lessons). Expand the series by useful principles rather than requiring one episode per book.

## The first book lesson

Proposed example: an agent needs to add a records export. In one design, its caller must assemble authentication, pagination, and transport handling scattered across helpers. In the other, a records interface owns those mechanics and documents its ordering, completeness, and failure behavior. Walk through what the caller must learn in each version before it can implement the export. This is a hypothetical example, not a reported project result.

Begin with human review of tests at that public interface. In this example, the tests could express whether all matching records must appear exactly once, which ordering is promised, and what the caller observes after a later page fails. The interface file communicates those same obligations compactly. The caller's working context can then contain the public agreement without the authentication or pagination machinery. Reviewing whether those obligations are the right ones is part of the human design work ([R06](research/replaceable-modules.md#r06-recursive-modules-and-human-reviewed-behavioral-contracts)).

Then change the assignment: the agent must alter pagination itself. It opens the pagination component and the contracts of its collaborators. Authentication and transport internals remain behind their own interfaces. This makes the disclosure rule concrete: the relevant detail depends on the task, and composition makes that detail independently accessible. Measure the paths inspected and actual run usage before claiming a token benefit. The book-to-agent connection is documented in [A01](research/sources.md#a01-engineering-fundamentals-as-context-design) and Marshall's clarification in [R06](research/replaceable-modules.md#r06-recursive-modules-and-human-reviewed-behavioral-contracts).

**A deep module must be manageable from both sides of its interface.** The caller needs a compact, complete account of how to use it. The maintainer needs internal boundaries that let it work on the relevant part. Marshall rejects a single file containing 100,000 tokens as a useful interpretation of depth. A module can compose further modules that isolate functional domains, like his Russian dolls, with the same information-hiding discipline recurring inside ([D7](DECISIONS.md#d7-deep-modules-use-recursive-composition)).

Depth describes how much useful capability an interface makes available relative to what callers must understand. File size is a separate concern. The teaching test is whether the caller can use the outer module without opening its internals, and whether a maintainer can change an inner domain without loading the entire outer implementation. This combines Ousterhout's abstractions with Marshall's agent workflow ([R01 and R06](research/replaceable-modules.md#r01-ousterhouts-abstraction-supports-composition)).

### Public interfaces and tests that leave room for change

Sandi Metz adds discipline to the contract: express what a caller needs to request while keeping the receiver's implementation decisions private. The verified example comes from *99 Bottles of OOP*, coauthored with Katrina Owen and TJ Stankus. It provides a concrete example of separating requests from their implementation ([M01](research/metz-interfaces-and-tests.md#m01-describe-what-callers-can-request)).

Metz's [message-testing matrix](research/metz-interfaces-and-tests.md#m02-choose-assertions-by-message-direction-and-type) distinguishes incoming, outgoing, and private messages, and queries from commands. Its rules are defaults with cost-based exceptions. Use the matrix to decide which obligations each test protects.

In the proposed export example, the outer suite checks exported records, declared failure behavior, and any required interaction with an external destination. Assertions about which private pagination helper runs, or the order of internal helper calls, would make those choices part of what the suite preserves. An agent replacing pagination with a different traversal strategy would then have to change tests even if callers receive the same promised behavior. That is a failure of the replacement demonstration, not evidence that the new traversal violates the public contract.

The paginator can still have its own interface and focused tests inside the module. **Public and private depend on the boundary being considered.** Its interface is public to its immediate collaborators and private to the exporter’s external callers. Preserve the outer suite during a rewrite. Keep child-level tests while the child contract exists, and let those tests evolve or retire when that internal abstraction is deliberately replaced. This recursive application is the series' synthesis ([M04](research/metz-interfaces-and-tests.md#m04-public-and-private-depend-on-the-chosen-boundary)).

Metz's POODR examples also demonstrate a double drifting from its real collaborator and use a shared interface check to catch that mismatch. The shown check verifies message availability, which is narrower than behavioral equivalence ([M03](research/metz-interfaces-and-tests.md#m03-test-doubles-must-track-the-real-interface)). For this series, human review should check that substitutes and real components agree about the relevant behavior, with integration evidence where needed. An isolated green test built on an invented collaborator is insufficient evidence for the composed system.

The resulting review question is: does this test protect an obligation at the intended seam, or accidentally make a private decision permanent? That question connects human review directly to the implementation freedom given to agents ([M05](research/metz-interfaces-and-tests.md#m05-human-review-governs-the-contract-agents-implement), [D10](DECISIONS.md#d10-add-metz-on-public-and-private-interfaces-and-testing)).

### Replace the implementation and preserve the agreement

Marshall's third benefit is the ability to rewrite internals that have become unworkable while retaining the contract expressed in interface tests ([D9](DECISIONS.md#d9-contracts-support-replaceable-implementations)). Continue the example by replacing the pagination implementation and running the same public-interface checks against both versions. The durable investment is the understood behavior and its verification. The implementation can change behind it.

Chad Fowler explicitly connects his current regeneration model to earlier service replacement at Wunderlist in [Compile to Architecture](https://aicoding.leaflet.pub/3mgfsrk75ac2l). [The Phoenix Primitives](https://chadfowler.com/regenerative-software/3mjfruwwuck2d/) describes specifications, evaluations, context boundaries, and provenance surviving implementation replacement. His early talk and current essays provide the source lineage in [R02–R05](research/replaceable-modules.md#r02-phoenix-preserves-the-knowledge-needed-for-replacement). These ideas can be applied to module boundaries inside a process. Separate deployment is not a requirement of Marshall's proposed workflow.

The assurance is as strong as the contract and the checks that express it. Failure behavior, side effects, state compatibility, and relevant operational limits need coverage when callers depend on them. Tests of individual modules also need checks of their interactions, a point Fowler makes in [The Regenerative Grain](https://chadfowler.com/regenerative-software/3mfai4nqg6224/) ([R04](research/replaceable-modules.md#r04-the-grain-must-preserve-coherent-behavior)). A proposed workflow consequence is to review a change to the contract as a separate design decision from an implementation change intended to preserve it. Weakening a test to accommodate a replacement would change the agreement being verified.

This gives the deep-module material four possible short lessons: human review of the behavioral contract, composition as progressive disclosure, interface tests that leave room for change, and replacing an implementation against retained expectations. Use them as a connected mini-series if the combined example is too large for one post and clip.

## One principle in two formats

Proposed lesson pattern:

1. Show a recognizable failure or a small before-example.
2. Explain one principle and credit its source.
3. Apply it to a specific agent task with an after-example.
4. Give the reader one action to try and a way to check the result.

The short post carries the example, reasoning, and citations. The video teaches the same complete idea with one visible artifact, such as an interface, task brief, test failure, or review finding. A starting production target is 400–700 words and roughly 60–120 seconds, adjustable after a pilot. These are suggested editorial lengths, not platform limits or an approved cadence. Detailed scripts can wait until Marshall chooses the first lesson's example.

TikTok, YouTube, and LinkedIn are the selected video destinations ([D5](DECISIONS.md#d5-post-and-video-unit)). Keep Yount Labs as the canonical written archive and give each platform a complete useful lesson, consistent with the [posting strategy](../../docs/2026-posting-strategy.md). This series adds video destinations without requiring changes to the site's general editorial cadence.

## Build toward the course

Keep a learning objective, source entry, before/after artifact, small exercise, and acceptance check with every lesson. The course can then group the material by what a learner can do: scope and supply context, design boundaries and handoffs, change behavior with feedback, and investigate results. Add the transitions and a worked end-to-end project when assembling it.

For the eventual course exercise, have the learner take one change through task decomposition, context loading, implementation, review, and integration. Assess correctness and evidence alongside token use. The exercise tests how the principles work together. It also provides a place to show when delegation creates more work than it saves.

Next editorial step: choose the opening lesson's concrete task and develop its post outline and video beats. The book shortlist and sequence above are ready for Marshall's revision.
