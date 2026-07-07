"""
PDF Q&A Agent using LlamaIndex.

Loads a PDF, indexes it, and answers questions about its content.
Maintains conversation history for follow-up questions.

Usage:
    python agent.py --pdf path/to/document.pdf
    python agent.py --pdf report.pdf --question "What is the main finding?"
"""

import argparse
import os

from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.readers.file import PDFReader


import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

Settings._llm = Ollama(model="gemma4:e4b")
Settings._embed_model = OllamaEmbedding(model_name="embeddinggemma")

load_dotenv()


def build_index(pdf_path: str) -> VectorStoreIndex:
    parser = PDFReader(return_full_document=False)  # 默认为 False，按页返回
    file_extractor = {".pdf": parser}

    print(f"📄 读取并索引 PDF {pdf_path}...")
    reader = SimpleDirectoryReader(input_files=[pdf_path], file_extractor=file_extractor)
    docs = reader.load_data()
    index = VectorStoreIndex.from_documents(docs, callback_manager=Settings.callback_manager)
    print(f"✅ 索引完成 {len(docs)} chunk(s)")
    return index


def interactive_qa(index: VectorStoreIndex):
    llm = Settings._llm
    memory = ChatMemoryBuffer.from_defaults(token_limit=4096)
    chat_engine = index.as_chat_engine(
        chat_mode="context",
        llm=llm,
        memory=memory,
        verbose=False,
    )

    print("\n💬 PDF Q&A 智能体已准备就绪。输入 'quit' 退出。\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "q"):
            break
        if not question:
            continue
        response = chat_engine.chat(question)
        print(f"\n智能体: {response.response}\n")


def single_question(index: VectorStoreIndex, question: str):
    query_engine = index.as_query_engine(similarity_top_k=5)
    response = query_engine.query(question)
    print("\n" + "=" * 60)
    print("📋 答案")
    print("=" * 60)
    print(response.response)
    if hasattr(response, "source_nodes"):
        print(f"\n📚 引用的 chunk(s): {len(response.source_nodes)}")


def main():
    parser = argparse.ArgumentParser(description="PDF Q&A 智能体")
    parser.add_argument("--pdf", required=True, help="要查询的 PDF 文件路径")
    parser.add_argument("--question", help="要查询的问题（可选），用于交互式模式")
    args = parser.parse_args()

    index = build_index(args.pdf)

    if args.question:
        single_question(index, args.question)
    else:
        interactive_qa(index)


if __name__ == "__main__":
    main()
