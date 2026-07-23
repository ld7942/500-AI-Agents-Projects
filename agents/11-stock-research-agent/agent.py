"""
股票研究智能体 使用 Agno + Yahoo Finance.

提供全面的股票分析：价格数据、财务指标、分析师评级和AI驱动的投资总结。

用法:
    python agent.py --ticker AAPL
    python agent.py --ticker NVDA
"""

import argparse
import os

from dotenv import load_dotenv

load_dotenv()

try:
    import yfinance as yf
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def get_stock_data(ticker: str) -> dict:
    if not HAS_YFINANCE:
        return {"ticker": ticker, "error": "yfinance 未安装", "mock": True}

    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker": ticker,
        "name": info.get("longName", ticker),
        "sector": info.get("sector", "N/A"),
        "industry": info.get("industry", "N/A"),
        "price": info.get("currentPrice", info.get("regularMarketPrice", 0)),
        "market_cap": info.get("marketCap", 0),
        "pe_ratio": info.get("trailingPE", "N/A"),
        "forward_pe": info.get("forwardPE", "N/A"),
        "peg_ratio": info.get("pegRatio", "N/A"),
        "revenue_growth": info.get("revenueGrowth", "N/A"),
        "profit_margin": info.get("profitMargins", "N/A"),
        "dividend_yield": info.get("dividendYield", 0),
        "52w_high": info.get("fiftyTwoWeekHigh", "N/A"),
        "52w_low": info.get("fiftyTwoWeekLow", "N/A"),
        "analyst_rating": info.get("recommendationKey", "N/A"),
        "target_price": info.get("targetMeanPrice", "N/A"),
        "description": info.get("longBusinessSummary", "")[:500],
    }


def analyze_stock(data: dict) -> str:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )

    stock_info = "\n".join(f"{k}: {v}" for k, v in data.items() if k != "description")

    messages = [
        SystemMessage(content="你是一个专业的股票分析师。请提供一个简洁的股票分析,包括:投资假设(2-3句),关键优势(3个点),关键风险(3个点),估值评估,和一个判断(购买/持有/卖出，带简单的理由). 保持在300字以下."),
        HumanMessage(content=f"分析股票:\n{stock_info}\n\n公司描述: {data.get('description', 'N/A')}"),
    ]

    response = llm.invoke(messages)
    return response.content


def format_number(n) -> str:
    if isinstance(n, (int, float)):
        if n >= 1e12:
            return f"${n/1e12:.2f}T"
        if n >= 1e9:
            return f"${n/1e9:.2f}B"
        if n >= 1e6:
            return f"${n/1e6:.2f}M"
        return f"${n:.2f}"
    return str(n)


def main():
    parser = argparse.ArgumentParser(description="股票研究智能体")
    parser.add_argument("--ticker", required=True, help="股票代码（例如：AAPL）")
    args = parser.parse_args()

    print(f"\n📈 研究 {args.ticker}...\n")

    data = get_stock_data(args.ticker)

    print("=" * 60)
    print(f"📊 {data.get('name', args.ticker)} ({args.ticker})")
    print("=" * 60)
    print(f"价格: ${data.get('price', 'N/A')}  |  市场市值: {format_number(data.get('market_cap', 0))}")
    print(f"行业: {data.get('sector')}  |  行业: {data.get('industry')}")
    print(f"P/E: {data.get('pe_ratio')}  |  前向P/E率: {data.get('forward_pe')}  |  PEG: {data.get('peg_ratio')}")
    print(f"52周范围: ${data.get('52w_low')} - ${data.get('52w_high')}")
    analyst_rating = data.get("analyst_rating") or "N/A"
    print(f"分析师评级: {str(analyst_rating).upper()}  |  目标价格: ${data.get('target_price', 'N/A')}")

    print("\n🤖 AI 分析结果:")
    print("-" * 40)
    analysis = analyze_stock(data)
    print(analysis)


if __name__ == "__main__":
    main()
