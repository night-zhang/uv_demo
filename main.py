from typing import Union
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

from config import cfg
from src.router import web_router
from src.middleware import my_middleware
from contextlib import asynccontextmanager

app = FastAPI(
    debug=cfg.debug,
)

app.include_router(web_router)

my_middleware(app)


# 应用生命周期事件，异步上下文管理器
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    # logger_init()
    # db_init()
    # db_setting()
    # service_init()
    # send_email()
    yield

    # logger
    # db_close()
    # service_close()
    # send_email()
    print("Application shutdown")


# 查询服务器运行状态
@app.get("/run_state")
async def run_state():
    return {"Server state": "Running"}
