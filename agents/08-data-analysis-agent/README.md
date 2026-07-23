# Data Analysis Agent

使用自然语言与数据对话。加载任何 CSV 或 Excel 文件，并使用自然语言提出分析问题。智能体会生成 Python/pandas 代码来回答问题。

**Framework**: LangChain (Pandas Agent)  
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
# 演示模式 — 自动创建示例销售数据
python agent.py --allow-dangerous-code

# 使用自己的数据
python agent.py --file your_data.csv --allow-dangerous-code

# 单个问题
python agent.py --file sales.csv --question "每月销售额趋势是多少？" --allow-dangerous-code
```

## 安全说明

此演示使用 LangChain 的 pandas 智能体，它会执行模型生成的 Python 代码。仅在受信任的提示和非敏感数据上使用 `--allow-dangerous-code`。

## 示例问题

- "每个产品的总销售额是多少？"
- "哪个区域的平均订单价值最高？"
- "显示销售量最高的5天"
- "销量和收入之间的相关性是什么？"

## 示例数据

首次运行时会自动创建 `sample_data.csv`，包含以下字段：
- **date**: 日期
- **product**: 产品（笔记本、手机、平板、显示器、键盘）
- **region**: 区域（北美、南部、东美、西美）
- **quantity**: 数量
- **unit_price**: 单价
- **revenue**: 收入