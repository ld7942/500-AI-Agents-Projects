"""
简历解析智能体使用 LangChain.

从简历文本或PDF中提取结构化信息：
联系信息、技能、经验、教育、提供候选人的摘要和适合度分数。

Usage:
    python agent.py --resume resume.txt
    python agent.py --resume resume.pdf --job-desc "一个5+年经验的高级Python开发人员..."
"""

import argparse
import json
import os
import re

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

PARSE_PROMPT = """从这个简历中提取结构化信息并返回JSON:
{
  "name": "full name",
  "email": "email or null",
  "phone": "phone or null",
  "location": "city, country or null",
  "linkedin": "URL or null",
  "github": "URL or null",
  "summary": "2-3 sentence professional summary",
  "years_experience": number,
  "current_title": "current/most recent job title",
  "skills": {
    "languages": ["Python", "JavaScript", ...],
    "frameworks": ["Django", "React", ...],
    "tools": ["Docker", "Git", ...],
    "soft_skills": ["leadership", ...]
  },
  "experience": [{"title": "...", "company": "...", "duration": "...", "highlights": ["..."]}],
  "education": [{"degree": "...", "institution": "...", "year": "..."}],
  "certifications": ["..."],
  "languages_spoken": ["English", ...]
}
返回有效的JSON字符串,不包含Markdown格式."""

FIT_PROMPT = """返回JSON:
{
  "fit_score": 0-100,
  "fit_label": "Excellent|Good|Fair|Poor",
  "strengths": ["matching point 1", "matching point 2", ...],
  "gaps": ["missing skill 1", ...],
  "recommendation": "Hire|Consider|Pass",
  "recommendation_reason": "2-3 sentence explanation"
}
返回有效的JSON字符串,不包含Markdown格式."""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def read_resume_text(path: str) -> str:
    if path.endswith(".pdf"):
        try:
            import pypdf
            with open(path, "rb") as f:
                reader = pypdf.PdfReader(f)
                return "\n".join(page.extract_text() for page in reader.pages)
        except ImportError:
            print("⚠️  pypdf 未安装. 请使用: pip install pypdf")
            raise
    with open(path) as f:
        return f.read()


def parse_resume(text: str) -> dict:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    messages = [SystemMessage(content=PARSE_PROMPT), HumanMessage(content=text)]
    response = llm.invoke(messages)
    return parse_json_response(response.content)


def score_fit(profile: dict, job_desc: str) -> dict:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    messages = [
        SystemMessage(content=FIT_PROMPT),
        HumanMessage(content=f"候选人简历:\n{json.dumps(profile, indent=2)}\n\n岗位描述:\n{job_desc}"),
    ]
    response = llm.invoke(messages)
    return parse_json_response(response.content)


SAMPLE_RESUME = """
Jane Doe
jane.doe@email.com | +1 (555) 123-4567 | San Francisco, CA
linkedin.com/in/janedoe | github.com/janedoe

SUMMARY
Senior Python developer with 7 years of experience building scalable web applications
and data pipelines. Led teams of 5-8 engineers at Series B startups.

EXPERIENCE
Senior Software Engineer | TechCorp Inc. | 2021-present
- Architected microservices platform handling 10M requests/day using FastAPI + Kubernetes
- Reduced API latency by 40% through Redis caching and async optimization
- Led migration from monolith to microservices (12-month project, 5 engineers)

Software Engineer | DataFlow Systems | 2018-2021
- Built ML data pipelines processing 500GB/day using Apache Spark and Airflow
- Developed REST APIs with Django REST Framework serving 50k daily users

SKILLS
Languages: Python, JavaScript, SQL, Bash
Frameworks: FastAPI, Django, React, Spark
Tools: Docker, Kubernetes, Redis, PostgreSQL, Git, Airflow
Cloud: AWS (EC2, S3, RDS, Lambda)

EDUCATION
B.S. Computer Science | UC Berkeley | 2017

CERTIFICATIONS
AWS Solutions Architect Associate
"""


def main():
    parser = argparse.ArgumentParser(description="简历解析器智能体")
    parser.add_argument("--resume", help="简历文件路径(.txt或.pdf)")
    parser.add_argument("--job-desc", help="岗位描述匹配")
    args = parser.parse_args()

    if args.resume:
        print(f"\n📄 解析简历: {args.resume}")
        text = read_resume_text(args.resume)
    else:
        print("\n📄 使用示例简历(传递 --resume 使用您自己的简历)")
        text = SAMPLE_RESUME

    profile = parse_resume(text)

    print("\n" + "=" * 60)
    print("👤 解析后的简历")
    print("=" * 60)
    print(f"姓名: {profile.get('name')}")
    print(f"职务: {profile.get('current_title')}")
    print(f"经验: {profile.get('years_experience')} 年")
    print(f"技能: {', '.join(profile.get('skills', {}).get('languages', []))}")
    print(f"\n摘要: {profile.get('summary')}")

    if args.job_desc:
        print("\n" + "=" * 60)
        print("📊 岗位匹配分析结果")
        print("=" * 60)
        fit = score_fit(profile, args.job_desc)
        fit_label = fit.get("fit_label", "N/A")
        label_emoji = {"Excellent": "🟢", "Good": "🟡", "Fair": "🟠", "Poor": "🔴"}.get(fit_label, "⚪")
        print(f"{label_emoji} 岗位匹配分数: {fit.get('fit_score', 'N/A')}/100 ({fit_label})")
        print(f"✅ 优势: {', '.join(fit.get('strengths', [])[:3])}")
        print(f"⚠️  缺陷: {', '.join(fit.get('gaps', ['未识别'])[:3])}")
        print(f"🎯 建议: {fit.get('recommendation', 'N/A')}")
        print(f"💭 建议理由: {fit.get('recommendation_reason', 'N/A')}")


if __name__ == "__main__":
    main()
