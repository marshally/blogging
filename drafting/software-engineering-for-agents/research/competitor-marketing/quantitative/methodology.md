# Quantitative comparison: methods and evidence limits

Run `quant-2026-10-14` uses the fixed UTC interval **[2026-07-16T00:00:00Z, 2026-10-14T00:00:00Z)**. This is 90 days. Counters are snapshots at their actual retrieval timestamps. Prior October 13 dossier numbers are historical leads and are not imported as current measurements or a growth series.

## Frozen contract and identity

The supplied version 1.0 schema and initial 51-metric registry govern all records. The coordinator serialized and validated both before collection, then recorded their SHA-256 hashes in `run.json`. No registry extension is currently authorized. Seven people map to five competitor groups in that manifest. Coauthored books have one work ID. Each account is measured separately, with owner-to-account relationships backed by evidence. Publisher, employer, partner, and guest-host audiences stay separate.

Account IDs use platform and known handle; Bluesky content URLs use DID and post key. LinkedIn content retains the observed post slug on `www.linkedin.com` without tracking parameters; duplicate activity IDs require coordinator resolution before merge. Fetched URLs and pagination parameters remain unchanged in capture receipts. A reserved candidate identity does not establish ownership.

## Collection and classification

Workers collect by source family into separate shards. Every relied-on original response is preserved byte-for-byte after transfer/content decoding, with SHA-256, byte length, media type, encoding when known, UTC retrieval time, and allowlisted response headers. Failed retrievals remain receipts. Search/tool results, rendered DOM, and screenshots cannot substitute for archived originals supporting accepted numeric observations. Unknown measurements use null, never zero.

Content kinds separate original posts, reposts, replies, quote posts, articles, newsletter issues, video uploads, and podcasts. Reposts use the repost event date. Primary intent follows the dominant visible purpose: teaching steps is tutorial, showing an artifact is demonstration, arguing a position is opinion, direct book emphasis is book promotion, an offer is service promotion, milestones are announcements, and a roundup is curation. Insufficient evidence receives unknown. AI engineering relevance is primary, partial, none, or unknown. A short video requires native Shorts/Reels classification or explicit source format evidence; duration alone is insufficient. Language follows visible content.

## Denominators and formulas

A complete public window requires archived pagination through the start boundary or exhausted history, with no known gap for the declared filters. It cannot prove deleted or private material never existed. Selected posts support sample counts and sample medians, never whole-feed cadence. `scripts/derive.py` owns counts, rates, quantiles, differences, and lineage. Rates use 90/7 weeks. Active-week fraction uses the 12 complete seven-day bins anchored at window start, excluding the final six days. Counts deduplicate content IDs. Every derived result records input IDs and script hash.

Medians use the middle value or mean of two middle values. The 75th percentile interpolates at `(n-1)*0.75`. Engagement observations are retrieval-time counters for posts of different ages, not seven-day performance. Fractions describe their collected population. Follower growth requires comparable dated observations; inconsistent cached counts cannot establish it. Book counter changes are net differences. Derivative counts require explicit attribution; reuse lags preserve source time precision.

## Evidence tiers

Direct platform counters are direct observations. Authors' and publishers' disclosed sales are first-party reports, with scope and reporting date retained. An archived self-report does not become independently audited sales. Secondary reports remain third-party reports. Book demand proxies remain separate from units sold. Advertised price, capacity, and scheduled events cannot establish revenue, filled seats, or delivery. Candidate claims without archived originals remain unavailable.

## Verification and execution record

Collection and validation results will be appended after the shards are merged. The working branch is `research/quantitative-competitors-2026-10-14`; nothing will be pushed or published. Model assignments follow the handoff: GPT-6.1 Sol medium for general research, high for sales ambiguity, and a separate audit if available. These are workload choices, not model-performance measurements.

### Operational clarifications during collection

LinkedIn returned nonstandard HTTP status 999. Version 1.0 permits only 100–599 or null. The affected pre-validation draft receipts were preserved as supplemental `tool_response` objects and replaced with new UUIDs, `http_status: null`, and an explicit nonstandard-status explanation. This is a documented correction of invalid draft receipts, an exception to normal append-only collection. Original response bodies remain unchanged. It does not represent a successful profile retrieval.

A Bluesky repost has its own repository record. Its canonical content URL is the resolved public PDS `com.atproto.repo.getRecord` URL for that repost record; its AT URI is native_id. The event's repository createdAt determines publication, with subsecond precision truncated to the schema's seconds. Target post engagement is not assigned to the repost. A fully traversed requested window may stop at an archived wholly pre-window page rather than lifetime exhaustion. In those coverage records, `pagination_exhausted: true` means the requested-window pagination is complete; sampling_detail states the stopping boundary.

The X account `uberto` belongs to a different person. Barbini's official conference biography links `ramtop`; that is the selected X identity. An unverified Bluesky candidate for Skowroński remains in discovery coverage without an owned-account assertion. Known identities are corroborated through distinctive linked works and public biographies, not display names alone.

[Amazon's ranking explanation](https://kdp.amazon.com/en_US/help/topic/G201648140) says ranks reflect relative activity and are unsuitable as an accurate activity counter or cross-category comparison. Each format can have a separate rank. Its complete original is capture `3a42f513-d056-40dd-ac76-6a9f464d211e`. [LinkedIn's analytics documentation](https://www.linkedin.com/help/linkedin/answer/a518885?lang=en-US) states that post analytics are private to the account holder; its original is capture `e979de70-63d7-442c-b849-fdcf5eb1a4ce`. Public reactions and comments do not supply private impressions, clicks, or demographics.

Formula IDs with unavailable inputs are explicit `unavailable` records in `observations.jsonl`, with null lineage. They are not computed results. `derived-metrics.jsonl` contains only successful calculations with `evidence_class: derived`, resolving the contract's requirement that unknown values use `evidence_class: unavailable`. The calculator excludes sub-day counter differences, reports the actual elapsed interval for eligible growth, and never labels incidental retrieval differences as 30- or 90-day growth. Quantile reporting requires at least four contributing posts. Medians use the latest exact counter per collected post and separate platform, content kind, and format. They describe samples wherever coverage is incomplete.

### Selection and correction log

The book worker's observation `b4bb4f9c-1647-481c-8b44-eb86b25793af` recorded the correct Ingram paperback date with edition scope but attached it to the work entity. The coordinator created `book:beyond-vibe-coding-paperback-9798341634756`, its `edition_of` edge, and correction `a467ca4b-7973-499a-9f7b-f606a7d18dbf`. Use the correction for the paperback's September 23, 2025 publication date. The original observation remains an explicitly superseded raw alternative; neither establishes O'Reilly's online-edition date. Work and edition are not added as separate competing titles.

The newsletters worker replaced two invalid pre-validation draft `audience_type` enum values with new-UUID observations using `all`. Their original disclosed subscriber quantities remain total-subscription lower bounds. This is another documented exception to append-only draft collection; no sealed accepted source bytes or figures were overwritten. The X worker likewise preserved a rejected-identity draft receipt as a supplemental artifact and replaced its incorrect source-owner attribution with a new-UUID receipt. These corrections preserve the identity trap without assigning another person's account to Barbini.
