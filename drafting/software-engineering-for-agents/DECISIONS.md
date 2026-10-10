# Decisions for software engineering for agents

Recorded 2026-10-10 from Marshall's series proposal and follow-up answers. These are his explicit choices. The episode order, examples, and production suggestions in `README.md` remain proposals.

## D1. Central argument

Teach how software-engineering fundamentals become even more important in the age of agentic coding. The series combines agent-specific topics with principles from Marshall's favorite engineering books.

## D2. Opening model

Start with context-efficient, single-purpose agents that swarm together to solve problems. Each agent should have the context necessary to understand and solve its assigned problem, with progressive disclosure keeping that context manageable.

## D3. Token targets and accounting scope

Marshall proposed finishing below 250,000 tokens, preferably below 150,000. Asked whether this meant active context, cumulative per-agent consumption, or total swarm consumption, he selected: “Total tokens used by each agent to finish its task.” Use cumulative per-agent task consumption as the metric. Treat the numbers as his operating targets. They are not sourced universal performance thresholds.

## D4. Book principles and starting inventory

Present a concept from a book, then explain its importance for agentic coding. Marshall named deep modules from John Ousterhout as the example. He directed the initial book search to the book-based skills in `~/code/marshally/agent-skills`' software-engineering module. That inventory is a starting list, not an approval of every book or the proposed episode order.

## D5. Post and video unit

Each principle should fit a short blog post with a short video version for TikTok, YouTube, and LinkedIn. Exact length, recording style, and cadence are undecided. The platform selections apply to this series and extend the destinations described in the existing posting strategy.

## D6. Eventual course

Later weave the pieces together into a course. Marshall's working title is “what the masters of software engineering can teach us about doing ai coding better”. Preserve that framing while the curriculum develops.

## D7. Deep modules use recursive composition

Marshall identified tension in the assistant's claim that focused agents can work with substantial deep modules. A single file containing 100,000 tokens is not the intended architecture. Deep modules can use composition to isolate internal domains of functionality, recurring at smaller boundaries, like Russian dolls. The model must keep both caller context and internal maintenance context workable. The number is his counterexample, not a newly selected universal file-size limit.

## D8. Human steering centers on modules, seams, and contracts

Marshall identifies two benefits of deep-module boundaries: humans can carefully review the interface tests as a contract, and calling agents can load the interface file to understand usage without loading internals. He anticipates substantial human steering over which modules exist, the seams where they communicate, and the behavior observed at those seams. Preserve this as a central architectural argument. The brief's concrete export-test examples illustrate the idea and are not requirements Marshall has chosen for a real component.

## D9. Contracts support replaceable implementations

Marshall's third benefit is that unworkable internals can be rewritten while preserving the contract expressed in tests. He connects this to Chad Fowler's early microservices writing and current Phoenix architecture. The research verifies the current connection and an earlier talk, while the precise early blog article remains unidentified. Preserve replaceability as part of the argument. Passing the selected tests supplies assurance about what they cover, not an assertion that they exhaust every behavior or interaction. Separate review of contract changes is an assistant proposal in the brief, not an additional approval policy selected by Marshall.

## Research limits

The mappings from book principles to agent workflows are proposed applications. Quantified effects on token use, correctness, or speed remain unsubstantiated until demonstrated. The source ledgers distinguish verified primary evidence, secondary skill summaries, and unsupported claims. No additional general voice or workflow preference has been inferred from this conversation.
