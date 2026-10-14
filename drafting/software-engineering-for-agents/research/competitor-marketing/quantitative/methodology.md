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
