"""
Lesson 01: Your First CrewAI Agent

Demonstrates the fundamentals of CrewAI:
- Creating agents with roles, goals, and backstories
- Defining tasks
- Running a simple crew

Run: python agent.py
"""

from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI

llm =  "ollama/gemma4:e4b"

# 1. Define the agent
researcher = Agent(
    role="AI 研究员",
    goal="研究并总结 AI 最新的发展",
    backstory="""你是一位经验丰富的AI研究员，始终关注AI智能体领域的最新论文、框架和应用。
    你为技术受众撰写清晰、准确的摘要。""",
    llm=llm,
    verbose=True,
)

# 2. Define the task
research_task = Task(
    description="""研究并撰写一份简明的简报，主题为：
    "2026年AI智能体的现状"

    涵盖内容：
    - 什么是AI智能体以及它们为何重要
    - 三大顶级框架（CrewAI、LangGraph、AutoGen）
    - 2个产生影响的真实用例
    - 未来发展趋势

    控制在300字以内，面向技术受众。""",
    expected_output="一份关于2026年AI智能体的简明技术简报",
    agent=researcher,
)

# 3. Create and run the crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n" + "=" * 60)
    print("最终结果:")
    print("=" * 60)
    print(result)
