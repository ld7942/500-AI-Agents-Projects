"""
Lesson 02: Multi-Agent Crew with Tool Use

Demonstrates:
- Multiple specialized agents with different roles
- Custom tools (web search, calculator)
- Sequential and hierarchical processes
- Agent collaboration patterns

Run: python agent.py --topic "quantum computing applications"
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from crewai.tools import BaseTool
from dotenv import load_dotenv
from pydantic import Field

load_dotenv()

llm = "ollama/gemma4:e4b"


# Custom Tool: Word Counter
class WordCountTool(BaseTool):
    name: str = "wordCountTool"
    description: str = "计算一段文本字符串中的文字数量. 输入: 文本字符串."

    def _run(self, text: str) -> str:
        count = len(text.split())
        return f"文字数量: {count}"


# Custom Tool: Text Formatter
class TextFormatterTool(BaseTool):
    name: str = "textFormatterTool"
    description: str = "将文本格式化为编号列表. 输入: 逗号分隔的项目."

    def _run(self, items: str) -> str:
        item_list = [i.strip() for i in items.split(",")]
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(item_list))


word_counter = WordCountTool()
formatter = TextFormatterTool()

# Agent 1: Researcher
researcher = Agent(
    role="高级研究员",
    goal="彻底研究主题并提供事实准确的结构化信息",
    backstory="博士研究员，擅长综合多个来源的信息。",
    llm=llm,
    tools=[word_counter],
    verbose=True,
)

# Agent 2: Writer
writer = Agent(
    role="技术作家",
    goal="将研究转换为清晰、吸引人的技术受众内容。",
    backstory="获得10年AI/ML文档编写经验的获奖技术作家。",
    llm=llm,
    tools=[formatter],
    verbose=True,
)

# Agent 3: Editor
editor = Agent(
    role="内容编辑器",
    goal="审核并完善内容，确保清晰、准确和简洁。",
    backstory="资深编辑，确保所有内容符合最高质量标准。",
    llm=llm,
    verbose=True,
)


def run_crew(topic: str) -> str:
    research_task = Task(
        description=f"""研究主题: "{topic}"

        查找:
        1. 核心定义和关键概念（3个要点）
        2. 当前应用（3个实际例子）
        3. 未来潜力（2个预测）
        4. 主要挑战或限制

        使用 word_counter 工具验证输出不超过250个单词。""",
        expected_output="包含定义、应用和未来展望的研究简报",
        agent=researcher,
    )

    writing_task = Task(
        description=f"""将研究转换为关于"{topic}"的吸引人的技术文章。

        结构化:
        - Hook 开头（包含1-2个句子）
        - 什么是（清晰定义）
        - 为什么重要（使用 formatter 工具格式化为编号列表）
        - 影响（2个实际例子）
        - 召唤行动关闭

        目标: 200-250 字数, 技术但可访问.""",
        expected_output="已完成的技术文章，准备发布",
        agent=writer,
        context=[research_task],
    )

    editing_task = Task(
        description="""审核文章内容：
        1. 准确性（检查事实是否与研究一致）
        2. 清晰度（去除专业术语，改善流畅度）
        3. 简洁性（删减冗余内容）
        4. 添加引人注目的标题和副标题

        返回最终润色版本。""",
        expected_output="最终编辑后的文章，包含标题、副标题和润色后的内容",
        agent=editor,
        context=[research_task, writing_task],
    )

    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=True,
    )

    return str(crew.kickoff())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="多智能体研究 & 写作主题")
    parser.add_argument("--topic", default="AI 代理在医疗领域的应用", help="研究主题")
    args = parser.parse_args()

    print(f"\n🚀 开始处理主题: {args.topic}\n")
    result = run_crew(args.topic)

    print("\n" + "=" * 60)
    print("最终章节:")
    print("=" * 60)
    print(result)
