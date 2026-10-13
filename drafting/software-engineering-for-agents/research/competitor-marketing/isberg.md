# Peter Isberg: social media and content marketing

Checked **October 13, 2026**. Internal research memo for *Standing on the Shoulders of Giants: A Software Engineering Primer for Agentic Coding*. Recent sampling window: July 16–October 13, 2026, with three earlier video examples for launch context. Related: [book comparison](../competitive-analysis.md), [primer marketing plan](../../marketing-plan.md).

## Decisive findings

**Isberg's clearest public marketing asset is a connected set of books, usable tools, documentation, and demonstrations.** The publisher-hosted author biography links the companion repositories. Their READMEs link back to the book, and the concurrency-testing repository also links a commercial license page. This establishes a navigable commercial path. Whether readers take it, and how much it sells, remains unknown. [I01, I03, I04, I05]

**His book receives distribution through other people's channels.** The observed examples include a featured toolmaker's LinkedIn announcement, a reviewer explicitly acknowledging a Packt review copy, a corporate event recap, and Swedish maker directories and roundups. These are separate owners with separate audiences. They do not establish Isberg's own posting frequency or an author-controlled launch team. [I07–I12]

**There is an earlier Leanpub offering and a later Packt edition.** The retired Leanpub page reports a July 23 update. Packt dates *Vibe Coding Architecture at Scale* September 2, 2026. This is relevant to the primer's proposed self-publication/publisher sequence, but there is no public account here establishing what secured the publisher relationship, whether audience evidence mattered, or how the editions differ. [I02, I06]

**The most useful caution is a broken purchase journey.** Maker listings and a July book trailer still send prospective readers to the retired Leanpub page. The observed GitHub profile has been updated to the printed title and an Amazon destination. A long-lived content catalog needs a maintained destination for its next step. [I06, I10, I13, I16]

## Identity, channels, and ownership

