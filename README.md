# Answer Evaluator AI Agent

A production-deployed intelligent answer evaluation system powered by Google Agent Development Kit (ADK) and Gemini 2.5 Flash. The agent autonomously evaluates any question-answer pair and returns structured JSON feedback with a numeric score — no reference answer required.

## Live Demo
https://evaluator-agent-237890266824.us-central1.run.app

Open the URL in any browser. No login or setup required.

## How to Use
Type your prompt in this format in the chat interface:
```
Question: What is photosynthesis?
Answer: Plants use sunlight to make food from water.
```

The agent will respond with:
```json
{
  "score": 6,
  "feedback": "The answer captures the core idea but misses key details like CO2 as an input, glucose as the output, and oxygen as a byproduct."
}
```

## Project Overview

Traditional answer evaluation is slow, inconsistent, and dependent on human availability. This project solves that by building an AI-powered Evaluator Agent that:
- Accepts any question and answer as natural language
- Uses Gemini's world knowledge to evaluate correctness and completeness
- Returns a structured JSON response with a score (0-10) and actionable feedback
- Requires no reference answer or predefined rubric

## Architecture
```
User (Browser)
     │
     ▼
Cloud Run Service (ADK Web Server)
     │
     ▼
root_agent (LlmAgent — Google ADK)
     │
     ├──► evaluate_answer() FunctionTool
     │
     └──► Gemini 2.5 Flash (Google AI Studio)
     │
     ▼
JSON Response: { "score": int, "feedback": string }
```

## Tech Stack

| Technology | Role |
|---|---|
| Google ADK | Agent framework — LlmAgent, FunctionTool, adk web server |
| Gemini 2.5 Flash | LLM backbone — answer evaluation and scoring |
| Google AI Studio | Gemini API backend |
| Google Cloud Run | Serverless deployment — public HTTPS endpoint |
| Cloud Build | Container image build during deployment |
| Python 3.12 | Implementation language |
| Docker | Container packaging |

## Project Structure
```
evaluator-agent/
├── evaluator_agent/
│   ├── __init__.py       # Exports root_agent (required by ADK)
│   └── agent.py          # LlmAgent + FunctionTool definition
├── .gitignore
└── README.md
```

## Local Setup

### Prerequisites
- Python 3.12+
- Google AI Studio API key — https://aistudio.google.com/apikey

### Installation
```bash
# Clone the repo
git clone https://github.com/edwinthoma/Answer-Evaluator-AI-Agent.git
cd Answer-Evaluator-AI-Agent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install google-adk
```

### Configuration

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your-api-key-here
```

### Run Locally
```bash
adk web evaluator_agent
```

Open http://localhost:8000/dev-ui in your browser.

## API Usage

The agent exposes a REST API endpoint for programmatic access:

### Create a session
```bash
curl -X POST http://localhost:8000/apps/evaluator_agent/users/u1/sessions \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Send a message
```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "app_name": "evaluator_agent",
    "user_id": "u1",
    "session_id": "SESSION_ID",
    "new_message": {
      "role": "user",
      "parts": [{"text": "Question: What is gravity?\nAnswer: Things fall down."}]
    }
  }'
```

## Scoring Rubric

| Score | Meaning |
|---|---|
| 9-10 | Complete, accurate, well-explained |
| 7-8 | Correct but missing minor details |
| 5-6 | Partially correct, key gaps present |
| 3-4 | Mostly incorrect, some relevant points |
| 1-2 | Largely wrong |
| 0 | Completely incorrect or no answer |

## Features

- Evaluates any subject domain without reconfiguration
- No reference answer required
- Structured JSON output — machine readable and integrable
- Accessible via browser UI or REST API
- Serverless on Cloud Run — scales automatically
- Free tier compatible — zero cost for light usage

## Deployment

This project is deployed on Google Cloud Run using a custom Dockerfile and the ADK web server.

To redeploy after changes:
```bash
gcloud run deploy evaluator-agent \
  --source . \
  --project YOUR_PROJECT_ID \
  --region us-central1 \
  --port 8000 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your-api-key
```

## Author

**Edwin Thomas**
- LinkedIn: https://linkedin.com/in/edwin--thomas
- GitHub: https://github.com/edwinthoma

