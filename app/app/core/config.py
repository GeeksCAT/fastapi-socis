from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "fastapi-socis"

settings = Settings()