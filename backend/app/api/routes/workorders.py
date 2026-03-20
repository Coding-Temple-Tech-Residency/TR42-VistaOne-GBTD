from fastapi import APIRouter, Depends, HTTPException
from app.db.schemas.work_orders import WorkOrderCreate, WorkOrderUpdate, WorkOrderResponse
from app.services.workorder_services import WorkOrderService
from app.dependencies import get_current_user, require_operator_owns_work_order
from app.db.db import get_db

router = APIRouter(prefix="/workorders", tags=["Work Orders"])


@router.get("/", response_model=list[WorkOrderResponse])
async def list_workorders(user=Depends(get_current_user), db=Depends(get_db)):
    return await WorkOrderService.list_for_user(db, user)


@router.get("/{workorder_id}", response_model=WorkOrderResponse)
async def get_workorder(workorder=Depends(require_operator_owns_work_order)):
    return workorder


@router.post("/", response_model=WorkOrderResponse)
async def create_workorder(
    data: WorkOrderCreate,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    return await WorkOrderService.create(db, user, data.dict())


@router.patch("/{workorder_id}", response_model=WorkOrderResponse)
async def update_workorder(
    workorder_id: int,
    updates: WorkOrderUpdate,
    workorder=Depends(require_operator_owns_work_order),
    db=Depends(get_db)
):
    return await WorkOrderService.update(db, workorder, updates.dict(exclude_unset=True))
