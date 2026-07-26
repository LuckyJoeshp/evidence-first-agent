# Evidence First

让结果先出现，但不牺牲关键证据。

[English](README.md) · [日本語](README.ja.md) ·
[MIT 许可证](LICENSE)

`evidence-first` 是面向编程 agent 的输出整形 skill。它让答案、已验证状态或
真实阻塞点在首屏可见，同时保留所有可能改变技术或研究决策的事实。

它不是“越短越好”的 skill。证据很多时应当分层、制表或链接到制品，而不是
静默删除。

## 安装

### Codex

```bash
codex plugin marketplace add LuckyJoeshp/evidence-first-agent --ref main
codex plugin add evidence-first@evidence-first-agent
```

安装后新开一个 thread。对于遗漏证据可能改变判断的复杂技术或研究任务，
Codex 会自动选择这个 skill；琐碎修改、简单事实问题、日常对话和开放式
brainstorming 保持普通模式。

仍可为单个任务强制调用：

```text
$evidence-first
```

自动选择只作用于当前任务，不是全局常驻。说 `normal mode` 或
`stop evidence-first mode` 可在当前任务停用。

### Claude Code

```bash
claude plugin marketplace add LuckyJoeshp/evidence-first-agent
claude plugin install evidence-first@evidence-first-agent
```

然后输入 `/evidence-first`。

其他 agent、更新、卸载、手动安装及 Claude Code 可选常驻模式见
[INSTALL.md](INSTALL.md)。

## 核心契约

规则冲突时按以下顺序处理：

1. system、harness 与用户明确要求
2. 正确性、安全性与证据完整性
3. agent 自主执行与任务完成
4. 可操作性与可扫描性
5. 简洁和风格

必须保留：

- 需求、约束和验收条件
- 观测事实，以及分开标注的推断和假设
- 支持证据与实质性反证
- 不确定性、局限、样本边界和决策边界
- 通过、失败、跳过、不可用及未运行的检查
- 风险、回滚点、引用、制品路径和审计标识

不存在“五项上限”，也不强制制造用户作业、下一步或没有校准依据的分钟估时。

完整契约见 [SKILL.md](skills/evidence-first/SKILL.md)。

## 前后对比

### 修改前

> 发布基本准备好了。格式、类型检查和单元测试都不错。还有几个认证集成问题，
> 后续也应该跑完剩余测试并验证回滚。

### Evidence First

> **发布阻塞。**
>
> | 检查 | 结果 |
> | --- | --- |
> | 格式检查 | 通过 |
> | 类型检查 | 通过 |
> | 单元测试 | 812 项通过 |
> | 集成测试 | 3 项认证失败 |
> | 端到端测试 | 因集成失败而未运行 |
> | 数据库迁移 dry-run | 通过 |
> | 回滚恢复 | 未测试 |
>
> 剩余风险：认证失败阻止发布，回滚可恢复性仍未验证。下一动作归 agent：
> 先诊断三项认证失败，再运行被阻塞的检查。

第二种输出更容易阅读，但没有把“未运行”包装成绿灯。

## 相比上游的变化

本项目 fork 自
[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)，保留其“答案优先”
和“进度可见”的优点。

本 fork 面向证据密集型 agent 工作重新定义了契约：

- 用渐进披露替代硬性压缩
- 让证据完整性高于风格
- agent 能完成的工作继续由 agent 完成
- 移除列表上限、强制结束语、强制下一步和强制估时
- 移除医学化表述，默认不跨无关话题持续
- 允许 Codex 按任务自动选择，并设置明确的反向触发边界
- 在评测中加入证据遗漏和证据角色混淆闸门

上游版权与 MIT 条款继续保留在 [LICENSE](LICENSE)。

## 评测状态

仓库包含成对 baseline/candidate runner、盲评评分和专门捕捉证据遗漏的案例。

```bash
python3 scripts/run_evals.py validate
python3 -m unittest discover -s tests -v
```

这些测试通过只能证明评测工具能工作，**不能证明 skill 已提升真实任务表现**。
当前尚未发布成对模型基准。未来任何效果声明都必须同时公开响应、模型与 CLI
版本、trial 数、rubric 和盲评分数，详见
[evals/README.md](evals/README.md)。

## 安全

Codex 插件仅声明 instruction skill，不添加 MCP、网络服务或项目写入能力。
评测 runner 只有维护者手动运行时才会启动配置的模型 CLI。

marketplace 中的可安装插件固定到 `v1.1.0` release tag；marketplace 目录本身
从 `main` 获取。

## 许可证

MIT。
