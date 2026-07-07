# PDF Q&A Agent

加载任意 PDF 文件并允许您就其内容提问。支持单问题和交互式聊天两种模式。

**框架**: LlamaIndex  
**LLM**: Gemma 4（本地运行）  
**Embedding**: Ollama Embedding (embeddinggemma)

## 环境设置

```bash
pip install -r requirements.txt
```

**本地 LLM 设置**:
- 确保 Ollama 服务运行中：`ollama serve`
- 拉取模型：`ollama pull gemma4`
- 拉取嵌入模型：`ollama pull embeddinggemma`
- 服务地址：`http://localhost:11434`

## 运行

```bash
# 交互式问答（推荐）
python agent.py --pdf your_document.pdf

# 单问题模式
python agent.py --pdf research_paper.pdf --question "使用了什么方法论？"
```

## 使用场景

- 研究论文分析
- 合同审查
- 财务报告问答
- 技术文档聊天

## 功能特点

- ✅ 支持交互式聊天，保持对话历史
- ✅ 支持单问题快速查询
- ✅ 使用向量索引进行高效检索
- ✅ 显示引用的文档片段数量