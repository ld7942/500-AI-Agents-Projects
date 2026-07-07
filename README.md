# 500+ AI Agent 项目与用例 （中文本地版本）

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/ld7942/500-AI-Agents-Projects?style=for-the-badge&color=yellow)](https://github.com/ld7942/500-AI-Agents-Projects/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/ld7942/500-AI-Agents-Projects?style=for-the-badge&color=blue)](https://github.com/ld7942/500-AI-Agents-Projects/network/members)
[![Contributors](https://img.shields.io/github/contributors/ld7942/500-AI-Agents-Projects?style=for-the-badge&color=green)](https://github.com/ld7942/500-AI-Agents-Projects/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](CONTRIBUTION.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ld7942/500-AI-Agents-Projects?style=for-the-badge)](https://github.com/ld7942/500-AI-Agents-Projects/commits/main)

**最全面的 AI Agent 项目、用例和可运行实现集合。**

## 项目源自
```bash
https://github.com/ashishpatel26/500-AI-Agents-Projects
```
**本项目进行本土化更改，所有依赖都采用免费开源或者本地部署。**

[🚀 快速开始](#-快速开始) • [🗺️ 浏览 Agent](#-按框架浏览) • [🏭 按行业分类](#-行业用例) • [🤝 贡献](#-贡献) • [📊 框架对比](#-框架对比)

</div>

---

![AI Agent Use Cases](images/AIAgentUseCase.jpg)

## 这是什么？

一个精心整理的 **500+ AI Agent 项目** 集合 —— 包含生产示例、教程和可运行代码，涵盖所有主要框架（LangGraph、CrewAI、AutoGen、Agno）和行业（医疗保健、金融、教育、网络安全等）。

**适用人群：**
- 🧑‍💻 **开发者** — 正在构建第一个或下一个 AI Agent
- 🔬 **研究者** — 调研 Agent 领域
- 🏢 **团队** — 评估用于生产环境的框架
- 🎓 **学生** — 从真实示例中学习 Agent 架构

---

## ⚡ 快速开始

选择一个框架，在 5 分钟内运行一个 Agent：

```bash
# 克隆仓库
git clone https://github.com/ld7942/500-AI-Agents-Projects.git
cd 500-AI-Agents-Projects

# 运行 agents/ 目录下的任意 agent
cd agents/01-web-research-agent
pip install -r requirements.txt
cp .env.example .env        # 添加你的 API 密钥
python agent.py
```

> `agents/` 目录下的所有 Agent 都是自包含的，拥有各自的 `requirements.txt` 和 `.env.example`。无需进行 monorepo 设置。

---

## 🗺️ 导航指南

| 我想... | 前往 |
|---|---|
| 立即运行一个可工作的 Agent | [`agents/`](agents/) |
| 按 AI 框架浏览 | [按框架分类用例](#-按框架浏览) |
| 按行业浏览 | [行业用例](#-行业用例) |
| 了解选择哪个框架 | [框架对比](#-框架对比) |
| 添加我自己的 Agent | [贡献指南](CONTRIBUTION.md) |
| 通过课程学习 | [`crewai_mcp_course/`](crewai_mcp_course/) |

---

## 📊 框架对比

选择框架？以下是使用场景指南：

| 框架 | 最佳用途 | 复杂度 | 多 Agent | 流式输出 | 本地 LLM |
|---|---|---|---|---|---|
| **LangGraph** | 有状态工作流、RAG 管道、复杂图 | ⭐⭐⭐ | ✅ | ✅ | ✅ |
| **CrewAI** | 基于角色的团队、业务自动化、快速原型 | ⭐⭐ | ✅ | ✅ | ✅ |
| **AutoGen** | 代码生成、研究、自修复工作流 | ⭐⭐⭐ | ✅ | ✅ | ✅ |
| **Agno** | 轻量级单 Agent、工具集成、快速迭代 | ⭐ | ✅ | ✅ | ✅ |
| **LlamaIndex** | 文档问答、企业级 RAG、数据管道 | ⭐⭐ | ⚠️ | ✅ | ✅ |

**快速决策指南：**
- 刚入门 → **Agno** 或 **CrewAI**
- 需要有状态图 + RAG → **LangGraph**
- 构建代码编写/研究 Agent → **AutoGen**
- 企业文档管道 → **LlamaIndex**

---

## 🏭 行业用例

![Industry Mind Map](images/industry_usecase1.png)

| 用例 | 行业 | 描述 | 代码 |
|---|---|---|---|
| **HIA（健康洞察 Agent）** | 医疗保健 | 分析医疗报告并提供健康洞察 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/harshhh28/hia.git) |
| **AI 健康助手** | 医疗保健 | 使用患者数据进行疾病诊断和监测 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/ahmadvh/AI-Agents-for-Medical-Diagnostics.git) |
| **自动化交易机器人** | 金融 | 通过实时市场分析实现股票交易自动化 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MingyuJ666/Stockagent.git) |
| **Agent Wallet SDK** | 金融 | 面向 AI Agent 的非托管智能合约钱包 SDK，支持强制消费限额 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/up2itnow0822/agent-wallet-sdk) |
| **虚拟 AI 导师** | 教育 | 提供个性化教育服务 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/hqanhh/EduGPT.git) |
| **24/7 AI 聊天机器人** | 客户服务 | 全天候处理客户咨询 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NirDiamant/GenAI_Agents/blob/main/all_agents_tutorials/customer_support_agent_langgraph.ipynb) |
| **产品推荐 Agent** | 零售 | 根据用户偏好和历史记录推荐产品 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/RecAI) |
| **自动驾驶配送 Agent** | 交通 | 优化路线并自主配送包裹 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sled-group/driVLMe) |
| **工厂流程监控 Agent** | 制造业 | 监控生产线并确保质量控制 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yuchenxia/llm4ias) |
| **房产定价 Agent** | 房地产 | 分析市场趋势以确定房产价格 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/AleksNeStu/ai-real-estate-assistant) |
| **智能农业助手** | 农业 | 提供作物健康和产量预测的洞察 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/mohammed97ashraf/LLM_Agri_Bot) |
| **能源需求预测 Agent** | 能源 | 预测能源使用以优化电网管理 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yecchen/MIRAI) |
| **内容个性化 Agent** | 娱乐 | 根据偏好推荐个性化媒体 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/crosleythomas/MirrorGPT) |
| **法律文档审查助手** | 法律 | 自动化文档审查并突出关键条款 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/firica/legalai) |
| **招聘推荐 Agent** | 人力资源 | 为职位空缺推荐最合适的候选人 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sentient-engineering/jobber) |
| **虚拟旅行助手** | 酒店旅游 | 根据偏好规划旅行行程 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/nirbar1985/ai-travel-agent) |
| **AI 游戏伙伴 Agent** | 游戏 | 通过实时辅助提升玩家体验 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/onjas-buidl/LLM-agent-game) |
| **实时威胁检测 Agent** | 网络安全 | 识别潜在威胁并缓解攻击 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NVISOsecurity/cyber-security-llm-agents) |
| **电商个人购物 Agent** | 电商 | 帮助客户找到心仪的产品 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/Hoanganhvu123/ShoppingGPT) |
| **物流优化 Agent** | 供应链 | 规划高效配送路线并管理库存 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/OptiGuide) |
| **Vibe Hacking Agent** | 网络安全 | 基于自主多 Agent 的红队测试服务 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/PurpleAILAB/Decepticon) |
| **Citadel** | 软件开发 | 编排 Claude Code Agent 集群，支持生命周期钩子、技能、活动管理和事后分析驱动架构 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/SethGammon/Citadel) |
| **MediSuite-AI-Agent** | 健康保险 | 自动化医院/保险理赔工作流 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/ahmedmansour5/MediSuite-Ai-Agent) |
| **Lina 埃及医疗聊天机器人** | 医疗保健 | 埃及医疗辅助聊天机器人 | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/dina-khalid/Lina-Egyptian-Medical-Chatbot) |

