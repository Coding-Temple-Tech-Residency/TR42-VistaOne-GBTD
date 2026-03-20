# app/api/__init__.py
from fastapi import APIRouter
from .routes import protected

api_router = APIRouter()
api_router.include_router(protected.router, prefix="/protected", tags=["protected"])
