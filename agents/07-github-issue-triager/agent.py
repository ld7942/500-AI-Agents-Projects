"""
GitHub Issue Triager using LangChain.

Analyzes a GitHub issue and produces: severity label, category,
reproduction steps summary, and suggested assignee type.

Usage:
    python agent.py --title "Login fails on mobile Safari" --body "When I try..."
    python agent.py --issue-url https://github.com/owner/repo/issues/123
"""

import argparse
import os
import json
import re

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

TRIAGE_PROMPT = """你是一个GitHub问题分类器.请分析问题并返回一个JSON对象,包含以下字段:
{
  "severity": "critical|high|medium|low",
  "category": "bug|feature|documentation|question|performance|security",
  "priority_score": 1-10,
  "labels": ["list", "of", "suggested", "labels"],
  "summary": "one sentence summary",
  "reproduction_clear": true/false,
  "assignee_type": "frontend|backend|devops|documentation|security|any",
  "needs_more_info": true/false,
  "triage_notes": "2-3 sentences of triager notes"
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


def triage_issue(title: str, body: str, labels: list[str] = None) -> dict:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )

    issue_text = f"标题: {title}\n\n内容:\n{body}"
    if labels:
        issue_text += f"\n\n现有标签: {', '.join(labels)}"

    messages = [
        SystemMessage(content=TRIAGE_PROMPT),
        HumanMessage(content=issue_text),
    ]

    response = llm.invoke(messages)
    return parse_json_response(response.content)


def fetch_github_issue(url: str) -> tuple[str, str, list]:
    """从GitHub API获取问题详情."""
    import re
    import requests

    match = re.match(r"https://github.com/([^/]+)/([^/]+)/issues/(\d+)", url)
    if not match:
        raise ValueError(f"无效的GitHub问题URL: {url}")

    owner, repo, issue_num = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_num}"
    r = None
    try:
        r = requests.get(api_url, timeout=10)
        r.raise_for_status()
    except:
        print(f"从GitHub获取问题失败,使用示例数据: {api_url}")
        with open("example_github_api.json", "r", encoding="utf-8") as f:
            r = requests.Response()
            r.status_code = 200
            r.text = f.read()
        
    data = r.json()
    return data["title"], data.get("body", ""), [l["name"] for l in data.get("labels", [])]


def main():
    parser = argparse.ArgumentParser(description="GitHub问题分类器")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--issue-url", help="GitHub问题URL")
    group.add_argument("--title", help="问题标题 (与--body使用)")
    parser.add_argument("--body", default="", help="内容文本")
    args = parser.parse_args()

    if args.issue_url:
        print(f"\n🔍 从GitHub获取问题...")
        title, body, labels = fetch_github_issue(args.issue_url)
    else:
        title, body, labels = args.title, args.body, []
        
    print(f"\n🏷️  分类: {title}\n")
    result = triage_issue(title, body, labels)

    severity = result.get("severity", "medium")
    labels = result.get("labels", [])
    severity_emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(severity, "⚪")

    print("=" * 60)
    print("📋 分类报告")
    print("=" * 60)
    print(f"{severity_emoji} 严重性: {severity.upper()} (优先级: {result.get('priority_score', 'N/A')}/10)")
    print(f"📁 类别: {result.get('category', 'N/A')}")
    print(f"👤 分配给: {result.get('assignee_type', 'any')} team")
    print(f"🏷️  标签: {', '.join(labels)}")
    print(f"📝 摘要: {result.get('summary', 'N/A')}")
    print(f"❓ 是否需要更多信息: {'Yes' if result.get('needs_more_info') else 'No'}")
    print(f"🔍 是否清晰: {'Yes' if result.get('reproduction_clear') else 'No'}")
    print(f"\n💭 注意: {result.get('triage_notes', 'N/A')}")


if __name__ == "__main__":
    main()
