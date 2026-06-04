from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.inventory_model import Inventory

from app.schemas.inventory_schema import (
    InventoryCreate,
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