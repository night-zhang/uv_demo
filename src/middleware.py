import time
from collections import defaultdict

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware


# 函数式的中间件写法
def my_middleware(app: FastAPI):
    @app.middleware("http")
    async def count_time(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        response.headers["X-Response-Time"] = str(duration)
        print(f"Request URL: {request.url}, Duration: {duration:.4f} seconds")
        return response
    
    @app.middleware("http")
    async def log_request(request: Request, call_next):
        print(f"Request method: {request.method}, URL: {request.url}")
        response = await call_next(request)
        print(f"Response status code: {response.status_code}")
        return response
    
    app.add_middleware(RateLimitMiddleware)
    # 处理跨域问题，注意这么设置不一定安全，生产环境中需要更严格的设置
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# 类形式的中间件
class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        # 虽然fastapi本身有一个中间件堆来存储数据，最好fastapi本身不要存储数据，扔给redis更好
        self.request_records: dict[str, float] = defaultdict(float) 
        
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        current_time = time.time()
        
        if current_time - self.request_records[ip] < 5:
            return Response(
                content="Too many requests, please try again later.",
                status_code=429
            )
        response = await call_next(request)
        self.request_records[ip] = current_time
        return response