# Evidence First

Outcome-first responses without evidence loss.

[简体中文](README.zh-CN.md) · [日本語](README.ja.md) ·
[MIT License](LICENSE)

`evidence-first` is an output-shaping skill for coding agents. It makes the
answer, verified status, or real blocker easy to find while preserving the
facts that determine a technical or research decision.

It is deliberately **not** a shortest-answer skill. Large evidence is layered,
tabulated, or linked—not silently deleted.

## Install

### Codex

```bash
codex plugin marketplace add LuckyJoeshp/evidence-first-agent --ref main
codex plugin add evidence-first@evidence-first-agent
```

Start a new thread after installation. Codex selects the skill automatically
for substantial technical or research work where losing evidence could change
the decision. Trivial edits, simple factual questions, casual conversation,
and open-ended brainstorming stay in the normal mode.

You can still force the skill for one task with:

```text
$evidence-first
```

Automatic selection is task-scoped, not always-on. Say `normal mode` or
`stop evidence-first mode` to disable it for the current task.

### Claude Code

```bash
claude plugin marketplace add LuckyJoeshp/evidence-first-agent
claude plugin install evidence-first@evidence-first-agent
```

Then type `/evidence-first`.

See [INSTALL.md](INSTALL.md) for other agents, updates, uninstalling, manual
installation, and the optional Claude Code always-on flag.

## The core contract

When rules conflict, apply this priority order:

1. System, harness, and explicit user requirements
2. Correctness, safety, and evidence integrity
3. Agent ownership and task completion
4. Actionability and scanability
5. Brevity and style

The skill must preserve:

- requirements, constraints, and acceptance criteria
- observed facts, separately labeled inference and assumptions
- supporting evidence and material counterevidence
- uncertainty, limitations, and sample or decision boundaries
- passed, failed, skipped, unavailable, and unrun checks
- risks, rollback points, citations, artifacts, and audit identifiers

There is no five-item cap. There is no forced user homework, fabricated next
step, or uncalibrated minute estimate.

Read the complete contract in
[SKILL.md](skills/evidence-first/SKILL.md).

## Before and after

### Before

> The release is almost ready. Formatting, type checking, and unit tests look
> good. There are a few auth integration issues to investigate, and we should
> probably run the remaining tests and verify rollback.

### Evidence First

> **Release blocked.**
>
> | Check | Result |
> | --- | --- |
> | Formatting | Passed |
> | Type checking | Passed |
> | Unit tests | 812 passed |
> | Integration tests | 3 auth failures |
> | End-to-end tests | Not run because integration failed |
> | Migration dry-run | Passed |
> | Rollback restoration | Not tested |
>
> Remaining risk: the auth failures block release, and rollback recoverability
> is still unverified. The agent owns the next action: diagnose the three auth
> failures, then run the blocked checks.

The second response is easier to scan without turning missing evidence into a
green result.

## What changed from the upstream skill

This project is a fork of
[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) and retains its
useful answer-first and progress-visibility ideas.

This fork changes the contract for evidence-heavy agent work:

- replaces hard brevity rules with progressive disclosure
- makes evidence integrity outrank style
- keeps agent-owned work with the agent
- removes forced list caps, closers, next actions, and time estimates
- removes medical framing and cross-topic persistence by default
- lets Codex select the skill automatically with explicit negative triggers
- adds evidence-preservation cases and release gates to the evaluation harness

Upstream copyright and MIT terms remain in [LICENSE](LICENSE).

## Evaluation status

The repository includes paired baseline/candidate runners, blinded scoring, and
cases designed to catch evidence omission or role mixing.

```bash
python3 scripts/run_evals.py validate
python3 -m unittest discover -s tests -v
```

Passing these unit tests validates the harness mechanics, **not** the skill's
real-world effectiveness. No paired model benchmark is published yet. Any
future effectiveness claim must include the responses, model and CLI versions,
trial count, rubric, and blinded scores described in
[evals/README.md](evals/README.md).

## Security

The Codex plugin declares only an instruction skill. It adds no MCP server,
network service, or project write capability. The evaluation runner launches a
configured model CLI only when a maintainer runs it manually.

The marketplace entry pins the installable plugin to the `v1.1.0` release tag;
the marketplace catalog itself is read from `main`.

## License

MIT.
