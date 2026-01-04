# How to Create Claude Code Plugins

Claude Code plugins are extensions that enhance Claude Code with custom slash commands, specialized agents, hooks, skills, and MCP servers. Plugins can be shared across projects and teams, providing consistent tooling and workflows.

## Overview

Plugins allow you to package and distribute custom functionality across your organization or team. A plugin is a collection of one or more components that extend Claude Code capabilities.

### What You Can Include in a Plugin

- **Slash Commands** - User-triggered shortcuts (e.g., `/feature-dev`, `/commit`)
- **Agents** - Specialized sub-agents for complex workflows
- **Skills** - Context-aware capabilities that Claude automatically applies
- **Hooks** - Event handlers that automate actions at specific moments
- **MCP Servers** - External tool and data source integrations

## Plugin Structure

Every plugin follows a standardized directory structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: Plugin metadata
├── commands/                 # Optional: Slash commands
│   ├── command-1.md
│   ├── command-2.md
│   └── ...
├── agents/                   # Optional: Sub-agents
│   ├── agent-1.md
│   ├── agent-2.md
│   └── ...
├── skills/                   # Optional: Agent Skills
│   ├── skill-1/
│   │   └── SKILL.md
│   ├── skill-2/
│   │   └── SKILL.md
│   └── ...
├── hooks/                    # Optional: Event handlers
│   └── hooks.json
├── .mcp.json                 # Optional: MCP server configuration
└── README.md                 # Documentation
```

### Important Directory Rules

- **Only `plugin.json` goes in `.claude-plugin/`** directory
- **All other components** (commands/, agents/, skills/, hooks/) must be at the plugin root level
- Components cannot reference files outside the plugin directory
- Paths using `../` will break after installation

## Creating the plugin.json Manifest

The `plugin.json` file is required and must be located at `.claude-plugin/plugin.json`.

### plugin.json Schema

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description of what your plugin does",
  "author": {
    "name": "Your Name",
    "email": "your-email@example.com",
    "url": "https://github.com/your-username"
  },
  "homepage": "https://github.com/your-org/my-plugin",
  "repository": "https://github.com/your-org/my-plugin",
  "license": "MIT",
  "keywords": [
    "keyword1",
    "keyword2",
    "keyword3"
  ]
}
```

### Field Descriptions

- **name** (required): Unique identifier for your plugin (lowercase, hyphens allowed)
- **version**: Semantic version (e.g., "1.0.0", "0.1.0")
- **description**: One-line summary of plugin functionality
- **author**: Object with `name` (required), `email`, and `url` (optional)
- **homepage**: URL to plugin documentation or repository
- **repository**: GitHub repository URL
- **license**: License type (MIT, Apache-2.0, etc.)
- **keywords**: Array of searchable tags

## Creating Slash Commands

Slash commands are user-triggered actions accessible via `/command-name`.

### Command File Structure

Commands are markdown files stored in the `commands/` directory with YAML frontmatter:

```markdown
---
description: Brief description shown in /help
arguments:
  - name: argument-name
    description: What this argument does
    required: false
    options:
      - option1
      - option2
allowed-tools:
  - Bash(git status:*)
  - Bash(npm:*)
argument-hint: "[argument] [flags]"
disable-model-invocation: false
---
# Command Title

Instructions for Claude when executing this command.

Include examples, templates, or expected outputs here.
```

### Frontmatter Fields

- **description**: Shown in `/help` - be concise
- **arguments**: Array of argument definitions
  - `name`: Argument identifier
  - `description`: What the argument does
  - `required`: Boolean (default: false)
  - `options`: Suggested values or choices
- **allowed-tools**: Tools this command can access
- **argument-hint**: Display hint like "[filename]" or "[message]"
- **disable-model-invocation**: Hide command from model context (default: false)

### Example Command

File: `commands/create-feature.md`

```markdown
---
description: Create a new feature following Feature-Sliced Design
arguments:
  - name: feature-name
    description: Name of the feature to create
    required: true
  - name: slice
    description: FSD slice (layer/segment)
    required: false
    options:
      - ui
      - api
      - model
argument-hint: "[feature-name] [slice]"
---
# Create Feature

Create a new feature directory structure following Feature-Sliced Design architecture.

## Steps

1. Validate feature name
2. Create directory structure
3. Initialize module files
4. Generate index exports

Use the provided arguments to customize the feature structure.
```

## Creating Agents (Sub-agents)

Agents are specialized AI assistants for complex, multi-step workflows.

### Agent File Structure

Agents are markdown files stored in the `agents/` directory:

```markdown
---
name: Agent Display Name
description: When and why to use this agent
capabilities:
  - capability1
  - capability2
skills:
  - skill-name-1
  - skill-name-2
---
# Agent Title

System prompt and behavior instructions for this agent.

Describe the agent's role, goals, and constraints.

## Responsibilities

- Task 1
- Task 2
- Task 3

## Interaction Guidelines

Instructions on how Claude should use this agent.
```

