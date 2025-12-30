# Plugin MCP Servers Reference

## Location
`.mcp.json` at plugin root or inline in plugin.json

## Configuration Format

```json
{
  "mcpServers": {
    "server-name": {
      "command": "path/to/server",
      "args": ["--flag", "value"],
      "env": {
        "VAR_NAME": "value"
      },
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

## Example: Database Server

```json
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    }
  }
}
```

## Example: NPM Package Server

```json
{
  "mcpServers": {
    "api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

## Example: Python Server

```json
{
  "mcpServers": {
    "python-tools": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}",
      "env": {
        "PYTHONPATH": "${CLAUDE_PLUGIN_ROOT}/src"
      }
    }
  }
}
```

## Integration Behavior
- Servers auto-start when plugin is activated
- Servers appear as standard MCP tools in Claude's toolkit
- Servers integrate seamlessly with existing Claude tools
- Plugin servers configured independently from user MCP servers
