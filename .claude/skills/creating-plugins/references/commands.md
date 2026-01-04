# Plugin Commands Reference

## Location
`commands/` directory at plugin root

## File Format
Markdown files with YAML frontmatter

## Command Structure

```markdown
---
description: Brief description of what this command does
---

# Command Name

Detailed instructions for Claude when this command is invoked.

## Purpose
Explain what this command accomplishes.

## Behavior
Describe how Claude should respond when this command is used.

## Examples
Provide examples of expected input/output.
```

## Example: hello.md

```markdown
---
description: Greet the user with a personalized message
---

# Hello Command

Greet the user warmly and ask how you can help them today.
Make the greeting personal and encouraging.
```

## Example: deploy.md

```markdown
---
description: Deploy the application to the specified environment
---

# Deploy Command

Guide the user through the deployment process:

1. Verify all tests pass
2. Check for uncommitted changes
3. Confirm the target environment
4. Execute the deployment script
5. Verify deployment success

## Arguments
- `env`: Target environment (staging/production)
- `--skip-tests`: Skip test verification (not recommended)

## Safety
Always confirm before deploying to production.
```

## Naming Convention
- Use kebab-case for filenames: `my-command.md`
- Command is invoked as `/my-command`
