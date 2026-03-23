from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, SessionLocal
from app.models import Base
from app.core.seed import seed_roles, seed_admin, seed_demo_data

from app.auth.routes import router as auth_router
from app.vendors.routes import router as vendors_router
from app.msa.routes import router as msa_router
from app.workorders.routes import router as workorders_router
from app.invoices.routes import router as invoices_router
from app.compliance.routes import router as compliance_router

Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    seed_roles(db)
    seed_admin(db)
    seed_demo_data(db)

app = FastAPI(title="Operator Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(vendors_router)
app.include_router(msa_router)
app.include_router(workorders_router)
app.include_router(invoices_router)
app.include_router(compliance_router)
