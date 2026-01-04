# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Claude Code plugin marketplace repository containing multiple plugins that extend Claude Code functionality. The marketplace is registered under `jeongsk-claude-skills`.

## Project Structure

```
claude-skills/
├── .claude-plugin/marketplace.json  # Marketplace definition
├── .claude/                          # Project-level Claude Code config
│   ├── agents/                       # Project agents (plugin-developer)
│   ├── skills/                       # Project skills (plugin-creator)
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

- Claude Code Skills Overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
- Get started with Agent Skills in the API: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart.md
- Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md
- How to create plugins for Claude Code: https://code.claude.com/docs/en/plugins.md
- Prompt engineering guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview.md
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices.md