---

## 🔧 按框架浏览

### CrewAI

基于角色的多 Agent 框架。非常适合业务自动化。

| 用例 | 行业 | 描述 | GitHub |
|---|---|---|---|
| 📧 邮件自动回复流 | 通讯 | 根据预定义条件自动回复邮件 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/email_auto_responder_flow) |
| 📝 会议助手流 | 生产力 | 组织会议、安排日程和准备议程 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/meeting_assistant_flow) |
| 🔄 自我评估循环流 | 人力资源 | 促进绩效评估的自我评估 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/self_evaluation_loop_flow) |
| 📈 潜在客户评分流 | 销售 | 评估并评分潜在客户以优先联系 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/lead-score-flow) |
| 📊 营销策略生成器 | 营销 | 通过分析市场趋势制定营销策略 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/marketing_strategy) |
| 📝 职位发布生成器 | 招聘 | 通过分析职位要求创建职位发布 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting) |
| 🔄 招聘工作流 | 招聘 | 通过自动化招聘任务简化招聘流程 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/recruitment) |
| 🔍 匹配简历到职位 | 招聘 | 将候选人简历匹配到合适的职位 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/match_profile_to_positions) |
| 📸 Instagram 帖子生成器 | 社交媒体 | 自动生成和安排 Instagram 帖子 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/instagram_post) |
| 🌐 着陆页生成器 | 网页开发 | 自动创建网站着陆页 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator) |
| 🎮 游戏构建组 | 游戏开发 | 通过自动化创建流程辅助游戏开发 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/game-builder-crew) |
| 💹 股票分析工具 | 金融 | 提供股票市场数据分析工具 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis) |
| 🗺️ 旅行规划师 | 旅行 | 辅助规划旅行行程 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner) |
| 🎁 惊喜旅行规划师 | 旅行 | 根据用户偏好规划惊喜旅行 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/surprise_trip) |
| 📚 使用流程写书 | 创意写作 | 辅助作者进行结构化写作工作流 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/write_a_book_with_flows) |
| 🎬 剧本写作助手 | 创意写作 | 通过模板和指导辅助剧本写作 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/screenplay_writer) |
| ✅ Markdown 验证器 | 文档 | 验证 Markdown 文件的格式正确性 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/markdown_validator) |
| 🧠 Meta Quest 知识库 | 知识管理 | 管理 Meta Quest 知识以进行信息检索 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/meta_quest_knowledge) |
| 🤖 NVIDIA 模型集成 | AI 集成 | 将 NVIDIA AI 模型集成到工作流中 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/nvidia_models) |
| 🗂️ 会议准备 | 生产力 | 准备会议材料并设置议程 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/prep-for-a-meeting) |
| 🛠️ 入门模板 | 开发 | 用于新 CrewAI 项目的入门模板 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/starter_template) |
| 🔗 CrewAI + LangGraph 集成 | AI 集成 | CrewAI 与 LangGraph 之间的集成 | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/CrewAI-LangGraph) |

