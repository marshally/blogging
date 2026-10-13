# Book landing page

Marshall requested a public book landing page at [vibeengineeringprimer.com](https://vibeengineeringprimer.com) on 2026-10-13, with email collection for a mailing list. The implementation uses the working marketing label “The Vibe Engineer’s Primer” and presents the cover as a concept for a book in development. The selected full title in D19 remains unchanged.

The page is published through OpenAI Sites at [the native hosting address](https://vibe-engineering-primer.bronzeflea7.chatgpt.site). Hover holds the custom domain's DNS. The apex A records target `162.159.143.30` and `172.66.3.26`, with ownership-verification TXT records supplied by Sites. DNS propagation and certificate activation are external to the source deployment.

Domain status at 2026-10-13 14:08 UTC: the saved Hover records were verified after reloading its DNS page, and both verification TXT records resolved publicly. Public A-record lookup still returned Hover's old parking address, `216.40.34.41`. Sites reported provider status `active`, SSL status `pending_validation`, and overall status `pending`. Custom-domain ID: `appgdom_6ace396043048191a6a508de351960f3`. Refresh this existing domain's status after propagation, then verify HTTPS and signup on the custom hostname before reporting it live. The native hosting address is already operational.

Source lives in the separate Git checkout at `sites/vibe-engineering-primer/`, excluded from the parent blogging repository to preserve its independent publishing history. Site project ID: `appgprj_6ace35e513fc8191bc62e3d86c5b6650`. The initial published source commit is `66ff776d4695139efb9298a0bd08368eb692bc21`. Reuse this Site ID for future updates. The checkout's `OPERATIONS.md` describes maintenance and `CONTENT-SOURCES.md` records the copy's project sources.

Signups are stored privately in the Site's D1 `DB` binding, in `subscribers`. This is a separate book-interest list, an implementation assumption pending a delivery-service choice. There is no welcome email, confirmation email, or campaign sender yet. Connect an email provider before the first mailing, preserving consent and including an unsubscribe mechanism. Subscriber records can be read through the owner's Sites database tools. Keep exports private.

The form normalizes and deduplicates addresses, records consent, rejects invalid or cross-origin submissions, and limits automated submissions. A browser management cookie lets a new subscriber remove that signup from the privacy page. No public endpoint lists subscriber addresses.

Validation on 2026-10-13: TypeScript and the production build passed; desktop and 390px mobile layouts were inspected; local tests covered successful persistence, validation failures, duplicates, and authorized removal. A synthetic signup on the published native domain was verified in the live database and removed. The database was empty afterward. No mailing was sent.
