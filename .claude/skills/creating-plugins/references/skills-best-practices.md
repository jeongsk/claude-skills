# Skill Authoring Best Practices

## Core Principles

### 1. Respect the Context Window

The context window is a public good. Only include information Claude doesn't already possess. Challenge every piece:

- Does Claude truly need this information?
- Can this be learned from a reference file loaded on demand?
- Can a script generate this information instead of storing it?

### 2. Match Specificity to Task Fragility

Different tasks require different levels of specificity:

- **High Freedom Tasks** (multiple valid approaches): Use broad guidance, let Claude explore
- **Medium Freedom Tasks** (preferred patterns with variation): Provide structured approaches with flexibility
- **Low Freedom Tasks** (fragile operations): Be extremely specific, use templates, provide examples

Example:
```markdown
# Creative Writing Skill
Use broad guidelines about voice and style.

# Data Processing Skill
Be very specific about data validation, transformation steps, and output format.
```

### 3. Progressive Disclosure

Load content in three levels:
1. **Metadata**: Always available (name, description)
2. **SKILL.md Body**: Loads when skill is triggered
3. **Resources**: Load on demand

```
Metadata tier (~100 characters)
  ↓
SKILL.md body (~2000 tokens)
  ↓
References (~5000 tokens each, loaded as needed)
```

## Naming Conventions

### Skill Names

Use **gerund form** (verb + -ing) for clarity. This describes the activity or capability:

- Good: `pdf-processing`, `data-analysis`, `content-generation`
- Poor: `pdf`, `analysis`, `generator`

### Naming Rules

The `name` field must follow these rules:
- Maximum 64 characters
- Lowercase letters, numbers, and hyphens only
- Cannot start or end with a hyphen
- No XML tags
- No reserved words

### Directory Names

Match the skill directory name to the `name` field:
```
pdf-processing/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

## SKILL.md Frontmatter

### Required Fields

```yaml
---
name: skill-name
description: Clear description of what the skill does and when to use it
---
```

### Optional Fields

```yaml
---
name: skill-name
description: Description text (max 1024 characters)
license: Apache-2.0
allowed-tools: "Tool1, Tool2, Tool3"
metadata:
  author: organization-name
  version: "1.0"
---
```

### Frontmatter Guidelines

**Name Field**
- Use lowercase letters, numbers, and hyphens
- Maximum 64 characters
- Be specific and searchable

**Description Field**
- Maximum 1024 characters
- Explain WHAT the skill does
- Explain WHEN to use it (critical for discovery)
- Write in third person
- Include all "when to use" information here
- Do NOT save this for the body (the body only loads after triggering)

Good description:
```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

Poor description:
```
A skill for processing PDFs with various tools.
```

**Allowed-Tools Field**
```yaml
allowed-tools: "Bash, Read, Write"
```

This restricts which tools Claude can use when the skill is active. Useful for:
- Preventing unintended tool usage
- Keeping Claude focused on the skill's purpose
- Security and reliability

## SKILL.md Body Content

### Structure

There are no strict format requirements for the body. Write whatever helps Claude perform the task effectively. However, these structures work well:

```markdown
# Skill Title

## Overview
Brief summary of what Claude should do with this skill.

## Process Steps
1. Step 1
2. Step 2
3. Step 3

## Key Guidelines
- Guideline 1
- Guideline 2
- Guideline 3

## Examples
### Example 1: Scenario A
Input: ...
Process: ...
Output: ...

### Example 2: Scenario B
...

## Templates
[Include templates for output format]

## References
See references/filename.md for [more details about this topic].

## Advanced Features
[Optional advanced capabilities]
```

### Content Guidelines

**Keep It Concise**
- Recommended maximum: Under 5000 tokens for the full SKILL.md body
- This is loaded entirely when the skill is triggered
- Move detailed information to reference files

**Use Examples Liberally**
Examples help Claude understand what success looks like:
```markdown
## Examples

### Good Output
[Show what Claude should produce]

### Bad Output
[Show what Claude should avoid]

### Edge Cases
[Handle special situations]
```

**Consistency in Terminology**
Choose one term for each concept and use it throughout:
```markdown
# Good: Consistent
- Call it "Customer" everywhere
- Call the process "Customer Acquisition" everywhere

# Bad: Inconsistent
- Sometimes "Customer", sometimes "Client"
- Sometimes "Acquisition", sometimes "Onboarding"
```

**Output Templates**
Provide templates that match your needs:
```markdown
## Output Format

### For Simple Tasks
Result: [brief summary]

### For Complex Tasks
## Analysis
[Detailed findings]

## Recommendations
- Recommendation 1
- Recommendation 2

## Next Steps
[Action items]
```

