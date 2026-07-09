"""
Email Drafting Agent using CrewAI.

A two-agent crew that drafts professional emails:
- Analyst agent: understands context and tone requirements
- Writer agent: drafts the final email

Usage:
    python agent.py
    python agent.py --context "Follow up on the Q3 proposal sent last week" --tone "professional"
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()


def build_email_crew(context: str, tone: str, recipient: str) -> str:
    analyst = Agent(
        role="邮件上下文分析员",
        goal="理解邮件上下文,提取关键点并定义邮件结构",
        backstory="你是一个专业的商务沟通分析员,能够将复杂的邮件需求简化为清晰的邮件要求.",
        llm="ollama/gemma4:e4b",
        verbose=False,
    )

    writer = Agent(
        role="专业邮件作者",
        goal="根据分析结果，创作专业的邮件内容",
        backstory="你是一个专业的商务沟通作者,能够根据分析结果创作专业的邮件内容.",
        llm="ollama/gemma4:e4b",
        verbose=False,
    )

    analyze_task = Task(
        description=f"""分析邮件需求:
上下文: {context}
接收人: {recipient}
目标语气: {tone}

提取：目的、需要涵盖的关键点、行动号召、主题行建议。""",
        agent=analyst,
        expected_output="邮件摘要：目的、关键点、呼叫操作、建议的主题行",
    )

    write_task = Task(
        description=f"""根据分析结果，创作专业的邮件内容。
语气: {tone}. 接收人: {recipient}.
包含：主题行、问候语、正文段落、结束语、签名占位符。
保持简洁 — 正文under 200 words.""",
        agent=writer,
        expected_output="完整格式化的邮件，准备发送",
        context=[analyze_task],
    )

    crew = Crew(
        agents=[analyst, writer],
        tasks=[analyze_task, write_task],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()
    return str(result)


def main():
    parser = argparse.ArgumentParser(description="专业的邮件创作智能体")
    parser.add_argument("--context", default="跟进我们上周二的产品演示。他们似乎很感兴趣，但还没有回复。", help="邮件上下文/目的")
    parser.add_argument("--tone", default="professional and friendly", help="邮件语气")
    parser.add_argument("--recipient", default="a potential client", help="接收人")
    args = parser.parse_args()

    print(f"\n✉️  创作邮件...\n")
    email = build_email_crew(args.context, args.tone, args.recipient)

    print("=" * 60)
    print("📧邮件")
    print("=" * 60)
    print(email)


if __name__ == "__main__":
    main()
