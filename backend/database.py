from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import uuid
from datetime import datetime

# ✅ SQLite database file (single source of truth)
SQLALCHEMY_DATABASE_URL = "sqlite:///./car_lease.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency for FastAPI routes
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Initialize database (create tables if they don’t exist)
def init_db():
    # Import models inside the function to avoid circular import
    import backend.models
    Base.metadata.create_all(bind=engine)


# ✅ Helper: save_contract
def save_contract(db: Session, dealer_offer_name: str, vin: str, terms: str, user_id: str = None):
    from backend.models import Contract  # import here to avoid circular import
    if user_id is None:
        user_id = str(uuid.uuid4())

    contract = Contract(
        user_id=user_id,
        contract_type="lease",
        doc_status="analyzed",
        dealer_offer_name=dealer_offer_name,  # must be a string
        vin=vin,                              # must be a string
        terms=terms,                          # must be a string
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(contract)
    db.commit()
    db.refresh(contract)
    return contract


# ✅ Helper: save_contract_sla
def save_contract_sla(db: Session, contract_id: str, sla_data):
    from backend.models import ContractSLA
    sla = ContractSLA(
        id=str(uuid.uuid4()),
        contract_id=contract_id,
        apr_percent=sla_data.apr_percent,
        term_months=sla_data.term_months,
        monthly_payment=sla_data.monthly_payment,
        down_payment=sla_data.down_payment,
        early_termination_fee=sla_data.early_termination_fee,
        mileage_allowance_yr=sla_data.mileage_allowance_yr,
        red_flags=sla_data.red_flags,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(sla)
    db.commit()
    db.refresh(sla)
    return sla
