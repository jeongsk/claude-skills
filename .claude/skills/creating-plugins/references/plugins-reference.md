# Claude Code Plugins Reference

Complete technical reference for creating and configuring Claude Code plugins.

## Plugin Structure Reference

### Complete Plugin Directory Tree

```
plugin-name/
├── .claude-plugin/
│   ├── plugin.json                 # REQUIRED
│   └── marketplace.json            # Optional (for hosting marketplace)
├── commands/                       # Optional directory
│   ├── command-1.md
│   ├── command-2.md
│   └── README.md
├── agents/                         # Optional directory
│   ├── agent-1.md
│   ├── agent-2.md
│   └── README.md
├── skills/                         # Optional directory
│   ├── skill-1/
│   │   ├── SKILL.md                # REQUIRED in each skill
│   │   ├── references/
│   │   │   ├── doc-1.md
│   │   │   ├── doc-2.md
│   │   │   └── data.json
│   │   └── scripts/
│   │       └── helper.sh
│   ├── skill-2/
│   │   └── SKILL.md
│   └── README.md
├── hooks/                          # Optional directory
│   └── hooks.json                  # Event handler configuration
├── .mcp.json                       # Optional
├── scripts/                        # Optional
│   ├── init.sh
│   ├── validate.sh
│   └── cleanup.sh
├── README.md                       # Recommended documentation
├── LICENSE                         # Recommended
└── .gitignore                      # Recommended

```

### Component Locations (Critical)

| Component | Location | Required | Auto-discovered |
|-----------|----------|----------|-----------------|
| Plugin metadata | `.claude-plugin/plugin.json` | Yes | Yes |
| Slash commands | `commands/*.md` | No | Yes |
| Sub-agents | `agents/*.md` | No | Yes |
| Skills | `skills/*/SKILL.md` | No | Yes |
| Hooks | `hooks/hooks.json` | No | Yes |
| MCP servers | `.mcp.json` | No | Yes |

## Configuration Schemas

### plugin.json JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Claude Code Plugin Manifest",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Unique identifier (lowercase, hyphens allowed)",
      "pattern": "^[a-z0-9-]+$",
      "minLength": 1,
      "maxLength": 50
    },
    "version": {
      "type": "string",
      "description": "Semantic version (e.g., 1.0.0)",
      "pattern": "^\\d+\\.\\d+\\.\\d+(-.*)?$"
    },
    "description": {
      "type": "string",
      "description": "Brief description of plugin",
      "maxLength": 200
    },
    "author": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Author name (required)"
        },
        "email": {
          "type": "string",
          "format": "email"
        },
        "url": {
          "type": "string",
          "format": "uri"
        }
      },
      "required": ["name"]
    },
    "homepage": {
      "type": "string",
      "format": "uri",
      "description": "Plugin documentation homepage"
    },
    "repository": {
      "type": "string",
      "format": "uri",
      "description": "Source code repository URL"
    },
    "license": {
      "type": "string",
      "description": "SPDX license identifier",
      "enum": ["MIT", "Apache-2.0", "GPL-3.0", "ISC", "BSD-3-Clause", "Unlicense"]
    },
    "keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Searchable tags",
      "maxItems": 10
    }
  },
  "required": ["name"]
}
```

### marketplace.json JSON Schema

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Marketplace identifier"
    },
    "version": {
      "type": "string",
      "description": "Marketplace version (semantic versioning)"
    },
    "description": {
      "type": "string",
      "description": "Marketplace description"
    },
    "owner": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Owner or organization name"
        },
        "email": {
          "type": "string",
          "format": "email"
        },
        "url": {
          "type": "string",
          "format": "uri"
        }
      },
      "required": ["name"]
    },
    "plugins": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Plugin name identifier"
          },
          "source": {
            "type": "string",
            "description": "Local path (./dir), GitHub (org/repo), or URL"
          },
          "description": {
            "type": "string",
            "description": "Plugin description"
          },
          "version": {
            "type": "string",
            "description": "Plugin version"
          },
          "category": {
            "type": "string",
            "enum": ["development", "productivity", "security", "learning", "integration", "other"]
          },
          "author": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "email": {"type": "string"},
              "url": {"type": "string"}
            }
          },
          "keywords": {
            "type": "array",
            "items": {"type": "string"}
          }
        },
        "required": ["name", "source"]
      }
    }
  },
  "required": ["name", "plugins"]
}
```

### Command File YAML Frontmatter Schema

```yaml
---
# Required
description: "String (shown in /help)"

# Optional
arguments:
  - name: "argument-name"
    description: "What this argument does"
    required: false
    options:
      - "option1"
      - "option2"

argument-hint: "[argument] [flags]"
allowed-tools:
  - "Bash(git status:*)"
  - "Bash(npm:*)"
  - "Write"
  - "Edit"

model: "claude-3-5-haiku-20241022"
disable-model-invocation: false
---
```

### Agent File YAML Frontmatter Schema

```yaml
---
# Required
name: "Display Name"
description: "When to use this agent"

# Optional
capabilities:
  - "capability1"
  - "capability2"

skills:
  - "skill-name-1"
  - "skill-name-2"
---
```

### Skill YAML Frontmatter Schema

```yaml
---
# Required
name: "Skill Display Name"
description: "What this skill teaches Claude"

# Optional
license: "Apache-2.0"
allowed-tools: "Read, Write, Bash"
metadata:
  author: "organization-name"
  version: "1.0"
  tags:
    - "tag1"
    - "tag2"
---
```

