# Story Notes: Sean, Twilio, and the remembered lesson

## Known facts supplied by Marshall

- Sean Kilgore is a software architect/staff-plus type engineer.
- Sean taught Marshall a great deal about leading large teams from the IC chair.
- They were building platform tools at Twilio.
- Marshall initially tried to build an SLA from expected downtime associated with
  different activities.
- Sean showed him that vendor SLAs establish a boundary first: even if the team and
  application were perfect, the underlying services constrain what can be supported.
- The platform used EC2, Application Load Balancer, ElastiCache, RDS, and S3.
- Marshall does not remember exact quotations from the exchange.
- A further lesson is that a single Region is a failure boundary. A service that must
  remain available through Regional failure needs a multi-Region design.
- The most important reader lesson is the distinction between `ALL` and `ANY`:
  required components multiply availability; redundant alternatives multiply
  unavailability.

## Unknown; do not invent

- Date or approximate year.
- Office, room, call, whiteboard, document, spreadsheet program, or other setting.
- The immediate business trigger or customer.
- The precise SLA target under discussion.
- Exact downtime activities or estimates Marshall originally listed.
- Sean's exact words, gestures, or order of questions.
- The exact synchronous customer operation.
- Whether ElastiCache was Redis or Memcached and whether it was Multi-AZ.
- Whether RDS and the compute fleet were Multi-AZ.
- Whether S3 was a hard dependency for the anchor request.
- Whether the platform was single-Region or multi-Region at the time.

## Safe narrative technique

- Report the lesson in indirect speech.
- Say that the exact wording is lost to memory.
- Use equations and present-day diagrams as Marshall's explanation now, not as a
  claimed transcript of what Sean drew then.
- If a Socratic question is useful, frame it as the question Sean taught Marshall to
  ask, not a quotation Sean definitely spoke.
- Keep Sean's introduction short; the post is not a profile or a résumé.
- Preserve the emotional truth: Marshall brought a careful inside-out calculation;
  Sean revealed the outside-in constraint.

## Story-to-argument mapping

| Story beat | Technical lesson | Staff-plus lesson |
|---|---|---|
| Marshall estimates team-caused downtime | Application availability matters, but is not the whole system | Local optimization can answer the wrong question |
| Sean asks Marshall to assume perfection | Remove the application term to expose dependency limits | Change the frame before improving the spreadsheet |
| The service inventory becomes request paths | Hard dependencies, soft dependencies, and customer operations | Draw the system, not the org chart |
| A Region becomes the shared boundary | Multi-AZ does not survive Regional loss | Increase the scope of the question |
| A second Region changes `ALL` to `ANY` | Parallel redundancy multiplies failure probabilities | Architecture changes relationships, not merely components |

## Disclosure requirement

The eventual draft needs one brief disclosure that the lesson is real but the exact
conversation is not recoverable. Do not call invented dialogue a reconstruction; there
should be no invented dialogue to excuse.
