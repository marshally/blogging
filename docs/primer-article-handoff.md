# Accept a finalized primer article

The private [primer repository](https://github.com/marshally/vibe-engineering-primer) owns primer drafts, research, author edits, and its own style guide. Finalization and style harvesting happen there. Blogging owns the approved publication copy and its distribution under [the posting strategy](2026-posting-strategy.md).

When a primer handoff arrives, verify its receipt at `docs/primer-handoffs/YYYY-MM-DD-<slug>.json` against the identified primer source commit. It must identify the source path, baseline and harvest revisions (or an explicit no-harvest result), publication path, and SHA-256 for the article and every exported asset. The [source procedure](https://github.com/marshally/vibe-engineering-primer/blob/main/docs/article-handoff.md) defines the fields and authorship boundary.

Confirm the prose matches the approved source apart from documented mechanical corrections and publication-path rewrites. Check every image, thumbnail, and other local link from the final `posts/` path. Keep provenance and research in the primer; public article citations must resolve to their actual public sources. Include downscaled photo assets and PNG derivatives of SVGs where required by [the WordPress procedure](publishing-wordpress.md).

Accept the article, exported assets, and receipt as already finalized. Skip draft-baseline discovery and style harvesting in blogging, and leave `docs/writing-style.md` unchanged. If a receipt is absent or inconsistent, recover the handoff from the primer source before accepting the copy. Stage only the approved publication files and receipt, commit, and open the requested review. A later correction begins in the primer and arrives as an explicit update with a new source revision. Keep prior receipts in Git history.

Acceptance into Git is separate from live WordPress publication or distribution. Follow the scope of Marshall's current approval and the normal publishing instructions for those actions. General blog posts continue the existing finalize-post workflow.

## Migration cutover

The cleanup branch is based directly on blogging `main` at `654ac3bd42029d1129f5a47e9ff907699ff94bba`. It depends on the verified private destination, not on merging the quantitative-research branch. The newer source-branch material is already imported there; merging that old research branch later would restore retired working copies.

Keep cleanup unmerged for review. Before cutover, preserve any new local-only state in the old nested `sites/vibe-engineering-primer/` checkout, then relocate that recovery checkout outside blogging. Remove its old local `codegraph.json` include entry and regenerate the blogging index. The migration retained the original checkout and complete recovery bundles; their exact local paths and recovery procedure are recorded in the destination's `docs/migration/README.md`. Reverting the focused source-cleanup commit restores the old tracked files, but reconcile newer primer work before resuming authoring there.
