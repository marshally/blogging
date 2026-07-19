# Marshall Yount 2026 Posting Strategy

Status: approved July 19, 2026

## Purpose

This strategy is designed to make Marshall Yount visible to the network he has already built, expand that network over time, establish a durable public body of work, support a private search for senior technical roles, and create an audience from which a podcast can later launch.

The immediate job-search objective is not to announce that Marshall is looking for work. It is to make his experience, judgment, and point of view easy to encounter and easy to remember while he updates his profiles and contacts people privately.

The medium-term objective is to build an audience that may later become a podcast audience. The podcast will have separate branded accounts when it exists; Marshall's personal accounts will amplify it.

The long-term objective is to share what Marshall has learned during a thirty-year career and accumulate a body of work that remains useful beyond any particular platform.

Marshall is comfortable spending roughly three to five hours per week on writing, adaptation review, publishing, and conversation. This is a capacity boundary for the workflow, not a quota or prescribed cadence.

## Positioning

Marshall publishes everywhere as Marshall Yount. Yount Labs is the name of the owned website and archive, not a separate social-media persona.

The professional throughline is:

> I find and fix the parts of the system that are slowing everyone else down.

The positioning is aimed at Principal, Staff, Architect, and similarly senior technical leadership roles. It should demonstrate technical breadth, architectural judgment, the ability to improve engineering systems and organizations, and leadership through influence. It should not imply a conventional executive people-management track that Marshall does not claim.

## Governing principles

### Curiosity chooses the subject

There are no mandatory content pillars, topic quotas, or editorial calendar. Marshall writes about questions and subjects that genuinely pique his curiosity. Those may span software architecture, technical systems, engineering organizations, team improvement, careers, leadership, consulting, and other domains.

Distribution follows the writing. The strategy does not distort the writing into a predetermined content program.

### Native value beats promotion

Every social adaptation should reward someone who never leaves that platform. It may be shorter than the article, but it must contain a complete idea rather than merely announcing or teasing a link.

The underlying opinion stays consistent across platforms. The framing, assumed context, length, and presentation change to fit each audience.

### The website is permanent; platforms are rented

YountLabs.com is the canonical archive, the stable professional destination, and the subscriber entry point. Social platforms provide discovery and conversation. They do not replace the owned archive.

### Optimize for recognition, not virality

The strategy's practical purpose is to make Marshall top-of-mind with people who may recommend, introduce, hire, invite, or collaborate with him. A thoughtful response from a relevant person can be more valuable than a large number of anonymous impressions.

### Conversation remains human

Marshall responds to substantive comments on his work and sometimes comments substantively on other people's work. There is no engagement quota, engagement pod, automated commenting, or performative daily routine.

### Measure before changing behavior

The publishing system reports reach, engagement, and outcomes. It does not automatically rewrite the strategy or optimize Marshall's voice. Changes remain deliberate human decisions.

## Platform portfolio

| Platform | Role | Current status |
|---|---|---|
| YountLabs.com | Canonical archive, professional destination, subscription, and contact | Primary |
| Email | Direct relationship with opted-in readers | Primary |
| LinkedIn personal profile | Professional discovery, durable long-form work, and conversation | Primary |
| Facebook personal profile | Staying visible to Marshall's broad existing network | Primary |
| Threads | Conversational text and compact observations | Active |
| Bluesky | Technical and intellectually curious discussion | Active |
| X | Additional technical reach and existing-network visibility | Active, but not central |
| Medium | Selective long-form discovery | Conditional |
| DEV Community | Software engineering, architecture, engineering organizations, teams, and leadership | Conditional |
| Instagram | No current natural role | Inactive until reconsidered |
| Hacker News and Reddit | Communities where participation should precede promotion | Inactive unless Marshall becomes a participant |

All current social accounts use Marshall Yount's identity. No Yount Labs social accounts are needed. Instagram is explicitly out of scope for now.

## Platform adaptation playbook

