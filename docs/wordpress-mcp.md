# WordPress.com MCP

This repository uses the WordPress.com remote MCP server:

```text
https://public-api.wordpress.com/wpcom/v2/mcp/v1
```

WordPress.com MCP access must be enabled for the account or individual site. Availability and tool permissions are controlled in WordPress.com under **AI and MCP**. See the [WordPress.com MCP setup guide](https://wordpress.com/support/mcp/).

## Claude Code

Claude Code discovers the shared project configuration in the repository-root `.mcp.json`. The tracked configuration contains only the server name, transport, and URL.

On first use, approve the project-scoped server in Claude Code, run `/mcp`, and complete the WordPress.com browser authorization flow. OAuth tokens are stored locally by Claude Code and never belong in the repository.

## Codex

Codex MCP registration is user-level rather than repository-level. Each user registers the server locally:

```bash
codex mcp add wpcom-mcp --url https://public-api.wordpress.com/wpcom/v2/mcp/v1
```

Codex should start browser authorization automatically. If manual authentication is needed, run:

```bash
codex mcp login wpcom-mcp
```

See the [WordPress.com MCP client documentation](https://developer.wordpress.com/docs/mcp/) for current client instructions.

## Credential boundary

Never commit access tokens, refresh tokens, authorization headers, client secrets, or local client state. The repository stores only the credential-free endpoint configuration and setup documentation. Every user authorizes their own WordPress.com account through OAuth.
