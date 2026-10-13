# Handoff: finish citation checks for the voice-models memo

Written 2026-10-13. Paste the prompt below into a new session to finish the work. The checks so far were run by loading each page with `curl`. Bloomberg, Macmillan (`us.macmillan.com`), pulitzer.org, and bloomsbury.com returned proxy 403s or Cloudflare challenges. The Internet Archive (`web.archive.org`) reset the connection. A session with those hosts allowed, or a browser-capable session, should be able to close most items.

## Prompt

> Finish the incomplete citation checks in `drafting/software-engineering-for-agents/research/voice-models.md`. Read `AGENTS.md` first, especially drafting rule 7 (claims trace to research). A fact counts as verified only if a page you actually loaded states it. Search snippets and memory do not count. Prefer the publisher, author, or original outlet (primary). Wikipedia, Open Library, WorldCat, and the Library of Congress count as secondary.
>
> For each item below, load the source and record the outcome in the memo's matching bibliography line or table row: verified primary, verified secondary, contradicted, or still unverified with the reason. If a fact is contradicted, correct the memo text. Do not change the style readings or candidate moves. Commit each resolved author as its own commit with the reason in the message (AGENTS.md commit policy), then push.
>
> Open items:
>
> 1. **Ellen Ullman, *Close to the Machine*.** Confirm the original publication (expected City Lights, 1997). Macmillan's Picador page (https://us.macmillan.com/books/9781250002488/closetothemachine/) was blocked. Try City Lights, Open Library, WorldCat, or LoC.
> 2. **Ellen Ullman, *Life in Code*.** Confirm the original publication (expected MCD / Farrar, Straus and Giroux, 2017). Macmillan (https://us.macmillan.com/books/9781250181695/lifeincode/) was blocked.
> 3. **Tracy Kidder, 1982 Pulitzer Prize, General Nonfiction, for *The Soul of a New Machine*.** The Hachette page confirms a Pulitzer but not the year or category. pulitzer.org (https://www.pulitzer.org/prize-winners-by-year/1982) was blocked.
> 4. **Douglas Hofstadter, *Gödel, Escher, Bach*.** Confirm the 1979 original publication and the 1980 Pulitzer Prize, General Nonfiction (https://www.pulitzer.org/prize-winners-by-year/1980, blocked). The Hachette page shows only the 1999 paperback date.
> 5. **John McWhorter, *The Power of Babel*.** Sources conflict: Open Library gives Times Books, 2001; Wikipedia gives Henry Holt, 2002. Find the original publisher and year from a copyright page, LoC record, or publisher page.
> 6. **John McWhorter, *Words on the Move*.** Henry Holt, 2016 is verified via Open Library. The September 6, 2016 on-sale date needs the Macmillan page (https://us.macmillan.com/books/9781627794732/wordsonthemove/), which was blocked.
> 7. **John McWhorter, original publishers of *Our Magnificent Bastard Tongue* (2008) and *Nine Nasty Words* (2021).** Penguin Random House pages confirm the dates but name Avery only for the paperbacks. Optional: only matters if the memo names the original imprint.
> 8. ***Lexicon Valley* current status.** The Substack about page says the show moved to Booksmart Studios. Check booksmartstudios.com for whether McWhorter currently hosts it, and update the memo's wording if so.
> 9. **Anthony Bourdain, Bloomsbury imprints.** *Kitchen Confidential* (2000) and *A Cook's Tour* (2001) are verified as Bloomsbury via Wikipedia and Open Library. Confirm the first-edition imprint (Bloomsbury USA vs. Bloomsbury Press) from bloomsbury.com or a catalog record. Optional unless an imprint is cited.
> 10. **Paul Ford, "What Is Code?", Bloomberg Businessweek, June 11, 2015.** https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/ was blocked. Confirm author, title, outlet, and date.
> 11. **Matt Levine, *Money Stuff*.** https://www.bloomberg.com/account/newsletters/money-stuff was blocked. Confirm it is Levine's newsletter at Bloomberg Opinion, from any Bloomberg page that loads.
> 12. **James Mickens, "The Night Watch."** Author, title, and November 2013 are verified from the USENIX PDF. Confirm it ran in *;login:* (the "logout" column), e.g. from https://www.usenix.org/publications/login-logout/november-2013-login-logout/night-watch.
>
> Also still open: no quotations from any author in the memo have been verified, and the memo uses none. Leave the do-not-use ledger as is unless you verify a specific quote from a primary source.
>
> Done means every item above is resolved or marked with why it still cannot be checked, and the memo's evidence-tier labels match.