### Frontmatter Fields

- **name**: Display name for the agent
- **description**: When/why to use this agent
- **capabilities**: Array of what the agent can do
- **skills**: Array of skill names to auto-load

### Example Agent

File: `agents/code-reviewer.md`

```markdown
---
name: Code Reviewer
description: Specialized agent for reviewing pull requests with focus on code quality and patterns
capabilities:
  - PR analysis
  - Pattern detection
  - Best practices validation
  - Test coverage assessment
skills:
  - code-quality-standards
  - testing-best-practices
---
# Code Review Agent

You are an expert code reviewer specializing in identifying potential issues and improvements.

## Review Dimensions

- **Code Quality**: Readability, maintainability, performance
- **Testing**: Test coverage, test quality
- **Security**: Vulnerability scanning, input validation
- **Architecture**: Design patterns, modularity
- **TypeScript**: Type safety, type annotations

## Confidence Scoring

Provide confidence scores (0-100) for each finding to help filter false positives.

## Output Format

Report findings with:
1. Location (file:line)
2. Issue category
3. Severity (low/medium/high)
4. Suggested improvement
5. Confidence score
```

## Creating Skills

Skills are context-aware capabilities that Claude automatically applies when relevant.

### Skill Directory Structure

```
skills/
└── skill-name/
    ├── SKILL.md                  # Required
    ├── references/               # Optional
    │   ├── guide.md
    │   ├── examples.json
    │   └── ...
    └── scripts/                  # Optional
        └── helper.sh
```

### SKILL.md Format

```markdown
---
name: skill-display-name
description: Clear description of what this skill teaches Claude and when to use it
---
# Skill Title

Core instructions and knowledge for this skill.

## When to Use

Describe scenarios where Claude should apply this skill.

## Key Principles

1. Principle 1
2. Principle 2
3. Principle 3

## Examples

### Example 1
Description and expected behavior.

### Example 2
Description and expected behavior.

## References

See the `references/` directory for detailed documentation.
```

### Skill Best Practices

1. **Progressive Disclosure**: Start with essential info in frontmatter, provide details in SKILL.md body, reference external docs for deep dives
2. **Auto-trigger Description**: Help Claude decide when to automatically apply this skill
3. **Reusability**: Design skills to work across different contexts
4. **Reference Files**: Use the `references/` subdirectory for linked documentation

## Creating Hooks

Hooks are event-driven automations that execute at specific moments in the Claude Code workflow.

### Hook Configuration

Hooks are configured in `hooks.json` in the plugin root:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/init.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate-bash.sh"
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
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

### Hook Types

**SessionStart** - Runs when a Claude Code session starts
- Use for: Loading context, setting up environment variables, displaying project info

**PreToolUse** - Runs before tool execution
- Use for: Input validation, security checks, command filtering
- Can block execution or modify inputs

**PostToolUse** - Runs after tool execution
- Use for: Formatting output, validation, cleanup
- Sees both input and output

### Hook Matchers

The `matcher` field filters which tools trigger the hook:

- `"*"` - All tools
- `"Bash"` - Only bash commands
- `"Write|Edit"` - Write or Edit tools (pipe for multiple)
- Tool names support wildcards: `"Bash(git:*)"`, `"Bash(npm:*)"`

### Environment Variables

Hooks have access to:
- `CLAUDE_PROJECT_DIR` - Root project directory
- `CLAUDE_CODE_REMOTE` - true if in web environment
- `CLAUDE_ENV_FILE` - For SessionStart to persist variables
- `CLAUDE_PLUGIN_ROOT` - Plugin installation directory

### Using ${CLAUDE_PLUGIN_ROOT}

Always use `${CLAUDE_PLUGIN_ROOT}` for intra-plugin paths because plugins are installed in a cache directory:

```json
{
  "type": "command",
  "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"
}
```

### Hook Exit Codes

- **0** - Success; stdout shown to user
- **2** - Blocking error; stderr fed to Claude as context for retry
- Other codes - Hook failure handled by Claude Code

## Creating MCP Server Integrations

MCP (Model Context Protocol) servers extend Claude with access to external tools and data sources.

### .mcp.json Configuration

```json
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["-m", "mcp_server_module"],
      "env": {
        "API_KEY": "${CLAUDE_ENV_VAR_NAME}"
      }
    }
  }
}
```

### Server Fields

- **command**: Executable to run the server
- **args**: Command arguments
- **env**: Environment variables passed to server
- **env.** placeholders can reference system environment variables

## Testing Your Plugin Locally

### Step 1: Create a Test Directory

