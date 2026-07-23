"""
旅游计划员智能体, 使用 CrewAI.

Multi-agent crew that:
- 目的地研究员: 收集目的地信息
- 活动计划员: 创建每日活动
- 预算分析师: 计算成本

Usage:
    python agent.py --destination "Tokyo, Japan" --days 5 --budget 2000
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def build_travel_crew(destination: str, days: int, budget: float, interests: str) -> str:
    llm="ollama/gemma4:e4b"

    researcher = Agent(
        role="目的地研究员",
        goal=f"收集{destination} 的信息, 并提供旅行洞察",
        backstory="专业旅行记者, 已访问 100+ 国家. 熟悉最佳隐藏宝藏和实用技巧.",
        llm=llm,
        verbose=False,
    )

    planner = Agent(
        role="活动计划员",
        goal=f"创建{destination} 的详细行程",
        backstory="专业旅行顾问, 已有 15 年的定制行程经验.",
        llm=llm,
        verbose=False,
    )

    budget_analyst = Agent(
        role="预算分析师",
        goal=f"根据预算 ${budget} 估算行程成本",
        backstory="专业金融旅行顾问, 帮助旅客在预算内最大化体验.",
        llm=llm,
        verbose=False,
    )

    research_task = Task(
        description=f"""收集{destination} 的信息, 并提供旅行洞察.
包括: 旅游的最佳时间, 住的区域, 必须去的景点,
当地美食, 运输技巧, 文化习俗.
旅客兴趣: {interests}.""",
        agent=researcher,
        expected_output="目的地摘要, 包括主要区域、景点、美食、实用技巧等",
    )

    planning_task = Task(
        description=f"""创建{destination} 的详细行程.
预算: 共计${budget} . 旅客兴趣: {interests}.
包括: 每天的活动, 餐厅推荐, 交通时间.
确保可实现且有趣.""",
        agent=planner,
        expected_output=f"每一天共计 {days}-天 行程, 包括活动、餐厅推荐、交通时间等",
        context=[research_task],
    )

    budget_task = Task(
        description=f"""根据预算 ${budget} 估算{days}-天 {destination} 成本.
包括: 航班, 住宿费用, 食物, 活动, 交通. 如果预算紧张, 请标记出来并建议调整.""",
        agent=budget_analyst,
        expected_output="预算估算, 包括航班、住宿费用、食物、活动、交通等",
        context=[research_task, planning_task],
    )

    crew = Crew(
        agents=[researcher, planner, budget_analyst],
        tasks=[research_task, planning_task, budget_task],
        process=Process.sequential,
        verbose=False,
    )

    return str(crew.kickoff())


def main():
    parser = argparse.ArgumentParser(description="旅游计划员智能体")
    parser.add_argument("--destination", default="北京", help="目的地")
    parser.add_argument("--days", type=int, default=7, help="天数")
    parser.add_argument("--budget", type=float, default=3000, help="预算")
    parser.add_argument("--interests", default="美食, 交通, 文化", help="旅客兴趣")
    args = parser.parse_args()

    print(f"\n✈️  计划前往 {args.days}-天 {args.destination} (预算: ${args.budget})\n")
    itinerary = build_travel_crew(args.destination, args.days, args.budget, args.interests)

    print("=" * 60)
    print("🗺️  行程计划")
    print("=" * 60)
    print(itinerary)


if __name__ == "__main__":
    main()
