# Plugin Marketplace Reference

## Marketplace Structure

```
marketplace-repo/
├── .claude-plugin/
│   └── marketplace.json     # Required
└── plugins/                 # Optional: bundled plugins
    └── my-plugin/
```

## marketplace.json Schema

### Required Fields

| Field     | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| `name`    | string | Marketplace identifier       |
| `owner`   | object | Maintainer info              |
| `plugins` | array  | List of available plugins    |

### Example marketplace.json

```json
{
  "name": "my-marketplace",
  "owner": {
    "name": "Dev Team",
    "email": "team@example.com"
  },
  "plugins": [
    {
      "name": "my-plugin",
      "source": "./plugins/my-plugin",
      "description": "My awesome plugin"
    }
  ]
}
```

## Plugin Sources

### Relative Path (same repo)
```json
{
  "name": "local-plugin",
  "source": "./plugins/local-plugin"
}
```

### GitHub Repository
```json
{
  "name": "github-plugin",
  "source": {
    "source": "github",
    "repo": "owner/plugin-repo"
  }
}
```

### Git URL
```json
{
  "name": "git-plugin",
  "source": {
    "source": "url",
    "url": "https://gitlab.com/team/plugin.git"
  }
}
```

## Marketplace Commands

```bash
# Add marketplace
/plugin marketplace add owner/repo
/plugin marketplace add ./local-path

# List marketplaces
/plugin marketplace list

# Update marketplace
/plugin marketplace update marketplace-name

# Remove marketplace
/plugin marketplace remove marketplace-name
```

## Team Configuration

Add to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "team-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/plugins"
      }
    }
  }
}
```
