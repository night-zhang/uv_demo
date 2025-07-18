from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.users.router import router as users_router

web_router = APIRouter()
web_router.include_router(auth_router, prefix="/auth", tags=["登录认证"])
web_router.include_router(users_router, prefix="/users", tags=["用户管理"])
