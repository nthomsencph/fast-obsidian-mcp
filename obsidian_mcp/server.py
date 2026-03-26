import asyncio
import shlex

from fastmcp import FastMCP

mcp = FastMCP("obsidian-mcp")


@mcp.tool
async def obsidian_run(command: str) -> str:
    """Run an Obsidian CLI command. Pass the full command string after 'obsidian', e.g. 'read path="Notes/Todo.md"' or 'daily:append content="hello"'."""
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


def main():
    mcp.run()


if __name__ == "__main__":
    main()
