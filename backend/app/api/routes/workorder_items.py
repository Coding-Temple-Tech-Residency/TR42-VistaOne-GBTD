from fastapi import APIRouter, Depends, HTTPException
from app.db.schemas.work_order_items import WorkOrderItemCreate, WorkOrderItemUpdate, WorkOrderItemResponse
from app.services.workordrItens_services import WorkOrderItemService
from app.dependencies import require_operator_owns_work_order
from app.db.db import get_db

router = APIRouter(prefix="/workorders", tags=["Work Order Items"])


@router.get("/{workorder_id}/items", response_model=list[WorkOrderItemResponse])
async def list_items(workorder=Depends(require_operator_owns_work_order), db=Depends(get_db)):
    return await WorkOrderItemService.list_for_workorder(db, workorder.workorder_id)


@router.post("/{workorder_id}/items", response_model=WorkOrderItemResponse)
async def create_item(
    workorder_id: int,
    data: WorkOrderItemCreate,
    workorder=Depends(require_operator_owns_work_order),
    db=Depends(get_db)
):
    return await WorkOrderItemService.create(db, workorder_id, data.dict())


@router.patch("/items/{item_id}", response_model=WorkOrderItemResponse)
async def update_item(
    item_id: int,
    updates: WorkOrderItemUpdate,
    db=Depends(get_db)
):
    item = await WorkOrderItemService.get(db, item_id)
    if not item:
        raise HTTPException(404, "Item not found")
    return await WorkOrderItemService.update(db, item, updates.dict(exclude_unset=True))
