# Serialized publishing: the *Wool* model and its fit for the primer

Checked 2026-10-13. Internal planning reference, not post prose. Marshall asked for research on publishing the primer chapter by chapter, the way Hugh Howey published *Wool* ([D32](../DECISIONS.md#d32-serialized-publishing-research)). This report explains how the *Wool* serial worked, sets it beside the serialized and early-access models used for technical books, records the platform rules that constrain each one, and closes with an editorial assessment of the options. Nothing here selects a publishing strategy.

## Evidence status: read this first

**No source page could be fetched in this session.** The environment's network policy refused every outbound connection (proxy `CONNECT` 403) to publishersweekly.com, hughhowey.com, kdp.amazon.com, leanpub.com, manning.com and every other host tried. Only web search worked. Every entry below therefore comes from search-result summaries of the cited pages, not from reading them.

Under the repo's tiering, nothing here is **verified primary** yet. Entries are tiered as:

- **Lead, primary source.** The cited page belongs to the originator (Howey, Amazon, Leanpub, the author), so a fetch will probably confirm it. Treat it as secondary until fetched.
- **Lead, secondary.** Press or third-party reporting.
- **Folklore.** Anecdote, a conflicting figure, or an inference not traced to any source.

No quotation in this file has been checked against its page. Before any of this enters an outline, draft or the marketing plan, fetch the URL and re-tier the entry. To allow fetches, add the hosts under Network access in the cloud environment settings ([docs](https://code.claude.com/docs/en/cloud-environments#network-access)).

## Summary

- ***Wool* was not planned as a serial.** Howey released a standalone 12,000-word story on Kindle for $0.99 in July 2011. Reader demand pulled four more parts out of him within about three months, then an omnibus in January 2012 that became the main seller (W1–W6).
- **The mechanics were a feedback loop, not a release plan.** A complete first part, quick monthly-or-faster follow-ups written in response to reader email and reviews, each part longer than the last, and a bundled edition priced higher for readers who waited (W3–W7).
- **The audience became leverage.** Self-published e-book income let Howey turn down seven-figure offers that wanted e-book rights, and take a print-only deal with Simon & Schuster instead (W9–W11). This maps onto steps 4 and 5 of the [marketing plan](../marketing-plan.md): self-publish, then pitch publishers from a demonstrated audience.
- **The primer differs from *Wool* in two ways that matter.** Its chapters will be free on the blog first, and its subject changes fast. *Wool*'s parts were paid and its text was finished once. Andy Weir's free-then-$0.99 *The Martian* (T10) and Will Larson's free *StaffEng* site plus paid book (T6) are closer precedents for free-first.
- **Platform rules shape the choice.** Free blog chapters rule out KDP Select and Kindle Unlimited (P4). KDP does not deliver added chapters to people who already bought a book (P7), while Leanpub does (P9). Kindle Vella, Amazon's serial platform, closed in February 2025 (P13).

## Part 1: How *Wool* worked

### W1. Before *Wool*

**Lead, secondary.** Howey's first novel was *Molly Fyde and the Parsona Rescue* (2009). Sources disagree on whether a small press published it or he self-published it. [Wikipedia](https://en.wikipedia.org/wiki/Hugh_Howey); [College of Charleston](https://today.cofc.edu/2013/06/19/shattered-worlds/) (2013-06-19).

### W2. The standalone first part

**Lead, secondary.** Howey wrote the original *Wool*, about 12,000 words, on lunch breaks while working at a university bookstore. He released it in July 2011 as a standalone $0.99 Kindle short story through KDP, without promotion. [Writer's Digest](https://www.writersdigest.com/be-inspired/how-hugh-howey-turned-his-self-published-story-wool-into-a-success-a-book-deal); [Slate](https://slate.com/culture/2013/03/hugh-howey-and-wool-how-the-self-pubbed-sci-fi-writer-relates-to-fans.html) (March 2013). Confirm the exact release day.

### W3. Readers asked for more

**Lead, secondary; primary if the book is checked.** By about late October 2011, *Wool* was on Amazon's Kindle science-fiction bestseller list and readers were emailing Howey for more. The author's note in *The Stranded* (*Wool* 5) reportedly says he never intended a series and wrote the next four parts because demand kept growing. [Slate](https://slate.com/culture/2013/03/hugh-howey-and-wool-how-the-self-pubbed-sci-fi-writer-relates-to-fans.html); [RealClearBooks](https://realclearbooks.com/2013/03/04/wooly_mammoth_5101.html) (2013-03-04).

### W4. Parts 2–5 and their cadence

**Lead, secondary.** *Proper Gauge* (2), *Casting Off* (3), *Unraveling* (4) and *The Stranded* (5) came out between about October and December 2011, each longer than the one before. Writer's Digest reports about 3,000 copies of part 2 in a month and more than 10,000 a month for parts 3 and 4. [Writer's Digest](https://www.writersdigest.com/be-inspired/how-hugh-howey-turned-his-self-published-story-wool-into-a-success-a-book-deal). Exact release dates and per-part prices are unconfirmed; Howey's late-2011 blog archive or the Amazon listings should settle both.

### W5. The omnibus

**Lead, secondary.** The *Wool Omnibus* (parts 1–5) came out in January 2012. It reportedly sold about 23,000 copies in its first month and spent two weeks on the New York Times e-book fiction list. Sources disagree on when that list run happened. [Writer's Digest](https://www.writersdigest.com/be-inspired/how-hugh-howey-turned-his-self-published-story-wool-into-a-success-a-book-deal).

### W6. Omnibus price

**Folklore until fetched.** A Howey blog post reportedly says the omnibus launched at $4.99 and that he later raised it by $1; another source gives $5.99. Both may be right at different times. [The Loop](https://theloopnewspaper.com/story/2019/03/30/community/hugh-howey-and-his-novel-path-to-success/5181.html) (2019-03-30); the Howey post itself was not isolated.

### W7. Income

**Lead, secondary.** These figures come from different outlets and dates. Cite each with its source rather than as a steady rate.

| Period | Reported figure | Source |
|---|---|---|
| Jan–Mar 2012 | About $19,000, $50,000, then $70,000 a month from fiction | [Publishers Weekly](https://publishersweekly.com/pw/print/20120409/51416-self-made-bestseller-weighs-traditional-deals.html), 2012-04-09 |
| Summer 2012 | 20,000–30,000 e-books and about $150,000 a month | [Writer's Digest](https://www.writersdigest.com/be-inspired/how-hugh-howey-turned-his-self-published-story-wool-into-a-success-a-book-deal) |
| 2012 | About $120,000 a month, which a later interview frames as an average | WSJ (Alexandra Alter, March 2013), relayed by [CS Monitor](https://csmonitor.com/Books/chapter-and-verse/2013/0315/WOOL-Why-all-the-hype) and [Meet Innovators](https://meetinnovators.com/2013/08/12/hugh-howey-author-wool/) |
| 2012 | More than $1 million from digital sales | [Charleston Magazine](https://mail.charlestonmag.com/node/30010) (weak) |

The WSJ original was not located.

### W8. He repeated the pattern

**Lead, secondary.** The *Shift* prequels came out as three parts (2012 to about January 2013) and then an omnibus, so Howey serialized again. *Dust* (2013) came out as a single novel. [SF Encyclopedia](https://sf-encyclopedia.com/entry/howey_hugh); [FantasticFiction](https://fantasticfiction.com/h/hugh-howey). The years given for the *Shift* parts conflict between sources. No source was found in which Howey regrets serializing.

### W9. Film rights

**Lead, secondary (strong).** In May 2012, 20th Century Fox acquired *Wool* with Ridley Scott's Scott Free and Steve Zaillian's Film Rites. The film was never made. [Publishers Weekly](https://publishersweekly.com/pw/by-topic/industry-news/page-to-screen/article/51934-hugh-howey-s-wool-nabbed-by-20th-century-fox.html) (May 2012).

### W10. The print-only deal

**Lead, secondary.** Publishers Lunch reported in December 2012 that Simon & Schuster had bought US hardcover and paperback rights, with editions out in March 2013, while Howey kept the e-book. The WSJ put the deal at mid-six figures and reported that Howey had turned down several seven-figure offers that required e-book rights. Publishers Lunch called print-only deals rare, not unprecedented; Bella Andre's earlier deal with Mira was one. [Publishers Lunch](https://lunch.publishersmarketplace.com/2012/12/wool-author-makes-print-only-deal-with-simon-schuster/) (December 2012).

### W11. Why keeping e-book rights mattered

**Lead, secondary for the first claim; folklore for the second.** By the time of the S&S deal, the e-books were already earning Howey more than the advances on offer (W7, W10). The usual explanation is the royalty gap: KDP's 70% on e-books priced in the standard band, against roughly 25% of net on a traditional e-book contract. That comparison was not traced to a source in this session.

### W12. Foreign rights and television

**Lead, secondary.** UK rights went to Century (Random House UK). His agent, Kristin Nelson, had licensed the book in more than 18 territories by the time of the S&S deal. [Writers Write](https://www.writerswrite.com/self-published-sf-author-hugh-51420121).

**Lead, primary source.** Apple TV+'s *Silo* premiered on 2023-05-05. Graham Yost created it, Rebecca Ferguson stars and Howey is an executive producer. It adapts *Wool*, *Shift* and *Dust*. [Apple press release](https://www.apple.com/tv-pr/news/2023/03/apple-tv-unearths-first-look-at-gripping-new-series-silo-and-sets-global-premiere-for-friday-may-5-2023) (March 2023).

### W13. Later advocacy

**Lead, primary source.** From February 2014, Howey published *Author Earnings* reports with a data partner, estimating self-published authors' share of Amazon sales from bestseller-list data. Critics disputed the method. [Goodreads mirror of a 2014 report](https://www.goodreads.com/author_blog_posts/6721292-author-earnings-3rd-quarter-report-making-an-iceberg-from-an-ice-cube).

### What transfers from *Wool*

These are editorial readings of W1–W13, not findings.

1. **A complete first installment.** *Wool* 1 worked on its own, and the series grew out of demand. For a primer, that means each released chapter teaches a whole idea, which the marketing plan already requires of each article and video.
2. **Readers set the sequence.** Howey wrote the next parts in response to email and reviews. The primer's 113-lesson menu allows the same move: publish early chapters, watch which ideas draw the strongest response, and pick the next chapters accordingly.
3. **Short gaps between installments.** The parts arrived roughly monthly or faster while attention was high. A counter-post by another author argues that serials fail when the gaps run long ([Goodreads](https://www.goodreads.com/author_blog_posts/4943661-the-verdict-is-in-serializing-your-novel-does-not-work); not by Howey).
4. **The bundle captures readers who wait.** The omnibus sold more than the individual parts and at a higher price. Many readers prefer to wait for the whole thing.
5. **The audience becomes leverage.** Howey negotiated from proven sales and kept the rights that earned the most.

What doesn't transfer: fiction's cliffhangers, and the single fixed text. A book about agentic coding will need revision as tools change, and *Wool* never did.

### Myths and do-not-use

- **"First self-published author offered a print-only deal by a major publisher."** Publishers Lunch says such deals were rare, with an earlier example (W10). Say "rare."
- **"$150,000 a month" or "$120,000 a month" as a steady income.** The figures conflict, and one is an average (W7).
- **"*Wool* was planned as a serial."** Every source says the first part was a standalone (W3).
- **"Seven-figure Simon & Schuster deal."** The seven-figure offers were the ones he turned down (W10).
- **"Ridley Scott made a *Wool* film."** It was optioned and never made; the adaptation is the Apple TV+ series (W9, W12).
- **"Serializing your novel does not work" attributed to Howey.** It was written by another author.

## Part 2: Serialized and early-access models for technical books

### T1. Leanpub in-progress books

**Lead, primary source.** Leanpub lets authors publish a book while still writing it and release new versions as often as they like. Every buyer gets every update free, whenever they bought and whatever they paid. Authors set a minimum price, which can be $0, and a suggested price, and buyers choose any amount from the minimum up. Leanpub's help center describes starting cheap or free and raising the price as chapters land as a common pattern. [About Leanpub](https://leanpub.com/about); [variable pricing](https://help.leanpub.com/en/articles/110750-why-do-i-see-a-suggested-price-and-a-minimum-price-when-i-buy-a-leanpub-book-what-is-variable-pricing); [raising price over time](https://help.leanpub.com/en/articles/110704-can-i-change-the-price-of-my-book-after-publishing-it-for-example-can-i-start-cheap-release-new-chapters-over-time-and-increase-the-price-as-my-book-s-getting-more-valuable). Royalty terms are in P9.

### T2. Jeff Geerling's *Ansible for DevOps*

**Lead, primary source.** Geerling reported netting more than $25,000 from in-progress Leanpub sales before the book was finished (2015). By 2023, across 41 revisions, he reported about 87,000 copies and more than $300,000 in lifetime revenue across Leanpub, Amazon and iBooks, with sales shifting mostly to Amazon once a complete edition was listed there. [2015 post](https://www.jeffgeerling.com/blog/2015/25k-book-sales-and-im-almost-ready-publish/); [2023 post](https://www.jeffgeerling.com/blog/2023/self-publishing-technical-book-10-years/). This is the strongest technical-book precedent for selling a book while writing it and updating it for years.

### T3. Manning MEAP

**Lead, primary source.** Manning Early Access Program buyers get chapters as they are drafted, then the final ebook (and print, if bought). Each MEAP title has a liveBook discussion forum where readers comment and the author and editors respond. [Manning MEAP](https://www.manning.com/meap-program).

### T4. Pragmatic Bookshelf beta books

**Lead, primary source.** Beta ebook buyers get updates during the beta and for the life of the edition. Readers file errata through a per-title page, and the reports feed revisions. [PragProg on Medium](https://medium.com/pragmatic-programmers/programming-books-in-beta-from-the-pragmatic-bookshelf-b9633f78c620) (about 2024).

### T5. O'Reilly Early Release

**Lead, secondary.** O'Reilly sells raw, unedited Early Release chapters that update until the final ebook. [Author account](https://infrastructure-as-code.com/posts/early-release-is-available.html) (about 2016). No current O'Reilly page was found.

### T6. Will Larson's *Staff Engineer*

**Lead, primary source.** The stories and guides on StaffEng.com are free, and Larson said they would stay free. The self-published book, sold on Gumroad and Amazon, packages that material. A paid "Early Edition", still being revised from reader feedback, went on sale around January 2021, and its buyers got the final digital version too. [Early edition post](https://lethain.com/staff-eng-early-edition/); [book page](https://lethain.com/staff-engineer/). No sales figures were found. **This is the closest analogue to the primer's plan:** free web chapters, a paid packaged book, and a paid early edition.

### T7. Kent Beck's *Tidy First?*

**Lead, primary source.** Beck drafted chapters on his Substack before O'Reilly published the book in 2023. In a July 2023 post he framed paid subscriptions as a trade: subscribers got early access, and he got a finished draft plus feedback that improved the outline. [State of Tidy First](https://tidyfirst.substack.com/p/state-of-tidy-first). Some chapters were paid-only, so this is paid early access, not free-first. It is also evidence that a traditional technical publisher accepted material first drafted on a newsletter.

### T8. Gergely Orosz's *The Software Engineer's Guidebook*

**Lead, primary source.** After pitching to publishers and parting ways with one, Orosz self-published in 2023. The book took about four years. About two years after launch he reported roughly 40,000 copies and about $612,000 in royalties. [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-software-engineers-guidebook); [pitching post](https://blog.pragmaticengineer.com/four-years-on-writing-a-tech-book-pitching-to-a-publisher/). The book was not serialized; the case is about a newsletter audience serving as distribution.

### T9. Julia Evans's zines

**Lead, primary source.** Some early zines used "pay for early access, then free": *Let's learn tcpdump* (2017) sold early access to 190 buyers for $1,970 before going free. She reported $101,558 in zine revenue for 2018. A No Starch Press box set of her *free* zines sold about 4,000 copies by late 2019. [tcpdump zine](https://jvns.ca/blog/2017/05/14/learn-tcpdump-zine/); [2019 revenue](https://jvns.ca/blog/2019/10/01/zine-revenue-2019/); [2019 review](https://jvns.ca/blog/2019-year-in-review/). Free material still sold as print.

### T10. Andy Weir's *The Martian*

**Lead, secondary.** Weir posted chapters free on his website over several years. At readers' request he offered an e-reader file, then a Kindle edition at $0.99, which reportedly sold about 35,000 copies at roughly $0.30 each to him. Crown then bought print rights, and its edition came out in February 2014. [Hollywood Reporter](https://www.hollywoodreporter.com/news/how-a-99-cent-novel-842582) (2015); [Publishers Weekly](https://www2.publishersweekly.com/pw/print/20150914/68033-the-martians-chronicle.html) (2015-09-14). Sources disagree on whether the 35,000 took three or six months. **Fiction, but the closest free-first parallel to *Wool*:** readers who could read for free paid for the convenient edition.

### T11. Dickens's part-publication

**Lead, secondary.** *The Pickwick Papers* ran in 20 monthly parts from 1836 to 1837 at a shilling each. Sales grew from a first printing of about 1,000 to about 40,000 per part. [Victorian Web](https://victorianweb.org/authors/dickens/pickwick/patten.html). Readers paid for every part, so this is paid serialization, like *Wool*, not free-first.

### T12. Amazon's serial platforms

**Lead, primary source.** Amazon announced Kindle Serials on 2012-09-06: buyers paid once and received later episodes in the same book. [Amazon press release](https://press.aboutamazon.com/2012/9/amazon-publishing-introduces-kindle-serials-great-stories-one-episode-at-a-time). No end date was found. Kindle Vella is covered in P13.

### T13. Web serials and Substack

**Lead, secondary.** The common web-fiction model offers free public chapters on Royal Road and sells advance chapters through Patreon ([Lyse Beck](https://litopia.com/lyse-beck/a-royal-road-adventure/)). Authors also serialize books as Substack posts, sometimes paywalled; Chuck Palahniuk serialized a novel there ([TheWrap](https://www.thewrap.com/chuck-palahniuk-joins-substack-greener-pastures-novel/)). Both sell access to posts, not a downloadable book.

### T14. Does free cannibalize paid?

**Lead, primary source; mixed evidence.** John Hilton III and David Wiley (2010) compared BookScan print sales in the eight weeks before and after free digital editions of 41 books. Most groups rose, but 20 of 24 Tor titles fell, and the authors called the result correlational and not generalizable. [BYU ScholarsArchive](https://scholarsarchive.byu.edu/facpub/826).

**Lead, secondary; argument, not data.** Tim O'Reilly argued in 2002 that obscurity threatens authors more than piracy ([archive copy](https://gwern.net/docs/www/www.oreilly.com/a59d4d4af663b3a3d5c71ff21891e08cad65d9e5.html)). Cory Doctorow reports that his free Creative Commons novel went through six print runs while being downloaded 700,000+ times ([Creative Commons](https://creativecommons.org/2008/09/09/cory-doctorow-releases-content-selected-essays-on-technology-creativity-copyright-and-the-future-of-the-future/)).

### T15. Publishers and previously blogged material

**Lead, secondary; opinion.** Agent Chip MacGregor says many editors are uneasy about material that has already run on a blog, and advises holding some fresh content back ([MacGregor & Luedeke](https://macgregorandluedeke.com/blog/do-i-include-my-blog-experience-in-my-proposal)). Others say blog material is fine if the rights are clear; the legal problem is copyright assigned to a host site, as with guest posts. *Tidy First?* (T7) cuts the other way. Marshall owns the yountlabs.com posts, so the open question is a publisher's appetite, not its legal ability to take them.

### Do-not-use

- **"Hilton & Wikström" study.** The study is Hilton & Wiley (2010).
- **Leanpub's lifetime payout totals.** Its pages give conflicting figures.
- **Royal Road top-earner Patreon incomes** and **promotional Substack serial-fiction figures.** Secondhand estimates and marketing copy.
- ***An Elegant Puzzle* as "a collection of revised blog posts."** Widely repeated, not traced to a source.

## Part 3: Platform rules that constrain a serial

All entries are leads from official help pages unless marked otherwise. These pages change; refetch before relying on any figure.

### P1. KDP 70% band

**Lead, primary source.** A KDP help page says the 70% band's maximum list price on Amazon.com rose from $9.99 to $12.99 effective 2026-07-07. The $2.99 minimum is unchanged. Delivery costs ($0.15/MB in the US) come out of 70% royalties. [KDP pricing FAQ](https://kdp.amazon.com/en_US/help/topic/A301WJ6XCJ8KW0); [eBook royalties](https://kdp.amazon.com/en_US/help/topic/G200644210). Third-party guides add two conditions to check on the royalties page: the e-book must be priced at least 20% below the print edition, and some marketplaces pay 70% only for books in KDP Select.

### P2. $0.99 installments earn 35%

**Lead, primary source.** $0.99 is still allowed for files under 3 MB, at the 35% rate with no delivery fee, so a $0.99 installment earns about $0.35. [List price requirements](https://kdp.amazon.com/en_US/help/topic/G200634560). This matches the roughly $0.30 per copy reported for Weir (T10).

### P3. Content freely available online

**Lead, primary source.** KDP accepts content that is freely available on the web only from its copyright owner. Its content-quality guide also lists as disappointing content that is "too short", not significantly different from another book in the store, or that sends readers elsewhere for the full text. [Content guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390); [content quality guide](https://kdp.amazon.com/en_US/help/topic/G200952510). Marshall can publish his own blog chapters on KDP. Short per-chapter installments, or an omnibus that only repeats them, are at risk under the "too short" and "not significantly different" items.

**Folklore.** Authors widely report that KDP sends rights-verification emails when a book's text appears online. Keep proof of authorship ready.

### P4. KDP Select rules out free blog chapters

**Lead, primary source.** While enrolled in KDP Select, a book's digital edition must be available only through KDP, which Amazon says covers "your website, blogs, etc." Up to 10% may appear elsewhere as a sample. Terms run in 90-day periods. [KDP Select](https://kdp.amazon.com/en_US/select). **Chapters that stay free on the blog rule out KDP Select and Kindle Unlimited**, unless the blog copies are cut to 10% or less. Selling on Leanpub at the same time would also breach Select.

### P5. Series pages and box sets

**Lead, primary source.** KDP series pages can be ordered or unordered, and a Kindle box set can be attached to a series. KDP offers no paperback box set. [Series help](https://kdp.amazon.com/en_US/help/topic/GMFKBUS43QQ5AJ5A).

### P6. Pre-orders

**Lead, primary source; conflicting.** Pre-orders are ebook-only, and the final file is due 72 hours before release. One page gives a one-year window; another gives 18 months for pre-orders created on or after 2026-09-02. [Pre-orders](https://kdp.amazon.com/en_US/help/topic/G201499380).

### P7. Updates don't reach existing KDP buyers

**Lead, primary source.** Republishing an e-book serves the new file to new buyers only. KDP pushes updates to existing customers only for serious quality problems, and explicitly declines added or changed chapters. Significant changes count as a new edition. [Updating eBooks](https://kdp.amazon.com/en_US/help/topic/G200966010). On KDP, growing one book chapter by chapter strands early buyers. The KDP-native shape is separate installments plus a series page, as *Wool* did.

### P8. Print

**Lead, primary source.** KDP paperbacks need at least 24 pages, and spine text needs 79 or more. [Print options](https://kdp.amazon.com/en_US/help/topic/G201857950). A short installment can technically be printed but makes a poor paperback, so in practice print means the collected edition. *Wool*'s print edition came only with the S&S deal (W10).

### P9. Leanpub royalties

**Lead, primary source; terms conflict.** One Leanpub page gives 80% on every sale. Another gives 80% at $7.99 and above, and 80% minus $0.50 between $0.99 and $7.98. Leanpub authors may sell the same book anywhere else, including KDP outside Select. [About Leanpub](https://leanpub.com/about); [selling elsewhere](https://help.leanpub.com/en/articles/117414-can-i-sell-my-book-on-leanpub-and-on-amazon-or-on-other-self-publishing-platforms-at-the-same-time). The 2016 rate was 90% minus 50 cents; do not use it.

### P10. Gumroad and Payhip

**Lead, primary source.** Gumroad charges 10% + $0.50 per direct sale, and 30% for sales through its Discover marketplace ([pricing](https://gumroad.com/pricing)). Payhip's free plan takes 5% per sale; its $29 and $99 monthly plans take 2% and 0%, with card processing on top ([pricing](https://payhip.com/pricing)).

### P11. Substack and Ghost

**Lead, secondary.** Substack takes 10% of paid subscriptions plus Stripe fees. Ghost charges a flat hosting fee and takes no revenue share. Neither sells a downloadable ebook natively. [Ghost comparison](https://ghost.org/vs/substack) (vendor marketing).

### P12. Other stores

**Folklore until re-sourced.** Third-party guides give Kobo 70% at $2.99 and up and 45% below, Apple Books 70%, and Draft2Digital about 10% of retail. Re-source from the official author portals before use.

### P13. Kindle Vella closed

**Lead, secondary.** Amazon announced on 2024-10-29 that it would phase out Kindle Vella, saying it hadn't caught on as hoped. The last day to publish or buy tokens was 2024-12-04, and the platform closed in February 2025. [GeekWire](https://www.geekwire.com/2024/amazon-to-shut-down-kindle-vella-serial-book-platform-saying-it-hasnt-caught-on-as-wed-hoped/) (2024-10-30). No Amazon replacement for serialized reading was found. Vella was fiction-only.

## Part 4: Options for the primer

This section is an editorial assessment for Marshall to accept or reject. It assumes the marketing plan's sequence (free articles, then a self-published book, then a publisher pitch) and does not select a strategy.

| Model | Precedent | What's paid | Fit with free blog chapters | Main risk |
|---|---|---|---|---|
| A. *Wool*-style KDP installments, then an omnibus | *Wool* (W2–W5), *Shift* (W8) | Each part at $0.99–$2.99, then the omnibus | Allowed outside Select (P3, P4) | Thin parts read as "too short" or duplicate the blog (P3); $0.99 earns about $0.35 (P2); buyers of early parts get no revisions (P7) |
| B. Leanpub in-progress book | Geerling (T2), Manning and PragProg betas (T3, T4) | One growing book, updated free for every buyer | Allowed; sell on KDP outside Select once complete (P9) | Smaller storefront than Amazon; Geerling's sales moved to Amazon once a complete edition was listed there (T2) |
| C. Free site, paid packaged book and early edition | Larson (T6), Weir (T10), Evans (T9) | The edited, convenient edition | The blog is the free site | Paid value has to come from editing, ordering and format, because the text is free |
| D. Paid newsletter early access | Beck (T7) | Subscription to drafts | Conflicts with the free-first principle in the marketing plan | Recurring obligation, and splits the audience between free and paid |

**Assessment.** *Wool* shows the loop to copy: a complete first installment, quick follow-ups chosen from reader response, a bundle for readers who wait, and an audience that becomes negotiating leverage. Its specific mechanism, paid KDP parts with a fixed text, fits the primer less well than its loop. Two facts push toward model B or C, or a mix of the two:

1. **The chapters will be free on the blog.** Readers will pay for the edited, ordered, offline edition, not for access to the words (T6, T9, T10). Thin paid installments that repeat free posts are the weakest product, and KDP's content rules work against them (P3).
2. **The subject changes fast.** Agent tooling will change during the writing. Leanpub delivers every revision to every buyer (T1); KDP strands early buyers (P7). Kent Beck's follow-up book stalled partly because events overtook the material (T7 source, January 2026 post).

**One way to combine them, for discussion:** chapters go up free on yountlabs.com as articles. Each of the seven parts, once its chapters are written, is folded into a Leanpub in-progress edition, like Larson's paid early edition, at a low minimum price that rises as parts land. The early-edition releases serve as *Wool*'s installments: they set the cadence, gather feedback and build the buyer list. The complete edition then goes to KDP outside Select and to print. The publisher pitch follows the Howey pattern: lead with the demonstrated audience, and consider asking for print-only or limited rights, as Howey did (W10). That pitch rests on audience numbers this project doesn't have yet.

## Open questions for Marshall

1. Should paid editions follow each of the seven parts, or wait for the complete book?
2. Should anything be held back from the blog for the paid edition (exercises, worked examples, a part-level synthesis)? MacGregor's advice (T15) and model C both favor some paid-only material, but it trades against the 90%-free principle in the marketing plan.
3. Is KDP Select's reach worth pulling chapters down to 10% after the book ships? This report assumes not, since the free articles are the marketing.
4. How often should installments come out? *Wool*'s parts arrived about monthly; no cadence has been selected for the primer.

## Verification queue

When network access allows, fetch in this order: the Publishers Weekly 2012 articles (W7, W9), Publishers Lunch (W10), the KDP Select, content-quality and update pages (P3, P4, P7), Leanpub's pricing page (P9), Larson's early-edition post (T6), Geerling's posts (T2), and Howey's late-2011 blog archive for the *Wool* 2–5 release dates and prices (W4, W6).
