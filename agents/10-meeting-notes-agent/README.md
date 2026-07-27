# Meeting Notes Agent

将会议记录转换为结构化的会议纪要，包含摘要、操作项、决策和跟进项。

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
# 使用内置示例会议记录
python agent.py

# 使用自己的会议记录文件
python agent.py --transcript meeting_transcript.txt

# 直接输入文本
python agent.py --text "Alice: Let's ship by Friday. Bob: I need 2 more days for testing..."

# 自定义输出路径
python agent.py --transcript meeting_transcript.txt --output sprint_notes.md
```

## 输出

默认保存到 `会议纪要.md`。如果文件已存在，会保存为带时间戳的文件。输出内容包括：
- 执行摘要
- 关键决策
- 带负责人和截止日期的操作项
- 阻碍项
- 下次会议时间