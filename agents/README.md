# Agents — Working Implementations

每个文件夹都是一个独立的、可运行的 AI 智能体。无需复杂的仓库设置。

## Quick Start

```bash
cd agents/<agent-name>
pip install -r requirements.txt
python agent.py   # 需要本地 Ollama 运行 gemma4:e4b 模型
```

## Agent Index

| # | Agent | Framework | LLM | Industry | Difficulty |
|---|---|---|---|---|---|
| 01 | [Web Research Agent](01-web-research-agent/) | LangGraph | Gemma 4 (Ollama) | General | ⭐⭐ |
| 02 | [Code Review Agent](02-code-review-agent/) | LangChain | Gemma 4 (Ollama) | Software Dev | ⭐ |
| 03 | [PDF Q&A Agent](03-pdf-qa-agent/) | LlamaIndex | Gemma 4 (Ollama) | Research | ⭐ |
| 04 | [SQL Query Agent](04-sql-query-agent/) | LangChain | Gemma 4 (Ollama) | Data | ⭐⭐ |
| 05 | [Email Drafting Agent](05-email-drafting-agent/) | CrewAI | Gemma 4 (Ollama) | Communication | ⭐ |
| 06 | [News Summarizer Agent](06-news-summarizer-agent/) | LangChain | Gemma 4 (Ollama) | Media | ⭐ |
| 07 | [GitHub Issue Triager](07-github-issue-triager/) | LangChain | Gemma 4 (Ollama) | DevOps | ⭐⭐ |
| 08 | [Data Analysis Agent](08-data-analysis-agent/) | LangChain | Gemma 4 (Ollama) | Analytics | ⭐⭐ |
| 09 | [Resume Parser Agent](09-resume-parser-agent/) | LangChain | Gemma 4 (Ollama) | HR | ⭐ |
| 10 | [Meeting Notes Agent](10-meeting-notes-agent/) | LangChain | Gemma 4 (Ollama) | Productivity | ⭐ |
| 11 | [Stock Research Agent](11-stock-research-agent/) | LangChain | Gemma 4 (Ollama) | Finance | ⭐⭐ |
| 12 | [Travel Planner Agent](12-travel-planner-agent/) | CrewAI | Gemma 4 (Ollama) | Travel | ⭐⭐ |
| 13 | [Customer Support Agent](13-customer-support-agent/) | LangGraph | Gemma 4 (Ollama) | Customer Service | ⭐⭐⭐ |
| 14 | [Social Media Content Agent](14-social-media-agent/) | CrewAI | Gemma 4 (Ollama) | Marketing | ⭐ |
| 15 | [Unit Test Generator Agent](15-unit-test-generator/) | LangChain | Gemma 4 (Ollama) | Software Dev | ⭐⭐ |
| 16 | [Documentation Writer Agent](16-documentation-writer/) | LangChain | Gemma 4 (Ollama) | Software Dev | ⭐⭐ |
| 17 | [Recipe Recommendation Agent](17-recipe-agent/) | LangChain | Gemma 4 (Ollama) | Food | ⭐ |
| 18 | [Job Application Agent](18-job-application-agent/) | CrewAI | Gemma 4 (Ollama) | HR | ⭐⭐ |
| 19 | [Competitive Analysis Agent](19-competitive-analysis-agent/) | LangGraph | Gemma 4 (Ollama) | Business | ⭐⭐⭐ |
| 20 | [Multi-Agent Debate System](20-multi-agent-debate/) | LangChain | Gemma 4 (Ollama) | Research | ⭐⭐⭐ |

## Requirements

所有智能体都需要：
- Python 3.10+
- [Ollama](https://ollama.com/) 运行本地模型
- `gemma4:e4b` 模型（运行 `ollama pull gemma4:e4b`）

## Adding Your Agent

1. 创建文件夹：`agents/NN-your-agent-name/`
2. 包含文件：`agent.py`, `requirements.txt`, `README.md`, `metadata.yaml`
3. 按照 [PR 模板](../.github/PULL_REQUEST_TEMPLATE.md) 创建 PR
