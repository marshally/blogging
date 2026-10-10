# Dex Horthy: agentic coding sources

Research checked October 10, 2026. Internal research memo for the [lesson menu](../lesson-ideas.md). The author spells his name **Dex Horthy** and also appears as Dexter Horthy. This is a selected reading and viewing list, with his earlier advice distinguished from subsequent revisions. Curriculum connections below are our editorial synthesis.

## Evidence and retrieval

**Verified primary** means the material was retrieved from Horthy, HumanLayer, the original interviewer, or the conference publisher. It verifies what the source says, not every causal claim or reported productivity result. Each entry states whether its text, selected transcript passages, or only publication metadata was inspected. Video titles and channels were checked with YouTube's oEmbed endpoint where stated. No video was watched in full.

GitHub sources were inspected on `main`. The checked revisions were `humanlayer/12-factor-agents` at `d20c728368bf9c189d6d7aab704744decb6ec0cc` and `humanlayer/advanced-context-engineering-for-coding-agents` at `1a9b65e53bcf2052b7ef1778fbcfe2af65858a1e`. Branch links remain useful for following changes, while the revision links below preserve this pass's evidence.

### DH00. HumanLayer's own resource chronology

- **Source:** [HumanLayer - All Resources](https://www.humanlayer.dev/blog/humanlayer-resources), Dex Horthy. Page dated September 4, 2026, with later September items present when checked.
- **Evidence:** Verified primary. Full index text and linked destinations inspected. This is an evolving company chronology with promotional descriptions.
- **Use:** The most useful discovery index for his writing, presentations, interviews, and demonstrations. It groups the material into early agent engineering, coding context management, revisions to research-plan-implement, and software factories. Dates attributed to this index below are publication dates unless otherwise stated.

### DH01. 12-Factor Agents

- **Source:** [12-Factor Agents: Principles for building reliable LLM applications](https://github.com/humanlayer/12-factor-agents), Dex Horthy and contributors. April 15, 2025, according to DH00. [Checked README revision](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/README.md).
- **Companion presentation:** [12-Factor Agents: Patterns of reliable LLM applications](https://www.youtube.com/watch?v=8kMaTybvDUw), AI Engineer. Published July 3, 2025, according to DH00. [Original conference page](https://ai.engineer/talks/8kMaTybvDUw-12-factor-agents).
- **Evidence:** Verified primary. README and [factor 3](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-03-own-your-context-window.md) and [factor 10](https://github.com/humanlayer/12-factor-agents/blob/d20c728368bf9c189d6d7aab704744decb6ec0cc/content/factor-10-small-focused-agents.md) text inspected. Presentation title and AI Engineer channel verified through oEmbed, with the official overview inspected.
- **Takeaway:** Horthy places focused agents within software whose prompts, state, control flow, and errors remain explicit engineering concerns. Factor 3 illustrates shaping the information sent to a model. Factor 10 argues for bounded responsibilities that are easier to test and debug.
- **Series fit:** Part 1, especially IDs 6, 11, 15, and 19. Also a bridge to part 7 when discussing agent state and recovery. The guide primarily concerns building LLM applications, so applying it to a coding-agent swarm is a transfer we should explain.

### DH02. Advanced Context Engineering for Coding Agents

- **Source:** [Advanced Context Engineering for Coding Agents](https://www.humanlayer.dev/blog/advanced-context-engineering), Dex Horthy. The associated GitHub essay is dated August 29, 2025 in DH00. [Checked essay revision](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/1a9b65e53bcf2052b7ef1778fbcfe2af65858a1e/ace-fca.md).
- **Companion presentation:** [Advanced Context Engineering for Agents](https://www.youtube.com/watch?v=IS_y40zY-hc). The essay identifies a Y Combinator talk on August 20. DH00 dates the video publication August 25, 2025.
- **Evidence:** Verified primary. Essay sections on compaction, subagents, research-plan-implement, BAML examples, failed Parquet work, and human review inspected. Video destination retrieved from the author's index, video not reviewed.
- **Takeaway:** Research and plans serve as compact artifacts between stages. Exploration can run in a separate context and return focused findings. Horthy includes a failed investigation caused by inadequate understanding of dependencies, making this useful material about engineering judgment as well as context management.
- **Series fit:** Part 1, IDs 2, 5, 6, 9, and 15. Use the live-code investigation to motivate precise handoffs and preserving uncertainty. His team experiences illustrate the method without establishing a general productivity multiplier.

### DH03. No Vibes Allowed: Solving Hard Problems in Complex Codebases

- **Source:** [Original AI Engineer talk and transcript](https://ai.engineer/talks/rmvDxxNubIg-context-engineering-for-complex-codebases), Dex Horthy. AI Engineer Code 2025. [Video](https://www.youtube.com/watch?v=rmvDxxNubIg), published December 2, 2025 according to DH00.
- **Evidence:** Verified primary. Official overview and selected timestamped transcript passages inspected. Video title and AI Engineer channel verified through oEmbed.
- **Useful passages:** 6:35–8:15 on context isolation and research-plan-implement, 13:01–14:34 on progressive disclosure and fresh code research, 15:14–15:30 on code review, and 17:41–18:48 on adjusting process to task complexity.
- **Takeaway:** Assign subagents bounded investigations and return concise results. Repository guidance can be loaded by location, but its factual content can drift. Fresh research should follow the current code. He explicitly allows simpler workflows for simple changes.
- **Series fit:** Part 1, IDs 2, 5, 7, 11, and 19. At 15:14–15:23 he says the team's code is reviewed. Do not present this talk as an instruction to stop reading generated code.

### DH04. Dex Horthy and Matt Pocock together

- **Source:** [LIVE: Chat with AI Coding Wizard Dex Horthy](https://www.youtube.com/watch?v=NKu3T9FUjmU), hosted by Matt Pocock. January 2026 according to Horthy's own account in DH06. oEmbed currently returns this title, which differs from some search-result titles.
- **Evidence:** Verified primary metadata. Title and Matt Pocock channel verified through oEmbed. Full conversation and transcript were not reviewed. Horthy links a [segment beginning at 37:10](https://www.youtube.com/watch?v=NKu3T9FUjmU&t=2230) when discussing vertical slices in DH06.
- **Use:** A shared-influences viewing priority. Horthy's retrospective identifies their discussion of vertical slices and tracer bullets. Verify the exact conversational claims and speaker attribution before quoting or summarizing the segment in a post.
- **Series fit:** Part 3, ID 96, building a thin working path through the system, and ID 97, changes small enough to review. These mappings follow the subject Horthy attributes to the conversation, not an independently reviewed transcript.

### DH05. Everything We Got Wrong About Research-Plan-Implement

- **Source:** [Everything We Got Wrong About Research-Plan-Implement](https://www.youtube.com/watch?v=YwZR6tc7qYg), Dexter Horthy. Published March 24, 2026 according to DH00, which labels this recording “Lessons Learned Rolling Out RPI to Hundreds of Engineers.”
- **Evidence:** Verified primary metadata. Title and current publisher channel, AAIF Live, verified through oEmbed. The author's retrospective description was inspected. A full original transcript was not retrieved, so detailed talk claims remain a viewing task.
- **Related recording:** The author also links an [April 20, 2026 presentation](https://www.youtube.com/live/6IxSbMhT7v4?t=1947) under the same topic. Treat these as separate recordings, not interchangeable dates for one video.
- **Takeaway supported by the author's retrospective:** The workflow evolved toward smaller stages, explicit workflow control, and greater human ownership after the team's experience with unreviewed code. DH07 and DH08 provide accessible primary text for the revised position and current mechanics.
- **Series fit:** Part 1, IDs 8, 10, 15, and 99. A strong candidate for a lesson about revising a successful personal workflow when other people cannot reproduce its results.

### DH06. Why Software Factories Fail

- **Source:** [Why Software Factories Fail](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/1a9b65e53bcf2052b7ef1778fbcfe2af65858a1e/wsff.md), Dex Horthy. Essay published July 22, 2026 according to DH00. [Companion AI Engineer keynote](https://www.youtube.com/watch?v=Ib5GBkD555M), published July 23 according to the same index.
- **Evidence:** Verified primary. Essay passages on maintainability, the team's experience, system architecture, program design, and vertical slices inspected. Companion video's link and date came from the author's index, not a full viewing.
- **Takeaway:** Horthy argues that passing behavior checks can coexist with code becoming harder to change. He recommends human involvement in product decisions, system architecture, program design, and incremental delivery. Program design explicitly includes types, method signatures, layout, and call relationships. He cites Ousterhout, Robert C. Martin, and Martin Fowler as relevant foundations.
- **Series fit:** Parts 2–6, especially IDs 21, 28, 34, 40, 96, and 100. This directly supports the proposed bridge from older engineering books to agentic coding. His explanation of model incentives and broad maintainability limits is an argument to examine, not a universal result established by this essay.

### DH07. Context engineering with Dex Horthy

- **Source:** [Context engineering with Dex Horthy](https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy), interview by Gergely Orosz for The Pragmatic Engineer. July 15, 2026 according to DH00.
- **Evidence:** Verified primary host account. Published interview write-up, observations, references, and timestamp index inspected. Full recording not reviewed.
- **Takeaway:** The host records Horthy's revised view on owning generated production code, deliberate compaction, design review, and the limits of oversized implementation plans. The interview connects context management to broader software-factory design. Useful index points include RPI at 1:01:02, compaction at 1:06:18, and token use at 1:13:50.
- **Series fit:** Parts 1, 2, and 7, IDs 9, 21, 40, and 92. A useful later companion to DH02. Treat the host's account of the team's experience as reported experience, not independent measurement of the claimed outcome.

### DH08. Current HumanLayer workflow reference

- **Source:** [Skills and workflows reference](https://docs.humanlayer.com/reference/skills-workflows), HumanLayer. Undated documentation checked October 10, 2026. No personal author byline verified.
- **Evidence:** Verified primary company documentation. Workflow choices, research, design, outline, legacy planning, implementation, and artifact-role sections inspected. This documents current product behavior, not an immutable definition of Horthy's framework.
- **Takeaway:** The current RPI sequence is questions, research, design discussion, structure outline, implementation, and PR. A detailed plan is an older optional path. Research answers bounded questions against live code. Outlines describe vertical phases and checks. The documentation separately supports product and technical design artifacts.
- **Series fit:** Parts 1–3, IDs 8, 10, 15, 21, 96, and 99. A concrete example of evolving a large procedure into separately scoped stages. Here “TDD” names a technical design document. It does not mean the red-green-refactor practice in our part 3.

### DH09. Demonstrations to inspect next

These are primary viewing leads from DH00. Video destinations and the author's descriptions were retrieved, but the demonstrations themselves were not reviewed. They are useful candidates for finding concrete examples, not evidence that we reproduced their results.

| Recording | Published, per DH00 | What the author's index says it demonstrates |
|---|---|---|
| [Advanced Context Engineering for Coding Agents: AI That Works #17](https://www.youtube.com/watch?v=42AzKZRNhsk) | August 6, 2025 | Research-first work on a BAML bug, compared with planning without codebase research. |
| [No Vibes Allowed: Live Coding with AI Agents](https://www.youtube.com/watch?v=zNZs19fIDHk) | October 16, 2025 | Dex and Vaibhav Gupta taking timeout support through research, planning, and implementation. |

## Attribution and do-not-use ledger

- **Cumulative tokens are a separate quantity.** Marshall's preferred 150,000-token task target and 250,000-token ceiling measure total consumption by each agent. Horthy's active-context percentages and token thresholds do not validate those task budgets. Present any threshold as a dated, task-dependent practitioner heuristic. Evaluate our operating targets separately.
- **No universal productivity claim.** BAML anecdotes, code volume, and HumanLayer's reported speedups do not establish a controlled comparison or a promised result. Generated fixtures and other code generation can affect line counts. DH03 explicitly acknowledges this around 9:24.
- **No flattened chronology.** The August essay describes reducing Horthy's personal line-by-line review. The later 2025 conference transcript already says code is reviewed. Subsequent accounts describe a failed experiment and stronger ownership guidance. Preserve those distinctions when explaining the evolution.
- **No coinage claim from repetition.** Several sources credit Horthy with the term “context engineering.” This pass verifies his use and influence, not historical priority across all uses of the term.
- **HumanLayer bylines are not interchangeable.** [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents), March 12, 2026, and [Long-Context Isn't the Answer](https://www.hlyr.dev/blog/long-context-isnt-the-answer), March 23, 2026, are bylined Kyle. They are related company work, not verified Dex-authored essays. Their bylines and relevant context-management passages were checked.
- **Secondary discovery only.** Search returned third-party transcript mirrors, MLOps Talks summaries, and adaptation repositories. They helped locate originals but are not substantive evidence in this ledger. A summary site's claim is not a verified quotation from the speaker.
- **Not established here:** A universal instruction-count limit, a guarantee that review agents catch design failures, a proof that swarming beats a single agent, or a proof that models cannot produce maintainable code. No folklore has been promoted into the verified source list.

## Reading order and series opportunities

Start with DH03 for a compact presentation of context management, read DH02 for worked examples and failure cases, then pair DH05 with DH07 and DH08 so the series reflects the workflow's revisions. Read DH06 before shaping part 2. Watch DH04's vertical-slices segment when developing the part 3 tracer-bullet lesson. DH01 supplies reusable principles for both agent design and operations.

The strongest synthesis for this series is that boundaries carry several kinds of responsibility: they keep working context manageable, make assumptions and intended changes inspectable, and preserve human understanding as code production speeds up. That synthesis connects these sources to Marshall's module-contract model. It is our argument, not a quotation or a claim that Horthy has endorsed this exact curriculum.

Open work before publication: inspect the full March and April presentations, verify the joint livestream's relevant segment, and check any numerical or empirical claims against their original studies. Parts 4–7 still need their own testing, static-analysis, and operations sources. Horthy's writings give a useful connection to those subjects without replacing that research.
