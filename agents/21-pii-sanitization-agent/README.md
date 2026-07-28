# PII数据清理代理

在文本到达LLM或外部API**之前**，从中移除敏感数据。专为无法进行人工审核的自主代理管道而设计。

该代理使用Presidio库进行本地PII检测和清理，支持中文文本。检测并清理的敏感信息包括：电子邮件、电话、身份证号、银行账户、API密钥等，返回结构化的清理结果。

## 为什么这很重要

PII通过自主管道泄露是一个实际风险——代理将用户文本转发到LLM时，可能会意外暴露电子邮件、电话、税号或密钥。该代理作为安全护栏：先清理，再发送。

- 语义PII检测（准确率远高于仅使用正则表达式）
- 支持中文文本处理
- 安全关闭模式：发生任何错误时返回 `[REDACTED]`，绝不返回原始PII
- 审计追踪：代理不存储原始PII

## 快速开始

```bash
pip install -r requirements.txt
python agent.py --text "联系我：电话555-123-4567，邮箱a@b.com"
```

清理文件：

```bash
python agent.py --file input.txt
```

不提供参数时，运行内置演示：

```bash
python agent.py
```

## 示例输出

```json
{
  "status": "success",
  "sanitized_content": "你好，我是<PERSON>。我的邮箱是<EMAIL_ADDRESS>，电话是<PHONE_NUMBER>。账户号<REDACTED>。API密钥<REDACTED>。"
}
```

## 依赖

- Python
- spaCy中文模型 `zh_core_web_sm`
- Presidio Analyzer 和 Anonymizer

## 安装说明

```bash
pip install spacy presidio-analyzer presidio-anonymizer python-dotenv
python -m spacy download zh_core_web_sm
```

## 伦理考虑

- 原始输入不会被该代理存储。
- API错误时安全关闭——服务不可达时不会输出原始PII。
- 高风险部署（医疗、金融、法律）建议人工监督。
- 示例文本中包含的 `sk-abc123fakekeynotreal0000000000` 是**伪造**的测试数据，用于验证清理功能。

## 合规背景

适用于需要处理用户数据的代理间或代理到LLM的文本传输场景，符合GDPR、HIPAA等合规要求。

## 许可证

MIT（仓库根目录）。
