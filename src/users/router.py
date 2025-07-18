from fastapi import APIRouter


router = APIRouter()


@router.post("/register")
async def register_user():
    """注册用户"""
    pass

@router.post("/create")
async def create_user():
    """创建用户"""
    pass

@router.get("/read")
async def read_user():
    """读取用户信息"""
    pass

@router.get("/read/{user_id}")
async def read_user_by_id(user_id: int):
    """根据用户ID读取用户信息"""
    return {"user_id": user_id}

@router.put("/update/{user_id}")
async def update_user(user_id: int):
    """更新用户信息"""
    return {"user_id": user_id, "status": "updated"}

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    """删除用户"""
    return {"user_id": user_id, "status": "deleted"}

