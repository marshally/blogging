# Decisions for software engineering for agents

Recorded 2026-10-10 from Marshall's series proposal and follow-up answers. These are his explicit choices. The seven-part sequence selected in D13 governs the current plan. Individual episode order, examples, and production suggestions remain proposals.

## D1. Central argument

Teach how software-engineering fundamentals become even more important in the age of agentic coding. The series combines agent-specific topics with principles from Marshall's favorite engineering books.

## D2. Opening model

Start with context-efficient, single-purpose agents that swarm together to solve problems. Each agent should have the context necessary to understand and solve its assigned problem, with progressive disclosure keeping that context manageable.

## D3. Token targets and accounting scope

Marshall proposed finishing below 250,000 tokens, preferably below 150,000. Asked whether this meant active context, cumulative per-agent consumption, or total swarm consumption, he selected: “Total tokens used by each agent to finish its task.” Use cumulative per-agent task consumption as the metric. Treat the numbers as his operating targets. They are not sourced universal performance thresholds.

## D4. Book principles and starting inventory

Present a concept from a book, then explain its importance for agentic coding. Marshall named deep modules from John Ousterhout as the example. He directed the initial book search to the book-based skills in `~/code/marshally/agent-skills`' software-engineering module. That inventory is a starting list, not an approval of every book or the proposed episode order.

## D5. Post and video unit

Each principle should fit a short blog post with a short video version for TikTok, YouTube, and LinkedIn. Exact length, recording style, and cadence are undecided. The platform selections apply to this series and extend the destinations described in the existing posting strategy. D20 subsequently replaces the one-to-one production model with 2–10 videos per article.

## D6. Eventual course

Later weave the pieces together into a course. Marshall's original working title was “what the masters of software engineering can teach us about doing ai coding better”. Preserve that framing while the curriculum develops. D19 records the selected title.

## D7. Deep modules use recursive composition

Marshall identified tension in the assistant's claim that focused agents can work with substantial deep modules. A single file containing 100,000 tokens is not the intended architecture. Deep modules can use composition to isolate internal domains of functionality, recurring at smaller boundaries, like Russian dolls. The model must keep both caller context and internal maintenance context workable. The number is his counterexample, not a newly selected universal file-size limit.

## D8. Human steering centers on modules, seams, and contracts

Marshall identifies two benefits of deep-module boundaries: humans can carefully review the interface tests as a contract, and calling agents can load the interface file to understand usage without loading internals. He anticipates substantial human steering over which modules exist, the seams where they communicate, and the behavior observed at those seams. Preserve this as a central architectural argument. The brief's concrete export-test examples illustrate the idea and are not requirements Marshall has chosen for a real component.

## D9. Contracts support replaceable implementations

Marshall's third benefit is that unworkable internals can be rewritten while preserving the contract expressed in tests. He connects this to Chad Fowler's early microservices writing and current Phoenix architecture. The research verifies the current connection and an earlier talk, while the precise early blog article remains unidentified. Preserve replaceability as part of the argument. Passing the selected tests supplies assurance about what they cover, not an assertion that they exhaust every behavior or interaction. Separate review of contract changes is an assistant proposal in the brief, not an additional approval policy selected by Marshall.

## D10. Add Metz on public and private interfaces and testing

Marshall requested adding Sandi Metz's guidance on structuring public/private interfaces and testing them to the module model. The revision incorporates verified teaching on requests versus implementation, message-based testing, and test-double compatibility. Applying those ideas recursively to agent work and deciding which tests survive an internal rewrite are the series' synthesis. The added lesson's exact placement and example remain proposals. Record Metz's testing guidance with its exceptions rather than converting it into a universal prohibition on private tests or doubles.

## D11. Broaden the lesson menu

Marshall asked for a brainstorm of many more possibilities, suggesting 50 or 100 lessons. The revision supplies 100 candidates spanning agent mechanics and software-engineering fundamentals, each with a small demonstration and source leads. This expands the menu. It does not select all 100 for production, approve their order, or establish a publishing cadence. Newly proposed book connections require primary verification before becoming publication claims.

