from fastapi import APIRouter

from app.api.api_v1.endpoints import calculation

api_router = APIRouter()
api_router.include_router(calculation.router, prefix="/calculation", tags=["calculation"])
