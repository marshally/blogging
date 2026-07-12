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

## Drafting rules

1. **Always read `docs/writing-style.md` before writing or revising draft prose.** Not optional, not from memory — read the current version; it evolves after every finalized post.
2. **Commit every agent-authored draft immediately after writing it**, before Marshall touches it, with the `Co-Authored-By: Claude` trailer. This is load-bearing: the finalize workflow recovers Marshall's edits by diffing from the last agent-authored commit. An uncommitted agent draft destroys that signal.
3. **Marshall's edits to a draft are style signal, not noise.** Never overwrite, revert, or "clean up" his changes to a draft. When revising a draft he has edited, preserve his wording everywhere your revision doesn't specifically need to change it.
4. **Markdown paragraphs are single lines.** Never hard-wrap prose: each paragraph — including each footnote definition — is exactly one line in the markup. The only intentional in-paragraph line breaks are blockquote verse (lyric epigraphs).

## Finalizing a post

When Marshall approves a draft ("finalize it", "ship it", "this is done"), use the repo-local `finalize-post` skill (`.claude/skills/finalize-post/SKILL.md`). It publishes the post to `posts/` **and** harvests his edits into `docs/writing-style.md` — never publish by hand-copying the file, or the style learnings are lost.
