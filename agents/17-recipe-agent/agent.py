"""
Recipe Recommendation Agent using Agno-style single agent.

Suggests recipes based on available ingredients, dietary restrictions,
and time constraints.

Usage:
    python agent.py --ingredients "chicken, garlic, lemon, rosemary"
    python agent.py --ingredients "tofu, broccoli, soy sauce" --diet vegan --time 20
"""

import argparse
import json
import os
import re

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

RECIPE_PROMPT = """你是一个专业的厨师和营养师. 给定可用的食材和约束条件，建议 3 个食谱。返回 JSON 格式：
{
  "食谱": [
    {
      "名称": "食谱名称",
      "美食类型": "意大利/亚洲/等",
      "难度": "简单/中等/困难",
      "准备时间": "X minutes",
      "烹饪时间": "X minutes",
      "份量": N,
      "食材": ["成分 (数量)"],
      "缺少食材": ["可选步骤"],
      "步骤": ["步骤 1: ...", "步骤 2: ..."],
      "营养信息": {"卡路里": N, "蛋白质": "Xg", "碳水化合物": "Xg", "脂肪": "Xg"},
      "提示": "厨师提示"
    }
  ],
  "推荐": "食谱名称 (最佳匹配项)"
}
仅返回有效的 JSON."""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def get_recipes(ingredients: list[str], diet: str, time_limit: int, servings: int) -> dict:
    llm = ChatOpenAI(
        model="gemma4:e4b",
        base_url="http://localhost:11434/v1",
        api_key="langchain_learn_arthur",
        temperature=0,
        timeout=300
    )

    constraints = []
    if diet:
        constraints.append(f"饮食限制: {diet}")
    if time_limit:
        constraints.append(f"最大总时间: {time_limit} minutes")
    if servings:
        constraints.append(f"需要的份量: {servings}")

    messages = [
        SystemMessage(content=RECIPE_PROMPT),
        HumanMessage(content=f"可用食材: {', '.join(ingredients)}\n\n约束条件:\n{chr(10).join(constraints) if constraints else 'None'}"),
    ]

    response = llm.invoke(messages)
    return parse_json_response(response.content)


def display_recipe(recipe: dict):
    print(f"\n🍽️  {recipe.get('名称', '食谱')} ({recipe.get('美食类型', 'N/A')})")
    print(f"⏱️  准备时间: {recipe.get('准备时间', 'N/A')} | 烹饪时间: {recipe.get('烹饪时间', 'N/A')} | 难度: {recipe.get('难度', 'N/A')}")
    print(f"👥 份量: {recipe.get('份量', 'N/A')}")
    print(f"\n📝 成分:")
    for ing in recipe.get("食材", []):
        print(f"  • {ing}")
    if recipe.get("缺少食材"):
        print(f"\n➕ 可选步骤: {', '.join(recipe['缺少食材'])}")
    print(f"\n👨‍🍳 方法:")
    for i, step in enumerate(recipe.get("步骤", []), 1):
        print(f"  {i}. {step}")
    n = recipe.get("营养信息", {})
    if n:
        print(f"\n🥗 营养信息: {n.get('卡路里', '?')} cal | 蛋白质: {n.get('蛋白质', '?')} | 碳水化合物: {n.get('碳水化合物', '?')} | 脂肪: {n.get('脂肪', '?')}")
    if recipe.get("提示"):
        print(f"\n💡 提示信息: {recipe['提示']}")


def main():
    parser = argparse.ArgumentParser(description="饮食建议食谱智能体")
    parser.add_argument("--ingredients", default="鸡胸肉, 葱, 柠檬, 油油, 草莓, 土豆", help="可用食材")
    parser.add_argument("--diet", default="", help="饮食限制")
    parser.add_argument("--time", type=int, default=0, help="最大总时间")
    parser.add_argument("--servings", type=int, default=2, help="需要的份量")
    args = parser.parse_args()

    ingredients = [i.strip() for i in args.ingredients.split(",")]
    print(f"\n🍽 用以下成分寻找食谱: {', '.join(ingredients)}")
    if args.diet:
        print(f"🥗 饮食限制: {args.diet}")
    if args.time:
        print(f"⏱️  最大总时间: {args.time} minutes")

    result = get_recipes(ingredients, args.diet, args.time, args.servings)

    print("\n" + "=" * 60)
    recipes = result.get("食谱", [])
    recommended = result.get("推荐") or (recipes[0].get("名称", "N/A") if recipes else "N/A")
    print("✅ 推荐:", recommended)
    print("=" * 60)

    for recipe in recipes:
        display_recipe(recipe)
        print("\n" + "-" * 40)


if __name__ == "__main__":
    main()
