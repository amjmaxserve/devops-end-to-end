from pydantic import BaseModel


class InventoryCreate(BaseModel):
    name: str
    quantity: int


class InventoryResponse(BaseModel):
    id: int
    name: str
    quantity: int

    model_config = {
        "from_attributes": True
    }