---

### AutoGen

微软的代码生成、执行和多 Agent 研究框架。

**代码生成、执行和调试**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 🤖 通过代码生成、执行和调试实现自动化任务解决 | 软件开发 | 演示通过生成、执行和调试代码实现自动化任务解决 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_auto_feedback_from_code_execution) |
| 🧑‍💻 使用检索增强 Agent 进行代码生成和问答 | 软件开发 | 使用检索增强方法生成代码并回答问题 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat) |
| 🧠 使用基于 Qdrant 的检索进行代码生成和问答 | 软件开发 | 利用 Qdrant 增强检索增强 Agent 的性能 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat_qdrant) |

**多 Agent 协作**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 🤝 群聊（3 名成员，1 名管理者） | 协作 | 演示通过多 Agent 协作解决群组任务 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat) |
| 📊 通过群聊进行数据可视化 | 数据分析 | 使用多 Agent 协作创建数据可视化 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_vis) |
| 🧩 通过群聊解决复杂任务（6 名成员） | 协作 | 通过更大规模的群组协作解决复杂任务 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_research) |
| 🧑‍💻 使用编码和规划 Agent 解决任务 | 规划与开发 | 结合编码和规划 Agent 解决任务 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_planning.ipynb) |
| 📐 使用图转换路径解决任务 | 协作 | 使用图中的预定义转换路径解决任务 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/docs/notebooks/agentchat_groupchat_finite_state_machine) |
| 🧠 SocietyOfMindAgent 内心独白 | 认知科学 | 使用群聊模拟内心独白进行问题解决 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_society_of_mind) |
| 🔧 自定义发言者选择的群聊 | 协作 | 实现自定义发言者选择功能 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_customized) |

**顺序多 Agent 对话**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 🔄 顺序任务解决（单个发起 Agent） | 工作流自动化 | 使用单个发起 Agent 自动化顺序任务解决 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_chats) |
| ⏳ 异步顺序任务解决 | 工作流自动化 | 在一系列对话中处理异步任务解决 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_async_chats) |
| 🤝 使用不同发起 Agent 的顺序对话 | 工作流自动化 | 使用不同 Agent 发起每个对话的顺序任务解决 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchats_sequential_chats) |

**嵌套对话**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 🧠 使用嵌套对话解决复杂任务 | 问题解决 | 使用嵌套对话解决分层和复杂问题 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat) |
| 🔄 嵌套对话序列 | 问题解决 | 演示使用嵌套对话进行顺序任务解决 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_sequential_chats) |
| 🏭 使用嵌套对话的 OptiGuide 供应链 | 供应链 | 使用嵌套对话解决供应链优化问题 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat_optiguide) |
| ♟️ 使用嵌套对话的对话式国际象棋 | 游戏 | 使用嵌套对话和工具进行对话式国际象棋 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_chats_chess) |

