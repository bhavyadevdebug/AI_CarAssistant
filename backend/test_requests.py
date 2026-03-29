import json, requests

url = "http://127.0.0.1:8000/analyze_batch"

# Load OCR output file
with open("ocr_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Build payload using proper keys
payload = [
    {
        "file_name": item["file_name"],
        "contract_text": item["extracted_text"]
    }
    for item in data
]

# Send request
response = requests.post(url, json=payload, timeout=60)

# Pretty-print results grouped by file name
results = response.json()
for result in results:
    print(f"File: {result['file_name']}")
    print("Analysis:", json.dumps(result["analysis"], indent=2))
    print("-" * 80)