# Publishing to WordPress (yountlabs.com)

Mechanics for getting a post onto yountlabs.com through the WordPress.com MCP server. Load this before any WordPress publishing task. MCP setup and authentication live in `docs/wordpress-mcp.md`; the publish target and site constraints are in `AGENTS.md` under "Publishing targets".

## Posts

- Create with `posts.create` as a draft (`status: "draft"`), passing `wpcom_site: "yountlabs.com"` explicitly.
- After every create or update, share both links: edit `https://yountlabs.com/wp-admin/post.php?post=<id>&action=edit` and preview `https://yountlabs.com/?p=<id>&preview=true`.

## Media upload

`media.create` accepts only base64 file content inlined in the tool call — it cannot fetch from a URL. That is workable for small files (tens of KB) and infeasible for real image sets; never attempt to inline megabyte-scale files as base64.

The workflow that works for an image-bearing post:

1. Hand Marshall the exact file list (absolute paths) and the upload page `https://yountlabs.com/wp-admin/media-new.php`, and ask him to upload.
2. When he confirms, run `media.list` (newest first, with `include_fields` to keep the response small) and map filenames to attachment IDs and `source_url` values.
3. Rewrite the post's image blocks to those `source_url` values, adding `{"id":<N>}` to the block JSON and `class="wp-image-<N>"` to the `<img>` so the block editor treats them as library images.
4. Verify every rewritten URL with `curl -sI` (expect 200) before reporting done.

Notes:

- Media serves from `yountlabs.wordpress.com/wp-content/uploads/...`, not `yountlabs.com` — use `source_url` exactly as returned.
- Bulk manual uploads usually include extras and duplicates. Reconcile the library against the post's actual image list and report what is unused — never delete media on your own.
- Hotlinking `raw.githubusercontent.com` URLs from this public repo works and is fine for a draft under review; verify each URL resolves (200, correct content type) before relying on it.
