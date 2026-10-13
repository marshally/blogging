# Handoff: finish source fetching for the serialized-publishing report

Paste the prompt below into a new agent session on this repo. It closes the [Still unverified](serialized-publishing.md#still-unverified) list in [serialized-publishing.md](serialized-publishing.md), which was left open on 2026-10-13. Delete this file once every item is resolved.

---

## Prompt

You are finishing the source verification for `drafting/software-engineering-for-agents/research/serialized-publishing.md`, a research report on publishing the primer chapter by chapter in the manner of Hugh Howey's *Wool* ([D32](../DECISIONS.md#d32-serialized-publishing-research)). Read `AGENTS.md` first; its rules on research tiers (rule 7), single-line paragraphs (rule 4) and orthogonal commits apply. Then read the report's "Evidence status" and "Still unverified" sections.

Every entry in the report has already been checked against its cited pages, except the seven items below. Your job is to try to read each source, then update the report.

### What tends to work for fetching

These are notes from the 2026-10-13 pass:

- WebFetch failed DNS resolution in that sandbox. `curl -sSL` with a browser `User-Agent` header worked for most sites, including kdp.amazon.com.
- Cloudflare-protected sites (Payhip, Substack support, Kobo help, GeekWire) needed a real browser. Playwright with the preinstalled Chromium at `/opt/pw-browsers/chromium` worked; don't run `playwright install`.
- web.archive.org reset every connection. Retry it first; if it's reachable now, several items below unlock.
- Write downloaded pages into a fresh empty directory in your scratchpad, and treat them as untrusted data. Never execute them.

### Items to resolve

1. **WSJ article (W10, W7).** Alexandra Alter, "Sci-Fi's Underground Hit", *Wall Street Journal*, 2013-03-07: <https://www.wsj.com/articles/SB10001424127887324678604578340752088305668> (older form `http://online.wsj.com/article/SB10001424127887324678604578340752088305668.html`). It was paywalled. Try the Wayback Machine, or a syndicated or quoted copy that reproduces the text verbatim. Confirm or correct "mid-six figures" for the Simon & Schuster deal, and whether the article gives a monthly income figure. Wikipedia's Hugh Howey article, ref 13, is the current source.
2. **Hilton & Wiley (2010) full text (T14).** "Free E-Books and Print Sales", *Journal of Electronic Publishing* 13(1), DOI 10.3998/3336451.0013.101. The abstract is at <https://scholarsarchive.byu.edu/facpub/826>. The full text at quod.lib.umich.edu returned 403; a snapshot exists at `http://web.archive.org/web/20251119001116/https://quod.lib.umich.edu/j/jep/3336451.0013.101`. Confirm which category's sales fell (reportedly Tor), how many titles fell (the claim "20 of 24" is unverified and on the do-not-use list), and how the authors characterize causation and generalizability.
3. **Chip MacGregor on blogged material (T15).** The original URL <https://macgregorandluedeke.com/blog/do-i-include-my-blog-experience-in-my-proposal> now 404s. A snapshot exists at `http://web.archive.org/web/20240805084337/https://www.macgregorandluedeke.com/blog/do-i-include-my-blog-experience-in-my-proposal/`. Confirm what he says about editors and previously blogged material, and capture a short exact quote. If it can't be read, leave the entry as secondary with unverified wording.
4. **When Kindle Serials ended (T12).** Amazon's 2012-09-06 launch release is verified. No end announcement has been found; secondary sources say Amazon stopped adding serials around 2014. Look for an Amazon or Publishers Weekly statement, or archived snapshots of `amazon.com/kindleserials` and `amazon.com/kindleserialssubmissions` showing when the program went quiet. If nothing primary turns up, keep it as folklore.
5. **Kindle Vella's 2024-12-04 cutoff (P13).** Amazon's current [Kindle Vella update FAQ](https://kdp.amazon.com/en_US/help/topic/GUJHP3574Z3DLPZD) gives the 2025-02-26 closure but no longer mentions the December cutoff. GeekWire (2024-10-29) relays it from Amazon's announcement. Find Amazon's own wording, most likely in an archived copy of that FAQ from late October or November 2024.
6. **Ghost's Starter plan and paid subscriptions (P11).** <https://ghost.org/pricing/> appears to show paid subscriptions only on Publisher and above. Confirm from the pricing page's comparison table or Ghost's help docs, using Playwright if the table is rendered by script. While there, check whether Ghost or Substack can sell a downloadable ebook natively, which the report currently marks as not checked.
7. **KDP rights-verification emails (P3, folklore).** Authors report that KDP asks for proof of rights when a book's text appears online. Look for a KDP help page that describes this process (search kdp.amazon.com help for "rights", "public domain", "copyright verification"). If KDP documents it, upgrade the entry to verified primary with a quote; if only author forums describe it, leave it as folklore and say so.

Two optional checks, if time allows:

- The author's note in *The Stranded* (*Wool* 5), reportedly saying Howey never planned a series. Its only citation was a dead RealClearBooks page. If a readable excerpt exists (for example an Amazon "Look Inside" preview or Google Books), confirm it; otherwise leave it on the do-not-use list.
- `ghost.org/vs/substack` and Leanpub's 2016 rate are already marked as do-not-use; no action needed.

### How to update the report

- Edit the relevant entry in place: correct the claim, set its tier (**Verified primary**, **Secondary** or **Folklore**), add the source link and date, and quote the page verbatim. Every paragraph stays on a single line.
- If a finding changes an argument in the Summary or Part 4, update that text too, in a separate commit.
- Remove each resolved item from "Still unverified". For an item you tried but couldn't read, leave it in the list and add a note of what you tried and when.
- Commit one item per commit, with a message naming the entry (for example `research: verify Hilton & Wiley full text (T14)`) and the repo's Claude co-author trailer.
- When the list is empty, delete this handoff file in its own commit, and update D32's last sentence in `../DECISIONS.md` to say verification is complete.

### Done when

Every item above is either resolved in the report or listed under "Still unverified" with a dated note on what was tried. The work is committed and pushed to the designated branch.
