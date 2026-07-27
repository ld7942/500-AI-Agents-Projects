"""
Competitive Analysis Agent using LangGraph.

Multi-step agent that analyzes competitors:
1. Identifies key competitors
2. Analyzes each competitor's strengths/weaknesses
3. Generates competitive positioning recommendations

Usage:
    python agent.py --company "Notion" --industry "productivity software"
"""

import argparse
import os
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

load_dotenv()


class AnalysisState(TypedDict):
    messages: Annotated[list, add_messages]
    company: str
    industry: str
    competitors: list[str]
    competitor_analyses: dict[str, str]
    final_report: str


def identify_competitors(state: AnalysisState) -> AnalysisState:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    response = llm.invoke([
        SystemMessage(content="你是一个市场研究分析师。请列出5个主要竞争对手，用逗号分隔。其他内容。"),
        HumanMessage(content=f"公司: {state['company']}\n行业: {state['industry']}\n\n列出5个竞争对手："),
    ])
    competitors = [c.strip() for c in response.content.split(",")][:5]
    return {"competitors": competitors, "messages": [response]}


def analyze_competitor(state: AnalysisState) -> AnalysisState:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    analyses = {}

    for competitor in state["competitors"]:
        response = llm.invoke([
            SystemMessage(content="请提供100字左右的竞争对手分析，覆盖主要产品、优势、劣势、定价模型和目标市场。"),
            HumanMessage(content=f"分析 {competitor} 对 {state['company']} 的 {state['industry']} 市场分析："),
        ])
        analyses[competitor] = response.content

    return {"competitor_analyses": analyses}


def generate_report(state: AnalysisState) -> AnalysisState:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )

    analyses_text = "\n\n".join(
        f"**{name}:**\n{analysis}"
        for name, analysis in state["competitor_analyses"].items()
    )

    response = llm.invoke([
        SystemMessage(content="""你是一个战略顾问。请创建一个竞争对手分析报告，包含以下内容：
1. 执行摘要（3个句子）
2. 竞争 landscape 表格（公司、优势、劣势、价格）
3. 市场差距和机会（3个要点）
4. {company} 的战略建议（5个操作项）
5. 每个竞争对手的风险评估（High/Medium/Low）""".replace("{company}", state["company"])),
        HumanMessage(content=f"公司: {state['company']}\n行业: {state['industry']}\n\n竞争对手分析结果:\n{analyses_text}"),
    ])

    return {"final_report": response.content, "messages": [response]}


def build_graph():
    graph = StateGraph(AnalysisState)
    graph.add_node("identify", identify_competitors)
    graph.add_node("analyze", analyze_competitor)
    graph.add_node("report", generate_report)
    graph.set_entry_point("identify")
    graph.add_edge("identify", "analyze")
    graph.add_edge("analyze", "report")
    graph.add_edge("report", END)
    return graph.compile()


def main():
    parser = argparse.ArgumentParser(description="竞争对手分析智能体")
    parser.add_argument("--company", default="Notion", help="公司名称")
    parser.add_argument("--industry", default="生产效率和协作软件", help="行业")
    args = parser.parse_args()

    print(f"\n🔍 分析公司 {args.company} 的 {args.industry} 市场分析...\n")

    agent = build_graph()
    result = agent.invoke({
        "company": args.company,
        "industry": args.industry,
        "messages": [],
        "competitors": [],
        "competitor_analyses": {},
        "final_report": "",
    })

    print(f"🏢 确定的竞争对手: {', '.join(result['competitors'])}\n")
    print("=" * 60)
    print("📊 竞争分析分析报告")
    print("=" * 60)
    print(result["final_report"])


if __name__ == "__main__":
    main()
