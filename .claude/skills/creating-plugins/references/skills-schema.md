# SKILL.md Reference and Schema

## Overview

SKILL.md is the core file that defines an Agent Skill. It consists of two parts:
1. YAML frontmatter containing metadata
2. Markdown content containing instructions

## File Structure

```
skill-name/
├── SKILL.md (required)
└── Optional Resources
    ├── scripts/
    ├── references/
    └── assets/
```

## SKILL.md Format

```yaml
---
name: skill-identifier
description: What this skill does and when to use it
---

# Skill Instructions

Your markdown instructions go here...
```

## Frontmatter Specification

### Allowed Properties

According to the Agent Skills specification, only these properties are allowed in SKILL.md frontmatter:

```
- name
- description
- license
- allowed-tools
- metadata
```

Any other properties (like `version`, `author`, `category` at the top level) will cause validation errors.

### Required Fields

#### name (Required)

String identifying the skill.

**Constraints:**
- Maximum 64 characters
- Lowercase letters, numbers, and hyphens only
- Cannot start or end with a hyphen
- No XML tags
- No reserved words

**Format:** Gerund form (verb + -ing)

**Examples:**
```yaml
name: pdf-processing
name: data-analysis
name: content-generation
name: code-review
```

#### description (Required)

String describing what the skill does and when to use it.

**Constraints:**
- Maximum 1024 characters
- Non-empty
- No XML tags

**Requirements:**
- Explain WHAT the skill does
- Explain WHEN to use it
- Write in third person
- Include all "when to use" information here

**Example:**
```yaml
description: Extract text and tables from PDF files, fill forms, and merge documents. Use when working with PDF files or when the user mentions PDFs, forms, document extraction, or PDF manipulation.
```

### Optional Fields

#### license (Optional)

String specifying the license for the skill.

**Common values:**
```yaml
license: Apache-2.0
license: MIT
license: BSD-3-Clause
license: GPL-3.0
```

#### allowed-tools (Optional)

Comma-separated string of tools Claude can use when this skill is active.

**Purpose:**
- Restrict which tools Claude can access
- Keep Claude focused on the skill's purpose
- Improve security and reliability

**Syntax:**
```yaml
allowed-tools: "Tool1, Tool2, Tool3"
```

**Common tools:**
- Bash
- Read
- Write
- Execute

**Examples:**
```yaml
# For file operations
allowed-tools: "Read, Write, Bash"

# For scripts only
allowed-tools: "Bash"

# For minimal operations
allowed-tools: "Read"
```

#### metadata (Optional)

Object containing additional metadata about the skill.

**Typical fields:**
```yaml
metadata:
  author: organization-name
  version: "1.0.0"
  tags:
    - category
    - domain
```

## Complete Frontmatter Examples

### Minimal Skill

```yaml
---
name: greeting-skill
description: Generate personalized greetings for customers. Use when you need to create warm, professional greeting messages.
---
```

### Standard Skill

```yaml
---
name: data-analysis
description: Analyze datasets using statistical methods and company-specific metrics. Use when processing data, generating reports, or exploring trends.
license: Apache-2.0
allowed-tools: "Read, Write, Bash"
---
```

### Full Featured Skill

```yaml
---
name: document-generation
description: Create formatted documents following company brand guidelines. Use when generating reports, proposals, or internal documents.
license: Apache-2.0
allowed-tools: "Read, Write, Bash"
metadata:
  author: company-name
  version: "2.0"
  tags:
    - documentation
    - enterprise
    - formatting
---
```

## Markdown Body

### Structure Guidelines

The markdown body (everything after `---`) contains the skill's instructions.

**No mandatory format**, but effective structures include:

```markdown
# [Skill Title]

## Overview
[What this skill helps Claude do]

## Process
1. Step 1
2. Step 2
3. Step 3

## Key Guidelines
- Guideline 1
- Guideline 2

## Examples
### Example 1
[Show example input and output]

### Example 2
[Show another example]

## Advanced Features
[Optional advanced usage]

## Troubleshooting
[Common issues and solutions]

## References
See references/[filename].md for more information about [topic].
```

### Content Guidelines

**Recommended Length**: Under 5000 tokens
- This is loaded entirely when the skill is triggered
- Move detailed information to reference files

**Use Examples**: Include at least 2-3 concrete examples
**Consistency**: Use one term throughout for each concept
**Clarity**: Use imperative form for instructions

## Validation Rules

The SKILL.md file is validated against these rules:

### Frontmatter Validation

