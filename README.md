# Nanoagent Plugin 1 - Gitignore Decision Explainer

Given the contents of the repository-root `.gitignore` and candidate repository-relative paths, determine whether each path is ignored or included. For every path, report the final rule that determined the result.

## Supported .gitignore subset

- Exact file or path patterns, such as `notes.txt` and `build/output.log`
- `*` wildcards, such as `*.log`
- A `*` wildcard may match `/` characters in a candidate path
- Directory patterns ending in `/`, such as `cache/`
- A directory pattern `cache/` matches the exact candidate `cache` and paths below it
- `!` negation patterns, such as `!important.log`
- Rules are processed from top to bottom; the last matching rule wins
- Blank lines, lines beginning with `#`, and a lone `!` are ignored and do not receive rule numbers
- An empty `.gitignore` includes every candidate with null rule metadata

## Out of scope (for now)

- `**` recursive globs
- Nested `.gitignore` files
- Escaped `#` and `!`
- Full Git directory traversal behavior