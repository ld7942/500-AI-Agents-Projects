"""
社交媒体内容生成器, 基于CrewAI.

根据主题或文章URL生成平台优化的内容社交媒体帖子.

Usage:
    python agent.py --topic "2026 年度产品发布"
    python agent.py --topic "新品发布会: 2026 年度产品发布" --brand "小米"
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def generate_social_content(topic: str, brand: str, platforms: list[str]) -> str:
    llm="ollama/gemma4:e4b"

    strategist = Agent(
        role="社交媒体策略师",
        goal="分析主题并定义每个平台的关键消息、目标受众和语气",
        backstory="经验丰富的社交媒体策略师，有丰富的社交媒体策略经验，能够根据主题生成符合平台要求的内容帖子。",
        llm=llm,
        verbose=False,
    )

    writer = Agent(
        role="社交媒体文案作者",
        goal="根据策略生成符合平台要求的社交媒体帖子。",
        backstory="经验丰富的社交媒体文案作者，有丰富的社交媒体文案创作经验，能够根据策略生成符合平台要求的内容帖子。",
        llm=llm,
        verbose=False,
    )

    strategy_task = Task(
        description=f"""分析主题并定义每个平台的关键消息、目标受众和语气。
Topic: "{topic}"
Brand: {brand or 'Not specified'}
Platforms: {', '.join(platforms)}
""",
        agent=strategist,
        expected_output="内容策略: 消息, 目标受众, 情感钩子, #标签",
    )

    writing_task = Task(
        description=f"""为社交平台符合策略生成帖子: {', '.join(platforms)}
Topic: {topic}. Brand: {brand or 'General'}.

为每个平台符合策略生成帖子:
- 微博: 2条微博 + 线程开头
- 小红书: 2条帖子 + 情感钩子
- 抖音: 2条视频 + 15 #标签

生成符合平台要求的帖子。""",
        agent=writer,
        expected_output="符合平台要求的帖子。",
        context=[strategy_task],
    )

    crew = Crew(
        agents=[strategist, writer],
        tasks=[strategy_task, writing_task],
        process=Process.sequential,
        verbose=False,
    )

    return str(crew.kickoff())


def main():
    parser = argparse.ArgumentParser(description="社交媒体内容生成器")
    parser.add_argument("--topic", default="2026 年度产品发布", help="主题")
    parser.add_argument("--brand", default="", help="品牌名称")
    parser.add_argument("--platforms", default="微博,小红书,抖音", help="平台列表")
    args = parser.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",")]
    print(f"\n📱 生成内容为平台: {', '.join(platforms)}")
    print(f"📌 主题: {args.topic}\n")

    content = generate_social_content(args.topic, args.brand, platforms)

    print("=" * 60)
    print("✍️  生成内容")
    print("=" * 60)
    print(content)


if __name__ == "__main__":
    main()
