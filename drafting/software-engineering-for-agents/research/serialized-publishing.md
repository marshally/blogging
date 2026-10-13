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
- **Platform rules shape the choice.** Free blog chapters rule out KDP Select and Kindle Unlimited (P4). KDP now delivers revised editions to earlier buyers, but a large expansion may need a new edition (P7); Leanpub is built for a book that grows, with every update free to every buyer (T1). KDP also requires a serialized part to say so and bars installments that send readers elsewhere for the rest (P3, P5). Kindle Vella, Amazon's serial platform, closed in February 2025 (P13).

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

Each entry was checked against the platform's own page on 2026-10-13 and is verified primary unless marked otherwise. These pages change; refetch before relying on any figure.

### P1. KDP 70% band

**Verified primary.** "Effective July 7, 2026, the 70% royalty option price band is $2.99-$12.99 on Amazon.com, expanding from the previous range of $2.99-$9.99." The $9.99 cap had been in place since 2007. Delivery costs come out of 70% royalties, at $0.15/MB in the US. The list price must be "at least 20% below the list price on Amazon for any physical edition". Sales in Brazil, Japan, Mexico and India earn 70% only for books enrolled in KDP Select. [List price requirements](https://kdp.amazon.com/en_US/help/topic/G200634560); [Digital Book Pricing Page](https://kdp.amazon.com/en_US/help/topic/G200634500).

### P2. $0.99 installments earn 35%

**Verified primary.** $0.99 is the minimum list price at the 35% rate for files under 3 MB; the minimum rises to $1.99 at 3 MB and $2.99 at 10 MB, which matters for installments with images. KDP deducts no delivery cost at 35%. Amazon's own worked example gives $0.35 per $0.99 sale at 0% VAT. [List price requirements](https://kdp.amazon.com/en_US/help/topic/G200634560); [eBook royalties](https://kdp.amazon.com/en_US/help/topic/G200644210). This matches the roughly $0.30 per copy reported for Weir (T10).

### P3. Content freely available online

**Verified primary.** KDP "will not accept content under copyright that is freely available on the web unless it's provided by the owner of the copyright" ([content guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390)), so Marshall can publish his own blog chapters on KDP. The [content quality guide](https://kdp.amazon.com/en_US/help/topic/G200952510)'s list of disappointing content includes three more items that bear on a serial:

- "Content that is either marketed as a subscription or redirects readers to an external source to obtain the full content". An installment can't send readers to the blog for the rest.
- "Content that is not significantly different from content in another book available in the Kindle Store" and "Content that is too short". Thin per-chapter installments are at risk.
- "Content that is excessively reused, recycled, or repeated within or across books". The same page's multi-work section allows collections of "content you've previously published in your catalog", so an omnibus of one's own installments is allowed if the reuse isn't excessive.

**Folklore.** Authors widely report that KDP sends rights-verification emails when a book's text appears online. Keep proof of authorship ready.

### P4. KDP Select rules out free blog chapters

**Verified primary.** Enrolling in KDP Select means "you cannot distribute your book digitally anywhere else, including on your website, blogs, etc." ([KDP Select](https://kdp.amazon.com/en_US/select)). The Select terms also bar distributing "a book that is substantially similar" in digital format ([KDP terms](https://kdp.amazon.com/en_US/help/topic/G200627430)). Authors "may choose to make up to 10% of your book available on other sites as a sample" ([enrolling in Select](https://kdp.amazon.com/en_US/help/topic/GD9PMU58BV24QFZ7)). Terms run in 90-day periods. **Chapters that stay free on the blog rule out KDP Select and Kindle Unlimited**, unless the blog copies are cut to 10% or less. Selling on Leanpub at the same time would also breach Select.

### P5. Series pages, box sets and serial labeling

**Verified primary.** KDP series can be ordered or unordered ([reading order](https://kdp.amazon.com/en_US/help/topic/G29L44KLZ6RDYGDP)). A Kindle box set attaches to a series only "as related content", and KDP offers no paperback box set ([series help](https://kdp.amazon.com/en_US/help/topic/GMFKBUS43QQ5AJ5A)). KDP's [box set guidelines](https://kdp.amazon.com/en_US/help/topic/GD4TJFW4JEESLH4B) say it "encourages prioritizing individual titles linked to a series". They require a serialized release to say so in its description ("Episode 1," "Part 1 of 3") and to state that the work continues in later volumes. A box set of previously published titles should say so.

### P6. Pre-orders

**Verified primary.** Pre-orders are ebook-only and for new titles, with at most 10 active at a time. The final file is due 72 hours before release. A pre-order created on or after 2026-09-02 can be set up to 18 months out; earlier ones were limited to 12 months. [Pre-orders](https://kdp.amazon.com/en_US/help/topic/G201499380).

### P7. Updates reach existing KDP buyers

**Verified primary.** "For customers who bought your eBook before the update, the new version is delivered automatically after they finish a reading session and close the book," keeping their highlights and notes. Readers who have turned off Automatic Book Update don't receive it. KDP still declines *manual* update requests for added chapters or "significant changes that warrant a new edition", and the page doesn't say whether automatic delivery covers added chapters. [eBook update customer notifications](https://kdp.amazon.com/en_US/help/topic/G200966010). Revisions to a KDP edition now mostly reach early buyers, but a large expansion may still belong in a new edition. Many older guides say the opposite; don't rely on them.

### P8. Print

**Verified primary.** KDP paperbacks need at least 24 pages, and spine text is printed only on books with "more than 79 pages". [Paperback submission guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950). A short installment can technically be printed but makes a poor paperback, so in practice print means the collected edition. *Wool*'s print edition came only with the S&S deal (W10).

### P9. Leanpub royalties

**Verified primary.** "Leanpub's self-published authors earn 80% royalties on every sale of $7.99 and up, and 80% minus 50 cents on purchases below $7.99" ([About Leanpub](https://leanpub.com/about)). Since 2024 the minimum paid ebook price can be $0.99, or free; bundles start at $7.99 ([pricing article](https://help.leanpub.com/en/articles/10549058-leanpub-product-pricing-flexibility-to-enhance-your-book-marketing-opportunities-for-authors), 2025-02-13). A $0.99 sale earns about $0.29. Leanpub says it is "absolutely ok" to publish the same book on Leanpub and Amazon at once ([selling elsewhere](https://help.leanpub.com/en/articles/117414-can-i-sell-my-book-on-leanpub-and-on-amazon-or-on-other-self-publishing-platforms-at-the-same-time)), outside KDP Select (P4). The 2016 rate was 90% minus 50 cents; do not use it.

### P10. Gumroad and Payhip

**Verified primary.** Gumroad charges 10% + $0.50 per direct sale and 30% for sales through its Discover marketplace, with no monthly fee ([pricing](https://gumroad.com/pricing)). Payhip's free plan takes 5% per sale; its $29 and $99 monthly plans take 2% and 0%, and PayPal and Stripe fees apply on every plan ([pricing](https://payhip.com/pricing)).

### P11. Substack and Ghost

**Verified primary.** "Substack keeps 10% of subscription revenue, and Stripe charges its own payment processing fees" ([Substack support](https://support.substack.com/hc/en-us/articles/360037607131)). Ghost charges no transaction fee; its Starter plan is $18 a month and Publisher $29 a month, billed yearly ([Ghost pricing](https://ghost.org/pricing/)). Ghost's comparison table appears to limit paid subscriptions to Publisher and above; confirm before relying on it. Both sell access to posts. Whether either can sell a downloadable ebook was not checked.

### P12. Other stores

**Verified primary.** Kobo pays 70% on original works priced at $2.99 and up, with no cap, and 45% below ([Kobo Writing Life](https://kobowritinglife.zendesk.com/hc/en-us/articles/360058976032-What-will-my-earnings-be)). Apple Books pays "70% royalties on every ebook, regardless of price" ([Apple Books for Authors](https://authors.apple.com/)). Draft2Digital keeps about 10% of retail as commission, so authors get about 60% at most stores. It also charges a $20 activation fee, plus $12 a year for accounts earning under $100 ([D2D FAQ](https://draft2digital.com/faq/); [royalty rates](https://draft2digital.com/blog/royalty-rates/)).

### P13. Kindle Vella closed

**Verified primary for the closure; secondary for the December cutoff.** Amazon's FAQ says it wound down Kindle Vella "effective February 26, 2025" because it "didn't catch on as we'd hoped", and encourages authors to republish stories as ebooks ([Kindle Vella update FAQ](https://kdp.amazon.com/en_US/help/topic/GUJHP3574Z3DLPZD)). GeekWire reported the announcement on 2024-10-29 and relayed that no new episodes or tokens would be available after 2024-12-04 ([GeekWire](https://www.geekwire.com/2024/amazon-to-shut-down-kindle-vella-serial-book-platform-saying-it-hasnt-caught-on-as-wed-hoped/)). No Amazon replacement for serialized reading was found.

## Part 4: Options for the primer

This section is an editorial assessment for Marshall to accept or reject. It assumes the marketing plan's sequence (free articles, then a self-published book, then a publisher pitch) and does not select a strategy.

| Model | Precedent | What's paid | Fit with free blog chapters | Main risk |
|---|---|---|---|---|
| A. *Wool*-style KDP installments, then an omnibus | *Wool* (W2–W5), *Shift* (W8) | Each part at $0.99–$2.99, then the omnibus | Allowed outside Select (P3, P4) | Thin parts read as "too short" or duplicate the blog (P3); $0.99 earns about $0.35 (P2); each part must be labeled as part of a serial and can't point readers to the blog for the rest (P3, P5) |
| B. Leanpub in-progress book | Geerling (T2), Manning and PragProg betas (T3, T4) | One growing book, updated free for every buyer | Allowed; sell on KDP outside Select once complete (P9) | Smaller storefront than Amazon; Geerling's sales moved to Amazon once a complete edition was listed there (T2) |
| C. Free site, paid packaged book and early edition | Larson (T6), Weir (T10), Evans (T9) | The edited, convenient edition | The blog is the free site | Paid value has to come from editing, ordering and format, because the text is free |
| D. Paid newsletter early access | Beck (T7) | Subscription to drafts | Conflicts with the free-first principle in the marketing plan | Recurring obligation, and splits the audience between free and paid |

**Assessment.** *Wool* shows the loop to copy: a complete first installment, quick follow-ups chosen from reader response, a bundle for readers who wait, and an audience that becomes negotiating leverage. Its specific mechanism, paid KDP parts with a fixed text, fits the primer less well than its loop. Two facts push toward model B or C, or a mix of the two:

1. **The chapters will be free on the blog.** Readers will pay for the edited, ordered, offline edition, not for access to the words (T6, T9, T10). Thin paid installments that repeat free posts are the weakest product, and KDP's content rules work against them (P3).
2. **The subject changes fast.** Agent tooling will change during the writing. Leanpub is designed for a book that grows, delivering every revision to every buyer (T1). KDP now pushes revisions to earlier buyers too, but treats a large expansion as a possible new edition (P7). Kent Beck's follow-up book stalled partly because events overtook the material (T7 source, January 2026 post).

**One way to combine them, for discussion:** chapters go up free on yountlabs.com as articles. Each of the seven parts, once its chapters are written, is folded into a Leanpub in-progress edition, like Larson's paid early edition, at a low minimum price that rises as parts land. The early-edition releases serve as *Wool*'s installments: they set the cadence, gather feedback and build the buyer list. The complete edition then goes to KDP outside Select and to print. The publisher pitch follows the Howey pattern: lead with the demonstrated audience, and consider asking for print-only or limited rights, as Howey did (W10). That pitch rests on audience numbers this project doesn't have yet.

## Open questions for Marshall

1. Should paid editions follow each of the seven parts, or wait for the complete book?
2. Should anything be held back from the blog for the paid edition (exercises, worked examples, a part-level synthesis)? MacGregor's advice (T15) and model C both favor some paid-only material, but it trades against the 90%-free principle in the marketing plan.
3. Is KDP Select's reach worth pulling chapters down to 10% after the book ships? This report assumes not, since the free articles are the marketing.
4. How often should installments come out? *Wool*'s parts arrived about monthly; no cadence has been selected for the primer.

## Verification queue

When network access allows, fetch in this order: the Publishers Weekly 2012 articles (W7, W9), Publishers Lunch (W10), the KDP Select, content-quality and update pages (P3, P4, P7), Leanpub's pricing page (P9), Larson's early-edition post (T6), Geerling's posts (T2), and Howey's late-2011 blog archive for the *Wool* 2–5 release dates and prices (W4, W6).
