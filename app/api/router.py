from fastapi import APIRouter
from app.api import matches

api_router = APIRouter()

api_router.include_router(matches.router, prefix="/matches", tags=["Matches"])
