# The Tyranny of Nines

Blog post project: a remembered lesson from Sean Kilgore at Twilio becomes a practical
way to reason about service availability, AWS SLAs, dependency chains, redundancy, and
the architectural price of promising another nine.

## Status

- **Current phase:** research and outline
- **Current outline:** `outlines/outline-3k.md`
- **Draft:** not started
- **Target length:** approximately 3,000 words (provisional)
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

1. What customer-visible operation should anchor the worked example?
2. Was the original Twilio platform Multi-AZ? Multi-Region?
3. Which ElastiCache engine and topology did it use?
4. Was S3 synchronously required for the anchor operation, or could it degrade/fail
   independently?
5. What customer SLA was under discussion, if remembered?
6. Roughly when did the conversation occur? Current SLA figures will remain clearly
   separated from the historical anecdote regardless.
7. Should the financial `availability budget` frame serve as the piece's one extended
   metaphor, or should the story carry the structure without an additional metaphor?

## Resuming work with an AI assistant

Feed it, in order: `DECISIONS.md`, `/docs/writing-style.md`, the current outline, then
the research file relevant to the task. Do not invent dialogue, setting, timing, or
Twilio architecture details to make the anecdote more vivid.
