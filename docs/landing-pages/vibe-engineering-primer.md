# The Vibe Engineer’s Primer landing page

This is the operating guide for the book's public landing page and signup list. It lives under `docs/landing-pages/` so it remains easy to find as the book moves through drafting and publication. The [book brief](../../drafting/software-engineering-for-agents/README.md), [marketing plan](../../drafting/software-engineering-for-agents/marketing-plan.md), and [decision log](../../drafting/software-engineering-for-agents/DECISIONS.md) hold the editorial context.

## Where everything lives

| Item | Location |
|---|---|
| Public page | [vibeengineeringprimer.com](https://vibeengineeringprimer.com) |
| Native hosting address | [vibe-engineering-primer.bronzeflea7.chatgpt.site](https://vibe-engineering-primer.bronzeflea7.chatgpt.site) |
| Hosting | OpenAI Sites, running on Cloudflare |
| Domain and DNS | Hover |
| Site project ID | `appgprj_6ace35e513fc8191bc62e3d86c5b6650` |
| Custom-domain ID | `appgdom_6ace396043048191a6a508de351960f3` |
| Production signup list | D1 binding `DB`, table `subscribers` |
| Local application source | `sites/vibe-engineering-primer/`, a separate Git checkout ignored by this blogging repo |

## Retrieve the signup list

The public page accepts signups. The owner retrieves the records through authenticated Sites tools or its database viewer. There is no public subscriber-list endpoint or admin/download page on the landing site.

### Ask for a CSV

Use this request in a Codex conversation with the Sites connection available:

> Export the current signup list for The Vibe Engineer’s Primer at vibeengineeringprimer.com as a CSV. Include email, signup time in UTC, consent version, and source. Save it in my Downloads folder and report the number of exported subscribers. Omit internal IDs and management-token hashes. Tell me if the export is incomplete.

The agent reads the production records through Sites and creates the CSV locally. This does not require a website deployment or a Cloudflare login. A local development database contains only local data and is not the production list.

### Inspect the records yourself

Open the landing page's Site management entry in the account that owns it. In its Settings, open the database viewer, select binding `DB`, and open table `subscribers`. The Sites connector documents this viewer as the manual route for inspecting tables. Use the CSV request above when you need a file for another service.

### Procedure for the exporting agent

1. Read the Site identity from the table above or the source checkout's `.openai/hosting.json`. Call `sites_read_database_overview` with that exact `project_id` and use the returned binding and table names.
2. Call `sites_read_database_table_rows` for binding `DB` and table `subscribers`, beginning at offset `0`, with a limit of `25` or less.
3. Follow only the returned `model_projection.next_offset` until it is `null`. Check `has_more`, omission counts, and truncation flags. The tool accepts offsets only through `10000`; if a limit, omission, or truncation prevents complete retrieval, report a partial export and use the database viewer for further inspection.
4. Write a properly escaped CSV with the fields below. Convert `created_at` from Unix seconds to an ISO 8601 UTC timestamp, using the header `signed_up_at_utc`. Handle an empty list with headers and a zero-row result. Report the file path, row count, and retrieval time. Pages are read independently, so changes during retrieval can affect export consistency.

| Stored field | Export meaning |
|---|---|
| `email` | Normalized email address |
| `created_at` | Signup time, stored as Unix seconds |
| `consent_version` | Version of the consent notice shown at signup |
| `source` | Recorded signup source |

Keep subscriber exports outside this Git repository and the public Site assets. Omit `id` and `manage_token_hash` from mailing-list imports. The separate `signup_limits` table holds temporary abuse-control records, not subscribers.

## What signup currently does

The form stores unique, normalized addresses and the consent record in the private production database. It validates submissions and applies a honeypot and request limits. A new signup receives an HttpOnly management cookie so the subscriber can remove that signup from the privacy page in the same browser. Duplicate submissions do not grant access to an existing subscription.

This is a separate book-interest list covering book progress, related lessons, and launch news. It does not subscribe people to unrelated Yount Labs posts. There is no welcome email, confirmation email, or campaign sender yet, so addresses are not verified by email. Before sending the first mailing, connect an email provider, retain the consent information, and configure unsubscribe handling. A CSV is a copy of the list at retrieval time and will not track later removals automatically.

## Maintain the page and domain

Work on the application in its separate checkout, `sites/vibe-engineering-primer/`. Its `OPERATIONS.md` contains development notes, `CONTENT-SOURCES.md` explains the page copy, and `.openai/hosting.json` records hosting configuration. Commits in the blogging repo do not publish Site changes. For application updates, use the Sites skill with the existing project ID, validate the change, and publish the exact committed source through the supported workflow. Do not create a replacement Site.

Hover's apex (`@`) A records point to `162.159.143.30` and `172.66.3.26`. Keep the ownership-verification TXT records associated with this Site. If the domain fails while the native hosting address works, inspect Hover DNS and refresh the existing custom-domain status through Sites. Preserve the existing Site and domain IDs when investigating.

### Alternate domains

Marshall selected `vibeprimer.com` and `vibeengineersprimer.com` as redirects to `https://vibeengineeringprimer.com`. Both apex hostnames are attached to the same Site. Their Hover DNS uses the same two apex A records as the primary domain, plus their own ownership-verification TXT records.

| Alias | Sites custom-domain ID |
|---|---|
| `vibeprimer.com` | `appgdom_6ace4201e3b08191bf315a31423c0324` |
| `vibeengineersprimer.com` | `appgdom_6ace4203371081918869c5106470eb7f` |

The source checkout's `proxy.ts` redirects these exact hostnames with HTTP 308, retaining the path and query parameters. For example, `https://vibeprimer.com/privacy?utm_source=card` redirects to `https://vibeengineeringprimer.com/privacy?utm_source=card`. The canonical and native hosting addresses continue to serve the page. These entries configure the two requested apex hostnames, not wildcard or `www` aliases.

Forwarding is handled by the Site so it can work over HTTPS. [Hover's built-in forwarding](https://support.hover.com/support/solutions/articles/201000064747-managing-domain-forwarding) supports HTTP only. In Hover, maintain these aliases under DNS. The redirect behavior is maintained in the Site source.

## Verification record

On 2026-10-13, TypeScript and the production build passed. Desktop and 390px mobile layouts were inspected. Local checks covered persistence, validation failures, normalized duplicates, and cookie-authorized removal. A synthetic signup on the published native domain was verified in the live database and removed. The database was empty afterward. No mailing was sent. Initial published source commit: `66ff776d4695139efb9298a0bd08368eb692bc21`.

At 2026-10-13 14:32 UTC, Sites reported the custom domain, provider, and SSL certificate as `active`. An HTTPS request to `https://vibeengineeringprimer.com` returned HTTP 200 with the landing page's expected title. This supersedes the earlier pending DNS/certificate status. The production `DB` binding and `subscribers` table were also confirmed through the database overview tool. No subscriber export was performed while writing this guide.

On 2026-10-13, Site version 2 published the alias redirects from source commit `637e445b9101b4833949c98fd5f3bf663c7ae1c0`. TypeScript, the production build, and local HTTP checks passed for both alias roots, path/query preservation, and canonical/native hosts without redirect loops. Both sets of DNS changes were verified in Hover, and all four verification TXT records resolved publicly. At 14:42 UTC, public apex lookups still returned Hover's previous parking address and certificate validation was pending. A live redirect check remains necessary after propagation.
