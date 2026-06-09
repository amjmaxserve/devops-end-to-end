from fastapi import (
    FastAPI,
    Response,
    Depends,
    status
)

from sqlalchemy.orm import Session

from app.routes.inventory import router as inventory_router
from app.database import engine, get_db
from app.models.inventory_model import Base
from app.services.health_service import check_database
from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from fastapi import Response
from app.middleware.prometheus import PrometheusMiddleware


from app.exceptions import (
    InventoryNotFoundException,
    inventory_not_found_handler
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(
    InventoryNotFoundException,
    inventory_not_found_handler
)

app.include_router(
    inventory_router,
    prefix="/inventory",
    tags=["Inventory"]
)

app.add_middleware(
    PrometheusMiddleware
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
            "database": "connected",
            "service": "farm-inventory"
        }

    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "unhealthy",
        "database": "disconnected",
        "service": "farm-inventory"
    }

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

@app.get("/version")
def version():
    return {
        "version": "35",
        "track": "canary"
    }