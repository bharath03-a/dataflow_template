# Dataflow Template Toolkit

A toolkit for creating standardized Apache Beam pipelines for Google Cloud Dataflow across your organization.

## Overview

This project provides:

1. **Template** - A standardized Dataflow starter template
2. **CLI Tool** - Command-line interface for creating new projects
3. **MCP Server** - Model Context Protocol server for AI coding assistants

## Structure

```
dataflow_template/
│
├── pyproject.toml                # Main env for CLI/MCP tools
├── cli/
│   └── cli.py                    # CLI tool for creating projects
│
├── mcp_server/
│   └── mcp_server.py            # MCP server for AI assistants
│
├── template_files/               # The actual template
│   ├── dataflow_starter_kit/
│   │   ├── pipeline.py          # Main pipeline code
│   │   ├── transforms/
│   │   ├── options/
│   │   └── utils/
│   ├── Dockerfile
│   ├── pyproject.toml           # Template's pyproject.toml
│   └── README.md
│
└── README.md                     # This file
```

## Installation

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

## Usage

### Creating a New Dataflow Project

```bash
# Using the CLI tool
python -m cli.cli create /path/to/new/project

# Or after installation
dataflow-create create my-new-project
```

### Using MCP Server

The MCP server enables AI coding assistants (Cursor, Copilot, Claude) to create standardized projects.

**Note**: The MCP server is designed to be run by AI coding assistants, not for manual interaction. For manual usage, use the CLI instead.

See `mcp_server/README.md` for configuration details.

### Template Structure

Each project created from the template includes:

- **pipeline.py** - Main pipeline entry point
- **transforms/** - Reusable Beam transforms
- **options/** - Custom pipeline options
- **utils/** - Utility functions
- **Dockerfile** - Container configuration
- **pyproject.toml** - Project dependencies

## Quick Start with Created Project

After creating a project:

```bash
cd /path/to/new/project
uv sync
python -m dataflow_starter_kit.pipeline --input=1 --runner=DirectRunner
```

## Deployment

See `template_files/README.md` for detailed deployment instructions including:

- Local testing with DirectRunner
- Docker builds
- Google Cloud Dataflow deployment
- Flex template creation

## Contributing

To update the template:

1. Modify files in `template_files/`
2. Test with: `python -m cli.cli create /tmp/test-project`
3. Verify the created project works correctly

## License

[Your License Here]
