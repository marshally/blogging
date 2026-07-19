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

## Markdown → Gutenberg conversion

How the house draft conventions map to blocks (verified on a live post):

- **Footnotes** (`[^name]`): the native Gutenberg footnotes block. Each in-text reference becomes `<sup data-fn="<id>" class="fn"><a href="#<id>" id="<id>-link">N</a></sup>`, a `<!-- wp:footnotes /-->` block goes at the end of the content, and the notes themselves are a JSON-encoded array in the post's `meta.footnotes` field (`[{"id":"<id>","content":"<html>"}, …]`, in reference order). IDs need only be unique HTML ids; the editor renumbers automatically and renders hover previews.
- **YouTube thumbnail-link workaround** (an image linking to the video — a GitHub-markdown limitation): a real `core/embed` block, with the watch URL on its own line inside the wrapper div. Fold the separate caption line into the embed's `<figcaption>`.
- **Side-by-side image tables**: a `core/gallery` block with nested `core/image` blocks.
- **Italic caption paragraphs** under images: the image block's `<figcaption class="wp-element-caption">`. Drop the outer italics (figcaption styling covers it) and re-italicize the album/book titles that were reverse-italicized inside.
- After **every** `posts.create`/`posts.update`, check `_content_warnings` in the response — WordPress strips unsupported markup silently, and the warnings list is the only signal.
- For a targeted edit to an existing post, prefer `post-sections.list` then `post-sections.replace` (hash-guarded, one top-level block) over resending the full post content.
