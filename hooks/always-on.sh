#!/usr/bin/env sh
# SessionStart hook: injects the evidence-first ruleset when the user has
# opted in with $CLAUDE_CONFIG_DIR/.evidence-first-always (default ~/.claude).
# Never blocks session start: any failure exits 0.
#
# Pure POSIX sh so it runs anywhere Claude Code runs a command hook (sh on
# macOS/Linux, Git Bash on Windows) without depending on a Node install being
# on PATH.

claude_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
flag_path="$claude_dir/.evidence-first-always"

# Only fire when the user has opted in.
[ -f "$flag_path" ] || exit 0

# $0 is the absolute script path substituted into hooks.json by Claude Code,
# so resolve SKILL.md relative to it instead of trusting an exported env var.
script_dir=$(dirname -- "$0")
skill_path="$script_dir/../skills/evidence-first/SKILL.md"
[ -f "$skill_path" ] || exit 0

# Strip a leading YAML frontmatter block (--- ... --- at the very top of file).
body=$(awk '
  NR == 1 && $0 ~ /^---[[:space:]]*$/ { in_fm = 1; next }
  in_fm && $0 ~ /^---[[:space:]]*$/   { in_fm = 0; next }
  !in_fm                              { print }
' "$skill_path") || exit 0

printf 'EVIDENCE-FIRST MODE ACTIVE (always-on). Apply the ruleset below to every response in this session; delete %s to disable always-on mode.\n\n%s\n' \
  "$flag_path" "$body"
