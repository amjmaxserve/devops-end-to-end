from fastapi import (
    APIRouter, 
    HTTPException, 
    Depends
)

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.inventory_model import Inventory

from app.schemas.inventory_schema import (
    InventoryCreate,
    InventoryUpdate,
    InventoryResponse
)




router = APIRouter()


@router.post("/", response_model=InventoryResponse)
def create_inventory(
    item: InventoryCreate,
    db: Session = Depends(get_db)
):
    inventory = Inventory(
        name=item.name,
        quantity=item.quantity
    )

    db.add(inventory)
    db.commit()
    db.refresh(inventory)

    return inventory


@router.get("/", response_model=list[InventoryResponse])
def get_inventory(
    db: Session = Depends(get_db)
):
    return db.query(Inventory).all()


@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_inventory_by_id(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    item = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Inventory item not found"
        )

    return item

@router.put("/{inventory_id}", response_model=InventoryResponse)
def update_inventory(
    inventory_id: int,
    inventory_update: InventoryUpdate,
    db: Session = Depends(get_db)
):
    item = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Inventory item not found"
        )

    item.name = inventory_update.name
    item.quantity = inventory_update.quantity

    db.commit()
    db.refresh(item)

    return item

@router.delete("/{inventory_id}")
def delete_inventory(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    item = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Inventory item not found"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Inventory deleted successfully"
    }