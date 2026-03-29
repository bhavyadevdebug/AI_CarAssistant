from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/negotiate", tags=["Negotiation"])

class TermsInput(BaseModel):
    terms: str

@router.post("/")
async def negotiate(input: TermsInput):
    # Demo logic: look for common clauses
    text = input.terms.lower()
    suggestions = []

    if "mileage" in text:
        suggestions.append("Ask for a higher mileage allowance or lower excess mileage fee.")
    if "termination" in text:
        suggestions.append("Negotiate to reduce or waive the early termination fee.")
    if "disposition" in text:
        suggestions.append("Request removal or reduction of the disposition fee.")
    if not suggestions:
        suggestions.append("Consider asking for lower monthly payments or better incentives.")

    return {"message": " ".join(suggestions)}
