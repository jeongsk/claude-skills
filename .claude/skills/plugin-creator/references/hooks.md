# Plugin Hooks Reference

## Location
`hooks/hooks.json` at plugin root or inline in plugin.json

## Available Events

| Event              | Description                        |
| ------------------ | ---------------------------------- |
| `PreToolUse`       | Before Claude uses a tool          |
| `PostToolUse`      | After Claude uses a tool           |
| `UserPromptSubmit` | When user submits a prompt         |
| `Notification`     | When Claude Code sends notification|
| `Stop`             | When Claude attempts to stop       |
| `SubagentStop`     | When a subagent attempts to stop   |
| `SessionStart`     | At session start                   |
| `SessionEnd`       | At session end                     |
| `PreCompact`       | Before conversation compaction     |

## Hook Types

- `command`: Execute shell command or script
- `validation`: Validate file content or project state
- `notification`: Send alerts or status updates

## Configuration Format

```json
{
  "hooks": {
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
    ]
  }
}
```

## Example: Auto-format on file write

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

## Example: Pre-commit validation

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate-commit.sh"
          }
        ]
      }
    ]
  }
}
```

## Script Requirements
- Scripts must be executable: `chmod +x script.sh`
- Use `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths
