"""
Web Research Agent using LangGraph + DuckDuckGo Search.

Searches the web for a given topic, synthesizes findings, and returns
a structured research report.

Usage:
    python agent.py
    python agent.py --query "最新量子计算进展"
"""

import argparse
import os
import re
import sys
from typing import Annotated, TypedDict

# Fix Windows console encoding for emoji characters
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langchain_community.tools import DuckDuckGoSearchResults
import asyncio

load_dotenv()


class ResearchState(TypedDict):
    messages: Annotated[list, add_messages]
    query: str
    search_results: list[dict]
    report: str


def _parse_search_string(raw_str: str) -> list[dict]:
    results = []
    pattern = r'snippet:\s*(.+?)\s*, title:\s*(.+?)\s*, link:\s*(https?://\S+)\s*'
    matches = re.findall(pattern, raw_str, re.DOTALL)

    for match in matches:
        content, title, url = match
        results.append({
            'content': content.strip(),
            'title': title.strip(),
            'url': url.strip()
        })
    return results


def search_web(state: ResearchState) -> ResearchState:
    tool = DuckDuckGoSearchResults(locale="zh")
    try:
        raw_results = tool.invoke(state["query"])
    except Exception as e:
        print(f"搜索时出错: {e}")
        return {"search_results": []}
    
    if isinstance(raw_results, dict):
        results = raw_results.get("results", [])
    elif isinstance(raw_results, list):
        results = raw_results
    elif isinstance(raw_results, str):
        results = _parse_search_string(raw_results)
        if not results:
            results = [{"content": raw_results}]
    else:
        results = []
    return {"search_results": results}


def synthesize_report(state: ResearchState) -> ResearchState:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )

    try:
        results_text = "\n\n".join(
            f"Source: {r.get('url', 'N/A')}\nTitle: {r.get('title', 'N/A')}\nContent: {r.get('content', '')[:500]}"
            for r in state["search_results"]
        )
        messages = [
            SystemMessage(content="您是一位研究分析师。请将搜索结果综合成一份清晰、结构化的报告，包含：摘要、关键发现（要点）和来源。"),
            HumanMessage(content=f"研究查询: {state['query']}\n\n搜索结果:\n{results_text}"),
        ]
    except Exception as e:
        print(f"解析消息时出错: {e}")
        return {"report": "", "messages": []}

    try:
        response = llm.invoke(messages)
    except Exception as e:
        print(f"综合报告时出错: {e}")
        return {"report": "", "messages": []}
        
    return {"report": response.content, "messages": [response]}


def build_graph() -> StateGraph:
    graph = StateGraph(ResearchState)
    graph.add_node("search", search_web)
    graph.add_node("synthesize", synthesize_report)
    graph.set_entry_point("search")
    graph.add_edge("search", "synthesize")
    graph.add_edge("synthesize", END)
    return graph.compile()


async def main():
    parser = argparse.ArgumentParser(description="Web Research Agent")
    parser.add_argument("--query", default="2026年前言的AI Agent 项目", help="Research query")
    args = parser.parse_args()
    print(f"\n🔍 研究: {args.query}\n")
    
    agent = build_graph()
    result = agent.invoke({"query": args.query, "messages": [], "search_results": [], "report": ""})

    print("=" * 60)
    print("📄 研究报告")
    print("=" * 60)
    print(result["report"])


if __name__ == "__main__":
    asyncio.run(main())
