# Agent Skills Overview

## What Are Agent Skills?

Agent Skills are modular capabilities that extend Claude's functionality for specialized tasks. Each Skill packages instructions, metadata, and optional resources (scripts, templates, documentation) that Claude loads dynamically and uses automatically when relevant to your request.

Skills are "folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."

### Key Characteristics

- **Self-contained**: Each skill exists in its own directory with a SKILL.md file
- **Reusable**: Skills are available across Claude's products (Claude Code, Claude.ai, Claude API)
- **Dynamic Loading**: Claude automatically matches tasks to relevant skills and loads them on demand
- **Modular**: Package expertise, workflows, and best practices for specific domains

## The Progressive Disclosure Architecture

Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable. Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed.

This three-tier loading system ensures that the amount of context that can be bundled into a skill is effectively unbounded:

1. **Metadata Tier (Always Loaded)**: The skill's name and description from YAML frontmatter
2. **Body Tier (On Trigger)**: The full SKILL.md instructions load when Claude determines the skill is relevant
3. **Resource Tier (On Demand)**: Scripts, references, and assets load as Claude needs them

## Skill Structure

A skill is a directory containing the following structure:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter
│   │   ├── name (required)
│   │   └── description (required)
│   └── Markdown instructions
└── Optional Resources
    ├── scripts/ - Executable code (Python, Bash, JavaScript)
    ├── references/ - Documentation and resources
    └── assets/ - Templates, icons, fonts, etc.
```

### Minimum Requirement

At its simplest, a skill requires only a directory with a `SKILL.md` file containing:
- YAML frontmatter with `name` and `description` fields
- Markdown instructions that tell Claude how to use the skill

## Pre-built Skills Available

Anthropic provides pre-built Agent Skills for common document tasks:

- **PowerPoint (pptx)**: Creating and editing presentations
- **Excel (xlsx)**: Spreadsheets and data analysis
- **Word (docx)**: Document creation and formatting
- **PDF (pdf)**: Generating formatted PDF documents

These pre-built skills are available to Pro, Max, Team, and Enterprise users.

## Skills vs. Other Tools

### Skills vs. Subagents

- **Skills**: Add knowledge to the current conversation and help Claude understand how to perform tasks
- **Subagents**: Run in separate contexts with their own tools and isolated execution environments

Use Skills for guidance and standards; use subagents when you need isolation or different tool access.

### Skills vs. MCP Servers

- **MCP Servers**: Provide the actual tools and connections (e.g., database connections, API integrations)
- **Skills**: Teach Claude how to use those tools effectively

For example, an MCP server might connect Claude to your database, while a Skill teaches Claude your data model and query patterns.

## Availability

Agent Skills are available to:
- Pro, Max, Team, and Enterprise users on Claude.ai
- Users of Claude Code with plugin support
- API users via the Skills API and Agent SDK

## How Claude Discovers and Uses Skills

1. **Discovery Phase**: At startup, Claude loads all skill names and descriptions from YAML frontmatter into its context
2. **Matching Phase**: When you make a request, Claude determines which skills are relevant to your task
3. **Loading Phase**: The full SKILL.md content loads, providing detailed instructions
4. **Execution Phase**: Claude uses the skill's guidance, scripts, and resources to complete your task

## Use Cases

Skills can be created for a wide range of applications:

- **Creative**: Art styles, music composition, design patterns
- **Technical**: Web testing, API generation, code templates
- **Enterprise**: Brand guidelines, communication workflows, data analysis patterns
- **Personal**: Task automation, writing templates, personal workflows
- **Document Manipulation**: Creating reports, standardizing formats, batch processing

## References

- [Agent Skills Overview - Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
