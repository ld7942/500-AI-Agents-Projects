"""
Code Review Agent using LangChain.

Reviews Python code for bugs, security issues, style violations, and
suggests improvements. Accepts a file path or inline code snippet.

Usage:
    python agent.py --file path/to/code.py
    python agent.py --code "def add(a,b): return a+b"
"""

import argparse
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

SYSTEM_PROMPT = """你是一位专业的代码审查专家。请分析提供的代码并返回结构化的审查报告，涵盖以下方面：

1. **Bug 与正确性** — 逻辑错误、边界情况、异常处理
2. **安全问题** — 注入风险、密钥泄露、不安全操作
3. **性能** — 低效代码、不必要的计算、内存问题
4. **代码风格** — PEP 8 规范违反、命名约定、可读性
5. **改进建议** — 重构建议、更好的设计模式

格式：使用 Markdown。整体质量评级为：🟢 良好 / 🟡 需要改进 / 🔴 严重问题"""


def review_code(code: str, language: str = "python") -> str:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"请审查以下 {language} 代码:\n\n```{language}\n{code}\n```"),
    ]
    response = llm.invoke(messages)
    return response.content


def main():
    parser = argparse.ArgumentParser(description="代码审查智能体")
    parser.add_argument("--file", default="agents/01-web-research-agent/agent.py", help="要审查的文件路径（默认 Python 代码）")
    parser.add_argument("--code", default="", help="要审查的代码片段")
    parser.add_argument("--language", default="python", help="编程语言（默认 Python）")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            code = f.read()
        print(f"\n🔍 宣查： {args.file}\n")
    else:
        code = args.code
        print(f"\n🔍 宣查内联代码片段\n")

    review = review_code(code, args.language)

    print("=" * 60)
    print("📋 代码审查报告")
    print("=" * 60)
    print(review)


if __name__ == "__main__":
    main()
