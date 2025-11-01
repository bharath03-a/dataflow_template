"""
MCP server for Dataflow Template Toolkit.
Enables AI coding agents (Cursor, Copilot, Claude) to create standard Dataflow projects automatically.
"""

from mcp.server.fastmcp import FastMCP
import shutil
from pathlib import Path

mcp = FastMCP("Dataflow Template MCP")

@mcp.tool()
def create_dataflow_project(target_dir: str = "."):
    """
    Copies the standard Dataflow template into the given target directory.
    Usage:
        create_dataflow_project("/path/to/project")
    """
    template_dir = Path(__file__).parent.parent / "template_files"
    target_path = Path(target_dir).resolve()

    if not template_dir.exists():
        return f"Template directory not found at {template_dir}"

    shutil.copytree(template_dir, target_path, dirs_exist_ok=True)
    return f"Dataflow project created successfully at: {target_path}"

@mcp.tool()
def health_check():
    """Check if MCP server is running"""
    return "MCP server is alive"

if __name__ == "__main__":
    print("Starting Dataflow Template MCP server...")
    mcp.run()
