# Multi-Agent Debate System

两个 AI 智能体从对立的角度就任何主题进行辩论，由中立的 AI 裁判宣布获胜者并综合关键论点。

**Framework**: LangChain (multi-agent)  
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
# 使用默认主题
python agent.py

# 指定辩论主题
python agent.py --topic "AI 将消除更多工作岗位"

# 指定主题和轮数
python agent.py --topic "远程工作比办公室工作更好" --rounds 3
python agent.py --topic "加密货币将取代法定货币" --rounds 2
```

## 架构

```
主题 → [正方智能体] ↔ [反方智能体] (N 轮) → [裁判智能体] → 判决
```

### 智能体角色

| 角色 | 名称 | 专业领域 |
|------|------|----------|
| 🟢 正方 | Dr. Alex Chen | 技术经济学家和 AI 研究员 |
| 🔴 反方 | Prof. Sarah Martinez | 劳动经济学家和社会政策专家 |
| 🏛️ 裁判 | Judge | 辩论评估员 |

## 输出内容

- 📢 **辩论过程**: 每轮双方的论点
- 🎯 **判决**: 获胜者、每方分数（10分制）、最强论点、关键洞察力、平衡的综合结论

## 参数说明

- `--topic`: 辩论主题（默认："AI 将创建更多工作岗位而不是消除工作岗位"）
- `--rounds`: 辩论轮数（1-4，默认：2）