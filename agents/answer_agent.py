import os
import requests

API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

def generate_answer(prompt: str, system_prompt: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar",          
        "stream": False,           
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Perplexity error: {response.text}")

    data = response.json()

    return {
        "text": data["choices"][0]["message"]["content"],
        "citations": data.get("citations", [])
    }

