# 学习路线与阶段验收

更新：2026-10-26。九阶段均未验收；02 有历史探索脚本。先确认 01 基础，再执行 [API 基线](exec-plans/active/001-api-baseline.md)。按能力推进，不预设周数。

| 阶段 | 实践与功能验收 | 学习验收 |
| --- | --- | --- |
| [01 Python](../labs/01_python/README.md) | 函数、类型、异常、环境变量、JSON、模块与异步；离线示例可运行 | 独立修改函数，解释异常和同步/异步 |
| [02 LLM API](../labs/02_llm_api/README.md) | SDK、消息、流式、结构化输出、用量；覆盖缺配置与超时 | 解释端点、模型、token，独立改配置 |
| [03 Function Calling](../labs/03_function_calling/README.md) | 手写 schema、校验、分发与结果回传循环；验证未知工具与步数上限 | 区分模型请求与程序执行 |
| [04 LangChain](../labs/04_langchain/README.md) | 框架组件重建调用和工具链，与原生实现对照 | 解释抽象边界及适用条件 |
| [05 LangGraph](../labs/05_langgraph/README.md) | 状态、节点、条件边、检查点与人工介入；验证失败恢复 | 画状态图并独立添加分支 |
| [06 RAG](../labs/06_rag/README.md) | 摄取、切块、embedding、检索、引用与拒答；建立固定题集 | 区分检索/生成错误，对比切块参数 |
| [07 MCP](../labs/07_mcp/README.md) | 本地客户端发现并调用服务端工具，验证错误路径 | 解释协议、传输与 Function Calling 的分工 |
| [08 FastAPI](../labs/08_fastapi/README.md) | HTTP、校验、流式与生命周期；健康检查及成功/错误接口测试 | 解释异步阻塞、状态码与资源清理 |
| [09 Docker](../labs/09_docker/README.md) | 构建、运行服务；验证健康检查、停止与重启 | 解释镜像、容器、端口、卷与配置 |

综合实践：问题 → 工作流 → 检索或工具 → 带来源的答案 → HTTP 返回；通过 MCP 接入受限工具，Docker 复现运行。
状态：未开始 → 进行中 → 待学习验收 → 已完成。功能证据与学习证据齐备才能完成。跳阶段须记录已有能力和补课项。
