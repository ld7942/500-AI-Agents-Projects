# Web Research Agent

一个使用 LangGraph 的 Agent，通过网络搜索任何主题并综合生成结构化研究报告。

**框架**: LangGraph  
**LLM**: Gemma 4（本地运行）  
**搜索**: DuckDuckGo Search

## 功能

1. 接收研究查询
2. 使用 DuckDuckGo 搜索网页
3. 将搜索结果综合成结构化报告（摘要、关键发现、来源）

## 环境设置

```bash
pip install -r requirements.txt
```

**本地 LLM 设置**:
- 确保 Ollama 服务运行中：`ollama serve`
- 拉取模型：`ollama pull gemma4`
- 服务地址：`http://localhost:11434/v1`

**替代方案**: 如需使用 OpenAI API，请修改 `agent.py` 中的 LLM 配置。

## 运行

```bash
# 默认查询
python agent.py

# 自定义查询
python agent.py --query "量子计算最新进展"
```

## 示例输出

```
🔍 研究: 2026年前沿的AI Agent 项目

============================================================
📄 研究报告
============================================================
## 摘要
2026年，AI Agent 领域取得了显著进展，在推理能力、工具使用和多Agent协作方面有重大改进...

## 关键发现
- LangGraph 和 CrewAI 已成为生产级 Agent 的领先框架
- 开源模型如 Gemma 4 实现了本地部署的高性能 Agent
- ...

## 来源
- https://...
```

## 架构

```
用户查询 → [搜索节点] → DuckDuckGo 搜索 → [综合节点] → Gemma 4 → 报告
```