"""
Lesson 03: CrewAI + FastMCP Integration

Demonstrates:
- Building a FastMCP server that exposes tools
- Mirroring MCP server tools as CrewAI BaseTool wrappers
- Production pattern: keep tool contracts stable between MCP server and CrewAI wrappers

Architecture:
    MCP Server tool contracts → CrewAI tool wrappers → Output

Run the agent: python agent.py
Optional: run python mcp_server.py to inspect the matching FastMCP server tools.
"""

import asyncio
import json
import os
from datetime import datetime
from typing import Optional, Any

from crewai import Agent, Crew, Process, Task
from crewai.tools import BaseTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import Field

try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False

load_dotenv()

llm = "ollama/gemma4:e4b"

# MCP 服务器配置
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000")


class MCPClient:
    """MCP 客户端，用于调用 MCP 服务器上的工具"""
    
    def __init__(self, server_url: str = MCP_SERVER_URL):
        self.server_url = server_url
        self._available_tools: Optional[list] = None
    
    async def _call_mcp(self, tool_name: str, arguments: dict = None) -> Any:
        """调用 MCP 服务器上的工具"""
        if not HAS_HTTPX:
            raise ImportError("httpx 未安装，请运行: pip install httpx")
        
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments or {}
            }
        }
        
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.post(self.server_url, json=payload)
                response.raise_for_status()
                result = response.json()
                
                if "error" in result:
                    raise Exception(f"MCP 工具调用失败: {result['error'].get('message', '未知错误')}")
                
                return result.get("result", {}).get("content", "")
        except httpx.ConnectError:
            raise ConnectionError(f"无法连接到 MCP 服务器: {self.server_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MCP 服务器连接超时: {self.server_url}")
        except Exception as e:
            raise Exception(f"MCP 调用异常: {str(e)}")
    
    def call_tool(self, tool_name: str, arguments: dict = None) -> Any:
        """同步调用 MCP 服务器上的工具"""
        try:
            return asyncio.run(self._call_mcp(tool_name, arguments))
        except Exception as e:
            raise e


# 全局 MCP 客户端实例
mcp_client = MCPClient()


# CrewAI tool wrappers that mirror the FastMCP server's tool contracts.
# In production, replace these wrappers with a real MCP client adapter.
class DateTimeTool(BaseTool):
    name: str = "get_datetime"
    description: str = "获得当前日期和时间"

    def _run(self, query: str = "") -> str:
        """优先从 MCP 服务器获取当前日期时间，如果失败则使用本地实现"""
        try:
            # 优先尝试从 MCP 服务器获取
            result = mcp_client.call_tool("get_datetime")
            print(f"✅ DateTimeTool: 成功从 MCP 服务器获取数据")
            return result
        except (ConnectionError, TimeoutError, ImportError, Exception) as e:
            # 如果连接失败或获取失败，使用本地实现作为回退
            print(f"⚠️ DateTimeTool: MCP 服务器调用失败 ({str(e)}), 使用本地回退")
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

class JsonFormatterTool(BaseTool):
    name: str = "format_as_json"
    description: str = "将数据格式化为结构化JSON。输入：要格式化的数据的描述。"

    def _run(self, data_description: str) -> str:
        """优先从 MCP 服务器获取格式化后的 JSON，如果失败则使用本地实现"""
        try:
            # 优先尝试从 MCP 服务器获取
            # MCP 服务器的 format_as_json 接受 dict 参数
            result = mcp_client.call_tool("format_as_json", {
                "data": {
                    "formatted": True,
                    "timestamp": datetime.now().isoformat(),
                    "data": data_description,
                }
            })
            print(f"✅ JsonFormatterTool: 成功从 MCP 服务器获取数据")
            return result
        except (ConnectionError, TimeoutError, ImportError, Exception) as e:
            # 如果连接失败或获取失败，使用本地实现作为回退
            print(f"⚠️ JsonFormatterTool: MCP 服务器调用失败 ({str(e)}), 使用本地回退")
            return json.dumps({
                "formatted": True,
                "timestamp": datetime.now().isoformat(),
                "data": data_description,
            }, indent=2)


