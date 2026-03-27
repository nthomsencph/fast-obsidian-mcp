# Obsidian CLI — MCP Tool Reference

You have two tools:
- `obsidian_run(command)` — run any Obsidian CLI command. Pass the full command string after `obsidian`.
- `obsidian_edit(path, old, new)` — find and replace text in a note. Replaces the first occurrence of `old` with `new`. Atomic — no race conditions.

## Syntax rules

- **File targeting:** Always use `path="Folder/Note.md"` (exact). Never use `file=` (fuzzy, unreliable).
- **Named params:** `key=value` or `key="value with spaces"`.
- **Newlines in content:** Use `\n` for newline, `\t` for tab in content values.
- **Format output:** Use `format=json` (not positional `json`). Available on: `search`, `search:context`, `tasks`, `files`, `tags`, `backlinks`, `outline`, `properties`, `bookmarks`.

## Editing content

Use `obsidian_edit(path, old, new)` for surgical find-and-replace. For full rewrites, use `create ... overwrite` via `obsidian_run`.

## Context warning

`files`, `tasks`, and `tags` can return large output on big vaults. Prefer scoped queries (`search`, `outline`, `backlinks`) over full listings. Only retrieve all files/tasks/tags when you specifically need the full set.

## Common commands

| Action | Command |
|---|---|
| Read note | `read path="Folder/Note.md"` |
| Create note | `create path="Folder/Note.md" content="text"` |
| Overwrite note | `create path="Folder/Note.md" content="text" overwrite` |
| Append to note | `append path="Folder/Note.md" content="text"` |
| Prepend to note | `prepend path="Folder/Note.md" content="text"` |
| Delete note | `delete path="Folder/Note.md"` |
| Move note | `move path="Folder/Note.md" to="Other/Note.md"` |
| Rename note | `rename path="Folder/Note.md" name="NewName"` |
| Search | `search query="term" format=json` |
| Search with context | `search:context query="term" format=json` |
| List files | `files format=json` |
| List files in folder | `files folder="Folder" format=json` |
| Outline | `outline path="Folder/Note.md" format=json` |
| Backlinks | `backlinks path="Folder/Note.md" format=json` |
| Tags | `tags format=json` |
| Tasks | `tasks format=json` |
| Task toggle | `task path="Note.md" line=5 toggle` |
| Daily read | `daily:read` |
| Daily append | `daily:append content="text"` |
| Daily prepend | `daily:prepend content="text"` |
| Set property | `property:set path="Note.md" name="key" value="val"` |
| Read property | `property:read path="Note.md" name="key"` |
| Remove property | `property:remove path="Note.md" name="key"` |
| Word count | `wordcount path="Note.md"` |
