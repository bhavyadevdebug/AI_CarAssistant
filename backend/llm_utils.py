import requests, json
from llm_extractor import build_prompt

def chunk_text(text: str, size: int = 1000):
    return [text[i:i+size] for i in range(0, len(text), size)]

def extract_contract_details_from_text(text: str):
    chunks = chunk_text(text, size=1000)
    merged = {"parties": [], "risks": [], "dates": [], "suggestions": []}

    for chunk in chunks:
        prompt = build_prompt(chunk)
        print("🔍 Sending prompt (first 200 chars):", prompt[:200])

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False,
                    "format": "json"
                },
                timeout=300
            )
        except Exception as e:
            print("❌ Request to Ollama failed:", e)
            return {"error": f"LLM request failed: {e}"}

        if response.status_code != 200:
            print("❌ Ollama returned status:", response.status_code)
            return {"error": f"LLM returned status {response.status_code}"}

        content = response.json().get("response", "")
        print("🔍 Raw Ollama output:", content)

        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            print("❌ Invalid JSON from Ollama:", content)
            parsed = {"error": "Invalid JSON", "raw": content}
        except Exception as e:
            print("❌ Other parsing error:", e)
            parsed = {"error": str(e), "raw": content}

        # Merge results safely
        for key in merged:
            if key in parsed and isinstance(parsed[key], list):
                merged[key].extend(parsed[key])

    # Deduplicate lists
    for key in merged:
        merged[key] = list(set(merged[key]))

    return merged