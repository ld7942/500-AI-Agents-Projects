# Email Drafting Agent

一个使用 CrewAI 的双 Agent 系统，用于起草专业邮件。分析员 Agent 提取需求，然后作者 Agent 生成最终邮件。

**框架**: CrewAI  
**LLM**: Gemma 4（本地运行）

## 环境设置

```bash
pip install -r requirements.txt
```

**本地 LLM 设置**:
- 确保 Ollama 服务运行中：`ollama serve`
- 拉取模型：`ollama pull gemma4`
- 设置环境变量：`OLLAMA_BASE_URL=http://localhost:11434`

## 运行

```bash
# 默认示例
python agent.py

# 自定义邮件
python agent.py \
  --context "为软件项目延迟交付道歉" \
  --tone "apologetic but confident" \
  --recipient "客户项目经理"
```

## 架构

```
上下文 → [分析员 Agent] → 邮件摘要 → [作者 Agent] → 最终邮件
```

## 功能特点

- ✅ 双 Agent 协作：分析员理解需求，作者撰写邮件
- ✅ 支持自定义上下文、语气和接收人
- ✅ 自动提取关键点和主题行建议
- ✅ 输出专业格式的完整邮件