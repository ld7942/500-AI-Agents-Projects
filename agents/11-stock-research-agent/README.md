# Stock Research Agent

通过 Yahoo Finance 获取实时股票数据，并生成 AI 驱动的投资分析。

**Framework**: LangChain  
**LLM**: Gemma 4 (via Ollama)  
**Data**: Yahoo Finance（免费，无需 API key）

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
python agent.py --ticker AAPL
python agent.py --ticker NVDA
python agent.py --ticker TSLA
```

## 输出

实时基本面数据 + AI 分析，涵盖：
- 投资假设
- 关键优势（3个点）
- 关键风险（3个点）
- 估值评估
- 判断（购买/持有/卖出）