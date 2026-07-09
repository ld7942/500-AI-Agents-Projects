# SQL Query Agent

连接到任意 SQLite 数据库，通过生成和执行 SQL 来回答自然语言问题。

**框架**: LangChain  
**LLM**: Gemma 4（本地运行）

## 环境设置

```bash
pip install -r requirements.txt
```

**本地 LLM 设置**:
- 确保 Ollama 服务运行中：`ollama serve`
- 拉取模型：`ollama pull gemma4`
- 服务地址：`http://localhost:11434/v1`

## 运行

```bash
# 演示模式 — 自动创建示例电商数据库
python agent.py

# 使用自己的数据库
python agent.py --db path/to/your/database.sqlite

# 单问题模式
python agent.py --db demo.sqlite --question "每个国家的总收入是多少？"
```

数据库默认以只读模式打开。使用 `--allow-write` 可将 SQLite 连接切换为读写模式，允许生成的 SQL Agent 修改数据。

## 示例问题

- "我们每个国家有多少客户？"
- "销量前三的产品是什么？"
- "上个月的总收入是多少？"
- "哪个客户消费最多？"

## 架构

```
自然语言 → LLM（生成 SQL）→ SQLite → LLM（格式化答案）→ 响应
```

## 功能特点

- ✅ 自动创建演示数据库（demo.sqlite）
- ✅ 支持交互式问答
- ✅ 支持单问题快速查询
- ✅ 默认只读模式，保障数据安全
- ✅ 显示可用表名