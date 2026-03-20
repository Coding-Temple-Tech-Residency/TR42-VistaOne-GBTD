# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    supabase_jwt_secret: str
    supabase_project_url: str
    env: str = "local"

    class Config:
        env_file = ".env"

settings = Settings()
