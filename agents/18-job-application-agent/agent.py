"""
Job Application Agent using CrewAI.

Analyzes a job description and a candidate profile, then generates:
- Tailored cover letter
- Resume bullet points to highlight
- Interview preparation questions

Usage:
    python agent.py --job-desc "Senior Python Engineer at Stripe..." --candidate "7 years Python, FastAPI..."
"""

import argparse
import os

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

SAMPLE_JOB = """Stripe 高级 Python 工程师
我们正在寻找一名高级 Python 工程师加入我们的 API 平台团队。

要求：
- 5年以上 Python 开发经验
- 有分布式系统经验
- 深入理解 REST API 和微服务
- 有 PostgreSQL、Redis 经验
- 优先考虑有 Kubernetes 经验者
- 良好的沟通能力

职责：
- 设计并构建处理数百万日请求的高性能 API
- 主导技术设计评审
- 指导初级工程师
- 与产品经理协作评估技术可行性
"""

SAMPLE_CANDIDATE = """
Jane Doe — 7年Python开发经验
当前职位：DataCorp高级软件工程师
技能：Python、FastAPI、Django、PostgreSQL、Redis、Docker、Kubernetes、AWS
成就：
- 构建了日处理500万请求的API平台
- 领导4人工程师团队
- 将API延迟降低了40%
- 指导了3名初级工程师
教育背景：加州大学伯克利分校计算机科学学士学位
"""


def run_job_application_crew(job_desc: str, candidate_profile: str) -> str:
    llm = "ollama/gemma4:e4b"

    analyst = Agent(
        role="工作需求分析员",
        goal="分析工作需求，提取关键技能、文化信号和公司价值观",
        backstory="在 FAANG 公司工作，有10年招聘经验，擅长解码工作需求。",
        llm=llm,
        verbose=False,
    )

    writer = Agent(
        role="职业教练和申请材料编写员",
        goal="根据工作需求和候选人简历，创建定制的申请材料，最大化面试机会。",
        backstory="帮助500+名候选人找到顶级科技公司的岗位。",
        llm=llm,
        verbose=False,
    )

    analyst_task = Task(
        description=f"""分析这个工作描述：
{job_desc}

提取：前5个必填技能、文化信号、公司最重视的价值观、潜在风险标志和关键短语，用于申请材料。""",
        agent=analyst,
        expected_output="工作分析：关键需求、文化信号、重要关键词",
    )

    application_task = Task(
        description=f"""根据工作分析，为这个候选人创建申请材料：
{candidate_profile}

生成：
1. 申请信 (250-300 字, 3 段段落: hook, evidence, close)
2. 申请材料中包含的前 5 个必填技能、文化信号、公司最重视的价值观、潜在风险标志和关键短语，用于申请材料。
3. 104 个字，3 段段落：hook、证据、关闭。
4. 10 个面试问题，5 个行为问题，5 个技术问题，每个问题都有建议的答案框架。
""",
        agent=writer,
        expected_output="申请材料：申请信、简历高亮、面试问题、薪资范围",
        context=[analyst_task],
    )

    crew = Crew(
        agents=[analyst, writer],
        tasks=[analyst_task, application_task],
        process=Process.sequential,
        verbose=False,
    )

    return str(crew.kickoff())


def main():
    parser = argparse.ArgumentParser(description="工作申请材料编写员")
    parser.add_argument("--job-desc", default=SAMPLE_JOB, help="工作描述文本")
    parser.add_argument("--candidate", default=SAMPLE_CANDIDATE, help="候选人简历摘要")
    args = parser.parse_args()

    print("\n💼 准备工作申请材料...\n")
    result = run_job_application_crew(args.job_desc, args.candidate)

    print("=" * 60)
    print("📋 工作申请材料包")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()
