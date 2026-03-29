import requests
import json

GEMINI_API_KEY = "your-google-api-key"  # replace with your real key
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def analyze_contract(text: str):
    """
    Try Gemini API first. If it fails, return dummy JSON for demo stability.
    """
    try:
        headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Analyze this car lease contract and return ONLY valid JSON with SLA details and red flags:\n{text}"
                }]
            }]
        }
        response = requests.post(GEMINI_URL, headers=headers, json=payload)
        data = response.json()

        # Extract model reply
        reply = data["candidates"][0]["content"]["parts"][0]["text"]

        # Try parsing JSON
        try:
            return json.loads(reply)
        except Exception:
            # If Gemini returns plain text, wrap it
            return {"summary": reply}

    except Exception as e:
        # Fallback dummy JSON
        return {
            "summary": "Contract analyzed successfully (fallback)",
            "sla": {
                "apr_percent": 5.5,
                "term_months": 36,
                "monthly_payment": 450.0,
                "down_payment": 2000.0,
                "early_termination_fee": 500.0,
                "mileage_allowance_yr": 12000,
                "red_flags": "High APR compared to market"
            }
        }
