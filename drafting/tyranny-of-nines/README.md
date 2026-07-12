# The Tyranny of Nines

Blog post project: a remembered lesson from Sean Kilgore at Twilio becomes a practical
way to reason about service availability, AWS SLAs, dependency chains, redundancy, and
the architectural price of promising another nine.

## Status

- **Current phase:** drafting — first draft written, awaiting Marshall's edits
- **Current outline:** `outlines/outline-3k.md`
- **Draft:** `drafts/draft-1.md`
- **Target length:** approximately 3,600 words (provisional; grew with the cost and degraded-mode sections)
- **Primary reader takeaway:** **ALL multiplies availability. ANY multiplies
  unavailability.**

## Repo map

| Path | What it is |
|---|---|
| `DECISIONS.md` | Settled choices and factual/editorial guardrails |
| `outlines/outline-3k.md` | Narrative outline with section budgets and loaded guns |
| `research/story-notes.md` | Known facts, unknowns, and constraints for the Twilio story |
| `research/availability-math.md` | Series/parallel math, assumptions, and downtime conversions |
| `research/aws-slas.md` | Current AWS SLA snapshot for the services in the example |
| `research/worked-example.md` | Candidate request paths and checked calculations |
| `research/multi-region.md` | What multi-Region does, what it costs, and why it can fail |
| `research/sources.md` | Primary-source bibliography and claim map |
| `drafts/README.md` | Drafting gate; no article draft exists yet |

The house-voice prompt lives at `/docs/writing-style.md`. Read its current version
before drafting or revising prose.

## Open questions

None blocking. Exact SLO/SLA targets, Sean's exact words, and the immediate setting remain unremembered and stay out of the draft (D2, `research/story-notes.md`).

## Recently resolved (2026-07-12)

- No extended metaphor; the teaching story carries the structure (D10).
- The anchor operation is the database request, used consistently throughout (D11).
- The reader makes the naive inventory multiplication before request paths break it (D12).
- The next nine's price is engineering/ops brainpower, not a 2x hosting bill (D13); the beat combines quasi-math compression with the `distributed-systems problem` punchline.
- ElastiCache (historically Redis, Multi-AZ) is dropped from the worked example (D14).
- S3 enters as a degraded-mode dependency, with before/after arithmetic (D15).
- Story anchors: first-time internal SLO adoption (Google SRE book tradition), probably 2020, Multi-AZ but single-Region platform (D16).

## Resuming work with an AI assistant

Feed it, in order: `DECISIONS.md`, `/docs/writing-style.md`, the current outline, then
the research file relevant to the task. Do not invent dialogue, setting, timing, or
Twilio architecture details to make the anecdote more vivid.