| Platform | Best use | Default adaptation | Link and attribution policy |
|---|---|---|---|
| Yount Labs | Complete, permanent body of work | Full canonical article with citations, images, metadata, subscription, and contact paths | The article URL is self-canonical |
| Email | Relationship with readers who explicitly opted in | Complete article in minimal, readable HTML; include a web version, reply path, and unsubscribe mechanism | Link to the permanent web version, normally near the top or bottom rather than making the email a teaser |
| LinkedIn Article | Full professional prose and durable profile visibility | Complete native article with a cover image when appropriate, preserved reasoning, and necessary source citations | End with unlinked text: `Originally published on Yount Labs.` LinkedIn has no publisher-controlled canonical setting |
| LinkedIn feed | Professional discovery and conversation | A self-contained argument, observation, or substantial excerpt; when sharing a LinkedIn Article, the feed text should still contain useful substance | Do not include a Yount Labs link in the wrapper or first comment by default. Link internally to the LinkedIn Article when appropriate |
| Facebook | Broad-network recognition | A personal introduction plus an accessible, substantial version of the idea; assume less specialized context | Use a link only when the destination adds material value; the post itself must stand alone |
| Threads | Conversational reach | A strong standalone opening followed by compact prose or a short connected sequence | Include a link only when it materially helps; do not turn every post into blog promotion |
| Bluesky | Technical and intellectual discussion | A precise claim, compact explanation, or short thread; use platform-native mentions, facets, and alt text | Links and cards are acceptable when they improve the post, but are not mandatory |
| X | Additional reach | A tighter version of the Bluesky adaptation; create a thread only when the argument needs one | Account for the current cost and limitations of API publishing; links remain optional |
| Medium | Broadly relevant essays with plausible Medium discovery | Import the complete article and inspect formatting before publishing | Use Medium's import flow or advanced setting so the Yount Labs article is canonical |
| DEV | Technical and organizational writing relevant to software practitioners | Publish the complete article with enough context for readers outside Marshall's network and apply accurate tags | Set `canonical_url` to Yount Labs, whether imported manually or through RSS/API |

Platform versions are adaptations, not mechanically truncated copies. The publishing workflow may propose variants, but Marshall approves their exact text.

## LinkedIn policy

LinkedIn is the most important social platform for the near-term professional goal. It has two complementary publishing surfaces:

- LinkedIn Articles hold the full prose natively and remain visible in the Activity section of Marshall's profile. Start with ordinary Articles rather than a newsletter. A newsletter can be introduced later if a repeat LinkedIn readership develops.
- LinkedIn feed posts provide discovery and conversation. They should present a complete idea and may direct readers to the native LinkedIn Article where appropriate.

The evidence about external links is mixed and changes over time. LinkedIn does not publish a simple rule saying all external URLs are penalized. A June 2026 MagicPost analysis found a substantial disadvantage for attached external preview cards but no disadvantage for plain in-body URLs, while secondary reporting on Richard van der Blom's 2026 research warns that putting an external link in the first comment can also reduce reach. These studies have different datasets and methods and should not be treated as a permanent law of the platform.

The operational policy is deliberately conservative because it costs little and serves the native-value principle:

- Do not attach an external Yount Labs preview card to the feed wrapper for a LinkedIn Article.
- Do not place the Yount Labs URL in the first comment as an algorithm workaround.
- Use the unlinked attribution `Originally published on Yount Labs.` in the native Article because attribution matters even when a link is unnecessary.
- Keep necessary citations and source links in the body of a LinkedIn Article. Research integrity takes precedence over a speculative distribution advantage.
- Keep a permanent Yount Labs link on Marshall's profile and use LinkedIn Featured to expose the public positioning page and selected writing.
- Review Marshall's own analytics periodically. If his data contradicts the default policy, change the policy intentionally.

This approach is also consistent with LinkedIn's published emphasis on useful professional content, conversation, and both active and passive engagement signals such as comments, shares, and dwell time.

## Canonical publishing and WordPress

