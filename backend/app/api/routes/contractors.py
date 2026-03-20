from fastapi import APIRouter, Depends, HTTPException
from app.db.schemas.contractors import ContractorCreate, ContractorUpdate, ContractorResponse
from app.services.contractor_services import ContractorService
from app.dependencies import get_current_user, require_admin
from app.db.db import get_db

router = APIRouter(prefix="/contractors", tags=["Contractors"])


@router.get("/", response_model=list[ContractorResponse])
async def list_contractors(db=Depends(get_db)):
    return await ContractorService.list(db)


@router.post("/", response_model=ContractorResponse)
async def create_contractor(
    data: ContractorCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    return await ContractorService.create(db, user, data.dict())


@router.patch("/{contractor_id}", response_model=ContractorResponse)
async def update_contractor(
    contractor_id: int,
    updates: ContractorUpdate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    contractor = await ContractorService.get(db, contractor_id)
    if not contractor:
        raise HTTPException(404, "Contractor not found")

    if user.role != "admin" and contractor.auth_user_id != user.id:
        raise HTTPException(403, "Not authorized")

    return await ContractorService.update(db, contractor, updates.dict(exclude_unset=True))
