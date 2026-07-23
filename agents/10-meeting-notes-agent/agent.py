"""
会议纪要智能体.

将会议记录文本转换为结构化的会议纪要:
摘要、操作项、决策和跟进项。

使用:
    python agent.py --transcript meeting.txt
    python agent.py --text "John: Let's ship v2 next Friday..."
"""

import argparse
import json
import os
import re
import sys
import io
from datetime import date, datetime

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()

NOTES_PROMPT = """你是一个专业的会议纪要记录员。将会议记录转换为结构化的会议纪要，格式为 JSON:
{
  "meeting_title": "inferred title",
  "date": "today or mentioned date",
  "participants": ["name1", "name2"],
  "duration_estimate": "X minutes",
  "summary": "2-3 sentence executive summary",
  "key_decisions": ["decision 1", "decision 2"],
  "action_items": [
    {"task": "description", "owner": "person name or TBD", "due": "date or timeframe or TBD"}
  ],
  "discussion_topics": ["topic 1", "topic 2"],
  "blockers": ["blocker 1 or none"],
  "next_meeting": "scheduled time or TBD",
  "follow_up_questions": ["question needing resolution"]
}
返回有效的 JSON 格式."""

SAMPLE_TRANSCRIPT = """
Sarah: 好了各位，我们开始吧。今天是3号星期一，我们有 John、Mike 和 Lisa 参加。

John: 谢谢 Sarah。我主要想讨论的是 Q4 产品路线图。我们需要确定功能冻结日期。

Sarah: 我认为我们应该在11月15日之前冻结。这样 QA 在假日发布前有三周时间。

Mike: 我没问题。但我们还需要完成支付集成。Lisa，你那边的进展如何？

Lisa: 我大概完成了60%。我需要支付提供商的 API 文档。我已经发了两封邮件，但还没收到回复。

John: 我今天就去升级处理。我会联系 PaymentCo 的客户经理。这正在阻碍我们。

Sarah: 好的，那么 John 今天下班前会处理 PaymentCo 的升级事宜。Lisa 继续支付集成工作，目标在11月10日前完成。

Mike: 等 Lisa 准备好初稿后，我可以帮忙测试。假设我从11月11日开始测试。

Sarah: 很好。另外，我们决定从这个版本中砍掉社交登录功能。现在添加风险太大了。

John: 同意。我们会把它放到 Q1 的待办事项中。

Sarah: 还有其他阻碍吗？没有？好的。下周同一时间，11月10日见。
"""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def generate_meeting_notes(transcript: str) -> dict:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )
    messages = [
        SystemMessage(content=NOTES_PROMPT),
        HumanMessage(content=f"会议记录文本:\n\n{transcript}"),
    ]
    response = llm.invoke(messages)
    return parse_json_response(response.content)


def format_notes(notes: dict) -> str:
    lines = [
        f"# {notes.get('meeting_title', 'Meeting Notes')}",
        f"**日期:** {notes.get('date', date.today().isoformat())}  |  **持续时间:** {notes.get('duration_estimate', 'N/A')}",
        f"**参会人员:** {'、 '.join(notes.get('participants', []))}",
        "",
        "## Summary",
        notes.get("summary", ""),
        "",
        "## �键决策",
        *[f"- {d}" for d in notes.get("key_decisions", [])],
        "",
        "## 操作项",
    ]
    for item in notes.get("action_items", []):
        lines.append(f"- [ ] **{item.get('task', 'Task')}** — Owner: {item.get('owner', 'TBD')} | Due: {item.get('due', 'TBD')}")

    if notes.get("blockers"):
        lines += ["", "## 阻碍项", *[f"- {b}" for b in notes["blockers"]]]

    if notes.get("next_meeting") and notes["next_meeting"] != "TBD":
        lines += ["", f"**下次会议:** {notes['next_meeting']}"]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="会议纪要智能体")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--transcript", help="会议记录文本文件路径")
    group.add_argument("--text", help="会议记录文本直接")
    parser.add_argument("--output", default="会议纪要.md", help="Markdown 输出路径")
    args = parser.parse_args()

    if args.transcript:
        with open(args.transcript) as f:
            transcript = f.read()
        print(f"\n📝 处理: {args.transcript}\n")
    elif args.text:
        transcript = args.text
        print("\n📝 处理会议记录文本...\n")
    else:
        print("\n📝 使用样本会议记录文本\n")
        transcript = SAMPLE_TRANSCRIPT

    notes = generate_meeting_notes(transcript)
    formatted = format_notes(notes)

    print("=" * 60)
    print(formatted)
    print("=" * 60)

    # Save to file
    output_file = args.output
    if os.path.exists(output_file) and args.output == "meeting_notes.md":
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"会议纪要_{stamp}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted)
    print(f"\n✅ 保存到: {output_file}")


if __name__ == "__main__":
    main()