**工具**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 🌐 网络搜索：解决需要网络信息的任务 | 信息检索 | 搜索网络以收集完成任务所需的信息 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_web_info.ipynb) |
| 🔧 使用提供的工具作为函数 | 工具集成 | 演示如何将预提供的工具用作可调用函数 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_function_call_currency_calculator) |
| 📚 RAG 群聊 | 协作 | 支持检索增强生成的群聊 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_RAG) |
| 🔊 使用 Whisper 的 Agent 对话 | 音频处理 | 使用 Whisper 进行转录和翻译的 AI Agent | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_video_transcript_translate_with_whisper) |
| 📊 SQL：自然语言到 SQL 查询 | 数据库管理 | 将自然语言输入转换为 SQL 查询 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_sql_spider.ipynb) |

**多模态 Agent**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 🎨 带有 DALLE 和 GPT-4V 的多模态 Agent | 多媒体 AI | 结合 DALLE 和 GPT-4V 进行多模态 Agent 通信 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_dalle_and_gpt4v.ipynb) |
| 🖌️ 带有 Llava 的多模态 Agent | 图像处理 | 使用 Llava 进行多模态 Agent 对话 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_lmm_llava.ipynb) |
| 🖼️ 带有 GPT-4V 的多模态 Agent | 多媒体 AI | 利用 GPT-4V 进行视觉和对话交互 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_lmm_gpt-4v.ipynb) |

**可观测性与评估**

| 用例 | 行业 | 描述 | Notebook |
|---|---|---|---|
| 📊 AgentEval：多 Agent 评估系统 | 性能评估 | 评估基于 LLM 的应用程序实用性 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agenteval_cq_math.ipynb) |
| 📊 使用 AgentOps 跟踪 LLM 调用和错误 | 监控与分析 | 监控 LLM 交互、工具使用和错误 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentops.ipynb) |
| 🏗️ 使用 AgentBuilder 自动构建多 Agent 系统 | AI 开发 | 自动构建多 Agent 系统 | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/autobuild_basic.ipynb) |

---

### Agno

轻量级、快速的 Agent 框架。最适合单 Agent 工具和快速原型开发。

| 用例 | 行业 | 描述 | 代码 |
|---|---|---|---|
| 🤖 支持 Agent | AI 框架支持 | 为 Agno 框架提供实时答案、解释和代码示例 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/agno_support_agent.py) |
| 🎥 YouTube Agent | 媒体与内容 | 分析 YouTube 视频：摘要、时间戳、主题 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/youtube_agent.py) |
| 📊 金融 Agent（思考） | 金融 | 实时股票洞察、分析师推荐、金融深度分析 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/thinking_finance_agent.py) |
| 📚 学习伙伴 | 教育 | 查找资源、回答问题、创建学习计划 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/study_partner.py) |
| 🛍️ 购物伙伴 Agent | 电商 | 基于亚马逊、Flipkart 偏好的产品推荐器 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/shopping_partner.py) |
| 🎓 研究学者 Agent | 教育/研究 | 高级学术搜索、出版物分析、结构化报告 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent_exa.py) |
| 🧠 研究 Agent | 媒体与新闻 | 深度调查、NYT 风格报告 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent.py) |
| 🍳 食谱创建器 | 食品与烹饪 | 基于食材和偏好的个性化食谱 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/recipe_creator.py) |
| 🧠 金融推理 Agent | 金融 | 基于 Claude 3.5 Sonnet 和 Yahoo Finance 数据的股票分析 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/reasoning_finance_agent.py) |
| 🤖 README 生成 Agent | 软件开发 | 为 GitHub 仓库生成高质量 README | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/readme_generator.py) |
| 🎬 电影推荐 Agent | 娱乐 | 使用 Exa 和 GPT-4o 的个性化电影推荐 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/movie_recommedation.py) |
| 🔍 媒体趋势分析 Agent | 媒体与新闻 | 分析数字平台的新兴趋势和影响者 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/media_trend_analysis_agent.py) |
| ⚖️ 法律文档分析 Agent | 法律科技 | 使用向量嵌入分析法律 PDF 并提供洞察 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/legal_consultant.py) |
| 🤔 DeepKnowledge | 研究 | 通过深度推理迭代搜索知识库 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/deep_knowledge.py) |
| 📚 书籍推荐 Agent | 出版与媒体 | 使用文学数据和读者偏好的个性化书籍推荐 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/book_recommendation.py) |
| 🏠 MCP Airbnb Agent | 酒店旅游 | 使用 MCP 和 Llama 4 搜索 Airbnb 房源 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/airbnb_mcp.py) |
| 🤖 Agno Assist Agent | AI 框架 | 用于 Agno 框架问答的 GPT-4o Agent，支持混合搜索 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/agno_assist.py) |

