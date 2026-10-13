# Playwright MCP in this framework

MCP (Model Context Protocol) lets an AI assistant (Claude Desktop, Claude Code, VS Code)
drive a real browser through the Playwright MCP server. Config: `.mcp.json` in the repo root.

## Where MCP fits (say this in the interview)
MCP is a **design-time helper**, not part of the test run. The tests themselves stay
deterministic Python + Playwright. The AI helps us author and maintain them faster:

1. **Explore** - "Open https://www.saucedemo.com and log in as standard_user."
2. **Find locators** - "Give me stable selectors for the login form." -> we paste them into `locators/`.
3. **Draft scenarios** - "Draft a pytest test for adding an item to the cart." -> a human reviews it, then it goes into `tests/`.
4. **Debug failures** - "This step failed in CI, open the page and tell me what changed."

## Guardrails
- AI output is always reviewed by a human before it is committed.
- AI never edits tests silently in CI; CI only runs reviewed, committed code.

## Setup
- Claude Code: run `claude` in the repo root; it picks up `.mcp.json` automatically.
- Claude Desktop / others: copy the `mcpServers` block into the client's MCP config.
- Needs Node.js installed (`npx`).
