# Unit Test Generator Agent

分析 Python 代码并生成全面的 pytest 测试套件，涵盖正常路径、边界情况和错误条件。

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
# 为 Python 文件生成测试
python agent.py --file my_module.py

# 为内联代码生成测试
python agent.py --code "def divide(a, b): return a / b"

# 指定输出文件
python agent.py --file utils.py --output tests/test_utils.py
```

## 示例

输入：`shopping_cart.py`（包含 `add_item`, `remove_item`, `total` 方法）
输出：`test_shopping.py`（包含 20+ 个 pytest 测试，使用 fixtures、parametrize 和 mocking）

## 测试覆盖

生成的测试套件包含：
- ✅ 正常路径测试（预期的正常输入）
- ✅ 边界情况测试（边界值、空输入）
- ✅ 错误条件测试（无效输入、异常）
- ✅ 使用 `pytest.mark.parametrize` 参数化测试
- ✅ 模拟外部依赖（API 调用、文件 I/O、数据库）
- ✅ 目标代码覆盖率达到 90% 以上