## Bundled Resources

### Scripts Directory

Store executable code that Claude can run:

```
skill-name/scripts/
├── validate.py
├── process.sh
└── generate.js
```

**Guidelines:**
- Scripts should be self-contained
- Document dependencies clearly
- Handle edge cases gracefully
- Include error handling
- Comment your code for clarity

### References Directory

Store documentation loaded on demand:

```
skill-name/references/
├── company-guidelines.md
├── data-schema.md
└── examples.md
```

**Guidelines:**
- Keep individual files focused and readable
- Use clear section headings
- Include examples
- Link between related files
- Under 2000 tokens per file is ideal

### Assets Directory

Store files used in skill outputs:

```
skill-name/assets/
├── templates/
│   ├── report-template.docx
│   └── slide-template.pptx
├── fonts/
│   └── brand-font.ttf
└── images/
    └── logo.png
```

## Iterating on Skills

### Watch for These Patterns

As you iterate, pay attention to:

1. **Unexpected Exploration**: Is Claude exploring paths you didn't anticipate?
2. **Missed Connections**: Are there obvious connections Claude isn't making?
3. **Overreliance**: Is Claude relying too much on one section?
4. **Ignored Content**: Are parts of the skill going unused?

### Improvement Process

1. **Observe**: Watch how Claude actually uses the skill
2. **Question Assumptions**: Don't assume your structure is optimal
3. **Ask Claude to Reflect**: When things go wrong, ask Claude what went wrong
4. **Iterate**: Update based on actual usage, not predicted usage
5. **Test**: Re-test with real scenarios

```markdown
# When Something Goes Wrong

Ask Claude: "What context or guidance was missing? What confused you?"

Claude's answer reveals what you actually need to include.
```

## Testing Skills

### Testing Across Models

Skills effectiveness depends on the underlying model:
- Claude Opus 4.5: Handles complex, nuanced instructions
- Claude Haiku: Needs clearer, more explicit guidance

**Strategy**: Test your skill with all models you plan to use it with.

If a skill works with Opus but needs adjustment for Haiku:
- Make instructions more explicit
- Provide more examples
- Simplify complex concepts
- Add step-by-step breakdowns

### Testing Checklist

- [ ] Skill is discoverable (description is clear)
- [ ] Skill is triggered appropriately
- [ ] SKILL.md body loads when needed
- [ ] Scripts execute successfully
- [ ] References load when accessed
- [ ] Output matches expectations
- [ ] Edge cases are handled
- [ ] Works across target models

## Common Pitfalls

### 1. Poor Skill Descriptions

**Problem**: Claude doesn't know when to use the skill
```yaml
# Bad
description: A skill for writing

# Good
description: Improve writing quality by applying grammar rules, tone adjustment, and clarity enhancements. Use when the user asks to edit, revise, or improve written content.
```

### 2. Overloading the Body

**Problem**: All information in SKILL.md body, none in references
```markdown
# Bad: All 5000+ tokens in one place

# Good: Main skill, reference files for details
See references/advanced-techniques.md for detailed examples.
```

### 3. Inconsistent Terminology

**Problem**: Claude gets confused by switching terms
```
Don't mix "API endpoint", "endpoint", "API", "service" for the same thing.
```

### 4. Missing "When to Use"

**Problem**: Information buried in the body where it won't help discovery
```yaml
# Bad
description: A skill for data processing

# Good: Includes when to use
description: Process raw data files, clean records, and generate summary statistics. Use when working with CSV, JSON, or database exports, or when the user asks for data transformation.
```

### 5. No Examples

**Problem**: Claude doesn't understand what success looks like
```markdown
# Bad: Just instructions
Process the data according to guidelines.

# Good: Shows examples
## Example
Input: customers.csv with 1000 records
Process: Remove duplicates, validate emails, group by region
Output: cleaned_customers.json with 950 valid records, 50 duplicates logged
```

## Sharing and Distribution

### Claude Code Plugins

Package skills in Claude Code plugins for easy distribution:

```json
{
  "name": "my-skill-plugin",
  "version": "1.0.0",
  "skills": [
    "skill-name"
  ]
}
```

### Marketplace Registration

Register in a marketplace to share with others:

```json
{
  "name": "my-marketplace",
  "skills": [
    {"name": "skill-1", "source": "./skill-1"},
    {"name": "skill-2", "source": "./skill-2"}
  ]
}
```

### Documentation

Always include:
- What the skill does
- When to use it
- How to customize it
- Examples of usage
- License information

## References

- [Agent Skills Best Practices - Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Skill Creator Skill](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
