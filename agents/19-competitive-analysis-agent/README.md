# Competitive Analysis Agent

LangGraph 多步骤智能体，识别竞争对手、分析每个竞争对手的优势/劣势，并生成战略竞争分析报告。

**Framework**: LangGraph  
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
# 使用默认公司和行业
python agent.py

# 指定公司和行业
python agent.py --company "Notion" --industry "生产效率和协作软件"
python agent.py --company "Stripe" --industry "支付处理"
python agent.py --company "Figma" --industry "设计工具"
```

## 输出内容

- 📊 **执行摘要**: 3 个句子总结
- 📋 **竞争格局表格**: 公司、优势、劣势、价格
- 🎯 **市场差距和机会**: 3 个要点
- 💡 **战略建议**: 5 个操作项
- ⚠️ **风险评估**: 每个竞争对手的风险等级（High/Medium/Low）

## 工作流程

```
输入 → [识别竞争对手] → [分析每个竞争对手] → [生成报告] → 输出
```

1. **识别竞争对手**: 列出 5 个主要竞争对手
2. **分析竞争对手**: 对每个竞争对手进行 100 字左右的分析（产品、优势、劣势、定价、目标市场）
3. **生成报告**: 整合分析结果，创建完整的竞争分析报告