from fastapi import FastAPI

from models import Base
from database import SessionLocal, engine
from core.config import settings
from api.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(api_router)
