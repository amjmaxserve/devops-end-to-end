from pydantic import BaseModel, Field


class InventoryCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    quantity: int = Field(
        gt=0
    )


class InventoryUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    quantity: int = Field(
        gt=0
    )


class InventoryResponse(BaseModel):
    id: int
    name: str
    quantity: int

    model_config = {
        "from_attributes": True
    }