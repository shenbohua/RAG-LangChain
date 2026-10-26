# Agent 核心技术栈学习项目

主线：Python → LLM API → Function Calling → LangChain → LangGraph → RAG → MCP → FastAPI → Docker。
目标：构建可部署的知识助手，并能独立解释、修改和调试。

## 阅读入口

- [协作规则](AGENTS.md)与[架构地图](ARCHITECTURE.md)
- [学习路线与验收](docs/PLANS.md)
- [教学方式](docs/LEARNING.md)与[文档导航](docs/index.md)
- [下一步：API 基线](docs/exec-plans/active/001-api-baseline.md)

## 当前状态

2026-10-26：已有 [API 探索脚本](labs/02_llm_api/api_smoke.py)，使用 OpenAI SDK 调用 DashScope 兼容接口；从根目录 test.py 迁移并保留原有内容。真实调用、依赖环境、测试及部署均未验证。

## 目录与检查

labs 存放九阶段实验；src/agent_learning 为共享代码预留；tests 为离线测试预留；evals 记录质量评估；docs 保存规范与计划；scripts 提供维护检查。预留目录只有说明，不代表功能完成。

运行 `python scripts/check_docs.py` 检查本地文档，无第三方依赖或网络。
api_smoke.py 是手动联网实验，导入也可能触发付费请求，不属于自动测试。应用安装和启动命令待基线验证后补齐。不提交密钥、私人语料与敏感日志。

方法来源见[参考与适配](docs/references/harness-engineering.md)。
