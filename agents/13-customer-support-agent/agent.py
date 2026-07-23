"""
使用 LangGraph 和 RAG 的客户支持智能体。

利用知识库（产品文档）处理客户查询。
将复杂问题路由至人工升级处理。

使用方法：
    python agent.py
    python agent.py --kb-dir docs/          # 加载自定义知识库
"""

import argparse
import os
from pathlib import Path
from typing import Annotated, Literal, TypedDict

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

load_dotenv()

SAMPLE_KB = [
    "产品：CloudSync Pro。功能：支持5台设备实时同步，1TB存储空间，离线模式，30天版本历史。",
    "定价：基础版 $9/月（100GB，2台设备），专业版 $19/月（1TB，5台设备），商业版 $49/月（5TB，无限设备）。",
    "取消订阅：随时可在 账户 > 订阅 > 取消 中取消。付款后14天内可申请退款。",
    "密码重置：前往登录页面，点击'忘记密码'，输入邮箱。重置链接1小时内有效。",
    "同步问题：检查网络连接，确保应用已更新，尝试退出并重新登录。如问题持续，请联系客服。",
    "支持平台：Windows 10+、macOS 12+、iOS 15+、Android 10+、Linux（测试版）。",
    "数据安全：静态和传输过程中均采用AES-256加密。已通过SOC 2 Type II认证。零知识架构。",
    "文件大小限制：单个文件最大10GB（专业版/商业版），2GB（基础版）。文件总数无限制。",
]

ESCALATION_KEYWORDS = ["退款", "诉讼", "愤怒", "欺诈", "损坏", "数据丢失", "取消订阅", "收费", "计费错误"]


class SupportState(TypedDict):
    messages: Annotated[list, add_messages]
    user_input: str
    retrieved_context: str
    response: str
    escalate: bool


def retrieve_context(state: SupportState) -> SupportState:
    query = state["user_input"]
    if not hasattr(retrieve_context, "vectorstore"):
        texts = getattr(retrieve_context, "kb_texts", SAMPLE_KB)
        splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
        docs_split = splitter.create_documents(texts)
        embeddings = OllamaEmbeddings(
            model= "embeddinggemma",
            base_url="http://localhost:11434",
        )
        try:
            retrieve_context.vectorstore = FAISS.from_documents(docs_split, embeddings)
        except Exception as e:
            print(f"创建向量数据库失败: {e}")
            return {"retrieved_context": ""}

    docs = retrieve_context.vectorstore.similarity_search(query, k=3)
    context = "\n".join(d.page_content for d in docs)
    return {"retrieved_context": context}


def check_escalation(state: SupportState) -> SupportState:
    text = state["user_input"].lower()
    needs_escalation = any(kw in text for kw in ESCALATION_KEYWORDS)
    return {"escalate": needs_escalation}


def generate_response(state: SupportState) -> SupportState:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0.2,
        timeout=300
    )
    conversation = state["messages"][:-1]  # exclude latest user msg

    if state.get("escalate"):
        response_text = "我理解您的关注，我想确保这得到适当的关注。我会将您连接到一位资深的支持专家，他们可以直接直接解决这个问题。您将在2小时内收到回复。您的案件ID为：" + str(hash(state["user_input"]) % 100000)
    else:
        messages = [
            SystemMessage(content=f"""您是一个CloudSync Pro的客户支持智能体。
使用此知识库上下文准确回答:
{state['retrieved_context']}

，请友好、简洁、解决方案为导向。如果不确定，请诚实回答."""),
            *conversation,
            HumanMessage(content=state["user_input"]),
        ]
        response = llm.invoke(messages)
        response_text = response.content

    return {"response": response_text, "messages": [AIMessage(content=response_text)]}


def route_after_escalation_check(state: SupportState) -> Literal["generate", "generate"]:
    return "generate"


def build_graph():
    graph = StateGraph(SupportState)
    graph.add_node("retrieve", retrieve_context)
    graph.add_node("check_escalation", check_escalation)
    graph.add_node("generate", generate_response)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "check_escalation")
    graph.add_edge("check_escalation", "generate")
    graph.add_edge("generate", END)
    return graph.compile()


def load_kb_texts(kb_dir: str | None) -> list[str]:
    if not kb_dir:
        return SAMPLE_KB

    root = Path(kb_dir)
    if not root.is_dir():
        raise ValueError(f"知识库目录不存在: {kb_dir}")

    texts = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".txt", ".md"}:
            texts.append(path.read_text(encoding="utf-8"))

    if not texts:
        raise ValueError(f"知识库目录中没有找到.txt或.md文件: {kb_dir}")

    return texts


def main():
    parser = argparse.ArgumentParser(description="CloudSync Pro客户支持智能体")
    parser.add_argument("--kb-dir", help="包含支持知识库的目录")
    args = parser.parse_args()

    retrieve_context.kb_texts = load_kb_texts(args.kb_dir)
    if hasattr(retrieve_context, "vectorstore"):
        delattr(retrieve_context, "vectorstore")

    agent = build_graph()
    state = {"messages": [], "user_input": "", "retrieved_context": "", "response": "", "escalate": False}

    print("\n🎧 CloudSync Pro客户支持智能体")
    print("输入'quit退出\n")

    while True:
        user_input = input("客户: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        state["user_input"] = user_input
        state["messages"].append(HumanMessage(content=user_input))
        state = agent.invoke(state)

        escalation_indicator = " [ESCALATED]" if state.get("escalate") else ""
        print(f"\nAgent{escalation_indicator}: {state['response']}\n")


if __name__ == "__main__":
    main()