```bash
mkdir ~/.claude/test-marketplace
cd ~/.claude/test-marketplace
```

### Step 2: Copy Your Plugin

```bash
cp -r /path/to/plugin-name .
```

### Step 3: Create marketplace.json

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "test-marketplace",
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./plugin-name"
    }
  ]
}
```

### Step 4: Register Marketplace

In Claude Code:
```
/plugin marketplace add ~/.claude/test-marketplace
```

### Step 5: Install Plugin

```
/plugin install plugin-name@test-marketplace
```

### Step 6: Test Components

- Run `/your-command` to test commands
- Check skills are recognized via `/context` or in agent suggestions
- Verify hooks trigger with expected behavior

### Validation

Run validation:
```bash
/plugin validate
```

Or from command line:
```bash
claude plugin validate ~/.claude/test-marketplace
```

## Publishing Your Plugin

### Step 1: Prepare Repository

```
my-plugin/
├── .claude-plugin/plugin.json
├── commands/
├── agents/
├── skills/
├── hooks/
├── README.md
└── .gitignore
```

### Step 2: Create Marketplace

Create `.claude-plugin/marketplace.json` in your repository:

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "my-org-marketplace",
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./plugin-name"
    }
  ]
}
```

### Step 3: Push to GitHub

```bash
git remote add origin https://github.com/your-org/my-plugin
git push -u origin main
```

### Step 4: Share Marketplace

Users can then add your marketplace:
```
/plugin marketplace add your-org/my-plugin
/plugin install plugin-name@your-org-marketplace
```

## Best Practices

### Documentation

1. **README.md**: Explain what each component does
2. **Command descriptions**: Keep frontmatter descriptions concise
3. **Skill examples**: Provide concrete usage examples
4. **Comments**: Document complex hook logic

### Performance

1. **Keep skills focused**: Narrow, specific skills are better than broad ones
2. **Use progressive disclosure**: Link to external docs rather than embedding everything
3. **Optimize hooks**: Minimize hook runtime, use efficient scripts
4. **Lazy load**: Load skills/commands only when needed

### Security

1. **Hook validation**: Always validate inputs in hooks
2. **Tool permissions**: Specify `allowed-tools` in commands
3. **External data**: Validate MCP server responses
4. **Dependencies**: Pin versions in scripts

### Naming Conventions

- **Plugin names**: `kebab-case` (e.g., `my-plugin`)
- **Commands**: `/kebab-case-command`
- **Skills**: `kebab-case-skill-name`
- **Agents**: `PascalCase` in display name
- **Hook matchers**: Match tool names exactly

## Common Patterns

### Pattern 1: Workflow with Multiple Agents

```
plugin-workflow/
├── commands/
│   └── workflow.md           # Entry command
├── agents/
│   ├── planning-agent.md
│   ├── development-agent.md
│   └── review-agent.md
├── skills/
│   ├── architecture-patterns/
│   ├── code-standards/
│   └── testing-practices/
└── hooks/
    └── hooks.json            # PostToolUse for validation
```

### Pattern 2: Utility with Skills

```
plugin-utilities/
├── skills/
│   ├── util-skill-1/
│   ├── util-skill-2/
│   └── util-skill-3/
├── commands/
│   └── util-command.md       # Optional trigger command
└── .mcp.json                 # Optional external tools
```

### Pattern 3: Integration Plugin

```
plugin-integration/
├── .mcp.json                 # Primary feature
├── skills/
│   └── integration-skill/    # Supporting skill
└── commands/
    └── setup.md              # Setup/configuration
```

## Troubleshooting

### Plugin Not Appearing

1. Check `.claude-plugin/plugin.json` exists
2. Verify marketplace.json has correct `source` path
3. Run `/plugin validate`
4. Restart Claude Code

### Command Not Working

1. Check command file is in `commands/` (not `.claude-plugin/`)
2. Verify YAML frontmatter is valid
3. Check command references are correct
4. Test with `/command --help`

### Hooks Not Triggering

1. Verify `hooks.json` is in plugin root
2. Check matcher patterns match tool names
3. Verify script has execute permissions: `chmod +x script.sh`
4. Check hook timeout isn't being exceeded
5. Look for syntax errors in hook JSON

### Skills Not Loading

1. Verify `skills/skill-name/SKILL.md` exists
2. Check YAML frontmatter has `name` and `description`
3. Ensure skill directory is named correctly
4. Restart Claude Code after changes

## Resources

- [Claude Code Documentation](https://code.claude.com/docs)
- [Official Plugins Repository](https://github.com/anthropics/claude-code/tree/main/plugins)
- [Plugins Official Marketplace](https://github.com/anthropics/claude-plugins-official)
- [Claude Code Plugin Template](https://github.com/ivan-magda/claude-code-plugin-template)
