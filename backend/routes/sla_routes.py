from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from backend.ocr_extractor import extract_text_upload
from backend.llm_extractor import analyze_contract
from backend.database import get_db
from backend.models import Contract, ContractSLA
import uuid
from datetime import datetime

router = APIRouter(prefix="/sla", tags=["sla"])

# ✅ Test route (temporary, for debugging DB)
@router.post("/test")
async def test(db: Session = Depends(get_db)):
    contract = Contract(
        user_id = str(uuid.uuid4()),
        contract_type="lease",
        doc_status="test",
        dealer_offer_name="dummy.pdf",
        vin="TESTVIN123456789",
        terms="Sample contract text",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(contract)
    db.commit()
    db.refresh(contract)
    return {"contract_id": str(contract.id)}

# ✅ Real route
@router.post("/analyze_batch")
async def analyze_batch(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Step 1: OCR extraction
    text = await extract_text_upload(file)

    # Step 2: Analyze contract (LLM + VIN + risks)
    result = analyze_contract(text, db)  # <-- pass db here

    # Step 3: Save Contract record
    contract = Contract(
        user_id = str(uuid.uuid4()),  # replace with actual user_id from auth
        contract_type="lease",
        doc_status="analyzed",
        dealer_offer_name=file.filename,
        vin=result.get("vin"),          # <-- persist VIN
        terms=text,                     # <-- persist raw text
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(contract)
    db.commit()
    db.refresh(contract)

    # Step 4: Save SLA record linked to Contract
    contract_sla = ContractSLA(
        contract_id=contract.id,
        apr_percent=result.get("apr_percent"),
        term_months=result.get("term_months"),
        monthly_payment=result.get("monthly_payment"),
        down_payment=result.get("down_payment"),
        early_termination_fee=result.get("early_termination_fee"),
        mileage_allowance_yr=result.get("mileage_allowance_yr"),
        red_flags=",".join(result.get("red_flags", []))
    )
    db.add(contract_sla)
    db.commit()
    db.refresh(contract_sla)

    # Step 5: Return combined response
    return {
        "filename": file.filename,
        "contract_id": str(contract.id),
        "sla_id": str(contract_sla.id),
        "extracted_sla": result
    }