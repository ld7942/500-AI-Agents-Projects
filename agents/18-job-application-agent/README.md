# Job Application Agent

CrewAI 智能体，根据工作描述和候选人简历生成完整的工作申请材料包：求职信、定制化简历要点、面试准备问题和薪资范围建议。

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
# 使用内置示例数据
python agent.py

# 使用自己的工作描述和候选人信息
python agent.py \
  --job-desc "$(cat job_posting.txt)" \
  --candidate "$(cat my_profile.txt)"
```

## 输出内容

- 📄 **求职信**: 250-300 字，包含 hook、evidence、close 三个段落
- 🏷️ **简历要点**: 突出显示的前 5 个关键技能和成就
- 🎤 **面试问题**: 10 个面试问题（5 个行为问题 + 5 个技术问题），每个问题都有建议的答案框架
- 💰 **薪资范围建议**: 薪资谈判范围

## 工作流程

```
工作描述 → [需求分析员] → [申请材料编写员] → 申请材料包
```

1. **需求分析员**: 分析工作描述，提取关键技能、文化信号和公司价值观
2. **申请材料编写员**: 根据分析结果和候选人简历，创建定制化的申请材料

## 示例数据

程序内置了示例数据：
- **工作描述**: Stripe 高级 Python 工程师
- **候选人**: Jane Doe，7年Python开发经验，熟悉 FastAPI、Django、PostgreSQL、Redis、Kubernetes 等