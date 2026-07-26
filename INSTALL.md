# Install Evidence First

The stable plugin payload is pinned to release tag `v1.1.0`. The repository
marketplace catalog is read from `main` so future releases can move that pin
deliberately.

## Codex

### Install

```bash
codex plugin marketplace add LuckyJoeshp/evidence-first-agent --ref main
codex plugin add evidence-first@evidence-first-agent
```

Start a new thread after installation. Codex automatically selects the skill
for substantial technical and research tasks where omitted evidence could
change a decision. It stays off for trivial edits, simple factual questions,
casual conversation, and unconstrained brainstorming.

Explicit invocation remains available as an override:

```text
$evidence-first
```

Say `normal mode` or `stop evidence-first mode` to disable it for the current
task. Automatic selection is task-scoped and is not equivalent to always-on
mode.

### Verify

```bash
codex plugin list
```

Confirm `evidence-first` appears under the `evidence-first-agent` marketplace.

### Update

```bash
codex plugin marketplace upgrade evidence-first-agent
codex plugin remove evidence-first
codex plugin add evidence-first@evidence-first-agent
```

Start a new thread after reinstalling so Codex reloads the skill.

### Uninstall

```bash
codex plugin remove evidence-first
codex plugin marketplace remove evidence-first-agent
```

## Claude Code

### Install

```bash
claude plugin marketplace add LuckyJoeshp/evidence-first-agent
claude plugin install evidence-first@evidence-first-agent
```

Start a new session and type:

```text
/evidence-first
```

### Verify

```bash
claude plugin list
```

### Optional always-on mode

Installing the plugin does not enable always-on mode. Opt in with:

```bash
touch ~/.claude/.evidence-first-always
```

The `SessionStart` hook then loads the rules in new, resumed, cleared, and
compacted sessions. To return to on-demand mode:

```bash
rm ~/.claude/.evidence-first-always
```

The hook honors `CLAUDE_CONFIG_DIR` when the Claude configuration directory has
been moved. Say `stop evidence-first mode` or `normal mode` to stop the style
for the current session.

### Update

```bash
claude plugin marketplace update evidence-first-agent
claude plugin uninstall evidence-first
claude plugin install evidence-first@evidence-first-agent
```

### Uninstall

```bash
claude plugin uninstall evidence-first
claude plugin marketplace remove evidence-first-agent
```

Remove `~/.claude/.evidence-first-always` as well if it exists.

## Cursor, OpenCode, GitHub Copilot, Pi, and compatible agents

Agents that support the Agent Skills layout can use the community installer:

```bash
npx skills add LuckyJoeshp/evidence-first-agent
```

Select the target agent and project or global scope in the installer. Start a
new agent chat afterward because most skill indexes are loaded at session
start.

For an explicit target:

```bash
npx skills add LuckyJoeshp/evidence-first-agent -a cursor -y
npx skills add LuckyJoeshp/evidence-first-agent -a opencode -y
npx skills add LuckyJoeshp/evidence-first-agent -a github-copilot -y
```

Update or remove with:

```bash
npx skills update evidence-first
npx skills remove evidence-first
```

## Zed

In the Agent Panel, choose **Create skill from URL** and use the release-pinned
file:

```text
https://github.com/LuckyJoeshp/evidence-first-agent/blob/v1.1.0/skills/evidence-first/SKILL.md
```

Choose Project scope for one repository or User scope for all repositories.

## Gemini CLI

### Extension

```bash
gemini extensions install https://github.com/LuckyJoeshp/evidence-first-agent
```

Invoke `/evidence-first`.

### Release-pinned command

```bash
mkdir -p ~/.gemini/commands
curl -fsSL \
  https://raw.githubusercontent.com/LuckyJoeshp/evidence-first-agent/v1.1.0/skills/evidence-first/agents/gemini.toml \
  -o ~/.gemini/commands/evidence-first.toml
```

The command route is fixed to `v1.1.0`; inspect the file before installing if
your environment requires reviewed third-party instructions.

## Manual Agent Skill installation

Clone the reviewed release:

```bash
git clone --branch v1.1.0 --depth 1 \
  https://github.com/LuckyJoeshp/evidence-first-agent.git
```

Copy `skills/evidence-first/` into the target agent's skill directory. Keep the
folder name `evidence-first`.

## Activation behavior

- On Codex, the agent selects the skill automatically for substantial,
  evidence-sensitive work. Explicit invocation remains an override.
- Automatic or on-demand invocation applies to the current task and its
  follow-up turns.
- It stops carrying across an unrelated topic unless persistent mode is
  explicitly requested.
- A system, harness, or user output contract always outranks the skill.
- The skill changes response organization; it grants no tools or permissions.

## Local development

Use the canonical file at `skills/evidence-first/SKILL.md`. Keep the Cursor copy
byte-identical:

```bash
cp skills/evidence-first/SKILL.md \
  .cursor/skills/evidence-first/SKILL.md
```

Validate before publishing:

```bash
python3 scripts/run_evals.py validate
python3 -m unittest discover -s tests -v
```

The evaluation harness can run paid model calls. It never runs them during
normal plugin installation or skill invocation; see
[evals/README.md](evals/README.md) before using it.
