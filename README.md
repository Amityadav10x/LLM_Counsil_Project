🧠 LLM Council – Multi-Agent Decision System

This project implements a minimal LLM Council, where multiple independent AI agents generate answers, and separate judge agents evaluate them using a rubric to produce a single, reliable decision.
The system emphasizes clarity, safety, auditability, and explainability over complexity.

📌 Problem Statement
Single LLM responses can be biased, incomplete, or incorrect.
This project addresses that by using a council-style approach:

Multiple agents generate independent answers

Judges compare answers (without generating new ones)

A final decision is produced with confidence, risks, and citations

All steps are safety-gated and audit-logged


🤖 Agent Design
Answer Agents (3)

Each answer agent:

Receives the same user prompt

Uses a different system instruction

Runs independently

Does not see other agents’ outputs

Agent	Behavior
A	Factual and concise
B	Analytical and detailed
C	Cautious and risk-aware

This creates diverse reasoning paths without randomness.

Judge Agents (2)

Judges:

Do NOT generate answers

Compare answers A, B, and C

Use a rubric:

Accuracy

Completeness

Clarity

Risk

Output structured JSON only

📊 Decision Object

The final output is a structured Decision Object:

{
  "final_answer": "...",
  "confidence": 1.0,
  "selected_agent": "A",
  "risks": [],
  "citations": [...],
  "judge_votes": ["A", "A"]
}

Confidence

Calculated from judge agreement

Example: 2/2 judges agree → confidence = 1.0

🔐 Safety Gating

Input safety check runs before any LLM call

Output safety check scans generated content for risks

Detected risks are propagated into the final decision

🧾 Persistent Audit Log

All executions are logged to an append-only JSONL audit log:

Timestamp

User prompt

All agent answers

Judge evaluations

Final decision

📁 File:

audit_log.jsonl


Why JSONL?
JSON Lines is scalable, append-only, and commonly used in production logging systems.

⚙️ Tech Stack

Python 3

Perplexity API (REST)

Requests

Modular project structure (no frameworks required)

🚀 How to Run
1. Clone the repository
git clone <repo-url>
cd LLM-Council

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Set Perplexity API key
setx PERPLEXITY_API_KEY "pplx-your-api-key"


Restart the terminal after this step.

5. Run the system
python main.py

📦 Project Structure
LLM Council/
├── agents/
│   ├── answer_agent.py
│   └── judge_agent.py
├── audit/
│   └── logger.py
├── decision/
│   └── decision_builder.py
├── safety/
│   ├── input_gate.py
│   └── output_gate.py
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── audit_log.jsonl

🧠 Intentional Non-Automation

Judge conflict resolution is intentionally not automated.

Disagreement between judges is treated as a signal of uncertainty, not an error.
This enables human review at critical decision boundaries and avoids false confidence.

✅ Scope Notes

This project intentionally avoids:

UI / frontend

Model training

Memory systems

Tool calling

Vector databases

Over-engineering

The focus is clarity and correctness, as requested.

🏁 Summary

This project demonstrates:

Multi-agent reasoning

Deterministic decision making

Safety-aware orchestration

Audit-ready design

Explainable confidence scoring

It is minimal, extensible, and interview-ready.