Canonicalization tells search engines which URL represents the primary version when substantially similar prose appears in multiple places. It does not control social attribution or prevent people from reading another version.

For each complete article:

1. The Yount Labs page is the original and should contain a self-referential `rel="canonical"` element using its final absolute URL.
2. Medium's copy should declare the Yount Labs URL as canonical. Medium's import tool does this automatically, but the result should still be verified.
3. DEV's copy should set `canonical_url` to the Yount Labs URL.
4. LinkedIn Articles cannot currently declare a publisher-controlled canonical URL. The unlinked attribution is therefore for readers, not search engines.

WordPress itself emits canonical tags for singular content, and WordPress.com provides additional SEO controls depending on plan and plugins. Before expanding syndication, audit the actual Yount Labs configuration:

- Confirm every public post resolves to one preferred HTTPS URL.
- Inspect the rendered HTML and verify exactly one self-referential canonical tag.
- Confirm the site is public and is not discouraging search indexing.
- Confirm only one SEO system or plugin controls canonical metadata.
- Confirm RSS entries use the final article URLs.
- Recheck these properties after theme, domain, permalink, or SEO-plugin changes.

The same contract should survive the eventual move from WordPress to a static site on S3 and CloudFront. The renderer must emit the canonical URL from article metadata rather than infer it differently in each deployment.

## Email policy

The existing Yount Labs subscriber plugin should send the complete article by default. This respects readers who chose email as their reading surface and avoids turning every message into a click request.

Each message should include:

- the complete article in restrained, accessible HTML;
- a `Read on the web` link for readers who prefer the site;
- the permanent article URL;
- a working reply path;
- an unsubscribe mechanism; and
- alt text for meaningful images.

An excerpt-only email is an exception for an article whose web interaction, media, or size cannot be represented sensibly in email.

Before relying on this channel, identify the installed subscriber plugin and audit its behavior, sender identity, bounce handling, and SPF, DKIM, and DMARC alignment. The publishing system should integrate with the existing subscriber mechanism when practical rather than creating a second list.

## Publishing workflows

### Finished article

The canonical input is a finalized Markdown file in `posts/` in the blogging repository. A new finalized article automatically creates one draft distribution bundle containing:

- subscriber email;
- LinkedIn Article and its feed wrapper;
- Facebook;
- Threads;
- Bluesky; and
- X.

Medium and DEV are suggested only when the subject fits their audiences. Marshall may disable any destination before approval.

The app presents desktop and mobile previews for every selected destination. Marshall can edit a variant directly or request an agent-assisted revision. One final `Approve bundle` action authorizes the exact selected variants to publish at their scheduled times without another per-platform confirmation.

The Yount Labs publication is the first dependency in the bundle. Medium, DEV, email, and any other destination that refers to the canonical URL must wait until that URL resolves successfully and exposes the expected title and self-referential canonical metadata. This contract applies whether the current destination is WordPress or the future static site.

### Standalone short idea

A short observation can enter the same system without becoming a blog article. The app recommends only platforms where the thought naturally belongs. Marshall can alter that selection, edit the variants, and approve the bundle once.

Short ideas are not forced onto every active account and do not create filler for the website archive.

### Historical articles

The publishing system catalogs existing files in `posts/` but does not automatically queue them. Marshall may manually select an older article when it is newly relevant or useful.

### Source changes after publication

If a finalized source article changes after distribution, the app records drift and offers an update bundle for editable destinations such as the website, LinkedIn Articles, Medium, and DEV. It never silently synchronizes a changed article. A sent email cannot be edited; the app may instead offer a clearly labeled correction or follow-up email. Social feed posts remain historical artifacts unless Marshall explicitly publishes a correction or update.

## Identity and conversion paths

Every active account should make the same professional identity legible without repeating identical profile copy.

Yount Labs should provide three stable paths:

- a browsable writing archive;
- a public experience and positioning page; and
- subscribe and contact actions.

