from fastapi import APIRouter

from app.api.endpoints import users
from app.api.endpoints import enrolments

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(enrolments.router, prefix="/enrolments", tags=["enrolments"])
