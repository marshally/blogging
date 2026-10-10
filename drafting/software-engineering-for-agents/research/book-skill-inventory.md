# Book sources for software engineering for agents

Reviewed 2026-10-10 at Marshall's direction. Source repository: `~/code/marshally/agent-skills`, clean checkout at `24c4701`. The software-engineering plugin contains 30 `book-*` skill bundles. That is a bundle count, not a count of distinct books: the Python POODR bundle adapts the Ruby book.

The inventory identifies material Marshall has already chosen to encode in skills. It does not establish that he has selected every book for this series. Selected concept and provenance sections were read for the candidates below. Skills are discovery aids and secondary syntheses, including where a skill calls its training knowledge a primary source. Book claims need actual author, publisher, or book evidence before publication. All agent applications below are proposed teaching examples, not claims made by the book authors.

## Verified primary sources for initial lessons

### B01: Ousterhout and deep modules

Local lead: [A Philosophy of Software Design skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-a-philosophy-of-software-design/SKILL.md). Book attribution, deep interfaces, information hiding, and the warning against excessive fragmentation are verified in [C01 and C02](sources.md#c02-deep-modules-and-information-hiding).

Proposed application: compare how much neighboring implementation an agent needs to inspect before using two interfaces with the same capability. A small interface must still communicate behavior, constraints, and failure semantics. Measure any claimed token saving in a demonstration.

### B02: Hunt and Thomas and orthogonality

Local lead: [The Pragmatic Programmer skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-the-pragmatic-programmer/SKILL.md). The [licensed book excerpt for Topic 10](https://www.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/f_0028.xhtml), checked 2026-10-10, verifies that orthogonality is a named topic and introduces independence. The preview ends before the full software treatment. The local skill supplies the more specific interpretation about localized changes, which remains secondary pending a complete source excerpt.

Proposed application: compare two task divisions by the dependencies and shared decisions they create. Independent filenames alone do not demonstrate independent work. Treat reduced agent coordination as a hypothesis to demonstrate, not a result established by the book excerpt.

### B03: Beck and incremental TDD

Local lead: [Test Driven Development by Example skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-tdd-by-example/SKILL.md). The [publisher page](https://www.informit.com/store/test-driven-development-by-example-9780137585274) verifies the title, author, and book structure. Beck's [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd), dated 2023-12-11 and checked 2026-10-10, explains a test list followed by one runnable test, implementation to pass it, and optional refactoring. His article explicitly connects this explanation to misunderstandings of the book. Identify it as a later author clarification, not a book quotation.

Proposed application: have an agent prove one requested behavior before expanding the implementation. Derive expected results from requirements, and inspect a meaningful failure before the implementation change. Tests can encode mistaken assumptions, so passing them is evidence with a scope, not proof of every requirement.

### B04: Feathers and seams

Local lead: [Working Effectively with Legacy Code skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-working-effectively-with-legacy-code/SKILL.md). Feathers' [publisher-hosted chapter excerpt on seams](https://www.informit.com/articles/article.aspx?p=359417&seqNum=2), dated 2005-01-21 and checked 2026-10-10, explains substituting behavior without editing at the substitution site. It shows how this can exclude troublesome dependencies or expose conditions for tests.

Proposed application: isolate one external dependency so an agent can run a focused check of the requested change. The seam's suitability must come from the actual code and behavior. Do not attribute every scorecard item in the local skill to Feathers.

### B05: Beck and separating kinds of change

Local lead: [Tidy First skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-tidy-first/SKILL.md). Beck's [Distinctions With A Difference](https://newsletter.kentbeck.com/p/distinctions-with-a-difference), dated 2022-12-05 and checked 2026-10-10, distinguishes structural changes from behavioral changes and argues for separating them. It also discusses choosing when to tidy. This is an author essay supporting the concept, not a verified passage from the later book.

Proposed application: give an agent a separate, reviewable structural change before a feature only when it makes that feature easier. Show the behavior-preservation check. Avoid converting the question in the book's title into an unconditional instruction to refactor first.

### B06: Hendrickson and exploratory charters

Local lead: [Explore It skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-elisabeth-hendrickson-explore-it/SKILL.md). The [publisher's book extract on charters](https://media.pragprog.com/titles/ehxta/charters.pdf), copyright 2013 and checked 2026-10-10, teaches focused exploration with enough direction to be useful and enough freedom to discover unexpected behavior. Its worked example questions a developer's assumption about reused validation.

Proposed application: give an adversarial reviewer a focused question about a risk and ask for a reproducible counterexample. This adapts exploratory testing to agent review. It does not establish that a separate reviewer or fresh context reliably eliminates correlated errors, nor does it credit Hendrickson with inventing adversarial agents.

### B07: Butcher and experimental debugging

Local lead: [Debug It skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-debug-it/SKILL.md). The [publisher's diagnosis chapter extract](https://media.pragprog.com/titles/pbdp/diagnosis.pdf), copyright 2009 and checked 2026-10-10, describes forming a hypothesis from observed behavior and designing experiments to support or refute it. Reproduction supplies the starting point.

Proposed application: require the debugging agent to state a hypothesis and a discriminating experiment before patching. Compare the evidence trail with a sequence of speculative edits. Any claim of better speed or lower token use needs measurements.

### B08: Metz on interfaces and tests

Local lead: [Practical Object-Oriented Design in Ruby skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-practical-object-oriented-design-in-ruby/SKILL.md). Marshall selected public/private interfaces and their tests for the model. [The dedicated Metz ledger](metz-interfaces-and-tests.md) verifies the message-testing defaults and exceptions in her own slides, real/double interface checks in her POODR source examples, and request/implementation separation in *99 Bottles of OOP*, coauthored with Katrina Owen and TJ Stankus. Exact POODR chapter 4 wording remains unverified.

Proposed application: preserve behavioral expectations at the chosen module boundary while allowing internal collaborators to change. Apply this at nested boundaries without making a child's interface public to every outer caller. Keep the source's testing defaults distinct from the series' human-reviewed agent workflow.

## Secondary leads for later lessons

### B09: Fowler and behavior-preserving refactoring

The [Refactoring skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-refactoring/SKILL.md) supplies named transformation leads. Candidate lesson: give an agent one transformation with a behavior-preservation check. Verify the chosen transformation against Fowler's source before outlining the episode.

### B10: Evans and domain language

The [Domain-Driven Design skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-domain-driven-design/SKILL.md) supplies ubiquitous-language and bounded-context leads. Candidate lesson: prevent agents from assigning different meanings to the same domain word. The later [S02 check](curriculum-additions.md#s02-domain-language-shared-with-customers) verifies shared language and bounded contexts against Evans' own reference. Other concept-specific verification remains pending. A bounded context in DDD is not an LLM context window.

### B11: Majors, Fong-Jones, and Miranda and observability

The [Observability Engineering skill](../../../../agent-skills/plugins/marshally-software-engineering/skills/book-observability-engineering/SKILL.md) supplies event and trace-context leads. Candidate lesson: reconstruct a delegated task through inputs, tool calls, results, and verification evidence. Verify the selected principle against the book or its authors before drafting. Keep later author positions distinct from the book's edition.

## Folklore and unsubstantiated claims

No book-to-agent mapping above establishes a quantitative improvement. The broader thesis that engineering fundamentals matter more with agents is Marshall's argument to develop through examples. Do not present the local skill inventory as a study demonstrating it.

## Do-not-use ledger

Do not turn skill-generated wording into author quotations, invent chapter/page citations, treat training-data reconstructions as verified book text, or imply authors anticipated the exact agent workflow proposed here. Do not count the POODR Python adaptation as a separate Sandi Metz book. Preserve disagreements between authors rather than averaging their advice into a supposed consensus.
