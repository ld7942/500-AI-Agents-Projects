# Recipe Recommendation Agent

根据可用食材、饮食限制和时间约束，推荐 3 个食谱，包含完整的烹饪步骤、营养信息和厨师提示。

**Framework**: LangChain  
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
# 使用默认食材（鸡胸肉、葱、柠檬等）
python agent.py

# 指定食材
python agent.py --ingredients "鸡胸肉, 大蒜, 柠檬, 迷迭香"

# 指定食材、饮食限制和时间
python agent.py --ingredients "豆腐, 西兰花, 酱油" --diet vegan --time 20

# 指定份量
python agent.py --ingredients "意大利面, 番茄, 罗勒, 帕玛森芝士" --servings 4
```

## 输出内容

每个食谱包含：
- 🍽️ 食谱名称和美食类型
- ⏱️ 准备时间和烹饪时间
- 📝 食材清单（含数量）
- 👨‍🍳 详细烹饪步骤
- 🥗 营养信息（卡路里、蛋白质、碳水化合物、脂肪）
- 💡 厨师提示

## 参数说明

- `--ingredients`: 可用食材，逗号分隔（默认：鸡胸肉, 葱, 柠檬, 油, 草莓, 土豆）
- `--diet`: 饮食限制（如 vegan, vegetarian, gluten-free）
- `--time`: 最大总时间（分钟）
- `--servings`: 需要的份量（默认：2）