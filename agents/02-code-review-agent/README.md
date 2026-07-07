# 代码审查 Agent

一个 AI Agent，用于审查代码中的 Bug、安全问题、性能问题和代码风格违规。

**框架**: LangChain  
**LLM**: Gemma 4（本地运行）

## 环境设置

```bash
pip install -r requirements.txt
```

**本地 LLM 设置**:
- 确保 Ollama 服务运行中：`ollama serve`
- 拉取模型：`ollama pull gemma4`
- 服务地址：`http://localhost:11434/v1`

## 运行

```bash
# 审查文件（默认审查 01-web-research-agent/agent.py）
python agent.py

# 审查指定文件
python agent.py --file path/to/your/code.py

# 审查内联代码
python agent.py --code "def divide(a, b): return a / b"

# 审查非 Python 代码
python agent.py --file app.js --language javascript
```

## 示例输出

```
🔍 审查： agents/01-web-research-agent/agent.py

============================================================
📋 代码审查报告
============================================================
## 总体评价：🟡 需要改进

### 1. Bug 与正确性
- `divide(a, b)` 缺少除零检查 → `b=0` 时会引发 `ZeroDivisionError`

### 2. 安全问题
- 对外部参数没有输入验证

### 3. 性能
- 未发现明显性能问题

### 4. 代码风格
- 缺少类型提示

### 5. 改进建议
- 添加类型提示：`def divide(a: float, b: float) -> float`
- 当 `b == 0` 时抛出带描述性消息的 `ValueError`
```