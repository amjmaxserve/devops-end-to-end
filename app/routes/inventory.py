from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_inventory():
    return {
        "items": [
            {
                "id": 1,
                "name": "Rice",
                "quantity": 100
            }
        ]
    }