### hooks.json Schema

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "timeout": 60,
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/init.sh",
            "timeout": 30
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "timeout": 30,
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/cleanup.sh"
          }
        ]
      }
    ]
  }
}
```

### .mcp.json Schema

```json
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["-m", "server_module"],
      "env": {
        "API_KEY": "${API_KEY_ENV_VAR}",
        "BASE_URL": "https://api.example.com"
      },
      "disabled": false,
      "alwaysAllow": ["some_resource"]
    }
  }
}
```

## Hook Event Types

| Event | Trigger | Use Case |
|-------|---------|----------|
| `SessionStart` | New/resumed session | Load context, initialize environment |
| `PreToolUse` | Before any tool call | Validate, filter, modify inputs |
| `PostToolUse` | After tool completion | Format, validate outputs |
| `Stop` | Session ending | Cleanup, logging, teardown |

## Hook Matchers

Tool matching patterns:

```
"*"              # All tools
"Bash"           # Exact tool match
"Write|Edit"     # Multiple tools (pipe separator)
"Bash(git:*)"    # Tool with subcommand pattern
"Bash(npm:*)"    # Another subcommand pattern
```

## Hook Environment Variables

- `CLAUDE_PROJECT_DIR` - Current project root
- `CLAUDE_CODE_REMOTE` - true in web environment
- `CLAUDE_ENV_FILE` - Temp file for environment exports
- `CLAUDE_PLUGIN_ROOT` - Plugin installation directory

## Hook Exit Codes

- `0` - Success (stdout shown to user)
- `2` - Error (stderr fed to Claude)
- Other - Hook failure handled gracefully

## Plugin Size and Performance Guidelines

### Recommended Limits

| Component | Recommendation |
|-----------|-----------------|
| plugin.json | < 2 KB |
| Command file | < 5 KB |
| Agent file | < 10 KB |
| SKILL.md | 2-5 KB (body only) |
| hooks.json | < 5 KB |
| Hook script | < 100 KB |
| Total plugin | < 10 MB |

### Context Usage Estimates

| Component | Token Cost |
|-----------|------------|
| Plugin metadata (frontmatter) | ~100 tokens |
| Command in context | ~200-300 tokens |
| Agent definition | ~300-500 tokens |
| Skill frontmatter | ~100 tokens |
| Skill body | ~200-500 tokens |
| Referenced file | ~50-1000 tokens (file dependent) |

## Versioning Strategy

### Semantic Versioning

Use `MAJOR.MINOR.PATCH`:

- **MAJOR**: Breaking changes to plugin structure
- **MINOR**: New features (commands, agents, skills)
- **PATCH**: Bug fixes, documentation

## Configuration Inheritance

### Settings.json Plugin Configuration

```json
{
  "plugins": {
    "my-plugin@marketplace": {
      "enabled": true
    }
  },
  "marketplaces": {
    "marketplace": {
      "source": "owner/repo"
    }
  }
}
```

### Precedence Order

1. Project `.claude/settings.json` (highest priority)
2. Project `.claude/settings.local.json`
3. User `~/.claude/settings.json`
4. User `~/.claude/settings.local.json`
5. Plugin defaults (lowest priority)

## Common Issues and Solutions

### Issue: Plugin Not Appearing in `/plugin` Menu

**Solutions**:
1. Verify `.claude-plugin/plugin.json` is valid JSON
2. Check marketplace `source` path is correct
3. Run `/plugin validate` for detailed errors
4. Ensure `plugin.json` is in `.claude-plugin/` directory

### Issue: Commands Not Recognized

**Solutions**:
1. Command files must be in `commands/` directory (not elsewhere)
2. Verify YAML frontmatter is valid
3. Check command filenames are lowercase with hyphens
4. Restart Claude Code after changes
5. Run `/plugin validate` to check syntax

### Issue: Skills Not Loading

**Solutions**:
1. Verify `skills/skill-name/SKILL.md` file exists
2. Check YAML frontmatter has `name` and `description`
3. Ensure skill directory is named in kebab-case
4. Verify skill is auto-triggered or explicitly referenced
5. Check `/context` to see loaded skills

### Issue: Hooks Not Executing

**Solutions**:
1. Verify `hooks.json` is in plugin root (not `.claude-plugin/`)
2. Check JSON is valid with proper escaping
3. Verify script has execute permissions: `chmod +x script.sh`
4. Check matcher patterns exactly match tool names
5. Verify 60-second timeout isn't being exceeded
6. Check script exit codes (0 for success, 2 for errors)

### Issue: MCP Server Not Connecting

**Solutions**:
1. Verify `.mcp.json` is valid JSON
2. Check command and args are correct
3. Verify environment variables are set
4. Test MCP server runs independently
5. Check server startup timeout
6. Verify server outputs valid MCP protocol

## Resources and Examples

### Official Examples

- GitHub: https://github.com/anthropics/claude-code/tree/main/plugins
- Official Marketplace: https://github.com/anthropics/claude-plugins-official
- Plugin Template: https://github.com/ivan-magda/claude-code-plugin-template

### Example Plugins

- **agent-sdk-dev** - SDK development toolkit
- **code-review** - Automated code review with agents
- **feature-dev** - Feature development workflow
- **plugin-dev** - Plugin creation toolkit
- **pr-review-toolkit** - PR review specialization
- **commit-commands** - Git workflow automation

---

**Last Updated**: 2026-01-04
**Claude Code Version**: Latest
**Schema Version**: 1.0.0
