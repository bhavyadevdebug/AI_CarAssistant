from backend.database import Base, engine
from backend.models import ContractSLA

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")