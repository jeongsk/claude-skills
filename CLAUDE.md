# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Claude Code plugin marketplace repository containing multiple plugins that extend Claude Code functionality. The marketplace is registered under `jeongsk-claude-skills`.

## Project Structure

```
claude-skills/
├── .claude-plugin/marketplace.json  # Marketplace definition
├── .claude/                          # Project-level Claude Code config
│   ├── skills/                       # Project skills (creating-plugins)
│   └── settings.json                 # Plugin settings
├── fsd-helper/                       # FSD architecture plugin
├── reactflow-helper/                 # React Flow plugin
└── git-workflow/                     # Git workflow automation plugin
```

## Plugin Architecture

Each plugin follows this structure:
```
plugin-name/
├── .claude-plugin/plugin.json  # Plugin manifest (required)
├── commands/                   # Slash commands (*.md files)
├── agents/                     # Sub-agents (*.md files)
└── skills/                     # Skills with SKILL.md and references/
```

### Key Files

- **plugin.json**: Plugin manifest with name, version, description, author, keywords
- **commands/*.md**: Slash commands with YAML frontmatter (`description`, `arguments`) and markdown body
- **agents/*.md**: Agent definitions with frontmatter (`name`, `description`, `capabilities`) and system prompt
- **skills/*/SKILL.md**: Skill definitions with auto-trigger descriptions and reference documents

## Marketplace Configuration

The marketplace is defined in `.claude-plugin/marketplace.json`:
```json
{
  "name": "jeongsk-claude-skills",
  "plugins": [
    {"name": "plugin-name", "source": "./plugin-directory"}
  ]
}
```

## Adding a New Plugin

1. Create plugin directory with `.claude-plugin/plugin.json`
2. Add commands/agents/skills as needed
3. Register in `.claude-plugin/marketplace.json`
4. Optionally enable in `.claude/settings.json`

## Included Plugins

| Plugin | Description | Commands |
|--------|-------------|----------|
| **fsd-helper** | Feature-Sliced Design support | `/fsd-init`, `/fsd-slice`, `/fsd-segment`, `/fsd-check`, `/fsd-docs` |
| **reactflow-helper** | React Flow development | `/rf-docs`, `/rf-node`, `/rf-edge`, `/rf-example`, `/rf-setup` |
| **git-workflow** | Git automation | `/commit`, `/commit-push` |

## Command File Format

```markdown
---
description: Brief description shown in help
arguments:
  - name: argName
    description: Argument description
    required: false
---
# Command Title

Instructions for Claude when executing this command.
```

## Agent File Format

```markdown
---
name: Agent Name
description: When to use this agent
capabilities: ["capability1", "capability2"]
---
# Agent Title

System prompt and behavior instructions.
```

## Testing Plugins Locally

```bash
# Add local marketplace
/plugin marketplace add ./path-to-repo

# Install plugin
/plugin install plugin-name@marketplace-name
```

## References

All plugin and skill development documentation is available in the `creating-plugins` skill:

```
.claude/skills/creating-plugins/references/
├── plugins-guide.md          # Complete plugin creation guide
├── plugins-reference.md      # Technical schemas and configurations
├── plugin-structure.md       # Directory layout and plugin.json schema
├── marketplace.md            # Plugin distribution
├── commands.md               # Slash command format
├── agents.md                 # Sub-agent definitions
├── hooks.md                  # Event handlers
├── mcp-servers.md            # External tool integration
├── skills-overview.md        # What skills are and how they work
├── skills-best-practices.md  # Writing effective skills
└── skills-schema.md          # SKILL.md format and validation
```

External documentation:
- [Claude Code Documentation](https://code.claude.com/docs)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)