from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import status


class InventoryNotFoundException(Exception):
    def __init__(self, inventory_id: int):
        self.inventory_id = inventory_id


async def inventory_not_found_handler(
    request: Request,
    exc: InventoryNotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "Inventory Not Found",
            "inventory_id": exc.inventory_id
        }
    )