The correct author is the Gothenburg Java developer at [PIsberg on GitHub](https://github.com/PIsberg), whose profile links Deversity AB and `linkedin.com/in/peterisberg/`. The book's author biography independently supplies the same LinkedIn identity and companion repositories. Search results for an ABB/Hitachi Energy executive named Peter Isberg belong to another person. [I01, I03]

| Surface | Observed role and audience | Ownership boundary |
|---|---|---|
| [GitHub profile](https://github.com/PIsberg) and [profile source](https://github.com/PIsberg/PIsberg/blob/main/README.md) | Illustrated book, project, website, and contact directory for technical visitors | Author-controlled account. The current design groups tools around the path from agent work to production. |
| [VibeTags](https://github.com/PIsberg/vibetags) and [async-test-lib](https://github.com/PIsberg/async-test-lib) | Installation, examples, guides, walkthrough video, book references | Author-maintained repositories. Useful artifacts also carry commercial or donation links. |
| [Deversity](https://www.deversity.se/) | Product explanations, source links, installation, pricing, contact | Company destination connected directly from the author's profile. It sells tooling licenses. A separate consulting offer was not verified. |
| [Packt book page](https://www.packtpub.com/en-us/product/vibe-coding-architecture-at-scale-9781808654916) and online excerpts | Professional developers and technical leaders who want architecture and delivery control | Publisher-controlled distribution and purchase surfaces. |
| [Leanpub book](https://leanpub.com/vibe-architecture) and [author page](https://leanpub.com/u/isberg) | Earlier book discovery, video, author contact, other writing | Author storefront on a publishing platform. This particular book is retired. |
| [LinkedIn profile](https://www.linkedin.com/in/peterisberg/) | The author's linked professional identity | Profile returned HTTP 404 to a logged-out request. Its feed and follower total were not established. |
| [Anonymous Claudeholics on YouTube](https://www.youtube.com/channel/UC8PjiehoWSLY7PFVLAl5e6w) | Book trailer and tool walkthroughs linked from author-controlled surfaces | Channel identity verified from video metadata. Ownership by Isberg was **not** independently established. Call these author-linked videos, not his proven personal channel. |
| [Skeppat maker profile](https://www.skeppat.se/m/peter-isberg) and [Vibekollen profile](https://vibekollen.com/sv/vibecodare/peter-isberg) | Swedish maker discovery across his book, tools, and a game | Platform listings attribute the projects to Isberg. Who submitted each listing was not established. Roundups belong to the platform. |

The product names need care. Isberg's Java annotation project is `PIsberg/vibetags`, distinct from the unrelated `vibetags` GitHub organization for AI search visibility. The current Deversity site identifies VibeTags as MIT licensed, while async-test-lib and llm-fw use PolyForm Noncommercial with paid commercial licensing. The book biography and profile use broader “open source” language that does not accurately describe those two current licenses. [I03–I05, I17, I18]

## Dated examples

These 15 observations include **12 within the recent window** and three earlier videos. They mix promotional content, listings, documentation, and an author-profile revision. They are not 15 personal social posts. Dates come from platform metadata, visible dated pages, GitHub release/commit records, or publisher metadata. LinkedIn dates below are the public page's JSON-LD `datePublished` in UTC.

| Date | Owner and format | Hook or subject | Observed next step and source |
|---|---|---|---|
| July 9, 2026 | Anonymous Claudeholics, 10:31 YouTube walkthrough | VibeTags annotations, generated rules, and coding-tool integration | Description links the repository. The current repository embeds this video. [I14] |
| July 9, 2026 | Same channel, 7:47 walkthrough | Reproducing concurrency bugs with async-test-lib | Description links the repository, which embeds the walkthrough. [I15] |
| July 15, 2026 | Same channel, 6:29 book trailer | Architecture and structure as the complement to fast code generation | Description asks viewers to buy on Leanpub. The Leanpub product page embeds the trailer. [I13] |
| July 19, 2026 | Skeppat project listing, attributed to Isberg | *Vibe architecture book*, described as structured AI coding | Project link leads to Leanpub. Vibekollen also carries a July 19 listing. These may share discovery history, so do not count them as two independent author campaigns. [I10, I11] |
| July 23, 2026 | Leanpub product update | *Vibe architecture*, displayed as 90% complete | Last-update date on the now-retired listing. This is a manuscript/storefront milestone, not evidence of a social announcement that day. [I06] |
| July 24, 2026 | Skeppat editorial roundup | Book listed among 13 maker projects, alongside Isberg's game | Direct Leanpub link plus the platform's own newsletter signup. The email list belongs to Skeppat. [I12] |
| August 3, 2026 | Skeppat VibeTags listing, attributed to Isberg | Java annotations that protect code and guide AI implementations | Project/source links lead to the GitHub tool. [I19] |
| August 7, 2026 | Skeppat Deversity listing, attributed to Isberg | Concurrency testing for Java developers | Project link leads to Deversity. [I20] |
| August 11, 2026 | Isberg repository, llm-fw v0.4.0 release notes | Commercial-license support, alongside engineering changes | Explicit Deversity purchase link and contact route. Evidence of product documentation carrying a purchase action, not a launch advertisement. [I21] |
| August 14, 2026 | Skeppat editorial roundup | Deversity concurrency-testing project included among 15 projects | Direct company link. This demonstrates listing-to-roundup reuse. [I22] |
| September 2, 2026 | Packt publication milestone | *Vibe Coding Architecture at Scale*, first edition, 566 pages | Print/eBook purchase and online-reader options. [I02] |
| September 4, 2026 | Yves Gugger, LinkedIn native post | His LeanCTX tool appearing in Isberg's book | Congratulates Isberg and supplies a purchase link. One relevant participant amplified the book. Coordination or compensation was not established. [I07] |
| September 9, 2026 | Neha Jain, LinkedIn book post | Maintainability after AI generates working code | Amazon link, discussion question, and explicit thanks to Packt and its representative for a reading copy. This is disclosed review-copy amplification. [I08] |
| September 19, 2026 | Isberg, GitHub profile design revision | Align the visible title with the cover, improve contact actions, unify visual project cards | Public commits document title correction and an agent-to-production diagram. Current profile links the book, company, and email. [I16] |
| September 29, 2026 | WirelessCar, LinkedIn event recap with image | Turning AI experiments into useful work through an AI Day and hackathon | Names Isberg as author/VibeTags creator and summarizes his context-focused presentation. No book-purchase CTA. The post date does not establish the exact event date. [I09] |

## Launch sequence and content reuse

The visible sequence begins with tool videos and a book trailer in July, proceeds through a Leanpub listing and maker-directory coverage, and then reaches the September Packt edition, participant/reviewer posts, profile changes, and a corporate event recap. It is a reconstruction from public artifacts, not Isberg's stated campaign plan. A complete prelaunch email sequence, launch discount, advertising campaign, or personal posting calendar was not established.

Three reuse paths are directly visible:

1. **Book material and runnable tools refer to one another.** Packt's author biography sends readers to two companion repositories. VibeTags' README identifies the book chapter using it as a worked example. The concurrency library does the same for the chapter on asynchronous failures. These references connect teaching to something a reader can inspect and run. [I03–I05]
2. **Videos are reused at the point of evaluation.** Both repository READMEs embed tool walkthroughs, and their descriptions link back to the tools. The Leanpub page embeds the book trailer, which links back to that listing. This is verified cross-linking and embedding. It does not prove that prose was converted into scripts, who produced the videos, or that an article generated multiple clips. [I06, I13–I15]
3. **Directory entries become editorial mentions.** Skeppat's book and Deversity listing pages identify the relevant weekly roundups. The dated roundups contain those projects and links. This gives a concrete example of project discovery extending into someone else's recurring publication. [I10, I12, I20, I22]

The GitHub profile adds an unusually inspectable branding practice. September 19 commit messages explain replacing inconsistent visual elements with generated SVG cards and a common design, correcting the book title, and presenting a project sequence. The marketing interpretation is that a visitor can understand the relationship among the artifacts without already knowing the author. The commits prove the design work and intent, not improved conversion. [I16]

## Commercial paths that can actually be followed

| Path | What is verified | What is not established |
|---|---|---|
| Author profile → book purchase | Current GitHub profile has an Amazon book link. Packt sells the published edition. | Traffic, attribution, sales, or which destination converts better. |
| Book → companion repository → paid tool | Book biography links async-test-lib. That README links Deversity commercial pricing. | How often readers traverse this path or become customers. |
| Public repository/release note → llm-fw company page | README/release material and the company page present commercial licensing. | That the book promotes llm-fw specifically, or that book buyers purchase it. |
| Maker listing → editorial roundup → company | Deversity's listing, roundup mention, and company link are visible. | Referral traffic or customer acquisition attributable to the roundup. |
| Tool user → voluntary support | VibeTags README has a PayPal donation link. | Donation volume. |
| GitHub/company → contact | Direct contact actions are exposed. | A packaged consulting engagement, workshop menu, speaking fee, or lead qualification process. |

As checked, Deversity advertises async-test-lib commercial use from **€250 annually** for the smallest team tier and llm-fw from **€450 annually**. Those are listed offers, not transaction evidence. The latter page also describes paid support and negotiated redistribution arrangements. A reader can inspect or try these products under the terms presented on their sites. This commercial model differs materially from the primer's consulting priority: adopting it would create software maintenance and support obligations. [I05, I17, I18]

The earlier book route has a maintenance problem. The Leanpub page is retired and says it is no longer for sale, while historical directory entries and the trailer still direct people there. No replacement-buy link was observed in the inspected Leanpub page. This is a concrete example of why an owned book landing page can be useful even when checkout belongs to a publisher. It is not evidence that the stale route materially reduced sales. [I06, I10–I13]

## Visible metrics and limits

The following are retrieval snapshots on October 13, not historical growth measurements or comparable audience sizes:

| Surface | Visible snapshot | Interpretation limit |
|---|---|---|
| Isberg GitHub profile | 143 followers, 35 repositories | Followers are not email subscribers or buyers. Repositories are not content impressions. [I01] |
| VibeTags, as pinned on profile | 25 stars, 6 forks | Signals of repository interaction, not active installations or paying teams. [I01] |
| July VibeTags / async-test-lib videos | 77 / 23 views | Public video metadata only. Views do not establish tool adoption. [I14, I15] |
| July book trailer | 69 views | Includes no verified downstream purchase data. [I13] |
| Gugger LinkedIn book post | 32 reactions, 1 comment | Another person's post. No impressions denominator. [I07] |
| Jain LinkedIn review-copy post | 88 reactions, 23 comments | Another person's audience and review-copy relationship. No conversion evidence. [I08] |
| WirelessCar recap | 107 reactions, 2 comments | Host-owned event content mentioning several presenters. Cannot assign all response to Isberg. [I09] |

Personal LinkedIn reach, newsletter subscribers, website traffic, book sales, license revenue, consulting leads, growth rates, and marketing spend are **not established**. Site logos described as organizations observed in package-download telemetry must not be rewritten as endorsements, customers, or confirmed deployment. Deversity's own VibeTags page explicitly distinguishes these. [I17]

## Implications for the primer

The transferable advantage is the **inspectable demonstration**. Isberg's free artifacts let a practitioner examine how a claim becomes an engineering action. That aligns with the primer's proposed named principle, agent instruction, and observable check. Building an independent tooling business is optional and would be a substantial expansion of scope.

His visible resources include a publisher, maintained technical artifacts, access to a corporate speaking setting, and participation in a Swedish maker-discovery ecosystem. The VibeTags README describes one developer maintaining it in spare time. That statement concerns this project, not a verified staffing census for all of his marketing or company work. [I04, I09] The selected LinkedIn amplification also benefits from relationships a new author cannot assume are already available.

Four small proposed tests fit Marshall's current consulting-led plan. They are proposals, not changes to the approved strategy:

1. **Attach one runnable demonstration to one primer article.** Include the failure, the classical source, the agent instruction, and a check readers can repeat. Link it from the lesson and relevant profile surfaces. Record substantive developer questions and whether anyone reports reproducing the example.
2. **Give the demonstration one short walkthrough.** Embed it where a reader evaluates the example. Compare the questions produced by prose and video before expanding the adaptation workload. Isberg's examples support embedding and cross-linking, not a particular short-video cadence.
3. **Maintain a permanent primer destination.** Use it for the current article sequence, eventual book choices, and a clear consulting contact action. Keep the destination stable when publication arrangements change. Audit old calls to action at each release milestone.
4. **Test a practitioner talk with a useful takeaway.** A team session around one failure and its check could supply a practical result and, if the host chooses, an authentic public recap. Measure follow-up conversations and invitations. The WirelessCar example supports the format's existence, not a causal claim about getting hired.

## Evidence limits and do-not-use ledger

**Verified primary evidence:** author-controlled repositories and their history, company product pages, publisher/storefront metadata, public video metadata, the authors of the three LinkedIn posts, and maker platforms' own listings/roundups. The latter establish what those platforms published. They do not establish who submitted a listing. LinkedIn JSON-LD establishes precise post dates despite inconsistent relative labels in search results. Public HTTP requests retrieved pages where the search tool could not render them.

**Editorial inference:** the connected-artifact marketing model, the likely purpose of the profile redesign, relevance to Marshall's strategy, and the proposed tests. No acquisition economics were calculated.

**Unresolved:** the relationship between the retired Leanpub manuscript and the Packt publishing agreement, the exact YouTube channel owner and production workflow, a complete personal social feed, a personal newsletter or podcast, paid promotion, and revenue attribution. Failure to discover these is not proof of absence.

**Do not use:** the unrelated ABB/Hitachi profile, unrelated AI-visibility VibeTags organization, third-party GitHub mirrors as historical follower data, a blanket open-source description of current products, tool benchmark claims as independently validated results, site logos as customer proof, catalog dates as verified author-submission dates, or the earlier Leanpub listing as proof that self-publication earned a publisher contract.

## Primary source register

- **I01:** [GitHub author profile](https://github.com/PIsberg) and [current profile README](https://github.com/PIsberg/PIsberg/blob/main/README.md): identity, navigation, illustrated portfolio, snapshot counters. Image-link destinations were checked in the public README source because text extraction omits some cards.
- **I02:** [Packt product listing](https://www.packtpub.com/en-us/product/vibe-coding-architecture-at-scale-9781808654916): September 2 publication, title, edition, formats, intended professional audience. Primary publisher text was available through search indexing when direct rendering returned 403.
- **I03:** [Publisher-hosted author biography](https://subscription.packtpub.com/book/business-and-other/9781808654916/59/ch59lvl1sec34/chapter-bm-about-the-author): correct identity and direct companion-tool links.
- **I04:** [VibeTags README](https://github.com/PIsberg/vibetags#readme): video embed, book-chapter reference, project-maintenance statement, license and donation links.
- **I05:** [async-test-lib README](https://github.com/PIsberg/async-test-lib#readme): walkthrough, publication reference, commercial license purchase path and prices.
- **I06:** [Retired Leanpub listing](https://leanpub.com/vibe-architecture): July 23 update, completion label, embedded trailer, retired status. [Author storefront](https://leanpub.com/u/isberg) confirms identity and other writing.
- **I07:** [Yves Gugger's book-inclusion post](https://www.linkedin.com/posts/yves-gugger_this-is-a-pretty-cool-moment-leanctx-made-activity-7501573622570917888-lGab): September 4, 09:35:24 UTC.
- **I08:** [Neha Jain's disclosed review-copy post](https://www.linkedin.com/posts/neha-jain-279b80118_aiassisteddevelopment-softwarearchitecture-activity-7503403147059564544-skiP): September 9, 10:45:16 UTC.
- **I09:** [WirelessCar AI Day recap](https://www.linkedin.com/posts/wirelesscar_how-can-ai-experiments-become-useful-ways-activity-7510651957343358976-02M8): September 29, 10:49:27 UTC.
- **I10:** [Skeppat book listing](https://www.skeppat.se/p/vibe-architecture-book): July 19, Leanpub destination, link to editorial roundup.
- **I11:** [Vibekollen book listing](https://vibekollen.com/sv/projekt/vibe-architecture-book) and [dated profile activity](https://vibekollen.com/sv/vibecodare/peter-isberg?flik=resan): July 19, 2026 directory record, attribution and project link.
- **I12:** [Skeppat July 24 roundup](https://www.skeppat.se/veckan/2026-07-24): book mention, direct Leanpub link, platform email signup.
- **I13:** [Book trailer](https://www.youtube.com/watch?v=TLQKlD2c-98): July 15, 389 seconds, channel name and Leanpub CTA in public watch-page metadata.
- **I14:** [VibeTags walkthrough](https://www.youtube.com/watch?v=QF0YloxDjnY): July 9, 631 seconds, channel identity, repository destination.
- **I15:** [async-test-lib walkthrough](https://www.youtube.com/watch?v=5LBavovcHEg): July 9, 467 seconds, channel identity, repository destination.
- **I16:** [September 19 title/contact revision](https://github.com/PIsberg/PIsberg/commit/a12067f0378a7ad7e5c1ff83dabe2eee6288bf51) and [generated design/pipeline revision](https://github.com/PIsberg/PIsberg/commit/2e134efb4e12677acb58ee8b223b6bdd6e2a9b05): actual public-profile marketing changes and stated motivations.
- **I17:** [Deversity company site](https://www.deversity.se/) and [VibeTags product page](https://www.deversity.se/vibetags/): navigation, positioning, license distinction, installation actions, limits on company-logo claims.
- **I18:** [llm-fw product and pricing page](https://deversity.se/llmfw/): commercial tiers, installation/source/contact actions, stated checkout arrangements. Offer and claims only, not independent technical or commercial validation.
- **I19:** [Skeppat VibeTags listing](https://www.skeppat.se/p/vibetags-ai-guardrails-for-java): August 3, repository destination.
- **I20:** [Skeppat Deversity listing](https://www.skeppat.se/p/deversity-concurrency-testing-for-the-jvm): August 7, company destination and roundup reference.
- **I21:** [llm-fw v0.4.0 release](https://github.com/PIsberg/llm-fw/releases/tag/v0.4.0): August 11, commercial purchase/contact actions in release documentation. Date verified through GitHub's public releases API.
- **I22:** [Skeppat August 14 roundup](https://www.skeppat.se/veckan/2026-08-14): Deversity mention and company link.
