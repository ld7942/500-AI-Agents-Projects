"""
News Summarizer Agent using LangChain.

Fetches hot news from Weibo and produces structured summaries with key insights.

Usage:
    python agent.py
"""

import argparse
import os

import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

# 从微博获取热门新闻
def fetch_news_from_weibo() -> list[dict]:
    url = f"https://uapis.cn/api/v1/misc/hotboard?type=weibo"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data.get("list", [])


def summarize_news(articles: list[dict]) -> str:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )

    articles_text = "\n\n".join(
        f"Title: {a['title']}\nSummary: {a.get('extra', {}).get('desc', 'N/A')}\nHot Score: {a.get('hot_value', 'N/A')}"
        for a in articles[:5]
    )

    messages = [
        SystemMessage(content="你是一个新闻分析师. 请根据以下新闻文章,创建一个结构化的新闻摘要,包含以下内容:1) 主要新闻 (Top Story), 2) 主要主题 (Key Themes (3 bullet points)), 3) 什么要 (What to Watch), 4) 快速新闻列表 (Quick Headlines list)."),
        HumanMessage(content=f"文章:\n{articles_text}"),
    ]

    response = llm.invoke(messages)
    return response.content


def main():
    print(f"\n📰 从微博获取热门新闻...\n")
    articles = fetch_news_from_weibo()
    print(f"✅ 找到: {len(articles)} 条热门新闻")

    summary = summarize_news(articles)

    print("\n" + "=" * 60)
    print(f"📋 新闻摘要:")
    print("=" * 60)
    print(summary)


if __name__ == "__main__":
    main()
