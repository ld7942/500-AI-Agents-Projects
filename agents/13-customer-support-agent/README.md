# Customer Support Agent

基于 LangGraph 和 RAG 的客户支持智能体，利用知识库（产品文档）处理客户查询，并将复杂问题路由至人工升级处理。

**Framework**: LangGraph + FAISS  
**LLM**: Gemma 4 (via Ollama)

## Setup

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 Ollama

确保已安装 Ollama 并运行：

```bash
# 拉取 Gemma 4 模型
ollama pull gemma4:e4b

# 启动 Ollama 服务（默认端口 11434）
ollama serve
```

## Run

```bash
# 使用内置示例知识库
python agent.py

# 使用自定义知识库目录（包含 .txt/.md 文件）
python agent.py --kb-dir docs/
```

## 功能特性

- ✅ RAG 知识库问答
- ✅ 敏感问题自动升级检测（账单争议、数据丢失等）
- ✅ 保持对话历史
- ✅ 支持自定义知识库文档

## 知识库格式

将产品文档（.txt 或 .md 文件）放入知识库目录，智能体会自动加载并创建向量索引。

## 升级关键词

当用户输入包含以下关键词时，智能体会自动将问题升级：
- 退款、诉讼、愤怒、欺诈、损坏、数据丢失、取消订阅、收费、计费错误