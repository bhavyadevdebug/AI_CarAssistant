from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

# ✅ Import all routers, including negotiation
from backend.routes import auth_routes, sla_routes, vin_routes, contract_routes, negotiation_routes
from backend.database import init_db

app = FastAPI(title="Car Lease Analyzer")

# ✅ Enable CORS so React (http://localhost:3000) can call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"message": "You are authorized!", "token": token}

# ✅ Include all routers
app.include_router(auth_routes.router)
app.include_router(sla_routes.router)
app.include_router(vin_routes.router)
app.include_router(contract_routes.router)
app.include_router(negotiation_routes.router)   # <-- added

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Car Lease Analyzer API is running!"}
