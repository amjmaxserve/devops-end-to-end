from fastapi import (
    FastAPI,
    Response,
    status
    )

from app.routes.inventory import router as inventory_router

from app.database import engine
from app.models.inventory_model import Base
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.health_servce import check_database


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
def health(
    response: Response,
    db: Session = Depends(get_db)
):
    database_status = check_database(db)

    if database_status:
        return {
            "status": "healthy",
            "database": "connected"
        }

    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "unhealthy",
        "database": "disconnected"
    }