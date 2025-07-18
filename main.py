from typing import Union
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

from config import cfg
from src.router import web_router
from src.middleware import my_middleware
from contextlib import asynccontextmanager

app = FastAPI(
    debug=cfg.DEBUG,
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


# @app.middleware("http")
# async def only_for_request(request: Request, call_next):
#     print(f"Request URL: {request.url}")
#     response: Response = await call_next(request)
#     return response


# @app.middleware("http")
# async def only_for_response(request: Request, call_next):
#     response: Response = await call_next(request)
#     print(f"Response headers: {response.headers}")
#     return response



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/run_state")
async def run_state():
    return {"Server state": "Running"}

@app.get("/resources/path/{file}")
@app.post("/resources/path/{file}")
@app.put("/resources/path/{file}")
@app.delete("/resources/path/{file}")
async def http_url(*, request: Request, key1, key2):
    response = {
        "协议名称": request.url.scheme,
        "主机名": request.url.hostname,
        "端口": request.url.port,
        "资源路径": request.url.path,
        "参数": request.url.query,
        "key1的值": key1,
        "key2的值": key2,
        "请求头部": request.headers,
        "请求体": await request.body(),
    }
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}