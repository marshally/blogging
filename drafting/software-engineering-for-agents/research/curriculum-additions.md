# Sources for the seven-part curriculum

Checked 2026-10-10 after Marshall selected the sequence and added Unix composition, customer-aligned domain language, static analysis, and operational controls. These entries support the named concepts. Agent demonstrations remain proposals until implemented and measured.

## S01: Unix composition

Primary starting point: [*The Art of Unix Programming*, Eric S. Raymond](https://catb.org/~esr/writings/taoup/html/index.html), especially [Basics of the Unix Philosophy](https://catb.org/esr/writings/taoup/html/ch01s06.html). The author's indexed chapter excerpts describe focused programs, simple interfaces, composition through streams, and separating policy from mechanism. Direct chapter fetches failed during this check, so the evidence inspected was the search index's excerpts of the author's own text. Verify the full passage before quoting or making a historical attribution.

Proposed lessons: give a utility one coherent job, compose utilities through explicit input/output contracts, and separate reusable mechanisms from workflow policy. Relate these to deep modules through a concrete design comparison. Neither source establishes an ideal file length or proves that dividing work into more programs improves agent performance.

## S02: Domain language shared with customers

Verified primary source: [*Domain-Driven Design Reference*, Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), printed pages 2–4 (PDF pages 9–11). Evans describes consistency within a bounded context and a shared language used in code, diagrams, writing, and speech. Domain experts and developers refine the model together and resolve ambiguous terms.

Marshall's teaching emphasis is that domain terms in code should be unambiguous and strictly match the language used with customers. Proposed demonstration: trace a customer scenario through requirements, tests, and code, then resolve a conflicting term with the customer. Keep that consistency scoped to the relevant domain. Different bounded contexts can have different meanings, with explicit translation where they meet. This does not prescribe a single global vocabulary or mechanically copying ambiguous customer wording.

## S03: Static analysis and its evidence limits

Verified primary tool references:

- [SonarQube 10.6 metric definitions](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/code-metrics/metrics-definition), SonarSource: definitions for complexity and duplicated-code measures. This is a versioned reference for concepts, not a recommendation to install that release. Verify definitions against the analyzer used for a demonstration.
- [TypeScript handbook: narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), TypeScript contributors: exhaustiveness checking can expose a newly added union case that a handler omits.
- [ESLint core concepts](https://eslint.org/docs/latest/use/core-concepts/), ESLint contributors: configurable rules detect violations, with a distinction between automatic fixes and suggestions that may change logic.
- [dependency-cruiser rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md), Sander Verweij and contributors: dependency rules and cycle checks can operate at module or folder scope. Indexed repository excerpts inspected.
- [CodeQL data-flow analysis](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/), GitHub: data-flow and taint analyses track modeled relationships through code. Findings depend on what the analysis models.

Proposed lessons: type-check a changed contract, inspect a complexity warning, evaluate a duplication report, expose a dependency cycle, automate a recurring lint rule, and investigate a security data-flow warning. Compare the actual code and behavior before and after any fix. Static signals measure selected properties and reveal possible problems. A lower score or clean report does not establish overall correctness, useful design, or runtime reliability. Test coverage and mutation results belong with dynamic test evidence, and Git change frequency belongs with historical evidence.

## S04: Feature flags and progressive exposure

Verified primary source: [Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html), Pete Hodgson. The article distinguishes release, experiment, operations, and permissioning toggles. It describes operational controls for disabling or degrading features and introduces canary exposure. It also discusses toggle lifetime and carrying cost.

Proposed lessons: exercise an operational flag's enabled and disabled paths, then plan its retirement where appropriate. Separately, roll out a changed behavior to a limited group and use stated signals to continue or stop. The flag example complements the circuit-breaker material. Do not claim that every feature flag provides resilience, or that disabling a flag reverses data already written.

## Folklore and exclusions

No new quotation is proposed. Do not attribute the Unix tradition's invention to Raymond, turn metric thresholds into universal quality laws, or describe a candidate demonstration as a measured result. Specific tool selections and lesson counts are editorial proposals.
