# Plugin Agents Reference

## Location
`agents/` directory at plugin root

## File Format
Markdown files with YAML frontmatter

## Agent Structure

```markdown
---
description: What this agent specializes in
capabilities: ["task1", "task2", "task3"]
---

# Agent Name

Detailed description of the agent's role, expertise, and when Claude should invoke it.

## Capabilities
- Specific task the agent excels at
- Another specialized capability
- When to use this agent vs others

## Context and Examples
Examples of when to use this agent and what problems it solves.
```

## Example: security-reviewer.md

```markdown
---
description: Security code review specialist
capabilities: ["vulnerability detection", "security best practices", "OWASP compliance"]
---

# Security Reviewer

A specialized agent for reviewing code for security vulnerabilities
and ensuring compliance with security best practices.

## Capabilities
- Identify common vulnerabilities (XSS, SQL injection, etc.)
- Review authentication and authorization logic
- Check for sensitive data exposure
- Verify input validation and sanitization

## When to Use
- Before merging security-sensitive code
- During security audits
- When implementing authentication features
```

## Example: test-writer.md

```markdown
---
description: Automated test generation specialist
capabilities: ["unit tests", "integration tests", "test coverage"]
---

# Test Writer

Specialized in writing comprehensive test suites for code.

## Capabilities
- Generate unit tests with good coverage
- Write integration tests for API endpoints
- Create mock objects and test fixtures
- Identify edge cases and boundary conditions

## Approach
1. Analyze the code to understand functionality
2. Identify testable units and integration points
3. Generate tests with descriptive names
4. Include both positive and negative test cases
```

## Integration
- Agents appear in `/agents` interface
- Claude can auto-invoke based on task context
- Users can manually invoke agents