## D12. Show authors beside source titles

Marshall requested author names in the source-key table's “Starting point” column, exemplified by “The Pragmatic Programmer”, Dave Thomas and Andy Hunt. The table now includes full names and coauthors beside book titles, with edition qualifiers where needed to avoid ambiguous attribution.

## D13. Organize the series in seven parts

Marshall selected this order: (1) context efficient agent model, including narrowly focused adversarial reviews, (2) code architecture and design, (3) writing great code, (4) writing great tests, (5) molding architecture using refactoring, (6) measuring our quality with static code analysis, and (7) operations. This supersedes the earlier proposed alternating opening sequence.

Within architecture and design, he named deep modules, the Unix philosophy of small composable utilities that do one thing well, and domain-driven design. His stated domain-language requirement is that words in code be unambiguous and strictly match how the team talks to customers. Within writing great code, he named TDD's red, green, refactor cycle and Tidy First: when a refactoring makes the implementation easier, do it first. Operations includes observability, resilience such as circuit breakers and feature flags, and deployments.

The revision regroups all original 100 candidates under this sequence and adds 12 candidates to fill the newly explicit topics. Existing IDs are retained. These additions, their exact placement within each part, and the use of a recurring export example remain assistant proposals. The selected part order does not approve every candidate for production or establish a cadence.

## D14. Add Dex Horthy and Matt Pocock as contemporary influences

Marshall named Dex Horthy and Matt Pocock as additional influences and requested web searches for their writing and presentations on agentic coding. The research collects their own articles, repositories, recordings, and original event or interview pages, then maps selected material to the existing series. These influences complement the book sources. Their evolving recommendations are recorded as dated positions rather than treated as one fixed doctrine. This research does not change the selected seven-part order or Marshall's cumulative per-agent token targets.

## D15. Named principles as compact guidance

