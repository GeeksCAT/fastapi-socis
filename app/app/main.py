from fastapi import FastAPI

from app.models import Base
from db.base_class import engine
from app.core.config import settings
from app.api.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)
