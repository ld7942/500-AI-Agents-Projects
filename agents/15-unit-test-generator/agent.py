"""
单元测试生成智能体.

分析 Python 代码并生成全面的 pytest 测试套件，涵盖正常路径、边界情况和错误条件。

用法：
    python agent.py --file path/to/module.py
    python agent.py --code "def calculate_bmi(weight, height): return weight / height**2"
"""

import argparse
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

TEST_PROMPT = """您是一位资深的 Python 测试工程师。请为提供的代码生成全面的 pytest 测试套件。

要求：
1. 在适当的地方使用 pytest fixtures
2. 测试正常路径（预期的正常输入）
3. 测试边界情况（边界值、空输入）
4. 测试错误条件（无效输入、异常）
5. 使用描述性的测试名称：`test_function_name_scenario`
6. 为每个测试添加简短的文档字符串
7. 对重复性测试使用 `pytest.mark.parametrize`
8. 模拟外部依赖（API 调用、文件 I/O、数据库）
9. 目标代码覆盖率达到 90% 以上

仅输出完整的测试文件内容，可直接使用 `pytest` 运行。"""

SAMPLE_CODE = '''
def calculate_discount(price: float, discount_percent: float) -> float:
    """计算折扣后的价格."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


def find_longest_word(text: str) -> str:
    """查找文本字符串中最长的单词."""
    if not text or not text.strip():
        return ""
    words = text.split()
    return max(words, key=len)


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int = 1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name: str):
        if name not in self.items:
            raise KeyError(f"Item '{name}' not in cart")
        del self.items[name]

    def total(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self.items.values())
'''


def generate_tests(code: str, filename: str = "module") -> str:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    messages = [
        SystemMessage(content=TEST_PROMPT),
        HumanMessage(content=f"为以下python代码生成单元测试 (从 `{filename}`):\n\n```python\n{code}\n```"),
    ]
    response = llm.invoke(messages)
    return response.content


def main():
    parser = argparse.ArgumentParser(description="单元测试生成智能体")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--file", help="Python文件路径")
    group.add_argument("--code", help="内联代码")
    parser.add_argument("--output", help="输出文件路径")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            code = f.read()
        module_name = os.path.splitext(os.path.basename(args.file))[0]
        print(f"\n🧪 为文件生成单元测试: {args.file}")
    elif args.code:
        code = args.code
        module_name = "module"
        print(f"\n🧪 为内联代码生成单元测试")
    else:
        code = SAMPLE_CODE
        module_name = "shopping"
        print(f"\n🧪 为示例代码生成单元测试")

    tests = generate_tests(code, module_name)

    # Clean up markdown fences if present
    if tests.startswith("```"):
        lines = tests.split("\n")
        tests = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

    output_file = args.output or f"test_{module_name}.py"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tests)

    print(f"\n✅ 测试已保存到文件: {output_file}")
    print(f"\n运行测试: pytest {output_file} -v")
    print("\n" + "=" * 60)
    print(tests[:500] + "..." if len(tests) > 500 else tests)


if __name__ == "__main__":
    main()
