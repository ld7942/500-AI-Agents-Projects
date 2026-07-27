"""
Multi-Agent Debate System using AutoGen-style orchestration.

Two AI agents debate a topic from opposing sides, moderated by a judge
who declares a winner and synthesizes the key arguments.

Usage:
    python agent.py --topic "AI will eliminate more jobs than it creates"
    python agent.py --topic "Remote work is better than office work" --rounds 3
"""

import argparse
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()


class DebateAgent:
    def __init__(self, name: str, position: str, expertise: str):
        self.name = name
        self.position = position
        self.expertise = expertise
        self.llm =  ChatOpenAI(
            model="gemma4:e4b",
            base_url="http://localhost:11434/v1",
            api_key="langchain_learn_arthur",
            temperature=0.6,
            timeout=300
        )
        self.arguments = []

    def make_argument(self, topic: str, round_num: int, opponent_last_arg: str = "") -> str:
        system_msg = f"""你是 {self.name}, 一个 {self.expertise}.
你正在为 {self.position} on this topic.
你正在为 {self.position} 基于证据的有说服力的论点。
保持响应在150字以内,用中文回答。第 {round_num} 轮."""

        if opponent_last_arg:
            user_msg = f"主题: {topic}\n\n对手说: '{opponent_last_arg}'\n\n继续你的论点:"
        else:
            user_msg = f"主题: {topic}\n\n为你的打开论点 {self.position.upper()}:"

        response = self.llm.invoke([
            SystemMessage(content=system_msg),
            HumanMessage(content=user_msg),
        ])
        argument = response.content
        self.arguments.append(argument)
        return argument


class DebateJudge:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gemma4:e4b",
            base_url="http://localhost:11434/v1",
            api_key="langchain_learn_arthur",
            temperature=0,
            timeout=300
        )
        self.name = "Judge"
        self.expertise = "辩论评估员"

    def evaluate(self, topic: str, pro_agent: DebateAgent, con_agent: DebateAgent) -> dict:
        pro_args = "\n\n".join(f"第 {i+1} 轮: {a}" for i, a in enumerate(pro_agent.arguments))
        con_args = "\n\n".join(f"第 {i+1} 轮: {a}" for i, a in enumerate(con_agent.arguments))

        response = self.llm.invoke([
            SystemMessage(content="""你是 {self.name}, 一个 {self.expertise}.
你正在为 {topic} 两个论点。
返回一个结构化的判断，包含：赢家、每个论点的分数（每个论点10分）、每个论点的最强论点、关键洞察力、平衡的综合结论."""),
            HumanMessage(content=f"""主题: "{topic}"

PRO arguments ({pro_agent.name}):
{pro_args}

CON arguments ({con_agent.name}):
{con_args}

返回你的判断:"""),
        ])
        return {"verdict": response.content}


def run_debate(topic: str, rounds: int = 2) -> None:
    pro = DebateAgent(
        name="Dr. Alex Chen",
        position="FOR",
        expertise="technology economist and AI researcher"
    )
    con = DebateAgent(
        name="Prof. Sarah Martinez",
        position="AGAINST",
        expertise="labor economist and social policy expert"
    )
    judge = DebateJudge()

    print(f"\n{'='*60}")
    print(f"⚖️  论论主题: {topic}")
    print(f"{'='*60}")
    print(f"🟢 FOR: {pro.name} ({pro.expertise})")
    print(f"🔴 AGAINST: {con.name} ({con.expertise})")
    print(f"🏛️  轮数: {rounds}")
    print("=" * 60)

    last_con_arg = ""
    last_pro_arg = ""
    
    for round_num in range(1, rounds + 1):
        print(f"\n--- 第 {round_num} 轮 ---\n")

        pro_arg = pro.make_argument(topic, round_num, last_con_arg)
        print(f"🟢 {pro.name} (FOR):")
        print(pro_arg)

        con_arg = con.make_argument(topic, round_num, pro_arg)
        print(f"\n🔴 {con.name} (AGAINST):")
        print(con_arg)

        last_pro_arg = pro_arg
        last_con_arg = con_arg

    print(f"\n{'='*60}")
    print("🏛️  判决的判断")
    print("=" * 60)
    verdict = judge.evaluate(topic, pro, con)
    print(verdict["verdict"])


def main():
    parser = argparse.ArgumentParser(description="智能体辩论系统（多智能体）")
    parser.add_argument("--topic", default="AI 将创建更多工作岗位而不是消除工作岗位", help="辩论主题")
    parser.add_argument("--rounds", type=int, default=2, help="轮数 (1-4)")
    args = parser.parse_args()

    rounds = max(1, min(4, args.rounds))
    run_debate(args.topic, rounds)


if __name__ == "__main__":
    main()
