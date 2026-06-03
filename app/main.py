from fastapi import FastAPI
from app.routes.inventory import router as inventory_router

app = FastAPI()

app.include_router(
    inventory_router,
    prefix="/inventory",
    tags=["Inventory"]
)

@app.get("/")
def home():
    return {
        "message": "Farm Inventory API"
    }
