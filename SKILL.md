# Obsidian CLI — MCP Tool Reference

You have one tool: `obsidian_run(command)`. Pass the CLI command string (everything after `obsidian`).

## Syntax rules

- **File targeting:** Always use `path="Folder/Note.md"` (exact). Never use `file=` (fuzzy, unreliable).
- **JSON output:** Append `json` as a positional arg: `tasks json`, `files json`, `tags json`.
- **Headings:** Positional quoted arg: `read path="Note.md" "Section"`. Nested: `"Parent::Child"`.
- **Named params:** `key=value` or `key="value with spaces"`.

## Context warning

`files json`, `tasks json`, and `tags json` can return large output on big vaults. Prefer scoped queries (`search`, `outline`, `backlinks`) over full listings. Only retrieve all files/tasks/tags when you specifically need the full set.

## Common commands

| Action | Command |
|---|---|
| Read note | `read path="Folder/Note.md"` |
| Read section | `read path="Folder/Note.md" "Heading"` |
| Create note | `create path="Folder/Note.md" content="text"` |
| Append to note | `append path="Folder/Note.md" content="text"` |
| Append to section | `append path="Folder/Note.md" "Heading" content="text"` |
| Prepend to note | `prepend path="Folder/Note.md" content="text"` |
| Delete note | `delete path="Folder/Note.md"` |
| Move note | `move path="Folder/Note.md" to="Other/Note.md"` |
| Search | `search query="term" json` |
| Search with context | `search:context query="term" json` |
| List files | `files json` |
| Outline | `outline path="Folder/Note.md" json` |
| Backlinks | `backlinks path="Folder/Note.md" json` |
| Tags | `tags json` |
| Tasks | `tasks json` |
| Daily read | `daily:read` |
| Daily append | `daily:append content="text"` |
| Daily prepend | `daily:prepend content="text"` |
| Set property | `property:set path="Note.md" name="key" value="val"` |
| Read property | `property:read path="Note.md" name="key"` |
| Remove property | `property:remove path="Note.md" name="key"` |
