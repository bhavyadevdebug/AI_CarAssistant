from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from backend.database import get_db, save_contract, save_contract_sla
from backend.models import User
from backend.utils.ocr_utils import extract_text_from_pdf
from backend.utils.llm_utils import analyze_contract

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
SECRET_KEY = "your-secret-key"   # must match auth.py
ALGORITHM = "HS256"

router = APIRouter(prefix="/contracts", tags=["contracts"])

class SLAData(BaseModel):
    apr_percent: float | None = None
    term_months: int | None = None
    monthly_payment: float | None = None
    down_payment: float | None = None
    early_termination_fee: float | None = None
    mileage_allowance_yr: int | None = None
    red_flags: str | None = None


@router.post("/upload")
async def upload_contract(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    # 🔹 Decode JWT
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if not user_email:
            raise HTTPException(status_code=401, detail="Invalid token: missing subject")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # 🔹 Find user
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 🔹 Save file temporarily
    try:
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save failed: {str(e)}")

    # 🔹 OCR
    try:
        extracted_text = extract_text_from_pdf(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR failed: {str(e)}")

    # 🔹 LLM analysis
    try:
        analysis = analyze_contract(extracted_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    # 🔹 Save contract
    contract = save_contract(
        db,
        dealer_offer_name="Uploaded Contract",
        vin="UNKNOWN",
        terms=extracted_text,
        user_id=user.id
    )

    # 🔹 Save SLA if present
    if isinstance(analysis, dict) and "sla" in analysis:
        try:
            sla_data = SLAData(**analysis["sla"])
            save_contract_sla(db, contract.id, sla_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"SLA save failed: {str(e)}")

    return {"contract_id": contract.id, "analysis": analysis}