The public positioning page is not a downloadable resume. It explains Marshall's throughline, the kinds of systems and constraints he works on, representative outcomes, and how to contact him. Role-specific resumes remain private and are sent during targeted outreach.

LinkedIn Featured should link to the positioning page and a small number of selected articles. Social profiles should carry the permanent Yount Labs link so individual posts do not all need to promote the site.

Facebook writing posts may be public while ordinary personal activity keeps its normal privacy settings. The account remains Marshall's real personal profile rather than being converted into a sterile professional feed.

## Measurement design

The dashboard separates four layers instead of collapsing them into a single cross-platform score.

### Delivery

- publication success or failure;
- destination post identifier and URL;
- publication timestamp;
- rendered receipt or screenshot; and
- detected source drift.

### Reach

- platform-native impressions, views, opens, or delivered messages;
- follower or subscriber change; and
- profile and article views where exposed by the platform.

Reach metrics remain labeled by platform because an email open, LinkedIn impression, and Bluesky view are not interchangeable.

### Engagement quality

- comments and replies;
- reposts and shares;
- saves or bookmarks where available;
- substantive conversations Marshall identifies; and
- website visits and subscriptions.

Clicks to Yount Labs are useful, but they are not the primary measure because the strategy intentionally supplies complete value on other platforms.

### Outcomes

Marshall can privately record high-value outcomes that platforms cannot observe:

- introductions;
- recruiter or hiring-manager messages;
- consulting inquiries;
- podcast interest;
- invitations or collaboration opportunities; and
- explicit messages that a post reminded someone of Marshall or his work.

Reporting maps these outcomes to the three goals: job-search visibility, podcast runway, and long-term audience. It can identify patterns and prompt a review, but it does not automatically narrow Marshall's curiosity-driven subject matter to whatever recently generated the most impressions.

## Owned publishing application

The distribution workflow will eventually be implemented as a separate publishing repository. This blogging repository remains the source of article content; the application owns operational publishing data and integrations.

The workflow is not built around Buffer or another hosted scheduler. A third-party tool may be used as a disposable fallback, but it is neither the system of record nor a required dependency.

### Source boundary

The publishing application clones the blogging repository internally with read-only credentials and reconciles `posts/` against the last processed Git state. Git events and webhooks are not the core ingestion model.

Each post should eventually expose machine-readable YAML front matter containing at least:

- a stable article identifier;
- title;
- publication date;
- slug; and
- canonical URL.

The first implementation should support the current legacy post format while the archive is migrated. The source snapshot is identified by its Git blob SHA so the application can detect changes exactly.

### Operational storage

PostgreSQL is the source of truth for:

- source snapshots;
- platform variants;
- destination selections;
- approvals;
- schedules;
- publishing jobs;
- publication receipts;
- analytics snapshots; and
- the audit trail.

Object storage holds screenshots and generated or adapted media. Operational state is not committed back to Git.

### Approval integrity

The single approval covers the exact source snapshot, destination set, text, media, alt text, scheduling choices, and renderer/adapter versions shown in preview. A cryptographic hash binds those inputs. Any covered change invalidates the approval and returns the bundle for review.

### Integration policy

Use official APIs first where they provide the required behavior. Current likely API paths include Bluesky, Threads, LinkedIn member feed posts, X, and DEV. Use deterministic Playwright automation for missing publishing surfaces such as LinkedIn native Articles, Facebook personal-profile posts, Medium import, and other unsupported UI flows.

Browser automation must:

- use persistent authenticated sessions;
- undergo a platform-policy review before each automated UI publisher is enabled, with a supervised manual handoff retained where automation is not permitted or is too fragile;
- stop on unexpected UI, authentication challenges, or possible duplicates;
- never guess through an MFA or suspicious-account screen;
- capture a screenshot and platform receipt after publication; and
- make publication idempotent so retries do not create duplicates.

Deterministic validators enforce platform limits, approved link policies, attribution, media constraints, and required alt text before a job can run. The agent supplies judgment and adaptation; scripts own fragile limits, state transitions, and side effects.

