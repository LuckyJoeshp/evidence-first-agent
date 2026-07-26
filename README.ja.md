# Evidence First

結論を先に示しながら、重要な証拠を失わないための Agent Skill です。

[English](README.md) · [简体中文](README.zh-CN.md) ·
[MIT License](LICENSE)

`evidence-first` は、回答・検証済みの状態・実際のブロッカーを最初の画面で
見つけやすくしつつ、技術判断や研究判断を変え得る情報を保持します。

短さそのものを目的にはしません。証拠が多い場合は、要約の下に詳細を置く、
表にする、または成果物へリンクします。重要情報を黙って削除しません。

## インストール

### Codex

```bash
codex plugin marketplace add LuckyJoeshp/evidence-first-agent --ref main
codex plugin add evidence-first@evidence-first-agent
```

`$evidence-first` で明示的に呼び出します。無関係な作業へ出力スタイルが
持ち越されないよう、暗黙の呼び出しは既定で無効です。

### Claude Code

```bash
claude plugin marketplace add LuckyJoeshp/evidence-first-agent
claude plugin install evidence-first@evidence-first-agent
```

次に `/evidence-first` と入力します。その他の Agent、更新、削除、手動
インストールについては [INSTALL.md](INSTALL.md) を参照してください。

## 優先順位

競合する規則は次の順で解決します。

1. system、harness、ユーザーの明示的な要件
2. 正確性、安全性、証拠の完全性
3. Agent による作業の完遂
4. 実行しやすさと読みやすさ
5. 簡潔さと文体

要件、制約、反証、不確実性、失敗、スキップ、未実行の検査、リスク、
ロールバック、引用、成果物、監査識別子を保持します。項目数の上限、
不要なユーザー作業、作り物の次の手順、根拠のない分単位の見積もりは
設けません。

完全な規約は [SKILL.md](skills/evidence-first/SKILL.md) にあります。

## 上流プロジェクトとの関係

本プロジェクトは
[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) の fork です。
回答を先に示し、進捗を見える形にする考え方を引き継ぎ、証拠を多く扱う
Agent 作業向けに契約を変更しました。上流の著作権と MIT 条項は
[LICENSE](LICENSE) に保持されています。

## 評価状況

リポジトリには、証拠の欠落を検出する paired evaluation と単体テストが
含まれます。単体テストの成功は評価基盤を検証するだけで、Skill の実運用上の
効果を証明しません。現在、paired model benchmark は未公開です。

## License

MIT.
