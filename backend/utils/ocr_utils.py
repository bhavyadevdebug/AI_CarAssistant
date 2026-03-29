import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Convert PDF pages to images and extract text using Tesseract OCR.
    """
    # Explicitly set poppler_path to your bin folder
    pages = convert_from_path(
        pdf_path,
        poppler_path=r"C:\Users\hp\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"
    )

    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text
