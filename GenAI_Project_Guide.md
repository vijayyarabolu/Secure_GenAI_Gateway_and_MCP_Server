# Project 3: Secure GenAI Gateway & MCP Server
**Master Timeline Date: March 2024**

## 📚 Module 1: The GenAI Revolution & Platform Engineering
**"Why are we building this?"**

In 2024, every company wants to use LLMs (Large Language Models) like GPT-4 or Claude.
However, giving every developer direct access to OpenAI or AWS Bedrock is:
1.  **Unsafe**: They might send PII (Personally Identifiable Information) to the model.
2.  **Expensive**: No cost controls.
3.  **Chaotic**: No logs of who asked what.

**Your Solution**: A Centralized GenAI Gateway.
*   **You build**: A single API that everyone in the company must use.
*   **You control**: Security, Logging, and Cost.

---

## 📚 Module 2: The Architecture (Serverless)
We will use **AWS Serverless** because it scales to zero (costs nothing when no one uses it).

1.  **API Gateway**: The front door. It handles authentication (API Keys).
2.  **Lambda (Python)**: The brain. It:
    *   Receives the user's prompt.
    *   **Sanitizes it** (removes bad words or secrets).
    *   Calls **Amazon Bedrock** (the LLM).
    *   Logs the interaction to CloudWatch.
3.  **Amazon Bedrock**: The AWS service that hosts models like Claude 3 and Titan.

---

## 📚 Module 3: What is "MCP"?
**Model Context Protocol (MCP)** is a new standard.
Instead of just "asking a question", an MCP server can "give tools" to the AI.
*   *Example*: "Check the database for user X."
*   The AI can't check the DB itself. It asks the MCP server to do it.
*   We will build a simple version of this: A structured way to ask the AI to perform tasks.

---

## 📚 Module 4: Implementation Plan
1.  **Infrastructure**: Define the Lambda and API Gateway in `template.yaml` (SAM).
2.  **Code**: Write the Python logic in `lambda_function.py`.
3.  **Git History**: We will commit this with **March 2024** dates.

---

## 📚 Module 5: How to Deploy (AWS SAM)
**"How do I put this on the cloud?"**

For Project 4, we used CloudFormation directly. For this project, we use **AWS SAM (Serverless Application Model)**. It is a tool specifically for Lambda.

### Prerequisites
1.  Install AWS CLI and SAM CLI.
2.  Run `aws configure` to set your credentials.

### The Deployment Commands
Run these in your terminal (inside the `Secure_GenAI_Gateway` folder):

#### 1. Build
This packages your Python code and installs dependencies.
```bash
sam build
```

#### 2. Deploy
This uploads your code to AWS and creates the API.
```bash
sam deploy --guided
```
*   It will ask you questions (Stack Name, Region, etc.).
*   **Say YES** to "Confirm changes before deploy".
*   **Say YES** to "Allow SAM CLI IAM role creation".
*   **Say YES** to "GenAIFunction may not have authorization defined, Is this okay?".

### 3. Test
Once deployed, SAM will give you an **API Endpoint URL**. You can test it with `curl`:
```bash
curl -X POST https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, AI!"}'
```

### 4. Cleanup (Save Money!)
```bash
sam delete
```
