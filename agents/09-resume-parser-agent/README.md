# Resume Parser Agent

解析简历（TXT 或 PDF）为结构化 JSON，并可选地根据岗位描述对候选人进行匹配评分。

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
# 仅解析（使用内置示例简历）
python agent.py

# 解析您的简历
python agent.py --resume path/to/resume.pdf

# 解析 + 岗位匹配评分
python agent.py --resume resume.pdf --job-desc "高级Python工程师，具有K8s经验..."
```

## 输出内容

- **结构化信息**: 姓名、邮箱、电话、技能、工作经验、教育背景等
- **候选人摘要**: 2-3 句专业总结
- **匹配分数**: 0-100 分的岗位匹配度
- **招聘建议**: Hire | Consider | Pass

## 支持的文件格式

- **.txt**: 纯文本简历
- **.pdf**: PDF 格式简历（需要 pypdf 库）

## 示例简历

如果不提供 `--resume` 参数，程序会使用内置的示例简历进行演示，包含：
- 姓名、联系方式
- 专业摘要
- 工作经验（Senior Software Engineer, Software Engineer）
- 技能（Python, JavaScript, FastAPI, Django, Kubernetes 等）
- 教育背景
- 认证证书