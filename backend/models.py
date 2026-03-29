from sqlalchemy import Column, String, DateTime, ForeignKey, Float, Integer, Text
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    phone = Column(String(40), nullable=True)
    full_name = Column(String(200), nullable=True)
    auth_provider = Column(String(50), default="local", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # One user can have many contracts
    contracts = relationship("Contract", back_populates="user")


class Contract(Base):
    __tablename__ = "contracts"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    contract_type = Column(String(50), default="lease", nullable=False)
    doc_status = Column(String(50), default="draft", nullable=False)
    dealer_offer_name = Column(String(255), nullable=True)
    vin = Column(String(50), nullable=True)
    terms = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Link back to user
    user = relationship("User", back_populates="contracts")

    # One contract has one SLA
    sla = relationship("ContractSLA", back_populates="contract", uselist=False)


class ContractSLA(Base):
    __tablename__ = "contract_sla"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    contract_id = Column(String, ForeignKey("contracts.id"), nullable=False)
    apr_percent = Column(Float, nullable=True)
    term_months = Column(Integer, nullable=True)
    monthly_payment = Column(Float, nullable=True)
    down_payment = Column(Float, nullable=True)
    early_termination_fee = Column(Float, nullable=True)
    mileage_allowance_yr = Column(Integer, nullable=True)
    red_flags = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Link back to contract
    contract = relationship("Contract", back_populates="sla")
