"""
Documentation Writer Agent.

Generates comprehensive documentation for Python modules:
README, API reference, docstrings, and usage examples.

Usage:
    python agent.py --file path/to/module.py
    python agent.py --file src/utils.py --format readme
"""

import argparse
import ast
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()


def extract_structure(code: str) -> str:
    """Extract functions, classes, and their signatures from Python code."""
    try:
        tree = ast.parse(code)
        structure = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                args = [a.arg for a in node.args.args]
                structure.append(f"def {node.name}({', '.join(args)})")
            elif isinstance(node, ast.ClassDef):
                structure.append(f"class {node.name}:")
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        args = [a.arg for a in item.args.args]
                        structure.append(f"  def {item.name}({', '.join(args)})")

        return "\n".join(structure)
    except Exception:
        return "无法解析代码结构"


README_PROMPT = """你是一位技术文档专家。请为这个 Python 模块生成一份完整、专业的 README.md。

请包含：
1. 模块标题和一行描述
2. 功能列表（项目符号）
3. 安装部分
4. 快速入门及可运行的代码示例
5. API 参考（每个公共函数/类包含参数、返回类型、示例）
6. 配置（如有环境变量）
7. 错误处理部分
8. 贡献指南（如有）
9. 使用中文编写

请用清晰、开发者友好的 markdown 格式编写。内容要具体、详实。"""

DOCSTRING_PROMPT = """添加全面的 Google 风格文档字符串到每个缺少文档字符串的函数和类。

格式：
```
def function(param: type) -> return_type:
    \"\"\"一行描述。

    Args:
        param: 参数描述。

    Returns:
        返回值描述。

    Raises:
        ErrorType: 当发生此错误时。

    Example:
        >>> function(value)
        expected_output
    \"\"\"
```

Return完整的更新后的 Python 文件，包含添加的文档字符串."""


def generate_readme(code: str, filename: str) -> str:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    structure = extract_structure(code)
    messages = [
        SystemMessage(content=README_PROMPT),
        HumanMessage(content=f"文件: {filename}\n\n代码结构:\n{structure}\n\n完整代码:\n```python\n{code[:3000]}\n```"),
    ]
    return llm.invoke(messages).content


def add_docstrings(code: str, filename: str) -> str:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    messages = [
        SystemMessage(content=DOCSTRING_PROMPT),
        HumanMessage(content=f"为文件 {filename} 添加文档字符串:\n\n```python\n{code}\n```"),
    ]
    result = llm.invoke(messages).content
    # Clean markdown fences
    if "```python" in result:
        result = result.split("```python")[1].split("```")[0].strip()
    return result


SAMPLE_CODE = r'''
import hashlib
import re
from datetime import datetime


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def hash_password(password: str, salt: str = "") -> str:
    combined = f"{password}{salt}"
    return hashlib.sha256(combined.encode()).hexdigest()


def parse_date(date_string: str) -> datetime:
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y%m%d"]
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date: {date_string}")


class UserValidator:
    MIN_PASSWORD_LENGTH = 8

    def validate_username(self, username: str) -> tuple[bool, str]:
        if len(username) < 3:
            return False, "Username too short"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Only letters, numbers, underscores allowed"
        return True, ""

    def validate_password(self, password: str) -> tuple[bool, str]:
        if len(password) < self.MIN_PASSWORD_LENGTH:
            return False, f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters"
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r'\d', password):
            return False, "Password must contain at least one digit"
        return True, ""
'''


def main():
    parser = argparse.ArgumentParser(description="文档编写器智能体")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--file", help="要文档化的 Python 文件")
    group.add_argument("--code", help="要文档的代码片段")
    parser.add_argument("--format", choices=["readme", "docstrings", "both"], default="both", help="文档化格式")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            code = f.read()
        filename = os.path.basename(args.file)
    elif args.code:
        code = args.code
        filename = "module.py"
    else:
        code = SAMPLE_CODE
        filename = "validators.py"
        print("\n📝 使用示例验证模块")

    print(f"\n✍️  为 {filename} 生成文档...\n")

    if args.format in ("readme", "both"):
        print("📄 生成 README...")
        readme = generate_readme(code, filename)
        readme_file = f"README_{filename.replace('.py', '')}.md"
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(readme)
        print(f"✅ README 已保存到: {readme_file}")

    if args.format in ("docstrings", "both"):
        print("📝 添加文档字符串...")
        documented_code = add_docstrings(code, filename)
        output_file = f"documented_{filename}"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(documented_code)
        print(f"✅ 文档化代码已保存到: {output_file}")


if __name__ == "__main__":
    main()
