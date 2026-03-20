from fastapi import APIRouter, Depends, HTTPException
from app.db.schemas.invoices import InvoiceCreate, InvoiceUpdate, InvoiceResponse
from app.services.invoice_services import InvoiceService
from app.dependencies import get_current_user
from app.db.db import get_db

router = APIRouter(prefix="/invoices", tags=["Invoices"])


@router.get("/", response_model=list[InvoiceResponse])
async def list_invoices(user=Depends(get_current_user), db=Depends(get_db)):
    return await InvoiceService.list_for_user(db, user)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
async def get_invoice(invoice_id: int, user=Depends(get_current_user), db=Depends(get_db)):
    invoice = await InvoiceService.get(db, invoice_id)
    if not invoice:
        raise HTTPException(404, "Invoice not found")

    if user.role != "admin" and invoice.auth_user_id != user.id:
        raise HTTPException(403, "Not authorized")

    return invoice


@router.post("/", response_model=InvoiceResponse)
async def create_invoice(
    data: InvoiceCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    return await InvoiceService.create(db, user, data.dict())


@router.patch("/{invoice_id}", response_model=InvoiceResponse)
async def update_invoice(
    invoice_id: int,
    updates: InvoiceUpdate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    invoice = await InvoiceService.get(db, invoice_id)
    if not invoice:
        raise HTTPException(404, "Invoice not found")

    if user.role != "admin" and invoice.auth_user_id != user.id:
        raise HTTPException(403, "Not authorized")

    return await InvoiceService.update(db, invoice, updates.dict(exclude_unset=True))
