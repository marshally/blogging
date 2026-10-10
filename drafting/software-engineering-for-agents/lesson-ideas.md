# Short lessons on software engineering for agents

Lesson menu, 2026-10-10. The original 100 candidates are now organized under Marshall's selected seven-part sequence, with 13 additions for Unix composition, static analysis, feature flags, progressive exposure, application observability, and named principles as compact guidance. These 113 candidates remain a menu for selection. The seven-part order is selected. The placement and ordering of individual lessons are proposals. IDs remain stable from the original brainstorm and do not represent episode numbers.

Each candidate aims at one useful lesson for a short post and video, with room for examples and exercises when assembled into the course. The [source map](research/lesson-source-leads.md) distinguishes existing primary evidence from secondary book leads and original applications. **New book connections and teaching claims remain unsubstantiated for publication until researched.** Source labels are leads to investigate, not claims that those authors described agent workflows. No quantitative benefit is assumed.

## 1. Context efficient agent model

Begin with focused assignments, sufficient context, progressive disclosure, and explicit integration ownership. Narrowly focused adversarial review belongs in this opening model. Teach review charters and evidence here, then apply them throughout the series.

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 1 | Size the task to the token budget | Define a finishable outcome against the per-agent 150k target and 250k ceiling. | [MODEL](research/lesson-source-leads.md#source-key), [CONTEXT](research/lesson-source-leads.md#source-key) |
| 11 | Give each agent one outcome | Replace a vague assignment with one deliverable and an acceptance check. | [MODEL](research/lesson-source-leads.md#source-key) |
| 2 | A map before the manuals | Give an agent a useful index of the repository before asking it to choose detailed reading. | [CONTEXT](research/lesson-source-leads.md#source-key) |
| 3 | Load invariants first | Identify the constraints an agent must know before it begins exploring or changing code. | [MODEL](research/lesson-source-leads.md#source-key), [CONTEXT](research/lesson-source-leads.md#source-key) |
| 113 | Invoke a principle by name | Compare a short attributed reference, such as tracer bullets from The Pragmatic Programmer, with an expanded explanation for the same task. Inspect the resulting plan and code against the same acceptance criteria. Measure prompt length separately from total task tokens. | [POCOCK](research/matt-pocock.md#p12-leading-words-as-compact-guidance), [MODEL](research/lesson-source-leads.md#source-key) |
| 4 | Use the interface as working context | Complete a caller-side change using a component's documented contract. | [OUSTERHOUT](research/lesson-source-leads.md#source-key), [METZ](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 5 | Retrieve one level deeper | Follow one task into the relevant internal module while leaving sibling internals unopened. | [CONTEXT](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 6 | Trim tool output at the source | Compare a focused query with a command that fills the context with irrelevant output. | [CONTEXT](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 7 | Version the context | Attach repository revisions and source dates so an agent can recognize stale instructions or evidence. | [MODEL](research/lesson-source-leads.md#source-key) |
| 8 | Keep a decision ledger | Preserve an architectural choice and its rationale so the next agent can build on it. | [MODEL](research/lesson-source-leads.md#source-key) |
| 9 | Preserve uncertainty through compaction | Carry unresolved questions, rejected hypotheses, and evidence links into a shorter handoff. | [CONTEXT](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 10 | Route skills by intent | Write skill descriptions that help an agent load the right procedure for the current task. | [CONTEXT](research/lesson-source-leads.md#source-key) |
| 12 | Split work by dependencies | Compare delegation by filenames with delegation by independently changeable responsibilities. | [PRAGMATIC](research/lesson-source-leads.md#source-key), [HARDPARTS](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 13 | Draw the dependency graph before parallelizing | Identify what can run concurrently and what must wait for another result. | [MODEL](research/lesson-source-leads.md#source-key), [HARDPARTS](research/lesson-source-leads.md#source-key) |
| 14 | Give integration an owner | Make someone responsible for proving that individually completed pieces work together. | [MODEL](research/lesson-source-leads.md#source-key) |
| 15 | Design the handoff contract | Require results, evidence, assumptions, and unresolved dependencies from a delegated task. | [MODEL](research/lesson-source-leads.md#source-key), [CONTEXT](research/lesson-source-leads.md#source-key) |
| 16 | Give edits clear ownership | Demonstrate two agents working without accidentally overwriting the same change. | [MODEL](research/lesson-source-leads.md#source-key) |
| 19 | Keep tightly coupled work together | Examine a task where delegation costs more coordination than it removes. | [CONTEXT](research/lesson-source-leads.md#source-key), [HARDPARTS](research/lesson-source-leads.md#source-key) |
| 71 | Give adversarial review one focused question | Ask a narrowly focused reviewer to investigate one risk and supply evidence or a counterexample, with room to discover related failures. | [EXPLORE](research/lesson-source-leads.md#source-key) |
| 18 | Give reviewers independent starting context | Provide requirements and evidence without making the implementer's justification the review brief. | [MODEL](research/lesson-source-leads.md#source-key), [EXPLORE](research/lesson-source-leads.md#source-key) |
| 72 | Turn disagreement into a counterexample | Replace competing opinions with an input or execution that tests the disputed claim. | [EXPLORE](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 73 | Separate correctness from style preference | Show a review where a standards concern and a requirement failure need different remedies. | [MODEL](research/lesson-source-leads.md#source-key) |
| 75 | Require evidence for a review finding | Attach a location, reproduction, and observable consequence to a proposed defect. | [MODEL](research/lesson-source-leads.md#source-key) |
| 76 | Examine agreement built on a shared assumption | Give two reviewers the same mistaken premise and investigate why their agreement is insufficient. | [MODEL](research/lesson-source-leads.md#source-key) |
| 99 | Maintain skills as products | Give a reusable skill an owner, users, examples, checks, and a way to evolve. | [PLATFORM](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |

## 2. Code architecture and design

Introduce deep modules, small composable Unix utilities, and domain-driven design. Humans steer module boundaries and behavioral contracts. Customer conversations, domain code, and examples should use the same unambiguous terms within the relevant domain. The added source entries are [S01 and S02](research/curriculum-additions.md).

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 21 | Draw the seams before assigning the work | Have humans choose the important module boundaries and interactions before agents implement them. | [MODEL](research/lesson-source-leads.md#source-key) |
| 31 | Deep is different from large | Compare useful capability per unit of interface complexity with raw implementation size. | [OUSTERHOUT](research/lesson-source-leads.md#source-key) |
| 32 | Compose the Russian dolls | Give an internal functional domain its own boundary without exposing it to every outer caller. | [MODEL](research/lesson-source-leads.md#source-key), [METZ](research/lesson-source-leads.md#source-key), [OUSTERHOUT](research/lesson-source-leads.md#source-key) |
| 101 | Give each utility one coherent job | Split a multi-purpose tool at a useful responsibility boundary, then check that each resulting utility has a clear purpose and manageable interface. | [UNIX](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 102 | Compose utilities through explicit input and output | Connect two small utilities through a documented data format. Show how the next tool consumes the result without inspecting its producer. | [UNIX](research/lesson-source-leads.md#source-key) |
| 103 | Separate mechanism from workflow policy | Reuse a utility in two workflows that make different sequencing or policy choices. Keep those decisions in the composition. | [UNIX](research/lesson-source-leads.md#source-key) |
| 41 | Use the same unambiguous domain language as customers | Trace a customer scenario through requirements, tests, and code. Resolve conflicting meanings with the customer and keep terms consistent within the domain. | [DDD](research/lesson-source-leads.md#source-key) |
| 42 | Keep different models in bounded contexts | Show why the same business term can legitimately mean different things in separate domains. | [DDD](research/lesson-source-leads.md#source-key) |
| 43 | Translate at the boundary | Keep an external provider's terminology and data shapes from spreading through the domain. | [DDD](research/lesson-source-leads.md#source-key), [IDDD](research/lesson-source-leads.md#source-key), [GOOS](research/lesson-source-leads.md#source-key) |
| 23 | Separate questions from commands | Make it clear which interface operations return information and which change the world. | [METZ](research/lesson-source-leads.md#source-key) |
| 24 | Make failure part of the interface | Specify what callers observe when an operation cannot fulfill its promise. | [OUSTERHOUT](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 25 | Write down what must always remain true | Express a domain invariant before asking an agent to choose an implementation. | [DDD](research/lesson-source-leads.md#source-key), [TESTING](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 26 | Name operations for the caller's intent | Compare an interface named for business behavior with one named for its current machinery. | [METZ](research/lesson-source-leads.md#source-key), [CLEAN](research/lesson-source-leads.md#source-key) |
| 28 | Review contract changes as design changes | Distinguish a revised promise from a new implementation of the existing promise. | [MODEL](research/lesson-source-leads.md#source-key) |
| 33 | Find information leakage | Trace a supposedly private schema decision that forces several callers to change. | [OUSTERHOUT](research/lesson-source-leads.md#source-key) |
| 35 | Question the pass-through layer | Examine a wrapper whose interface adds work without hiding useful complexity. | [OUSTERHOUT](research/lesson-source-leads.md#source-key) |
| 36 | Give each layer a different abstraction | Follow a request through layers and identify where each one changes the level of meaning. | [OUSTERHOUT](research/lesson-source-leads.md#source-key), [CLEAN](research/lesson-source-leads.md#source-key) |
| 38 | Compose interchangeable behavior | Use composition to vary one policy without building a hierarchy for every combination. | [PATTERNS](research/lesson-source-leads.md#source-key), [METZ](research/lesson-source-leads.md#source-key) |
| 39 | Depend on stable promises | Point a volatile implementation at a stable collaborator contract. | [METZ](research/lesson-source-leads.md#source-key) |
| 40 | Design the interface twice | Compare two plausible boundaries before committing to the first generated design. | [OUSTERHOUT](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 44 | Use value objects to carry meaning | Replace interchangeable primitive values with representations that express units or domain rules. | [DDD](research/lesson-source-leads.md#source-key), [IDDD](research/lesson-source-leads.md#source-key) |
| 45 | Separate identity from attributes | Demonstrate why two records with matching fields may still represent different entities. | [DDD](research/lesson-source-leads.md#source-key) |
| 46 | Put consistency rules inside an aggregate | Choose the boundary within which a domain rule must hold atomically. | [DDD](research/lesson-source-leads.md#source-key), [IDDD](research/lesson-source-leads.md#source-key) |
| 47 | Make legal state transitions explicit | Replace scattered status checks with a model of allowed transitions. | [MODEL](research/lesson-source-leads.md#source-key), [DDD](research/lesson-source-leads.md#source-key) |
| 48 | Distinguish events from commands | Contrast a request to do something with a record that something happened. | [IDDD](research/lesson-source-leads.md#source-key) |
| 50 | Spend design effort on the core domain | Choose which decisions deserve bespoke modeling and which can use a simpler existing mechanism. | [DDD](research/lesson-source-leads.md#source-key), [PLATFORM](research/lesson-source-leads.md#source-key) |
| 100 | Let the masters disagree | Compare conflicting design advice on one concrete change and make the tradeoff explicit. | [OUSTERHOUT](research/lesson-source-leads.md#source-key), [METZ](research/lesson-source-leads.md#source-key), [CLEAN](research/lesson-source-leads.md#source-key) |

## 3. Writing great code

Teach the working rhythm: red, green, refactor, small coherent changes, and useful feedback. Tidy first when the refactoring makes the implementation easier. Include the minimum test mechanics needed for that workflow before examining test design in depth in part 4.

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 22 | Turn requirements into observable examples | Translate a desired capability into examples a human can review at its public boundary. | [TDD](research/lesson-source-leads.md#source-key), [GOOS](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 51 | Start with a test list | List the behavioral cases before choosing the first implementation step. | [TDD](research/lesson-source-leads.md#source-key) |
| 52 | Practice red, green, refactor | Write one meaningful failing test, implement enough to pass, then improve the structure while preserving behavior. | [TDD](research/lesson-source-leads.md#source-key) |
| 65 | Tidy first when it makes the implementation easier | Show a refactoring that simplifies the requested implementation, perform it first, then make the behavior change. Compare the cost with changing the code directly. | [TIDY](research/lesson-source-leads.md#source-key) |
| 66 | Separate structure from behavior in the diff | Make a cleanup and a feature independently understandable and reversible. | [TIDY](research/lesson-source-leads.md#source-key) |
| 17 | Use a spike to answer one question | Separate an experiment's learning objective from the obligations of production code. | [PRAGMATIC](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 20 | Turn stable procedures into scripts | Move repeatable mechanics out of repeated model deliberation and into a checkable tool. | [CONTEXT](research/lesson-source-leads.md#source-key), [PLATFORM](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 96 | Build a thin path through the whole system | Connect the major pieces with one end-to-end behavior before expanding each piece. | [GOOS](research/lesson-source-leads.md#source-key), [PRAGMATIC](research/lesson-source-leads.md#source-key) |
| 97 | Keep changes small enough to review | Compare human review effort and fault isolation for a large batch and several coherent changes. | [DELIVERY](research/lesson-source-leads.md#source-key), [TIDY](research/lesson-source-leads.md#source-key) |
| 77 | State a hypothesis before patching | Choose an experiment that distinguishes competing explanations of a failure. | [DEBUG](research/lesson-source-leads.md#source-key) |
| 78 | Reduce a failure to its smallest useful example | Remove irrelevant setup while preserving the behavior under investigation. | [DEBUG](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 80 | Bisect a regression | Use a known good and bad state to narrow the change that introduced a failure. | [DEBUG](research/lesson-source-leads.md#source-key), [HISTORY](research/lesson-source-leads.md#source-key) |

## 4. Writing great tests

Examine the quality of the evidence: contract tests, Metz's interface-testing guidance, trustworthy doubles, boundary cases, properties, and mutation testing. Use tests that protect the intended behavior while leaving implementation choices open.

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 53 | Derive expected results from the requirement | Catch a generated test that merely copies the implementation's answer. | [TESTING](research/lesson-source-leads.md#source-key), [TDD](research/lesson-source-leads.md#source-key) |
| 54 | Test a query through its result | Show how a result assertion can survive a change in the query's internals. | [METZ](research/lesson-source-leads.md#source-key) |
| 55 | Test both sides of a command appropriately | Separate the sender's obligation to issue a command from the receiver's obligation to carry it out. | [METZ](research/lesson-source-leads.md#source-key) |
| 56 | Keep private tests at the right scope | Decide which tests survive replacing an internal component and which belong to that retired component. | [METZ](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 57 | Keep doubles honest | Expose a green caller test whose substitute no longer matches the real collaborator. | [METZ](research/lesson-source-leads.md#source-key), [GOOS](research/lesson-source-leads.md#source-key) |
| 27 | Keep documentation and tests in agreement | Find a mismatch between an interface's written promise and its executable examples. | [METZ](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 58 | Derive boundary cases systematically | Choose examples at, below, and above a limit instead of inventing arbitrary test inputs. | [TESTING](research/lesson-source-leads.md#source-key) |
| 59 | Test properties across many examples | Check an invariant over generated inputs and inspect a minimized counterexample. | [TESTING](research/lesson-source-leads.md#source-key) |
| 60 | Challenge the tests with a deliberate fault | Use a small mutation to see whether the suite detects the behavior it claims to protect. | [MODEL](research/lesson-source-leads.md#source-key), [TESTING](research/lesson-source-leads.md#source-key) |
| 74 | Test interactions between correct components | Construct a case where two locally passing components disagree at their shared seam. | [MODEL](research/lesson-source-leads.md#source-key), [GOOS](research/lesson-source-leads.md#source-key) |
| 79 | Control time and randomness | Make a previously intermittent failure reproducible by controlling its inputs. | [TESTING](research/lesson-source-leads.md#source-key), [DEBUG](research/lesson-source-leads.md#source-key) |
| 89 | Test a shared-state race | Interleave two otherwise valid operations and check the required consistency rule. | [DATA](research/lesson-source-leads.md#source-key) |
| 93 | Regression-test the agent workflow | Keep representative tasks to evaluate a changed skill, prompt, or tool configuration. | [MODEL](research/lesson-source-leads.md#source-key), [PLATFORM](research/lesson-source-leads.md#source-key) |

## 5. Molding architecture using refactoring

Return to refactoring at the scale of responsibilities, seams, and module boundaries. Characterize existing behavior, choose an improvement, make explicit transformations, and preserve the relevant contracts. The earlier Tidy First lesson prepares a particular change. This section develops architectural changes through a sequence of refactorings.

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 61 | Characterize behavior before changing it | Capture what an unfamiliar component currently does and distinguish that from what it ought to do. | [LEGACY](research/lesson-source-leads.md#source-key) |
| 62 | Find a seam around a troublesome dependency | Make one behavior testable without requiring the whole production environment. | [LEGACY](research/lesson-source-leads.md#source-key) |
| 63 | Add a behavior beside the legacy tangle | Explore a sprout method or component as a bounded first change. | [LEGACY](research/lesson-source-leads.md#source-key) |
| 70 | Use history to choose the next improvement | Compare a frequently changed hotspot with equally messy code that rarely causes work. | [HISTORY](research/lesson-source-leads.md#source-key) |
| 67 | Name the refactoring move | Replace a vague cleanup request with one explicit transformation and preservation check. | [REFACTOR](research/lesson-source-leads.md#source-key) |
| 37 | Pull recurring complexity into its owner | Move a rule duplicated across callers behind the component responsible for it. | [OUSTERHOUT](research/lesson-source-leads.md#source-key) |
| 49 | Keep business rules with their owner | Move a domain decision out of workflow plumbing and into the component responsible for it. | [METZ](research/lesson-source-leads.md#source-key), [IDDD](research/lesson-source-leads.md#source-key), [ENTERPRISE](research/lesson-source-leads.md#source-key) |
| 68 | Distinguish duplicated knowledge from similar code | Examine whether two similar fragments really must change together. | [PRAGMATIC](research/lesson-source-leads.md#source-key) |
| 69 | Back out of the wrong abstraction | Try separating unlike cases before adding another option to an overloaded abstraction. | [METZ](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 30 | Replace internals against retained expectations | Run the same outer contract suite against two different implementations. | [PHOENIX](research/lesson-source-leads.md#source-key), [METZ](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 90 | Preserve durable data through a code rewrite | Include state compatibility and migration behavior in the replacement contract. | [DATA](research/lesson-source-leads.md#source-key), [PHOENIX](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |

## 6. Measuring our quality with static code analysis

Use static analysis to inspect types, complexity, duplication, dependency structure, mechanical rules, and potential security problems. Pair every signal with a concrete code question. The chapter includes change-amplification analysis as adjacent design evidence, while keeping test execution and history-based metrics distinct from static analysis. Tool references and evidence limits are recorded in [S03](research/curriculum-additions.md#s03-static-analysis-and-its-evidence-limits).

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 104 | Let types expose an incomplete change | Add a domain state and use an exhaustiveness check to locate the handler that no longer covers every case. | [STATIC](research/lesson-source-leads.md#source-key), [DDD](research/lesson-source-leads.md#source-key) |
| 105 | Investigate what a complexity score is telling you | Compare a nested function before and after a refactoring. Inspect its control flow and meaning alongside the analyzer score. | [STATIC](research/lesson-source-leads.md#source-key), [REFACTOR](research/lesson-source-leads.md#source-key) |
| 106 | Treat a duplication report as a design question | Inspect a reported duplicate and decide whether it represents shared knowledge or separately evolving behavior. | [STATIC](research/lesson-source-leads.md#source-key), [PRAGMATIC](research/lesson-source-leads.md#source-key) |
| 107 | Expose cycles in the dependency graph | Find a dependency cycle crossing a chosen module boundary and compare ways to remove it. | [STATIC](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 95 | Make an architectural rule executable | Use a fitness function to catch a forbidden dependency or broken boundary. | [EVOLUTION](research/lesson-source-leads.md#source-key), [STATIC](research/lesson-source-leads.md#source-key) |
| 108 | Automate a recurring review rule | Encode a repeated mechanical concern as a lint rule, then have the agent address its focused report and verify the result. | [STATIC](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 109 | Investigate a static security finding | Follow a reported path from untrusted input to a sensitive operation, confirm what the analyzer modeled, and demonstrate the relevant fix. | [STATIC](research/lesson-source-leads.md#source-key) |
| 34 | Measure change amplification | Count the places one small behavior change requires the agent to understand and edit. | [OUSTERHOUT](research/lesson-source-leads.md#source-key) |

## 7. Operations

Follow the code into use: observability first, then resilience, operational controls, and deployments. Include both application behavior and the agent workflow that delivers it. Feature flags and progressive exposure have primary source support in [S04](research/curriculum-additions.md#s04-feature-flags-and-progressive-exposure).

| ID | Candidate lesson | Small demonstration | Source leads |
|---|---|---|---|
| 112 | Instrument the customer journey | Trace one customer operation across module boundaries and collect enough context to investigate a simulated failure. | [OBSERVABILITY](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 91 | Trace a task across agent boundaries | Connect tool calls, handoffs, artifacts, and checks to one logical task. | [OBSERVABILITY](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 92 | Measure completed work alongside token use | Compare correctness, elapsed time, per-agent consumption, and total run consumption. | [DELIVERY](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 81 | Give every external operation a deadline | Trace how a stalled dependency consumes an agent's task budget. | [RELEASE](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 82 | Budget retries | Combine limited attempts, backoff, and a stopping condition for a failing dependency. | [RELEASE](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 83 | Recover from an uncertain write | Handle a timeout after submission by checking what happened before deciding what to do next. | [MODEL](research/lesson-source-leads.md#source-key), [DATA](research/lesson-source-leads.md#source-key) |
| 84 | Preserve operation identity across retries | Use one logical operation identifier to demonstrate duplicate-effect prevention. | [MODEL](research/lesson-source-leads.md#source-key), [DATA](research/lesson-source-leads.md#source-key) |
| 85 | Make cancellation release resources | Stop a task and check its subprocesses, locks, and temporary resources. | [RELEASE](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 86 | Stop hammering an unavailable dependency | Use a circuit breaker to demonstrate recovery behavior after repeated failures. | [RELEASE](research/lesson-source-leads.md#source-key) |
| 87 | Isolate a failing worker | Show a failure boundary that keeps one task from exhausting resources needed by others. | [RELEASE](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 88 | Control concurrency with backpressure | Compare unlimited fan-out with work admitted at a sustainable rate. | [RELEASE](research/lesson-source-leads.md#source-key), [DATA](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 110 | Make a feature flag an operational control | Exercise enabled and disabled paths during a simulated dependency failure, and specify when the flag should be retired. | [FLAGS](research/lesson-source-leads.md#source-key), [RELEASE](research/lesson-source-leads.md#source-key) |
| 94 | Verify the artifact that will actually run | Catch a case where checkout tests pass but the packaged artifact behaves differently. | [MODEL](research/lesson-source-leads.md#source-key) |
| 29 | Version a behavioral promise | Demonstrate an interface change that preserves an old caller while enabling a new one. | [DATA](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 64 | Expand, migrate, then remove | Evolve a schema or interface through compatible intermediate states. | [DATA](research/lesson-source-leads.md#source-key), [REFACTOR](research/lesson-source-leads.md#source-key), [MODEL](research/lesson-source-leads.md#source-key) |
| 111 | Release a change to a limited group first | Expose a new behavior gradually, with stated signals for continuing or stopping the rollout. | [FLAGS](research/lesson-source-leads.md#source-key), [RELEASE](research/lesson-source-leads.md#source-key) |
| 98 | Exercise rollback before relying on it | Demonstrate how a release can be reversed and what happens to state written by the new version. | [RELEASE](research/lesson-source-leads.md#source-key), [DATA](research/lesson-source-leads.md#source-key) |