class TaskPrioritizerTool(BaseTool):
    name: str = "prioritize_tasks"
    description: str = "按重要性对任务列表进行优先级排序。输入：逗号分隔的任务列表。"

    def _run(self, tasks_csv: str) -> str:
        try:
            # 优先尝试从 MCP 服务器获取
            # MCP 服务器的 prioritize_tasks 接受 list[str] 参数
            result = mcp_client.call_tool("prioritize_tasks", {
                "tasks": tasks_csv.split(",")
            })
            print(f"✅ TaskPrioritizerTool: 成功从 MCP 服务器获取数据")
            return result
        except (ConnectionError, TimeoutError, ImportError, Exception) as e:
            # 如果连接失败或获取失败，使用本地实现作为回退
            print(f"⚠️ TaskPrioritizerTool: MCP 服务器调用失败 ({str(e)}), 使用本地回退")
            tasks = [t.strip() for t in tasks_csv.split(",")]
            prioritized = [{"rank": i + 1, "task": task, "priority": ["高", "中", "低"][i % 3]}
                        for i, task in enumerate(tasks)]
            return json.dumps(prioritized, indent=2)


# MCP-connected agent
mcp_agent = Agent(
    role="MCP驱动的工作流编排器",
    goal="使用MCP工具编排复杂工作流并生成结构化输出",
    backstory="""你是一个高级AI代理，拥有MCP（模型上下文协议）工具的访问权限。
    你擅长使用这些工具收集数据、格式化输出和优先处理工作。
    你总是生成结构化、可操作的结果。""",
    llm=llm,
    tools=[DateTimeTool(), JsonFormatterTool(), TaskPrioritizerTool()],
    verbose=True,
)

# Coordinator agent
coordinator = Agent(
    role="项目协调器",
    goal="协调任务并生成最终项目状态报告",
    backstory="经验丰富的项目经理，能够综合信息并生成清晰的状态报告。",
    llm=llm,
    verbose=True,
)


def run_mcp_workflow(project_name: str, tasks: list[str]) -> str:
    tasks_str = ", ".join(tasks)

    gather_task = Task(
        description=f"""对于项目"{project_name}"，使用你的MCP工具来：
        1. 使用get_datetime工具获取当前日期时间
        2. 使用prioritize_tasks工具对这些任务进行优先级排序：{tasks_str}
        3. 使用format_as_json工具将结果格式化为JSON

        返回所有收集到的信息。""",
        expected_output="当前时间、优先级排序后的任务列表和格式化数据",
        agent=mcp_agent,
    )

    report_task = Task(
        description=f"""使用收集到的数据为"{project_name}"创建项目状态报告。

        报告格式：
        - 项目：{project_name}
        - 生成时间：[数据中的时间戳]
        - 状态：进行中
        - 任务优先级矩阵：[使用已排序的任务]
        - 下一步行动：[最高优先级未完成任务]
        - 执行摘要：2-3句话

        使其专业且可操作。""",
        expected_output="专业的项目状态报告",
        agent=coordinator,
        context=[gather_task],
    )

    crew = Crew(
        agents=[mcp_agent, coordinator],
        tasks=[gather_task, report_task],
        process=Process.sequential,
        verbose=True,
    )

    return str(crew.kickoff())


if __name__ == "__main__":
    project = "AI 智能体平台 v2.0"
    tasks = [
        "实现RAG管道",
        "编写单元测试",
        "部署到预发布环境",
        "更新文档",
        "安全审计",
        "性能基准测试",
    ]

    print(f"\n🔗 为{project}项目运行 MCP驱动的AI 工作流\n")
    result = run_mcp_workflow(project, tasks)

    print("\n" + "=" * 60)
    print("项目状态报告:")
    print("=" * 60)
    print(result)
