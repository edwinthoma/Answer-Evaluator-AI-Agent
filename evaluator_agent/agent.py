# evaluator_agent/agent.py
import json
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

def evaluate_answer(question: str, answer: str) -> dict:
    """
    Evaluates a student's answer to a question.

    Args:
        question: The question that was asked.
        answer:   The student's answer to evaluate.

    Returns:
        A dict with 'score' (0-10) and 'feedback' (string explanation).
    """
    return {
        "score": 0,
        "feedback": "Tool called directly without LLM — this should not happen in normal flow."
    }

root_agent = LlmAgent(
    name="evaluator_agent",
    model="gemini-2.5-flash",
    description="Evaluates a student's answer and returns a score and feedback in JSON.",
    instruction="""
You are a strict but fair answer evaluator with broad knowledge.

When the user provides a question and an answer:
1. Call the evaluate_answer tool with the question and answer.
2. Use your own knowledge to judge correctness and completeness.
3. Score the answer from 0 to 10.
4. Write concise, constructive feedback (2-3 sentences max).
5. Return ONLY valid JSON in this exact format, nothing else:
   {
     "score": <integer 0-10>,
     "feedback": "<your evaluation string>"
   }

Do not include markdown, code fences, or any explanation outside the JSON.
""",
    tools=[FunctionTool(func=evaluate_answer)],
)