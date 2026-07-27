# Documentation Writer Agent

为 Python 模块生成全面的文档：README、API 参考和 Google 风格的文档字符串。

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
# 生成 README + 文档字符串
python agent.py --file my_module.py

# 仅生成 README
python agent.py --file utils.py --format readme

# 仅添加文档字符串
python agent.py --file api.py --format docstrings
```

## 输出内容

### README 生成
- 模块标题和一行描述
- 功能列表（项目符号）
- 安装部分
- 快速入门及可运行的代码示例
- API 参考（每个公共函数/类包含参数、返回类型、示例）
- 配置（如有环境变量）
- 错误处理部分

### 文档字符串生成
- Google 风格文档字符串
- 参数描述（Args）
- 返回值描述（Returns）
- 异常描述（Raises）
- 代码示例（Example）

## 示例代码

如果不提供 `--file` 或 `--code` 参数，程序会使用内置的示例验证模块（`validators.py`），包含：
- `validate_email`: 邮箱验证
- `hash_password`: 密码哈希
- `parse_date`: 日期解析
- `UserValidator`: 用户验证器类