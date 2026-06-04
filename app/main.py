from fastapi import FastAPI

from app.routes.inventory import router as inventory_router

from app.database import engine
from app.models.inventory_model import Base

Base.metadata.create_all(bind=engine)

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

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }