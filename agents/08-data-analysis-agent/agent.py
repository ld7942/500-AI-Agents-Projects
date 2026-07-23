"""
数据分析智能体使用 LangChain + pandas.

加载一个CSV/Excel文件并使用自然语言回答关于它的分析问题。智能体生成Python/pandas代码来回答问题。

用法:
    python agent.py --file data.csv
    python agent.py --file sales.xlsx --question "每月销售额趋势是多少？"
"""

import argparse
import os

import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

load_dotenv()


def create_sample_data(path: str):
    """创建示例销售数据集用于演示."""
    import random
    from datetime import date, timedelta

    random.seed(42)
    rows = []
    products = ["笔记本", "手机", "平板", "显示器", "键盘"]
    regions = ["北美", "南部", "东美", "西美"]
    start = date(2024, 1, 1)

    for i in range(200):
        d = start + timedelta(days=random.randint(0, 364))
        rows.append({
            "date": d.isoformat(),
            "product": random.choice(products),
            "region": random.choice(regions),
            "quantity": random.randint(1, 20),
            "unit_price": round(random.uniform(50, 2000), 2),
            "revenue": 0,
        })

    df = pd.DataFrame(rows)
    df["revenue"] = df["quantity"] * df["unit_price"]
    df.to_csv(path, index=False)
    return df


def main():
    parser = argparse.ArgumentParser(description="数据分析智能体")
    parser.add_argument("--file", default="sample_data.csv", help="要分析的CSV或Excel数据文件或示例数据文件")
    parser.add_argument("--question", help="单个问题（省略则进入交互模式）")
    parser.add_argument(
        "--allow-dangerous-code",
        action="store_true",
        help="需要允许危险代码执行（仅在受信任的提示和非敏感数据上运行）。",
    )
    args = parser.parse_args()

    if args.file == "sample_data.csv" and not os.path.exists("sample_data.csv"):
        print("🏗️  创建示例销售数据集...")
        df = create_sample_data("sample_data.csv")
    else:
        ext = os.path.splitext(args.file)[1].lower()
        df = pd.read_excel(args.file) if ext in (".xlsx", ".xls") else pd.read_csv(args.file)

    print(f"\n📊 加载: {args.file} ({len(df)} 行 × {len(df.columns)}列）")
    print(f"📋 列: {', '.join(df.columns)}\n")
    
    if not args.allow_dangerous_code:
        print("⚠️  该智能体使用LangChain的pandas智能体，执行模型生成的Python代码。")
        print("请仅在受信任的提示和非敏感数据上运行。使用--allow-dangerous-code运行。")
        return

    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=args.allow_dangerous_code,
        agent_executor_kwargs={"handle_parsing_errors": True},
    )

    if args.question:
        print(f"❓ 问题: {args.question}")
        result = agent.invoke({"input": args.question})
        print(f"\n✅ 答案: {result['output']}")
    else:
        print("💬 数据分析智能体已准备就绪。请询问您的数据。输入quit退出。\n")
        print("示例问题:")
        print("  - 每个产品的总销售额是多少？")
        print("  - 哪个区域的平均订单价值最高？")
        print("  - 显示销售量最高的5天\n")
        while True:
            question = input("您: ").strip()
            if question.lower() in ("quit", "exit", "q"):
                break
            if not question:
                continue
            result = agent.invoke({"input": question})
            print(f"\n智能体: {result['output']}\n")


if __name__ == "__main__":
    main()
