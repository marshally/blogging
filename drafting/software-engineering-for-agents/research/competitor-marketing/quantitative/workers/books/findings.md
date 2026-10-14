# Books: archived quantitative collection

Collection date: October 14, 2026 UTC. The baseline is July 16–October 14, 2026, with the end exclusive. This shard collects current publication and reader-response snapshots plus bounded public sales-disclosure searches. It does not supply baseline growth or sales estimates. Retrieval seconds are in each capture receipt.

## Accepted sales disclosure

The [IT Revolution author biography](https://itrevolution.com/product/vibe-coding-book/) reports Gene Kim’s books sold **over one million copies**. Observation `dcba7901-8a3e-41bc-85aa-92ff91bcf338` records the threshold as a lower bound of 1,000,000 copies, evidence class `first_party_report`, subject `person:gene-kim`, scope `career_catalog`. This is a career aggregate, not *Vibe Coding* sales. The source names several authored/coauthored books but does not allocate units to titles. Its reporting date, format, geography, channel, paid/free split, returns treatment and exact measurement period are unknown. Do not add it to title totals or attribute it to Kim/Yegge’s joint book.

## Title results

| Title | Current publication evidence | Goodreads rating count / written reviews / mean | Sales result |
|---|---|---|---|
| Process Over Magic | 2026-06; published ([source](https://pragprog.com/titles/ubaidev/process-over-magic-beyond-vibe-coding/)) | 8 / 1 / 3.13 out of 5 ([snapshot](https://www.goodreads.com/book/show/250740200-process-over-magic)) | Null; no title-unit count found |
| Vibe Coding Architecture at Scale | Candidate September 2, 2026 / published; primary original blocked, values null | Null; Amazon access interstitial, no Goodreads title discovered | Null; no title-unit count found |
| Vibe Coding | 2025-10-21; published ([source](https://itrevolution.com/product/vibe-coding-book/)) | 464 / 62 / 3.71 out of 5 ([snapshot](https://www.goodreads.com/book/show/233858812-vibe-coding)) | Null; no title-unit count found |
| Beyond Vibe Coding | 2025-09-23; published ([source](https://ingramacademic.com/products/beyond-vibe-coding-9798341634756)) | 114 / 17 / 3.15 out of 5 ([snapshot](https://www.goodreads.com/en/book/show/232301660-beyond-vibe-coding)) | Null; no title-unit count found |
| Vibe Engineering | 2026-11; early_access ([source](https://www.manning.com/books/vibe-engineering)) | 8 / 3 / 4.63 out of 5 ([snapshot](https://www.goodreads.com/en/book/show/249119472-vibe-engineering)) | Null; no title-unit count found |

Goodreads snapshots come from complete archived original platform HTML and its `Book.aggregateRating` JSON-LD. The pages display specific ebook/Kindle/paperback editions, but Goodreads may aggregate reader responses across editions; the exact aggregation scope is unestablished and the book-format scope remains unspecified. Counts are platform ratings and reviews, not verified buyers or unit sales. Means preserve the platform’s two-decimal rounding. Kim/Yegge’s page reports 62 reviews while its paginated display says 61; the metric is explicitly `aggregateRating.reviewCount`, not a census of visible review bodies. Search-index counts differ from the original snapshots and are excluded from historical change calculations.

Publication details retain their native precision: PragProg supplies June 2026; IT Revolution supplies October 21, 2025; Ingram supplies September 23, 2025 for Osmani’s paperback ISBN 9798341634756. Ingram’s metadata is a third-party report, distinct from the inaccessible O’Reilly online-edition candidate of August 2025. Manning supplies an estimated November 2026 final release and current early access with all chapters available; no final publication day is invented. Isberg’s September 2 date is a publisher-search candidate whose original was blocked, so both date and status observations remain unavailable. The original author README links the current Amazon book. The archived earlier Leanpub *Vibe architecture* page is retired and last updated July 23, 2026; retirement is not applied to the Packt title.

## Bounded sales trail

Each title has its own coverage receipt linking an attempted primary publisher page, an author-controlled surface, and explicit title/author sales queries. Raw search tool outputs are archived separately as `tool_response`; they cannot support accepted numeric observations. No title-specific count survived these searches. All five title `book_units_sold` observations are null with `not_found`, which describes the inspected sources, not the entire public web or private publisher accounting. Shipped, printed, distributed and free-download counts likewise remain null.

- **Process Over Magic:** sales observation `7e7176ee-a1c6-4953-902a-0a37c406c51a`; coverage `c5864878-74e7-4b3a-be72-70150363e5cc`; publication observation `de9fcb3f-044f-4e63-a8d9-761577d8f8ed`; rating-count observation `72f398ca-7c73-4b5a-ba6c-763a3a5135cb`.
- **Vibe Coding Architecture at Scale:** sales observation `91b355f3-8d6b-44bf-a40f-dd7ed2c544a8`; coverage `de586e21-4412-4ed6-9ba8-5fb677f45e1b`; publication observation `6f9a78d9-b761-4c26-9a4f-a6478d973f31`; rating-count observation `46cb571a-a2bd-419d-8365-e494c4d2ccf5`.
- **Vibe Coding:** sales observation `b9ffc58c-ab97-40af-a869-7423aad5cf01`; coverage `28d60a53-611a-4467-8f15-7c037515680b`; publication observation `1571bac4-cfe2-441a-b681-ce07b7f71a6d`; rating-count observation `a960644d-791b-4ed4-aec8-7a916e0e79d7`.
- **Beyond Vibe Coding:** sales observation `962ee6b0-7a1a-4cc6-b362-8917cd35d512`; coverage `0f322bb9-70c3-4825-bdf5-7f636d9fed63`; publication observation `b4bb4f9c-1647-481c-8b44-eb86b25793af`; rating-count observation `6f610e06-ae3d-4747-8e54-8c1d0864c03c`.
- **Vibe Engineering:** sales observation `d2ef2df4-f3b6-42bb-84d5-f713b2d29a91`; coverage `4279fc7b-24a4-435e-b540-a41090958dd6`; publication observation `d753c8f8-6613-4129-b15c-be6341f072c9`; rating-count observation `2936d7e5-230b-4260-a814-2b2f50fc87d6`.

Primary sales inspections included PragProg’s book page and Barbini’s author announcement attempt; Packt’s catalog and Isberg’s current raw author README/retired Leanpub listing; IT Revolution’s book page, Kim archive, and Yegge’s owned book page; O’Reilly’s catalog attempt and Osmani’s homepage/companion site; Manning’s book page and Lelek’s author GitHub/Skowroński’s raw profile README. Barbini Medium, Packt and O’Reilly returned archived HTTP 403 bodies. A failed guessed Lelek raw-README branch and failed genekim.com retrieval are retained as failures; known author surfaces supplied the actual discovery trail. The title coverage receipts spell out query strings, timestamps and capture IDs.

## Exclusions and comparison limits

- Barbini’s publisher historically claimed rank 2 in Pragprog.com’s June 2026 Top 10. The complete original Bluesky JSON and HTML are archived. This is outside the baseline, supplies no units and lacks an exact format scope. The rank observation stays null with `definition_mismatch`; the candidate is retained in notes.
- Osmani’s September 10, 2025 original LinkedIn announcement claims rank 1 on Amazon in Generative AI and Software Design Tools. The storefront country and format are unspecified, and it is outside the baseline. It is retained as a candidate, not a current retailer rank or sales count.
- A Manning/VirtusLab search candidate offers thirty free signed special-edition copies at an event. An offer is not proof of distribution, and free copies are not paid sales. No distributed-units observation is accepted from it.
- Search returned 800+ copies and $11K for another technical author whose interview involved Skowroński. It is unrelated to this book or these authors’ sales and is excluded. Retailer available stock, bulk-order minimums, shop-wide eBay items sold and “sold out” labels are likewise excluded.
- No accepted current marketplace sales rank, longitudinal review/rating growth, paid/free book breakdown, or full-window sales measure was found. These are unknown, not zero.

## Delivery and verification

Shard contains 13 entities, 12 relationships, 36 captures, 56 observations and 6 coverage receipts. The content table is intentionally empty. Every non-null numeric value is backed by a complete archived original response. There are no derived metrics. Content-addressed archive bodies include blocked responses; one Amazon HTTP 200 response was inspected and classified as a soft block.

`scripts/validate.py workers/books --context quantitative` passes schema, archive hashes, source evidence, foreign keys and metric/scope semantics. Three manual locator warnings concern the blocked Amazon and Packt bodies and the explicitly labeled Packt search candidate; they do not support an accepted numeric value. No git changes were staged or committed by this worker.
