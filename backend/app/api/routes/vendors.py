from fastapi import APIRouter, Depends, HTTPException
from app.db.schemas.vendors import VendorCreate, VendorUpdate, VendorResponse
from app.services.vendor_services import VendorService
from app.dependencies import get_current_user, require_admin
from app.db import get_db

router = APIRouter()


@router.get("/", response_model=list[VendorResponse])
async def list_vendors(db=Depends(get_db)):
    return await VendorService.list(db)


@router.get("/{vendor_id}", response_model=VendorResponse)
async def get_vendor(vendor_id: int, db=Depends(get_db)):
    vendor = await VendorService.get(db, vendor_id)
    if not vendor:
        raise HTTPException(404, "Vendor not found")
    return vendor


@router.post("/", response_model=VendorResponse)
async def create_vendor(
    data: VendorCreate,
    user=Depends(require_admin),
    db=Depends(get_db)
):
    return await VendorService.create(db, data.dict())


@router.patch("/{vendor_id}", response_model=VendorResponse)
async def update_vendor(
    vendor_id: int,
    updates: VendorUpdate,
    user=Depends(require_admin),
    db=Depends(get_db)
):
    vendor = await VendorService.get(db, vendor_id)
    if not vendor:
        raise HTTPException(404, "Vendor not found")
    return await VendorService.update(db, vendor, updates.dict(exclude_unset=True))


@router.delete("/{vendor_id}")
async def delete_vendor(
    vendor_id: int,
    user=Depends(require_admin),
    db=Depends(get_db)
):
    vendor = await VendorService.get(db, vendor_id)
    if not vendor:
        raise HTTPException(404, "Vendor not found")
    await VendorService.delete(db, vendor)
    return {"message": "Vendor deleted"}
