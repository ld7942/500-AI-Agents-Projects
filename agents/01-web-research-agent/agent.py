"""
Web Research Agent using LangGraph + Tavily Search.

Searches the web for a given topic, synthesizes findings, and returns
a structured research report.

Usage:
    python agent.py
    python agent.py --query "latest advances in quantum computing"
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
    tool = DuckDuckGoSearchResults()
    
    raw_results = tool.invoke(state["query"])
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
    print("start parse message")
    try:
        results_text = "\n\n".join(
            f"Source: {r.get('url', 'N/A')}\nTitle: {r.get('title', 'N/A')}\nContent: {r.get('content', '')[:500]}"
            for r in state["search_results"]
        )
        messages = [
            SystemMessage(content="You are a research analyst. Synthesize the search results into a clear, structured report with: Summary, Key Findings (bullet points), and Sources."),
            HumanMessage(content=f"Research query: {state['query']}\n\nSearch results:\n{results_text}"),
        ]
    except Exception as e:
        print(f"Error in parse message: {e}")
        return {"report": "", "messages": []}
    finally:
        print("end parse message")

    try:
        response = llm.invoke(messages)
    except Exception as e:
        print(f"Error in synthesize_report: {e}")
        return {"report": "", "messages": []}
    finally:
        print("end synthesize_report")
        
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
    parser.add_argument("--query", default="latest advances in AI agents 2026", help="Research query")
    args = parser.parse_args()
    print(f"\n🔍 Researching: {args.query}\n")
    
    agent = build_graph()
    result = agent.invoke({"query": args.query, "messages": [], "search_results": [], "report": ""})

    print("=" * 60)
    print("📄 RESEARCH REPORT")
    print("=" * 60)
    print(result["report"])


if __name__ == "__main__":
    asyncio.run(main())
