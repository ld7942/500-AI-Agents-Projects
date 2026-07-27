# Travel Planner Agent

三智能体 CrewAI 系统，创建个性化旅行行程，包含目的地研究、每日计划和预算分解。

**Framework**: CrewAI  
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
# 使用默认目的地（北京，7天，预算$3000）
python agent.py

# 指定目的地、天数和预算
python agent.py --destination "东京, 日本" --days 7 --budget 3000

# 指定兴趣爱好
python agent.py --destination "巴黎, 法国" --days 5 --budget 5000 --interests "艺术, 葡萄酒, 建筑"
```

## 工作流程

```
目的地 → [目的地研究员] → [活动计划员] → [预算分析师] → 行程计划
```

1. **目的地研究员**: 收集目的地信息，提供旅行洞察
2. **活动计划员**: 创建详细的每日行程
3. **预算分析师**: 根据预算估算行程成本