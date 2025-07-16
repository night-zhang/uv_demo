from fastapi import APIRouter

from src.auth.router import router as auth_router

web_router = APIRouter()
web_router.include_router(auth_router, prefix="/auth", tags=["登录认证"])

