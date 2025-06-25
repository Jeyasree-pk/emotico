import os
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

async def _call_openai(messages, temperature=0.3, max_tokens=60):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(OPENAI_ENDPOINT, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

async def analyze_mood_llm(text: str) -> str:
    messages = [
        {"role": "system", "content": "You are an expert emotion detector."},
        {"role": "user", "content": f"Analyze the following text and reply with only a single word describing the primary emotion (e.g., happy, sad, angry, anxious, excited):\n\n{text}"}
    ]
    result = await _call_openai(messages)
    return result.split()[0].strip('.').lower()

async def detect_crisis_llm(text: str) -> bool:
    messages = [
        {"role": "system", "content": "You are a mental health risk detector."},
        {"role": "user", "content": f"Does this text suggest a crisis or suicidal intent? Reply with only true or false.\n\n{text}"}
    ]
    result = await _call_openai(messages, temperature=0, max_tokens=6)
    return "true" in result.lower()

async def summarize_llm(text: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful summarizer. Always return a concise summary."},
        {"role": "user", "content": f"Summarize this text in 1-2 sentences:\n\n{text}"}
    ]
    result = await _call_openai(messages, max_tokens=80)
    return result