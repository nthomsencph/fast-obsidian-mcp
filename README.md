# obsidian-mcp

A minimal MCP server that gives Claude Desktop and Cowork access to your local Obsidian vault via the official [Obsidian CLI](https://obsidian.md/help/cli).

## Why

Claude Desktop and Cowork run in a sandbox and cannot call the Obsidian CLI directly. This server bridges that gap over the MCP protocol.

## Design

One tool: `obsidian_run(command)`. It executes `obsidian <command>` as a subprocess and returns the output. All CLI knowledge lives in a [SKILL.md](SKILL.md) that the agent loads for syntax reference — not in tool schemas. This keeps the agent's context footprint minimal.

## Setup

Requires Python 3.11+, the Obsidian desktop app running, and the `obsidian` CLI in your PATH.

```bash
uv sync
```

Install as a tool:

```bash
uv tool install .
```

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "obsidian-mcp",
      "env": {
        "PATH": "/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
      }
    }
  }
}
```

The `PATH` env is required because Claude Desktop launches MCP servers in a minimal sandbox environment that doesn't inherit your shell's PATH. Without it, the server can't find the `obsidian` CLI binary. Adjust the paths if your `obsidian` binary is installed elsewhere (`which obsidian` to check).

## Usage examples

The agent calls `obsidian_run` with CLI command strings:

```
read path="Notes/Todo.md"
append path="Notes/Todo.md" "Log" content="New entry"
search query="meeting notes" json
daily:append content="- completed review"
tasks json
```

See [SKILL.md](SKILL.md) for the full command reference.

## Project structure

```
obsidian_mcp/
  server.py    # FastMCP server, one tool
pyproject.toml
SKILL.md       # CLI syntax reference for the agent
```
