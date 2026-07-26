import json
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "evidence-first"
MARKETPLACE_NAME = "evidence-first-agent"
VERSION = "1.0.0"
REPOSITORY_URL = "https://github.com/LuckyJoeshp/evidence-first-agent"


def read_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class RepositoryContractTest(unittest.TestCase):
    def test_plugin_identity_is_consistent(self):
        codex = read_json(".codex-plugin/plugin.json")
        claude = read_json(".claude-plugin/plugin.json")
        gemini = read_json("gemini-extension.json")
        antigravity = read_json("plugin.json")

        for manifest in (codex, claude, gemini, antigravity):
            self.assertEqual(PLUGIN_NAME, manifest["name"])
        for manifest in (codex, claude, gemini):
            self.assertEqual(VERSION, manifest["version"])
        self.assertEqual(REPOSITORY_URL, codex["repository"])

    def test_codex_plugin_is_instructions_only(self):
        manifest = read_json(".codex-plugin/plugin.json")

        self.assertEqual(["Instructions"], manifest["interface"]["capabilities"])
        self.assertNotIn("apps", manifest)
        self.assertNotIn("mcpServers", manifest)
        self.assertNotIn("hooks", manifest)

    def test_marketplace_pins_the_release(self):
        marketplace = read_json(".agents/plugins/marketplace.json")
        entry = marketplace["plugins"][0]

        self.assertEqual(MARKETPLACE_NAME, marketplace["name"])
        self.assertEqual(PLUGIN_NAME, entry["name"])
        self.assertEqual(f"{REPOSITORY_URL}.git", entry["source"]["url"])
        self.assertEqual(f"v{VERSION}", entry["source"]["ref"])
        self.assertEqual("AVAILABLE", entry["policy"]["installation"])
        self.assertEqual("ON_INSTALL", entry["policy"]["authentication"])

    def test_claude_marketplace_identity_is_consistent(self):
        marketplace = read_json(".claude-plugin/marketplace.json")

        self.assertEqual(MARKETPLACE_NAME, marketplace["name"])
        self.assertEqual(PLUGIN_NAME, marketplace["plugins"][0]["name"])

    def test_cursor_copy_matches_canonical_skill(self):
        canonical = (ROOT / "skills/evidence-first/SKILL.md").read_bytes()
        cursor = (ROOT / ".cursor/skills/evidence-first/SKILL.md").read_bytes()

        self.assertEqual(canonical, cursor)

    def test_skill_keeps_the_evidence_first_contract(self):
        skill = (ROOT / "skills/evidence-first/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Never trade\nevidence integrity for a shorter answer", skill)
        self.assertIn("Do not impose an arbitrary item or list limit", skill)
        self.assertIn("Do not turn an agent-owned", skill)
        self.assertIn("Never manufacture precision", skill)
        self.assertNotIn("Dopamine", skill)
        self.assertNotIn("Cap lists at 5", skill)

    def test_codex_invocation_is_explicit(self):
        config = (ROOT / "skills/evidence-first/agents/openai.yaml").read_text(
            encoding="utf-8"
        )

        self.assertIn('default_prompt: "Use $evidence-first', config)
        self.assertIn("allow_implicit_invocation: false", config)

    def test_gemini_command_is_valid_toml(self):
        with (ROOT / "skills/evidence-first/agents/gemini.toml").open("rb") as source:
            command = tomllib.load(source)

        self.assertIn("evidence-first", command["description"].lower())
        self.assertIn("decision-critical", command["prompt"])

    def test_readme_does_not_claim_unpublished_effectiveness(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("No paired model benchmark is published yet", readme)
        self.assertIn("not", readme[readme.index("Passing these unit tests") :].splitlines()[0])


if __name__ == "__main__":
    unittest.main()
