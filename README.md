# Secure GenAI Gateway & MCP Server

![AWS](https://img.shields.io/badge/AWS-Serverless-orange) ![GenAI](https://img.shields.io/badge/AI-Bedrock-purple) ![Security](https://img.shields.io/badge/Security-Sanitization-green)

## 🤖 Project Overview
This project implements a **Secure GenAI Gateway** that acts as a centralized control plane for accessing Large Language Models (LLMs) like **Amazon Bedrock**. It enforces security policies, sanitizes inputs to prevent PII leakage, and implements **Model Context Protocol (MCP)** patterns to route requests effectively.

**Key Features:**
*   **Centralized Gateway**: Single API entry point for all internal AI consumption.
*   **Input Sanitization**: Python-based middleware to strip PII and block prompt injection attacks.
*   **Model Context Protocol (MCP)**: Structured routing to provide LLMs with necessary context and tools.
*   **Private Access**: Configured with Resource Policies to restrict access to Corporate VPNs.
*   **Serverless Architecture**: Built on AWS Lambda and API Gateway for infinite scaling and zero idle cost.

## 🏗️ Architecture
1.  **API Gateway**: Handles authentication and rate limiting.
2.  **Lambda Middleware**: Executes sanitization logic and MCP routing.
3.  **Amazon Bedrock**: Provides access to foundation models (Claude 3, Titan, etc.).

## 🛠️ Tech Stack
*   **Compute**: AWS Lambda (Python 3.9)
*   **API**: Amazon API Gateway (REST)
*   **AI Model**: Amazon Bedrock (Claude 3 Sonnet)
*   **IaC**: AWS SAM (Serverless Application Model)

## 📂 Repository Structure
```
├── src/
│   ├── lambda_function.py  # Core Logic (Sanitization + Bedrock Call)
│   └── requirements.txt    # Dependencies
├── template.yaml           # AWS SAM Infrastructure Definition
└── GenAI_Project_Guide.md  # Detailed Documentation
```

## 🔒 Security Features
*   **PII Redaction**: Automatically detects and blocks sensitive data patterns (SSN, Email).
*   **Prompt Firewall**: Prevents "Jailbreak" attempts via system prompt enforcement.
*   **Audit Logging**: Full request/response tracing in CloudWatch Logs.

## 🚀 Deployment
To deploy this stack using AWS SAM:
```bash
sam build
sam deploy --guided
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
