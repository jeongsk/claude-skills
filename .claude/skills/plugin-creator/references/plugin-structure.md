# Plugin Structure Reference

## Directory Layout

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: Plugin metadata
├── commands/                 # Slash commands (optional)
│   └── command-name.md
├── agents/                   # Sub-agents (optional)
│   └── agent-name.md
├── skills/                   # Agent skills (optional)
│   └── skill-name/
│       └── SKILL.md
├── hooks/                    # Event handlers (optional)
│   └── hooks.json
├── .mcp.json                # MCP servers (optional)
└── scripts/                 # Utility scripts (optional)
```

## plugin.json Schema

### Required Fields

| Field  | Type   | Description                          |
| ------ | ------ | ------------------------------------ |
| `name` | string | Unique identifier (kebab-case)       |

### Metadata Fields

| Field         | Type   | Description              | Example                        |
| ------------- | ------ | ------------------------ | ------------------------------ |
| `version`     | string | Semantic version         | `"1.0.0"`                      |
| `description` | string | Brief plugin description | `"Deployment automation"`      |
| `author`      | object | Author info              | `{"name": "Dev", "email": ""}` |
| `homepage`    | string | Documentation URL        | `"https://docs.example.com"`   |
| `repository`  | string | Source code URL          | `"https://github.com/..."`     |
| `license`     | string | License identifier       | `"MIT"`                        |
| `keywords`    | array  | Search tags              | `["deploy", "ci-cd"]`          |

### Component Path Fields

| Field        | Type           | Description                   |
| ------------ | -------------- | ----------------------------- |
| `commands`   | string / array | Additional command files/dirs |
| `agents`     | string / array | Additional agent files        |
| `hooks`      | string / object| Hook config path or inline    |
| `mcpServers` | string / object| MCP config path or inline     |

### Example plugin.json

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "My awesome plugin",
  "author": {
    "name": "Developer",
    "email": "dev@example.com"
  },
  "keywords": ["utility", "automation"]
}
```

## Environment Variables

`${CLAUDE_PLUGIN_ROOT}` - Absolute path to plugin directory. Use in hooks and MCP configs.
