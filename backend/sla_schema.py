# This defines the structure of information we want from contracts

SLA_SCHEMA = {
    "document_type": "",
    "agreement_details": {
        "agreement_number": "",
        "agreement_date": ""
    },
    "parties": {
        "lessor": "",
        "lessee": ""
    },
    "vehicle_details": {
        "vin": "",
        "make": "",
        "model": "",
        "year": "",
        "fuel_type": ""
    },
    "financial_terms": {
        "monthly_payment": "",
        "interest_rate_or_apr": "",
        "down_payment": "",
        "lease_duration": "",
        "start_date": "",
        "end_date": "",
        "buyout_price": "",
        "mileage_limit": "",
        "excess_mileage_fee": ""
    },
    "penalties": {
        "late_fee": "",
        "early_termination_fee": "",
        "other_penalties": ""
    },
    "governing_law": "",
    "red_flags": [],
    "simple_explanation": ""
}
