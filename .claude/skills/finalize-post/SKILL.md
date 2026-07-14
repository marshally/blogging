---
name: finalize-post
description: Use when Marshall approves a blog post draft as done — "finalize it", "ship it", "publish this", "this is the final version" — or asks to harvest style learnings from his edits to a draft.
---

# Finalize Post

## Overview

Finalizing does two jobs, and the second is the one that's easy to skip: publish the
approved draft into `posts/`, and **harvest Marshall's edits as style signal** into
`docs/writing-style.md`. Every change he made to the agent draft is information about
his voice. Finalize time is the only moment that signal gets captured — publish without
harvesting and it's gone.

## Workflow

### 1. Identify the draft

The user-approved draft file under `drafting/<slug>/drafts/`: the one Marshall names,
else the one the post's README/DECISIONS marks as "current draft", else the newest. If
still ambiguous, ask — don't guess. The text in that file is final in substance:
publish it verbatim, except mechanical errors. A typo is never voice — fix spelling,
broken markdown, hyphenation, and internal inconsistencies on sight, listing the fixes
in the final report. Never alter wording, phrasing, or facts.

### 2. Find the agent baseline

The last agent-authored commit that touched the draft (agent commits carry the
`Co-Authored-By: Claude` trailer):

```bash
git log -n 1 --format='%H %ad %s' --grep='Co-Authored-By: Claude' -- <draft-file>
```

### 3. Extract Marshall's edits

```bash
git diff <baseline-sha> -- <draft-file>   # committed + uncommitted edits since baseline
```

Only the draft file's diff is style signal. Other modified files in the tree (research
notes, READMEs, unrelated work) are not — leave them out of the harvest and the commit.

- **Empty diff:** no edits — skip step 4, note in the final report that the draft
  shipped untouched, and continue.
- **Interleaved history** (an agent commit landed after Marshall started editing): the
  single diff misses earlier edits. Walk `git log -p --follow <draft-file>` and collect
  every change that is not part of an agent-authored commit.

### 4. Analyze the edits and update `docs/writing-style.md`

Classify each hunk: cut / addition / substitution / reorder / punctuation / formatting /
factual correction.

- **Factual corrections are not style.** Never put them in the style doc.
- For each style-relevant change, articulate the general rule it implies ("cuts hedging
  qualifiers before punchlines"), then place it in the existing section of
  `docs/writing-style.md` it belongs to. Amend a near-matching rule rather than adding a
  duplicate; if an edit contradicts a documented rule, the edit wins — rewrite the rule.
- Generalize to the principle, not the instance. The style doc holds general principles
  only; the triggering edit becomes the rule's example, never its scope. An edit removing
  "death" from a lesson implies a rule about heavy real-life topics; an edit cutting one
  joke implies a rule about when that device earns its place. If the rule you drafted
  only makes sense for this one post, you haven't found the rule yet.
- Write rules, not narrative. Nothing like "in the Van Halen post he changed X".
- **Unsure it generalizes?** Add it to an `## Emerging patterns (watch list)` section at
  the bottom of the doc. Promote to a rule when a later post confirms it; delete it when
  contradicted.

### 5. Publish

Copy the draft to `posts/YYYY-MM-DD-<slug>.md` (today's date; slug is the drafting
folder name, not the post title). "Verbatim" applies to the prose; the asset
references need work:

- Enumerate every image reference in the draft (markdown images, video thumbnails).
- Publish the referenced local assets where the `posts/` file can reach them
  (default: `posts/images/<slug>/` unless the repo has grown another convention),
  downscaling full-res originals first — honor any size notes in the post's
  `research/images.md` (multi-MB photos never ship at source resolution).
- Rewrite the draft's relative paths (`../images/…`) for the published file's
  location.
- After the copy, verify every image and thumbnail link in the published file
  resolves. A post with broken images is not published.

Leave `drafting/<slug>/` in place as the archive.

### 6. Commit and report

Stage **only** what this workflow produced — the new `posts/` file, its published
assets, and `docs/writing-style.md` — never `git add -A`; the tree may hold
unrelated work. Commit
them together (with the Claude trailer) and push. End with a report: where the post
landed, and each style learning recorded — quoting the edit that motivated it so
Marshall can veto misreadings.

## Common mistakes

| Mistake | Reality |
|---|---|
| Publish by copying the file, harvest "later" | Later never comes. Harvest before or with the publish commit. |
| Copy the markdown, forget the images | The draft references `../images/` paths that don't resolve from `posts/`. Publish the assets, rewrite the paths, verify every link. |
| Leave typos in "to preserve voice" | A typo is never voice. Fix mechanical errors on sight; never touch wording or substance. |
| Record a factual fix as a style rule | Content ≠ voice. Style doc gets style only. |
| Append every observation as a new bullet | Duplicates rot the doc. Amend existing rules; use the watch list for maybes. |
| Rewrite the style doc wholesale | Targeted edits only — the doc's structure and existing rules are themselves accumulated signal. |
