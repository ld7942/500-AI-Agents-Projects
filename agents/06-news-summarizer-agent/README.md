# News Summarizer Agent

从微博获取热门新闻并生成结构化的新闻摘要，包含主要新闻、关键主题、关注要点和快速新闻列表。

**Framework**: LangChain  
**LLM**: Gemma 4 (via Ollama)  
**Data**: 微博热搜 API

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
python agent.py
```

程序会自动从微博获取热门新闻并生成结构化摘要。

## 输出格式

新闻摘要包含以下内容：
1. **主要新闻** (Top Story)
2. **主要主题** (Key Themes) - 3个要点
3. **关注要点** (What to Watch)
4. **快速新闻列表** (Quick Headlines)