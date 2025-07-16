from fastapi import APIRouter


router = APIRouter()


@router.post("/login")
async def login():
    """登录"""
    pass