- Required fields present: `name` and `description`
- Frontmatter fields are only from allowed list
- `name` format follows constraints (lowercase, hyphens, etc.)
- `description` is non-empty and under 1024 characters
- No duplicate field names

### Common Validation Errors

**Error: properties must be in ('name', 'description', 'license', 'allowed-tools', 'metadata')**

Cause: Using invalid frontmatter properties

```yaml
# Wrong: 'author' and 'version' at top level
---
name: my-skill
description: Description
author: my-name
version: 1.0
---

# Right: 'author' and 'version' in 'metadata'
---
name: my-skill
description: Description
metadata:
  author: my-name
  version: "1.0"
---
```

**Error: name must be lowercase letters, numbers, and hyphens only**

Cause: Invalid characters in name

```yaml
# Wrong
name: MySkill        # Capital letters
name: my_skill       # Underscores
name: my skill       # Spaces

# Right
name: my-skill
name: my-data-skill
```

**Error: name must not start or end with a hyphen**

Cause: Hyphen at beginning or end

```yaml
# Wrong
name: -my-skill
name: my-skill-

# Right
name: my-skill
```

## JSON Schema Representation

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SKILL.md Schema",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 64,
      "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$",
      "description": "Lowercase, letters/numbers/hyphens only"
    },
    "description": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024,
      "description": "What skill does and when to use it"
    },
    "license": {
      "type": "string",
      "description": "License identifier (e.g., Apache-2.0, MIT)"
    },
    "allowed-tools": {
      "type": "string",
      "description": "Comma-separated list of allowed tools"
    },
    "metadata": {
      "type": "object",
      "properties": {
        "author": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "additionalProperties": true
    }
  },
  "required": ["name", "description"],
  "additionalProperties": false
}
```

## Progressive Disclosure in Practice

### How the Tiers Work

**Tier 1: Metadata (Always Available)**
```yaml
name: pdf-processing
description: Extract text and tables from PDFs...
```
Size: ~100-200 characters
Used by Claude to discover the skill.

**Tier 2: Full SKILL.md (Loads on Trigger)**
```markdown
# PDF Processing Skill

## Process
1. Load PDF...
[~2000 tokens of instructions]

See references/advanced-techniques.md for details
```
Size: ~2000-5000 tokens
Loaded when Claude determines the skill is relevant.

**Tier 3: Resources (Load on Demand)**
```
references/
├── advanced-techniques.md      (~1000 tokens)
├── error-handling.md          (~800 tokens)
└── examples.md                (~500 tokens)

scripts/
├── validate.py
├── process.sh
```
Size: Unlimited
Loaded only when Claude needs specific information.

## Tips for Effective SKILL.md

### 1. Discovery is in the Description

The `description` field determines if Claude uses your skill:
```yaml
# Good: Clear triggers
description: Create customer-facing sales documents (proposals, quotes, contracts). Use when generating professional sales materials or the user mentions proposals, quotes, or sales documents.

# Poor: No triggers
description: A skill for creating documents
```

### 2. Instructions Stay Concise

Keep the body clear and actionable:
```markdown
# Good: Concise and clear
## Process
1. Validate input format
2. Apply brand guidelines
3. Generate output

See references/brand-guidelines.md for detailed specifications.

# Poor: Too verbose
## Detailed Process Explanation
When you receive input, you need to check if it matches...
[paragraph after paragraph of explanation]
```

### 3. Link to References

Point to detailed information rather than embedding it:
```markdown
# Good: Points to reference
See references/color-palette.md for all approved brand colors.

# Poor: Embeds everything
## Color Specifications
Red: #FF0000, used for...
Blue: #0000FF, used for...
[20 more color definitions...]
```

### 4. Use Tools Constraints

Restrict what Claude can do:
```yaml
# For skills that should only read
allowed-tools: "Read"

# For skills that need to run scripts
allowed-tools: "Bash, Read"

# For skills that modify files
allowed-tools: "Read, Write, Bash"
```

## Creating a Skill

### Minimal Viable Skill

Start with just the required fields:

```yaml
---
name: my-first-skill
description: This skill helps with [specific task]. Use it when [specific triggers].
---

# My First Skill

## How to Use This Skill

Follow these steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Example

Input: [example input]
Output: [example output]
```

### Expanding the Skill

As you iterate, add:
1. More examples
2. Edge cases
3. Error handling
4. Reference files for complex topics
5. Scripts for deterministic operations

## Resources

- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Claude Skills Documentation](https://code.claude.com/docs/en/skills)
