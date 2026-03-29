import os
import io
import pdfplumber
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
import json
import re
from typing import Optional
from fastapi import UploadFile
from PIL import Image

def clean_text(text: str) -> str:
    text = re.sub(r'Generated with https?://\S+', '', text)
    text = re.sub(r'(?<=\w)\s+(?=\w)', '', text)
    text = re.sub(r'(\d)\s+(\d)', r'\1\2', text)
    text = re.sub(r'\$\s+', '$', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Point pytesseract to your installed Tesseract binary
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"[ocr] pdfplumber error for {pdf_path}: {e}")

    if not text.strip():
        try:
            pages = convert_from_path(pdf_path, dpi=300)
            for page in pages:
                text += pytesseract.image_to_string(page, lang="eng") + "\n"
        except Exception as e:
            print(f"[ocr] OCR fallback failed for {pdf_path}: {e}")

    return clean_text(text)

def extract_text_from_file(file_path: str) -> Optional[str]:
    if not os.path.exists(file_path):
        return None
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    else:
        try:
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img, lang="eng")
            return clean_text(text)
        except Exception as e:
            print(f"[ocr] image extraction failed: {e}")
            return None

# ✅ Wrapper for FastAPI UploadFile
async def extract_text_upload(file: UploadFile) -> str:
    contents = await file.read()
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"[ocr] pdfplumber error: {e}")

    if not text.strip():
        try:
            pages = convert_from_bytes(contents, dpi=300)
            for page in pages:
                text += pytesseract.image_to_string(page, lang="eng") + "\n"
        except Exception as e:
            print(f"[ocr] OCR fallback failed: {e}")

    return clean_text(text)

def process_folder(folder_path: str):
    results = []
    print("Checking folder:", folder_path)
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            extracted_text = extract_text_from_pdf(file_path)
            results.append({"file_name": file, "extracted_text": extracted_text})
    return results

if __name__ == "__main__":
    folder_path = "input documents"
    output = process_folder(folder_path)
    with open("ocr_output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
    print("OCR completed. Output saved.")