### Deployment boundary

The application and Playwright worker run as separate Kubernetes workloads in Marshall's homelab. Cloudflare Access gates the web interface, and the application still performs its own authentication and authorization. Interactive login or MFA recovery is available through an Access-protected browser session. Secrets follow the homelab's established Kubernetes and 1Password conventions. Kubernetes deployment manifests belong in the homelab repository, not the publishing application repository.

## Implementation sequence

Implementation should proceed in capability slices rather than attempting every platform at once:

1. Define post metadata, clone/reconcile the blogging repository, catalog the archive, and detect source drift.
2. Build bundle generation, deterministic validation, side-by-side previews, editing, approval hashing, and the audit trail without external publishing.
3. Add one API-based destination end to end, including scheduling, idempotency, receipts, and failure recovery.
4. Add the remaining API destinations one at a time.
5. Add Playwright destinations one at a time, beginning with the highest-value unsupported surface: LinkedIn Articles.
6. Integrate the existing subscriber system and verify deliverability.
7. Add analytics collection and private outcome recording.

This sequence is about implementation risk, not editorial pacing. It does not impose a posting schedule or a topic plan.

## Explicit non-goals

- Generating a list of article topics or content pillars.
- Dictating how often Marshall must write.
- Manufacturing engagement through quotas, pods, or automated comments.
- Publishing every idea everywhere.
- Automatically reposting the historical archive.
- Creating Yount Labs social accounts.
- Publicly announcing the job search.
- Publishing a public downloadable resume.
- Launching Instagram before there is a natural visual content source.
- Creating podcast accounts before the podcast exists.
- Allowing an agent to publish unapproved content or silently change approved content.
- Depending on Buffer or another hosted scheduler for core behavior or operational state.

## Research foundation

Platform mechanics and algorithm behavior change. These references were refreshed on July 19, 2026 and should be rechecked during implementation and during periodic strategy reviews.

### LinkedIn

- [Write and publish articles on LinkedIn](https://www.linkedin.com/help/linkedin/answer/a522427)
- [Difference between posts, articles, reposts, and newsletters](https://www.linkedin.com/help/linkedin/answer/a519819)
- [LinkedIn Sharing Guide](https://content.linkedin.com/content/dam/help/linkedin/en-us/LinkedIn-Sharing-Guide.pdf)
- [Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed](https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed)
- [Share on LinkedIn API](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [MagicPost: Do External Links Kill Your LinkedIn Reach?](https://magicpost.in/blog/linkedin-external-links-reach)
- [Alan Morrison's summary of 2026 external-link research](https://www.linkedin.com/pulse/linkedin-should-you-include-outbound-link-post-alan-s--v4idc)
- [Oktopost: The Tradeoff Between Engagement and Website Traffic in B2B Social](https://www.oktopost.com/wp-content/uploads/2026/02/Oktopost-research-The-tradeoff-between-engagement-and-website-traffic-in-B2B-social.pdf)

### Canonical syndication

- [Google Search Central: Specify a canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [WordPress canonical function](https://developer.wordpress.org/reference/functions/rel_canonical/)
- [WordPress.com SEO tools](https://wordpress.com/support/seo/seo-tools/)
- [Medium: Importing a post](https://help.medium.com/hc/en-us/articles/214550207-Importing-a-post-to-Medium)
- [Medium: Set a canonical link](https://help.medium.com/hc/en-us/articles/360033930293-Set-a-canonical-link)
- [DEV: Publishing from RSS or Atom](https://dev.to/p/publishing_from_rss_guide)

### Publishing integrations

- [Bluesky: Creating a post](https://docs.bsky.app/docs/tutorials/creating-a-post)
- [Meta's official Threads API workspace](https://www.postman.com/meta/threads/overview)
- [X API: Create or edit a post](https://docs.x.com/x-api/posts/create-post)
- [X API pricing](https://docs.x.com/x-api/getting-started/pricing)
