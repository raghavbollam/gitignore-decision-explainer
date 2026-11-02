# Nanoagent Plugin 1 - Gitignore Decision Explainer

With a given repository file tree and a .gitignore file, determine whether each path is ignored or included. For every path, report the final rule that determined the result.

## Supported .gitignore subset

- Exact file or path patterns, such as `notes.txt` and `build/output.log`
- `*` wildcards, such as `*.log`
- A `*` wildcard may match `/` characters in a candidate path
- Directory patterns ending in `/`, such as `cache/`
- `!` negation patterns, such as `!important.log`
- Rules are processed from top to bottom; the last matching rule wins
- Blank lines and lines beginning with `#` are ignored

## Out of scope (for now)

- `**` recursive globs
- Nested `.gitignore` files
- Escaped `#` and `!`
- Full Git directory traversal behavior