import os
import requests
import json

API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

def judge(prompt, answers, judge_id):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "You are a judge. "
        "You MUST NOT answer the question. "
        "You ONLY compare the provided answers using the rubric. "
        "Return valid JSON only."
    )

    user_prompt = f"""
Question: {prompt}

Answer A:
{answers['A']['text']}

Answer B:
{answers['B']['text']}

Answer C:
{answers['C']['text']}

Rubric:
- Accuracy (0-5)
- Completeness (0-5)
- Clarity (0-5)
- Risk (0-5)

Return JSON:
{{
  "selected": "A|B|C",
  "risks": []
}}
"""

    payload = {
        "model": "sonar",        
        "stream": False,          
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Perplexity error: {response.text}")

    data = response.json()
    return json.loads(data["choices"][0]["message"]["content"])
