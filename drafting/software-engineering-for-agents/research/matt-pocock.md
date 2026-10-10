# Matt Pocock on agentic coding

Researched 2026-10-10 at Marshall's request. This is a selected reading and viewing guide for the seven-part series, not a complete bibliography. AI Hero and Total TypeScript are Pocock's sites. Repository files were inspected as source material, not invoked as workflows. Lesson IDs refer to the existing menu and remain proposals for how to teach these ideas.

## Evidence and dates

The entries below distinguish an author's written argument, an event recording with a host transcript, and executable workflow instructions. These are primary evidence for what Pocock teaches and does. They do not independently demonstrate universal performance improvements. AI Hero's displayed dates say “Updated” and should not be represented as original publication dates. Videos with written companions were researched through the companion text unless stated otherwise. No claim here relies on having watched the entire recording.

## P01: Full Walkthrough: Workflow for AI Coding

Sources: [official AI Engineer talk and transcript](https://ai.engineer/talks/-QFHIoCo-Ko) and [original recording](https://www.youtube.com/watch?v=-QFHIoCo-Ko). AI Engineer Europe 2026, duration 1:36:30. YouTube's indexed first-party listing gives an upload date of 2026-04-24. The exact presentation date was not independently checked. YouTube oEmbed confirmed the title and AI Engineer channel.

Inspected: the host's overview and selected transcript passages. The workshop connects human alignment, requirements, vertical slices, implementation, and review. Particularly useful passages are approximately 1:05:24–1:06:15 on review in a fresh context, 1:06:43–1:08:24 on TDD, and 1:16:37–1:18:46 on testable deep modules and maintaining a human mental map of the design.

Series fit: parts 1–4, especially lessons 12–15, 18, 21, 31, 52, and 96. Proposed teaching use: follow one small feature through the workflow, then isolate each engineering principle for a short lesson. Context-window heuristics in this talk concern active context, a different measurement from Marshall's cumulative per-agent task budget.

## P02: A Complete Guide To AGENTS.md

Source: [article](https://www.aihero.dev/a-complete-guide-to-agents-md), updated 2026-01-18. Primary article text inspected.

Pocock recommends small persistent instruction files, links to focused guidance, nested disclosure, and removing stale or conflicting instructions. He also discusses skill loading as another way to introduce guidance when needed.

Series fit: part 1, lessons 2, 3, 7, and 10. Proposed example: compare a broad instruction dump with an index that routes an agent to the contract and procedure needed for one task. The article's instruction-count estimates cite other work and need separate verification. Tool-specific instruction loading rules must be checked against the runtime used in a demonstration.

## P03: How To Make Codebases AI Agents Love

Source: [video page and written companion](https://www.aihero.dev/how-to-make-codebases-ai-agents-love), updated 2026-02-26. Primary companion text inspected. AI Hero labels it as a video, but the underlying media was not independently played.

Pocock explicitly applies Ousterhout's deep modules to agent navigation: expose a clear interface, organize the implementation behind it, and test meaningful behavior at that boundary. He places human attention on interface design and uses the interface to disclose complexity progressively.

Series fit: parts 2, 4, and 5, lessons 4, 21, 30–32, and 56. This is a close contemporary influence on Marshall's model. Preserve the series' qualification that retained tests supply scoped evidence. The article's stronger suggestion that passing tests eliminates the need to inspect internals is advice to examine, not a correctness guarantee.

## P04: The /codebase-design Skill

Source: [current explanatory page](https://www.aihero.dev/skills-codebase-design), updated 2026-08-24, and [pinned skill source](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md). Relevant page sections and full skill source inspected.

Its interface vocabulary includes invariants, ordering, errors, configuration, and performance characteristics as well as type signatures. It explicitly permits a deep module to contain smaller internal parts and private seams. It also proposes examining where complexity would move if a module were removed.

Series fit: part 2, lessons 24, 31–35, and 40, and part 5, lessons 37 and 69. This directly supports investigating Marshall's recursive-composition model. Attribute the vocabulary and heuristics to Pocock. His description of Ousterhout's definition needs checking against Ousterhout before repeating it as a book claim. Do not silently adopt the skill's absolute seam rules as general laws.

## P05: My Skill Makes Claude Code GREAT At TDD

Source: [video page and written companion](https://www.aihero.dev/skill-test-driven-development-claude-code), updated 2026-02-10. Primary companion text inspected.

The teaching sequence uses one behavior at a time: a failing test, minimal implementation, and refactoring after tests pass. It favors public-interface behavior over assertions tied to internal structure and contrasts incremental work with generating a whole test layer and implementation layer separately.

Series fit: parts 3 and 4, lessons 51–57. Proposed example: give an agent an independent expected result, observe the relevant failure, and implement the behavior. A failing test alone cannot establish that a test is meaningful or prevent all misleading implementations. Read this alongside Metz's more contextual treatment of messages, collaborators, and testing exceptions. P10 records a later change in the repository's treatment of refactoring.

## P06: Tracer Bullets: Keeping AI Slop Under Control

Source: [article](https://www.aihero.dev/tracer-bullets), updated 2026-01-22. Primary article text inspected.

Pocock credits *The Pragmatic Programmer* and proposes implementing a narrow path through the system to obtain feedback before expanding it. His example connects a backend operation to one UI location before extending it to the remaining locations.

Series fit: parts 1 and 3, lessons 12, 14, 96, and 97. This is an explicit bridge between a classic book and agentic coding, matching Marshall's planned format. Verify the original book passage when teaching the book's concept. Treat Pocock's reported results as his experience, not a controlled comparison.

## P07: Essential AI Coding Feedback Loops For TypeScript Projects

Source: [video page and written companion](https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects), updated 2026-01-16. Primary companion text inspected.

The demonstration combines type checking, automated tests, commit hooks, formatting, and linting so an agent can receive actionable feedback while working. It also points to exercising the running application.

Series fit: parts 3, 4, and 6, especially lessons 52, 104, and 108. Proposed example: let a type or lint failure identify a specific problem, correct it, and verify the behavior separately. Distinguish static checks, test execution, and application checks. The series need not adopt the exact JavaScript tooling shown in the article.

## P08: AI Skills for Real Engineers

Source: [article and skill-system overview](https://www.aihero.dev/skills-post), updated 2026-04-27. Primary article text inspected.

Pocock describes small inspectable skills that compose into planning, domain clarification, requirements, vertical slices, and implementation. This snapshot uses names including `domain-model`, `to-prd`, and `to-issues`.

Series fit: part 1, lessons 10 and 99, and part 2, lesson 41. Useful teaching material: give a reusable procedure a clear purpose and arrange skills so the agent loads the relevant one. Treat command names as a dated snapshot. The later changelog and current source show that the workflow has evolved.

## P09: Skills Changelog: Ubiquitous Language -> /grill-with-docs

Source: [video page and written companion](https://www.aihero.dev/skills-changelog-ubiquitous-language-grill-with-docs), updated 2026-04-30. Relevant primary companion sections inspected.

The changelog combines a planning interview with persistent domain documentation. It supports distinct bounded contexts and records architectural decisions when their rationale would otherwise be lost. It also explains a more explicit vocabulary for discussing interfaces and implementations.

Series fit: parts 1 and 2, lessons 8, 15, 41, and 42. Proposed example: catch a term whose meaning changes between the customer conversation and the proposed implementation, resolve it, and record the chosen meaning. This is practical agent-workflow material to pair with Evans' original concept.

## P10: The current skills repository as an implementation artifact

Source: [mattpocock/skills](https://github.com/mattpocock/skills). GitHub API resolved `main` to `49dd158d1076134a641b33efb035946536778336`, committed 2026-10-09, during this research. Inspected the full pinned `codebase-design` and `tdd` files and selected review instructions.

The [review skill](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md) separates standards and specification review into agents with distinct briefs and reports. It distinguishes heuristic smells from hard violations and avoids repeating checks already enforced by tooling. Series fit: part 1, lessons 18, 71, 73, and 75, plus part 6.

The [TDD skill](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md) now puts refactoring in the review stage outside its red–green implementation loop. It also requires independent expected values and behavior tests at agreed seams. This differs from P05's presentation of red–green–refactor. Preserve both snapshots as evidence of an evolving workflow. Marshall's selected red–green–refactor curriculum remains unchanged.

## P11: 11 Tips For AI Coding With Ralph Wiggum

Source: [article](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum), updated 2026-01-08. Selected sections on feedback, step size, and prioritizing risk inspected.

Pocock describes a tradeoff between small tasks that receive frequent feedback and the startup cost of repeatedly selecting work and exploring a repository. He recommends trying uncertain integrations early and using explicit checks in unattended loops.

Series fit: parts 1 and 3, lessons 1, 13, 17, 19, 96, and 97. This supplies a useful counterweight to splitting every assignment as small as possible. It is a tutorial for applying the Ralph approach, not evidence that Pocock originated it. The numeric token limits chosen for this series remain Marshall's own operating targets.

## Reading and viewing priority

Start with P03 for the closest architectural connection, P01 for the overall workflow, and P02 for progressive disclosure. Then use P05–P07 for the code, tests, and static-analysis sections. P09 and P10 matter when discussing present-day domain and review practices. P04 and P11 help examine the tension between useful decomposition and excessive fragmentation.

## Limits and do-not-use ledger

- No new quotation is proposed. Preserve exact source attribution when developing scripts or posts.
- Do not turn context-window heuristics into evidence for cumulative task-token limits.
- Do not turn passing tests, typed code, or repeated reviewer agreement into comprehensive correctness claims.
- Do not combine an older article's skill names with current repository behavior and describe the result as one unchanged workflow.
- The accessible [Total TypeScript article titled The Case for TypeScript In The AI Coding Era](https://www.totaltypescript.com/the-case-for-typescript-in-the-ai-coding-era) exposed only its introduction. It remains an incomplete lead. P07 is the stronger inspected source for practical feedback loops.
- Third-party summaries helped discovery but are not the evidence for claims in this ledger. Conference abstracts and host summaries establish intended coverage. The selected transcript passages provide stronger evidence for the details recorded in P01.
