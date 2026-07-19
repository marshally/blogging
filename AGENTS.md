# AGENTS.md

Marshall Yount's blog-writing repo. Agents draft posts here; Marshall edits them; final posts get published to `posts/`.

## Repo layout

| Path | What it is |
|---|---|
| `docs/` | Orthogonal reference docs (see table of contents below) |
| `drafting/<slug>/` | Work-in-progress per post: research, outlines, drafts, decision log |
| `posts/` | Finalized posts, named `YYYY-MM-DD-slug.md` |
| `.claude/skills/` | Repo-local skills |

## Reference docs — table of contents

| Doc | When to load it |
|---|---|
| `docs/writing-style.md` | **Before drafting or revising any post prose.** This is the house-voice prompt; every draft must follow it. |
| `docs/2026-posting-strategy.md` | Before distribution, syndication, platform adaptation, or publishing-system work. It records approved platform decisions; do not infer content pillars or posting cadence. |
| `docs/wordpress-mcp.md` | When configuring, authenticating, or troubleshooting WordPress.com MCP access. |
| `docs/publishing-wordpress.md` | Before publishing or updating a post on WordPress: post creation, media upload, and conversion mechanics. |

## Drafting rules

1. **Always read `docs/writing-style.md` before writing or revising draft prose.** Not optional, not from memory — read the current version; it evolves after every finalized post.
2. **Commit every agent-authored draft immediately after writing it**, before Marshall touches it, with the `Co-Authored-By: Claude` trailer. This is load-bearing: the finalize workflow recovers Marshall's edits by diffing from the last agent-authored commit. An uncommitted agent draft destroys that signal.
3. **Marshall's edits to a draft are style signal, not noise.** Never overwrite, revert, or "clean up" his changes to a draft. When revising a draft he has edited, preserve his wording everywhere your revision doesn't specifically need to change it.
4. **Markdown paragraphs are single lines.** Never hard-wrap prose: each paragraph — including each footnote definition — is exactly one line in the markup. The only intentional in-paragraph line breaks are blockquote verse (lyric epigraphs).
5. **Marshall owns the big framing.** The extended metaphor and the piece's framing are his choices, not the agent's. But if you spot a non-tech domain whose match to the argument is extremely strong — the domain's own mechanics map onto the thesis at multiple points, not one cute parallel — raise it with him as a suggestion. Check it out with him; never weave it in unprompted.
6. **Style-fix commits are itemized for revert.** When applying a pass of style or de-telling fixes to a draft, make one commit per instance with the reason cited in the message — Marshall reverts individual calls he disagrees with. When a pass has dozens of mechanical instances (e.g. an em-dash conversion), relax to one commit per section. Never one blob commit.
7. **Claims trace to research.** Every factual claim, quote, and framework casting in an outline or draft must trace to an entry in the post's research files. A label with no research entry gets flagged "unsubstantiated" in the outline or logged in DECISIONS.md — never carried silently into a draft. Research files tier what they hold: verified (primary source), secondary, folklore (flagged as such), and a do-not-use ledger for caught fabrications and misattributed quotes, so a debunked quote can't re-enter the piece.
8. **Record explicit decisions as they happen.** During collaborative drafting, add Marshall's explicit selections, approvals, rejections, and stated rationales to the post's `DECISIONS.md` in the same revision that implements them. Project-specific choices stay ordinary decision entries. A potentially general voice or workflow lesson gets a `Style signal candidate:` line. Never wait until finalization to reconstruct decisions from a session transcript or infer them from agent-authored commits alone.

## Images

- Image files live in `drafting/<slug>/images/`.
- Every image — sourced or Marshall's own — gets a ledger entry in `drafting/<slug>/research/images.md`: name, what it shows, direct URL, source page, photographer/source, and exact license, with non-free entries (fair use, unclear license) explicitly flagged. `drafting/van-halen/research/images.md` is the exemplar format.
- Verify licenses by fetching the source page. Never invent or trust remembered URLs — verify each direct image URL exists.
- Marshall's own photos are named `YYYY-MM-DD-description.png`; sanity-check the date against the event before committing.
- Before placing an image, check its pixel dimensions and look for baked-in margins or whitespace.
- When editing a custom SVG or chart, audit every axis and relative position for unintended comparative claims. Treat each plotted point and its attached name, tagline, leader, and annotations as one movable group. Render and visually inspect the complete asset at its intended display size before committing.
- Full-res photos (multi-MB) get downscaled derivatives before publish; the publish-time asset step in the `finalize-post` skill owns that conversion.

## Commit policy

Commit as you go, in a series of orthogonal commits. Each commit contains one specific edit or idea — never a grab-bag of unrelated changes. Commits stack on top of each other, each delivering a tiny sliver of incremental value on the one before. Never batch a session's work into one omnibus commit at the end. This composes with drafting rule 2: the first complete draft is one commit, and every revision idea after it is its own commit on top, so Marshall's hand edits always diff cleanly against the latest agent-authored state.

When a draft contains both Marshall's unstaged prose and approved agent revisions, preserve the authorship boundary at the hunk level. Stage only the approved agent-authored hunks and leave every unrelated Marshall-authored hunk unstaged. Use any safe hunk-selective method; generated zero-context patches require `git apply --cached --unidiff-zero`. Commit Marshall-authored prose only on explicit request, and do not add a Claude co-author trailer to a commit containing only Marshall's prose.

## Finalizing a post

When Marshall approves a draft ("finalize it", "ship it", "this is done"), use the repo-local `finalize-post` skill (`.claude/skills/finalize-post/SKILL.md`). It publishes the post to `posts/` **and** harvests his edits into `docs/writing-style.md` — never publish by hand-copying the file, or the style learnings are lost.

## Publishing targets

- Posts publish to **yountlabs.com** (WordPress.com). Always pass `wpcom_site: "yountlabs.com"` explicitly to site-scoped MCP tools — the account-level abilities that would enumerate sites (user-sites, profile) are disabled in Marshall's MCP settings, so site discovery fails.
- `marshally.wordpress.com` is Marshall's personal blog, not a publish target: it is on the free WordPress.com plan, which blocks **all** MCP content operations.
