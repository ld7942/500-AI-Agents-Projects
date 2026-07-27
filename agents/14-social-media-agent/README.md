# Social Media Content Agent

根据主题或文章 URL 生成平台优化的社交媒体帖子。

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
# 使用默认主题（2026 年度产品发布）
python agent.py

# 指定主题
python agent.py --topic "远程工作的未来"

# 指定主题和品牌
python agent.py --topic "新品发布" --brand "小米"

# 指定平台（默认：微博,小红书,抖音）
python agent.py --topic "产品发布" --platforms "微博,小红书"
```

## 工作流程

```
主题 → [社交媒体策略师] → [社交媒体文案作者] → 生成内容
```

1. **社交媒体策略师**: 分析主题，定义每个平台的关键消息、目标受众和语气
2. **社交媒体文案作者**: 根据策略生成符合平台要求的社交媒体帖子

## 支持平台

- **微博**: 2条微博 + 线程开头
- **小红书**: 2条帖子 + 情感钩子
- **抖音**: 2条视频 + 15 #标签