---

### LangGraph

用于复杂、有状态 Agent 工作流和 RAG 管道的状态机框架。

| 用例 | 行业 | 描述 | 代码 |
|---|---|---|---|
| 🤖 聊天机器人模拟评估 | AI / QA | 模拟用户交互以评估聊天机器人性能 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation.ipynb) |
| 🧠 通过提示收集信息 | 研究 | 使用提示收集信息的 LangGraph 工作流 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbots/information-gather-prompting.ipynb) |
| 🧠 使用 LangGraph 的代码助手 | 软件开发 | 具有错误检查和迭代优化的弹性代码助手 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/code_assistant/langgraph_code_assistant.ipynb) |
| 🧑‍💼 客户支持 Agent | 客户支持 | 基于图的 Agent，用于处理客户咨询 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/customer-support/customer-support.ipynb) |
| 🔁 带重试的提取 | 数据提取 | 用于稳健数据提取的重试机制 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/extraction/retries.ipynb) |
| 🧠 多 Agent 工作流（主管） | 工作流编排 | 主管 Agent 编排多个专业 Agent | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.ipynb) |
| 🧠 分层 Agent 团队 | 工作流编排 | 顶层主管将任务委托给专业子 Agent | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/hierarchical_agent_teams.ipynb) |
| 🤝 多 Agent 协作 | 工作流编排 | 多个专业 Agent 共同解决复杂任务 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/multi-agent-collaboration.ipynb) |
| 🧠 计划与执行 Agent | 工作流编排 | Agent 生成多步骤计划然后按顺序执行 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb) |
| 🧠 SQL Agent | 数据库交互 | Agent 回答关于 SQL 数据库的问题 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/sql-agent.ipynb) |
| 🧠 反思 Agent | 工作流编排 | Agent 批评和修改自己的输出 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflection/reflection.ipynb) |
| 🧠 Reflexion Agent | 工作流编排 | Agent 反思行动以进行迭代改进 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflexion/reflexion.ipynb) |
| 🧠 自适应 RAG | 信息检索 | 根据查询复杂度动态调整检索 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag.ipynb) |
| 🤖 Agentic RAG | 智能 Agent | Agent 在生成响应之前确定最佳检索策略 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_agentic_rag.ipynb) |
| 🧠 纠正性 RAG (CRAG) | 信息检索 | 在生成之前评估和优化检索到的文档 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_crag.ipynb) |
| 🧠 Self-RAG | 信息检索 | 系统反思响应并在需要时检索额外信息 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_self_rag.ipynb) |
| 🧠 自适应 RAG（本地） | 信息检索 | 使用本地模型的自适应 RAG，支持离线使用 | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag_local.ipynb) |
| 🧠 Self-RAG（本地） | 信息检索 | 使用本地模型和数据源的 Self-RAG | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_self_rag_local.ipynb) |

---

## 🤝 贡献

欢迎贡献！🎉 本仓库通过社区贡献不断成长。

**贡献方式：**
1. **添加可运行的 Agent** — 在 `agents/` 目录中创建一个包含可运行代码的文件夹
2. **添加外部链接** — 在行业或框架表格中添加一行
3. **修复损坏的链接** — 打开 issue 或 PR
4. **改进文档** — 修复拼写错误、添加上下文、改进示例

**贡献步骤：**
1. Fork 仓库
2. 创建分支：`feat/agent-name` 或 `fix/description`
3. 按照 [贡献指南](CONTRIBUTION.md) 添加您的更改
4. 使用 PR 模板打开 PR

有关完整要求（metadata.yaml、requirements.txt 等），请参阅 [CONTRIBUTION.md](CONTRIBUTION.md)。

---

## Star 历史

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://api.star-history.com/svg?repos=ld7942/500-AI-Agents-Projects&type=date&legend=top-left"
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://api.star-history.com/svg?repos=ld7942/500-AI-Agents-Projects&type=date&legend=top-left"
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=ld7942/500-AI-Agents-Projects&type=date&legend=top-left"
  />
</picture>

---

## 📜 许可证

本仓库采用 MIT 许可证。有关更多信息，请参阅 [LICENSE](LICENSE) 文件。

---

<div align="center">

**⭐ 如果您觉得本仓库有用，请为它点赞 — 这有助于其他人发现它！**

[报告问题](https://github.com/ld7942/500-AI-Agents-Projects/issues) • [请求 Agent](https://github.com/ld7942/500-AI-Agents-Projects/issues/new?template=feature_request.md) • [贡献](CONTRIBUTION.md)

</div>