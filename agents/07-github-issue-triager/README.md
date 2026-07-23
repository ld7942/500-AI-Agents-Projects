# GitHub Issue Triager

自动分类 GitHub 问题：分配严重性、类别、标签和路由建议。

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
# 从 GitHub URL 获取问题
python agent.py --issue-url https://github.com/owner/repo/issues/123

# 直接输入标题和内容
python agent.py --title "App crashes on login" --body "Steps: 1. Open app 2. Click login 3. App crashes"
```

**注意**: 如果 GitHub API 请求失败，程序会自动使用示例数据 `example_github_api.json`。

## Output

```
🔴 Severity: CRITICAL (Priority: 9/10)
📁 Category: bug
👤 Assignee: backend team
🏷️  Labels: bug, critical, authentication
📝 Summary: Authentication crash affecting all users on login
```

## 输出字段

- **severity**: critical | high | medium | low
- **category**: bug | feature | documentation | question | performance | security
- **priority_score**: 1-10
- **labels**: 建议的标签列表
- **summary**: 一句话摘要
- **reproduction_clear**: 复现步骤是否清晰
- **assignee_type**: 建议分配给的团队类型
- **needs_more_info**: 是否需要更多信息
- **triage_notes**: 分类员备注