Marshall identified his favorite Pocock idea: a short phrase such as “deep modules (Ousterhout)” or “tracer bullets (The Pragmatic Programmer)” can trigger a model to work according to the reference material without spending substantial context on a detailed restatement. Make this a connection between the context-efficient agent model and the book-based lessons. The primary research in [P12](research/matt-pocock.md#p12-leading-words-as-compact-guidance) identifies Pocock's term, leading words, and records his explanation and examples. Neither Marshall's observation nor those sources establish a universal token saving or guarantee that a model applies a named concept correctly.

The added lesson candidate 113, its proposed comparison, and the suggestion to include a short invocation and observable result in each book lesson are assistant proposals implementing this emphasis. They do not select a specific episode for production or change the seven-part order.

## D16. Recommend further authors to follow

Marshall asked for other content authors in agentic coding similar to Pocock and Horthy. The [further-author research](research/further-authors.md) collects primary starting points and explains their relevance to his series. The recommendations remain candidates. This request does not select them as influences or approve additional lessons.

## D17. Weave contemporary authors through the lessons

Marshall requested integrating the recommended authors into the lesson ideas as source leads where appropriate. Add Simon Willison, Birgitta Böckeler, Armin Ronacher, Giles Edwards-Alexander, Addy Osmani, Geoffrey Huntley, and Kent Beck's contemporary agent writing to relevant existing candidates, alongside Pocock, Horthy, and the book sources. This supersedes the candidate-only status recorded in D16 for their use as source leads. Preserve author names in the source-key table's starting points.

The revision maps the researched material to existing lessons and labels useful counterpoints explicitly. It retains all 113 lesson IDs, titles, demonstrations, and the selected seven-part order. The individual mappings remain editorial applications. Selecting authors as source leads does not endorse every claim they make or approve all lessons for production.

## D18. Naming preferences: giants and primer

During title brainstorming for the series, book, or course, Marshall said he likes the concept of “standing on the shoulders of giants.” When exploring related expressions, he requested established English idioms rather than invented phrases. He subsequently said he likes “primer” as a term for the work. At this stage, these were naming preferences and the full title remained open. D19 records his subsequent selection.

## D19. Selected title

Marshall selected “Standing on the Shoulders of Giants: A Software Engineering Primer for Agentic Coding” as the full title. This supersedes the working title in D6 and resolves the naming question in D18. The planning brief now uses his exact wording.

## D20. Marketing plan and production sequence

On 2026-10-12, Marshall requested a very short, concise marketing plan. Write blog articles that can become book chapters, derive 2–10 short videos per article, use the content to pursue conference speaking, assemble and self-publish the book, use the demonstrated audience to pitch publishers, assemble the videos into a course, and optionally interview featured authors in a podcast. He anticipates hundreds of small pieces, one per topic. This supersedes D5's one-post/one-video unit without changing the lesson IDs or seven-part curriculum.

Marshall identified LinkedIn's push into short video as the opening and supplied a friend's results after 45 videos: 1,700 LinkedIn followers, 1,600 TikTok followers, and 700 Instagram followers. The [research note](research/marketing.md) preserves the report as an anecdote and distinguishes LinkedIn's verified investment in video from the hypothesis of better organic exposure.

The [marketing plan](marketing-plan.md) uses “The Vibe Engineer’s Primer,” Marshall's current wording for the effort. This is a working label for the plan, not an explicit replacement of the full title selected in D19. The draft prioritizes LinkedIn and includes TikTok, Instagram, and YouTube from the channel discussion. Instagram is a proposed series-specific extension to the general posting strategy. Account identity, handles, cadence, and numerical targets remain undecided. The subscriber path, measurement choices, and suggestions for adapting the book and course are editorial recommendations.

## D21. Append references on giving expertise away

On 2026-10-12, Marshall requested adding all three references from the attribution search to an appendix in the marketing plan: John Sonmez’s 90% free / 10% paid approach, Ramit Sethi’s statement about giving away 90% of his material, and Joe Pulizzi’s recommendation for well over 90% ungated content. The appendix includes source links, short quotations, context, and Sethi’s timestamp. [Research entries M04–M06](research/marketing.md#m04-john-sonmez-free-and-paid-content) record the evidence and attribution limits. This selects the references for inclusion without establishing the original source of the remembered advice or adopting a numerical free/paid target for the plan.

## D22. Lettered appendices and the free-content principle

On 2026-10-12, Marshall specified that the plan will have multiple appendix sections and named the existing section “Appendix A: Giving Expertise Away for Free.” He added the phrase “give 90% of what you know away for free, charge for the best 10%” to the consulting paragraph and requested linking it to Appendix A and committing the change. Preserve his wording. The phrase is his summary of the approach, including “the best 10%,” rather than a verbatim quotation attributed to one of the appendix’s sources. This adds an explicit free-content principle to the plan after D21’s reference-only selection.

## D23. Online-course opportunity appendix

On 2026-10-12, Marshall requested Appendix B on the large opportunity in online course sales, using Matt Pocock’s Pragmatic Engineer appearance and other accounts of how he entered courseware and its financial rewards. The appendix adds the origin story, reported sales milestones, workshop validation, publishing partnership and later change in demand. [Research entries M07–M10](research/marketing.md#m07-matt-pocock-on-the-pragmatic-engineer) distinguish primary testimony from audited financial evidence and the case’s implications from forecasts. Consulting remains the primary monetization objective in Marshall’s wording. Testing a paid workshop is an editorial suggestion, not an approved launch or revenue target.

## Research limits

The mappings from book principles to agent workflows are proposed applications. Quantified effects on token use, correctness, or speed remain unsubstantiated until demonstrated. The source ledgers distinguish verified primary evidence, secondary skill summaries, and unsupported claims. No additional general voice or workflow preference has been inferred from this conversation.
