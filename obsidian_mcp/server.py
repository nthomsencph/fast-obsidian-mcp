import asyncio
import shlex

from fastmcp import FastMCP

mcp = FastMCP("obsidian-mcp")


@mcp.tool
async def obsidian_run(command: str) -> str:
    """Run an Obsidian CLI command. Pass the full command string after 'obsidian',
    e.g. 'read path="Notes/Todo.md"' or 'daily:append content="hello"'."""

    args = shlex.split(command)
    proc = await asyncio.create_subprocess_exec(
        "obsidian",
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()

    if proc.returncode != 0:
        raise RuntimeError(
            stderr.decode().strip()
            or f"obsidian exited with code {proc.returncode}"
        )

    return stdout.decode().strip()


@mcp.tool
async def obsidian_edit(path: str, old: str, new: str) -> str:
    """Find and replace text in a note. Replaces the first occurrence of `old` with `new`."""
    js = (
        "(async()=>{"
        f"const f=app.vault.getAbstractFileByPath({_js_str(path)});"
        "if(!f) throw new Error('File not found');"
        f"let found=false;"
        f"await app.vault.process(f, c=>{{"
        f"const idx=c.indexOf({_js_str(old)});"
        f"if(idx===-1) throw new Error('Text not found in note');"
        f"found=true;"
        f"return c.substring(0,idx)+{_js_str(new)}+c.substring(idx+{len(old)});"
        f"}});"
        "return 'done'"
        "})()"
    )
    return await obsidian_run(f'eval code="{_escape_cli(js)}"')


def _js_str(s: str) -> str:
    """Encode a Python string as a JS string literal."""
    escaped = s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
    return f"'{escaped}'"


def _escape_cli(s: str) -> str:
    """Escape a string for use inside a double-quoted CLI argument."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    mcp.run()


if __name__ == "__main__":
    main()
