# Research ledger: software engineering for agents

Checked 2026-10-10. Internal planning reference, not post prose. Stable claim IDs below are intended for links from the series plan and future outlines. “Verified primary” means the source directly supports the attributed statement, not that a vendor's guidance or internal evaluation establishes a universal law. All concepts are paraphrased. No book quotations or page numbers have been verified.

## Source register

| ID | Primary source | Source date | Checked |
|---|---|---|---|
| S1 | John Ousterhout, [Software Design Book](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Updated 2021-11-16 | 2026-10-10 |
| S2 | John Ousterhout, Stanford CS 190, [Modular Design](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign) | Winter 2018 | 2026-10-10 |
| S3 | Anthropic Applied AI team, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 2025-09-29 | 2026-10-10 |
| S4 | Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | 2025-06-13 | 2026-10-10 |
| S5 | Barry Zhang, Keith Lazuka, Mahesh Murag, [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | 2025-10-16, update 2025-12-18 | 2026-10-10 |
| S6 | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) | Living documentation, no publication date shown | 2026-10-10 |

## Verified primary claims

### C01: Book attribution

John Ousterhout wrote *A Philosophy of Software Design*. His author page dates the second edition to July 2021 and identifies an expanded chapter on general-purpose modules and depth. Use his correct surname, Ousterhout. [S1](https://web.stanford.edu/~ouster/cgi-bin/book.php)

### C02: Deep modules and information hiding

Ousterhout's lecture describes depth as substantial functionality behind a simple interface. Interfaces include behavior, side effects, and usage constraints as well as signatures. Information hiding keeps knowledge and design decisions inside a module so callers need less knowledge and implementation changes can remain local. His notes credit David Parnas for information hiding. [S2, “Modular Design,” “Classes Should be Deep,” “Information Hiding”](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)

Depth does not mean few lines or many tiny classes. Ousterhout warns that excessive fragmentation adds interface complexity. He also recommends somewhat general-purpose interfaces rather than narrowly encoding today's use case. Keep this distinction when discussing focused agents. [S2, “Classes Should be Deep,” “Generic Classes are Deeper”](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)

### C03: Progressive disclosure and sufficient context

Anthropic recommends curating the smallest useful set of high-signal context while supplying enough information to guide behavior. Its progressive-disclosure approach retains references such as paths or links, then retrieves relevant detail during execution. This requires discoverable information and suitable tools. Exploration can add latency or follow dead ends, and some information can usefully be loaded at the start. [S3, “The anatomy of effective context,” “Context retrieval and agentic search”](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### C04: Focused agents can isolate exploratory context

Anthropic describes specialized subagents doing focused work in separate contexts and returning condensed findings to a coordinating agent. It also describes compaction and persistent notes as alternatives or complements for long tasks. This supports selective delegation as one context-management technique. It does not establish that every task should use multiple agents. [S3, “Context engineering for long-horizon tasks”](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### C05: Multi-agent gains depend on task structure and cost

Anthropic reports that its lead-agent/subagent research system outperformed a single-agent comparison on an internal research evaluation. Its reported strengths include independent avenues of investigation and broad searches. The report also says multi-agent systems consumed more tokens, increased coordination complexity, and fit poorly when workers needed the same context or had many interdependencies. These are findings about the reported research system and models, not evidence that swarms universally improve coding. [S4, “Benefits of a multi-agent system”](https://www.anthropic.com/engineering/multi-agent-research-system)

The team found delegation needed explicit objectives, output formats, source/tool guidance, and task boundaries to prevent duplicate work and gaps. [S4, “Prompt engineering and evaluations for research agents”](https://www.anthropic.com/engineering/multi-agent-research-system)

### C06: Skills offer a concrete disclosure mechanism

Anthropic's Skills design loads names and descriptions first, the relevant `SKILL.md` body when needed, and linked resources as the task requires them. This separates discovery metadata from procedural detail. Its examples also let agents execute scripts without reading the entire script into context. A skill packages capability and instructions, and need not be a separate agent. [S5, “The anatomy of a skill,” “Skills and code execution”](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### C07: Capacity, occupancy, and cumulative usage differ

Anthropic's API documentation describes a context window that must accommodate request contents and generated output. Instructions, messages, tool results, and tool definitions contribute. Prompt caching changes accounting categories, but cached input still occupies context. Thinking-token retention differs by model and configuration. Recheck those mechanics for the platform used in any demonstration. [S6, “How the context window works,” “The context window with thinking”](https://platform.claude.com/docs/en/build-with-claude/context-windows)

Use these working definitions for this series, derived from those mechanics:

| Term | What to measure |
|---|---|
| Context capacity | The configured model/runtime limit for a request, reserving room for output. |
| Current context occupancy | The tokens currently present for a particular call. Report peak occupancy separately when measuring a run. |
| Cumulative token usage | The sum of reported usage across calls for the chosen scope. State input/output categories, cache accounting, and whether coordinator and workers are included. Repeatedly supplied history can be counted repeatedly. |

A run can consume more tokens cumulatively than ever occupy one context. An isolated worker can reduce a coordinator's occupancy while increasing overall usage. These are accounting implications, not performance measurements. [S6](https://platform.claude.com/docs/en/build-with-claude/context-windows), [S4](https://www.anthropic.com/engineering/multi-agent-research-system)

## Proposed applications and evidence still needed

### A01: Engineering fundamentals as context design

Proposed series argument: a useful module boundary lets an agent solve a problem with fewer implementation details from elsewhere. Demonstrate this with the same concrete task against a leaking interface and a deep interface. The application combines [C02](#c02-deep-modules-and-information-hiding) with [C03](#c03-progressive-disclosure-and-sufficient-context). Ousterhout's sources do not discuss LLM agents or establish token savings.

### A02: Focused ownership with explicit handoffs

Proposed architecture: give each agent a bounded objective, sufficient initial context, paths to further detail, and a return contract carrying results, evidence, and unresolved dependencies. Delegate when work can be separated and reconciled. “Single purpose” describes ownership of the assigned outcome, not mandatory tiny functions or separate agents for every procedural step. This is a proposed synthesis of [C02](#c02-deep-modules-and-information-hiding), [C04](#c04-focused-agents-can-isolate-exploratory-context), and [C05](#c05-multi-agent-gains-depend-on-task-structure-and-cost).

### A03: The proposed 150,000 / 250,000 token budget

Marshall clarified that the budget means total tokens used by each agent to finish its task: preferably below 150,000 tokens, with a ceiling below 250,000. These are his operating targets for cumulative per-agent usage. They do not describe context-window occupancy or the combined spend of all agents. None of the sources above establishes either threshold as a general performance boundary. A later demonstration should report task success, model/runtime, the runtime's precise token-accounting categories, elapsed time, and verification evidence together.

### A04: Future topics need their own research

Adversarial review has not been researched here. Marshall directed the book inventory to the local `book-*` skills under `~/code/marshally/agent-skills/plugins/marshally-software-engineering/skills/`. Those sources are a separate research task. Add evidence before outlining future topics, and keep book concepts distinct from the series' original applications.

## Secondary sources

None used in this ledger.

## Folklore / unsubstantiated claims

“More agents always perform better,” “agents work best under 150,000 tokens,” and “a bigger context window removes the need for context engineering” are unsupported as universal claims here.

## Do-not-use ledger

No fabricated quotation was encountered. Exclude invented Ousterhout quotations or page references, claims that he prescribes tiny single-purpose modules, generalizations from Anthropic's research evaluation to all coding tasks, and presentations of Marshall's proposed token budgets as established model limits. Do not treat skill activation as proof that a separate agent was created.
