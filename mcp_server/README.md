# Dataflow Template MCP Server

MCP server for creating standardized Dataflow projects via AI coding assistants.

## Usage

This server is designed to be used by AI coding assistants (Cursor, Claude Desktop, etc.), not for manual interaction.

### For AI Assistants

Add this to your MCP client configuration:

```json
{
  "mcpServers": {
    "dataflow-template": {
      "command": "python",
      "args": ["-m", "mcp_server.mcp_server"],
      "cwd": "/path/to/dataflow_template"
    }
  }
}
```

### Available Tools

- **create_dataflow_project**: Creates a new Dataflow project from the template

### Manual Testing

For manual testing, use the CLI instead:

```bash
python -m cli.cli create my-project
# or
dataflow-create create my-project
```
