# -*- coding: utf-8 -*-
"""
PII数据清理代理 — TrustBoost API客户端。

在文本到达LLM或外部API之前，从中移除敏感数据（电子邮件、电话、身份证号、银行账户、
API密钥）。专为无法进行人工审核的自主代理管道而设计。

这是一个轻量级客户端：清理逻辑、模型和链上证明都在TrustBoost API后端运行。该代理展示了
隐私/安全模式 — 在调用LLM之前，对任何用户文本调用此代理。

使用方法：
    python agent.py --text "Call me at 555-123-4567, email a@b.com"
    python agent.py --file input.txt
    python agent.py   # 运行内置演示

当未设置API密钥/tx_hash时，使用免费试用版（50次清理）。
"""
import argparse
import os
import sys
import json
import spacy

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

def sanitize(text: str) -> dict:
    """将文本发送到prompt_armor并返回清理后的结果。

    参数:
        text: 可能包含PII的原始文本
    """
    try:
        configuration = {
            "nlp_engine_name": "spacy",
            "models": [
                {"lang_code": "zh", "model_name": "zh_core_web_sm"} # 指定你下载好的中文模型
            ]
        }
        provider = NlpEngineProvider(nlp_configuration=configuration)
        nlp_engine = provider.create_engine()
        analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["zh"])
        analyzer_results = analyzer.analyze(text, language="zh")
        anonymizer = AnonymizerEngine()
        ret = anonymizer.anonymize(text=text, analyzer_results=analyzer_results)
        return {
            "status": "success",
            "sanitized_content": ret.text,
        }
    except Exception as e:
        # Fail closed: do NOT return raw PII on transport error.
        print(e)
        return {
            "status": "error",
            "risk_category": "CRITICAL",
            "sanitized_content": "[REDACTED — 清理服务不可用]",
            "error": str(e),
        }


DEMO_TEXT = '''
你好，我是胡安·佩雷斯。我的邮箱是juan.perez@example.com，电话是+1-555-123-4567。RFC编号：PEMJ880126MNEZSN01。账户号0123456789。API密钥sk-abc123fakekeynotreal0000000000。
'''


def main():
    ap = argparse.ArgumentParser(description="PII数据清理代理 —  TrustBoost API客户端")
    ap.add_argument("--text", help="要清理的文本")
    ap.add_argument("--file", help="要清理的文本文件路径")

    args = ap.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        text = DEMO_TEXT
        print("未提供--text/--file参数。运行内置演示。\n")

    print("输入 :", text[:120] + ("..." if len(text) > 120 else ""))
    result = sanitize(text)
    print("\n清理结果 :")
    print(json.dumps(result, indent=2, ensure_ascii=False)[:800])


if __name__ == "__main__":
    main()