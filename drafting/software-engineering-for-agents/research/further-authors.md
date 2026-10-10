# Further authors to consider

Checked: 2026-10-10. Status: researched candidates, not Marshall-selected influences. This is an internal research memo. Primary articles and author pages below were inspected. Recommendations and connections to the curriculum are editorial judgments. These sources do not establish Marshall's proposed cumulative token budgets as universal performance thresholds.

## Simon Willison

Follow: [Simon Willison's Weblog](https://simonwillison.net/guides/agentic-engineering-patterns/) and his [newsletter options](https://simonwillison.net/newsletters/).

- **Verified primary: [“Red/green TDD,” Simon Willison](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/).** A chapter in his evolving *Agentic Engineering Patterns* guide. He explicitly presents the short instruction “Use red/green TDD” as shorthand for writing tests first, observing failure, and implementing the change that makes them pass. This directly matches Marshall's interest in invoking established engineering concepts with very little prompt text. His claim about model understanding is practitioner guidance, not a controlled comparison across models.
- **Verified primary: [“Subagents,” Simon Willison](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/).** Explains isolated research context, parallel work, and specialist review/test/debugging agents, with a linked session transcript. Emphasizes preserving the parent agent's context and cautions against excessive specialization. The numerical context-window discussion concerns working context, not total tokens consumed per task.

Editorial fit: the strongest immediate recommendation for Marshall's latest point. His guide supplies short lessons, concrete prompts, and inspectable examples across context management, testing, and understanding generated code. The two chapters were inspected as current guide pages, without asserting an original publication date.

## Birgitta Böckeler

Follow: [Birgitta's personal content index](https://birgitta.info/) and the [Exploring Generative AI collection](https://martinfowler.com/articles/exploring-gen-ai.html). The latter includes multiple authors, so preserve each article's byline.

- **Verified primary: [“Context Engineering for Coding Agents,” Birgitta Böckeler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html), February 5, 2026.** Distinguishes reusable instructions, guidance, and interfaces for retrieving further context. Discusses selective loading, scoped rules, skills, subagents, and the risk of accumulating unnecessary or contradictory instructions. Tool feature descriptions are a dated snapshot. The durable connection is deciding what context is needed and when to load it.
- **Verified primary: [“TDD inside the agent loop - theater or actual value?”, Birgitta Böckeler](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html), August 10, 2026, per the collection index.** Describes a small exploratory comparison of agent workflows with and without TDD instructions. It did not establish a clear TDD advantage in that setup. Limitations include small greenfield tasks, model-based quality judgments, and imperfect adherence. She distinguishes human-authored expectations, human test-review checkpoints, and a fully autonomous test loop.

Editorial fit: especially valuable for challenging the series constructively. Her work invites us to explain which mechanisms make an engineering practice useful and how we know an agent actually followed it. The TDD article is not evidence that TDD generally fails. It strengthens the case for human review of meaningful contracts and independent expected results.

## Armin Ronacher

Follow: [Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/), which links RSS and Atom subscriptions.

- **Verified primary: [“Agentic Coding Recommendations,” Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/), June 12, 2025.** Covers simple code, fast tools with useful errors, concise logs, observability, ordinary command-line tools, isolation for parallel work, and refactoring when complexity obstructs an agent. His examples connect basic engineering decisions to the agent's ability to make progress. Language preferences and tool settings are personal, dated observations.
- **Verified presentation lead: [Armin's talk index](https://lucumr.pocoo.org/talks/).** Lists “Agentic Coding” on June 30, 2025 and “The Friction Is Your Judgment” at AI Engineer on April 10, 2026, with slides and recording links. The index was inspected, but these recordings were not reviewed.

Editorial fit: a strong bridge from architecture and readable code into operations. His discussion of tool output and logs is particularly useful for showing how observability also helps agents during development.

## Giles Edwards-Alexander

Follow: [overwatering.org](https://overwatering.org/).

- **Verified primary: [“The Economic Benefit of Refactoring,” Giles Edwards-Alexander](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html), July 30, 2026.** Describes decomposing an oversized module while preserving its interface, then repeating a representative change at successive stages. His prompt explicitly invokes Martin Fowler's *Refactoring*. The reported decrease in input tokens is unusually relevant to Marshall's thesis, but the counts were approximations based on agent-reported characters. One application and one change do not establish a general savings rate.
- **Verified primary: [“An Accidental Blackboard,” Giles Edwards-Alexander](https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html), September 2, 2026.** Reports agents coordinating through shared plans and frequent repository updates during a team exercise. Connects the behavior to the blackboard pattern and acknowledges reproducibility uncertainty and CI overhead.

Editorial fit: a particularly specific candidate for the refactoring and collaborating-agent segments. His experiments offer hypotheses Marshall could reproduce with stronger token instrumentation and repeated trials.

## Addy Osmani

Follow: [Addy Osmani's blog](https://addyosmani.com/blog/), which links his newsletter and social profiles.

- **Verified primary: [“Agentic Code Quality,” Addy Osmani](https://addyosmani.com/blog/agentic-code-quality/), August 8, 2026.** Proposes surrounding agents with complementary checks for behavior, types, architecture, security, performance, and maintainability. Discusses verification capacity and directing scarce human attention. His predictions about the future of review are his position, not demonstrated universal outcomes.
- **Verified primary: [“Brownfield Agentic Engineering,” Addy Osmani](https://addyosmani.com/blog/brownfield-agentic-engineering/), September 14, 2026.** Relevant sections inspected: documenting constraints that code does not reveal, retaining research across sessions, fresh-context review, characterization tests, and turning repeated corrections into executable checks. He treats older systems as repositories of behavioral obligations that an agent must discover before changing them.
- **Verified presentation companion: [“Own the Outer Loop,” Addy Osmani](https://addyosmani.com/blog/own-the-outer-loop/), July 15, 2026.** His blog identifies it as the written version of his AI Engineer World's Fair 2026 closing keynote. The page and its introduction were inspected. The recording was not reviewed.

Editorial fit: a close match for the series' human steering, test design, static analysis, and operations sections. His writing offers material for making quality expectations executable and carrying them through delivery.

## Geoffrey Huntley

Follow: [Geoffrey Huntley's site](https://ghuntley.com/), with articles, workshops, and speaking links.

- **Verified primary: [“How to build a coding agent: free workshop,” Geoffrey Huntley](https://ghuntley.com/agent/).** The written workshop walks through the agent loop, tool calls, and context allocation, with linked code. The text was inspected, not the full recording. Its model-specific capacities and broad performance claims should be treated as dated guidance requiring separate verification.
- **Verified primary: [“Ralph Wiggum as a ‘software engineer’,” Geoffrey Huntley](https://ghuntley.com/ralph/), page dated July 14, 2025 and containing later additions.** Describes the recurring agent loop, persistent plans, feedback, and intervention when the process goes wrong. His examples and economic claims are reports, not controlled benchmarks. The page links a conversation with Dex Horthy.

Editorial fit: useful for the mechanics behind autonomous loops and a provocative comparison with Marshall's emphasis on maintainability. Study concrete mechanisms and failure examples separately from his broader forecasts.

## Kent Beck

Follow: [Software Design: Tidy First?, Kent Beck](https://newsletter.kentbeck.com/t/genies), especially the Coding with Genies collection and Genie Sessions. This adds his contemporary experiments to the books already in the series.

- **Verified primary summary: [“Taming the Genie: ‘Like Kent Beck’,” Kent Beck](https://kentbeck.com/summaries/taming-the-genie-like-kent-beck/), January 20, 2026.** His own site summarizes an experiment distinguishing persona prompts from explicit design guidance. Particularly relevant to Marshall's interest in short references: a person's name can carry different direction from a specific named principle. The original newsletter article could not be fetched through the web tool, so only the author's summary and topic index were inspected. Do not infer experimental detail from third-party retellings.
- **Verified primary: [“Genie Lessons: Nobody Wants Agents,” Kent Beck](https://newsletter.kentbeck.com/p/genie-lessons-nobody-wants-agents), April 23, 2026.** The written lesson describes coordination overhead he experienced while working with a coordinator, implementer, and verifier. He argues that tools should help people achieve outcomes without transferring agent management back to them. This is his reported experience with one workflow. The page discloses sponsorship by Augment Code.

Editorial fit: a direct bridge from one of Marshall's chosen book authors to current experimentation. His work can help test when short references suffice, when explicit constraints matter, and when delegation costs more attention than it saves.
