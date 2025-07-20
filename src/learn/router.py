from fastapi import APIRouter, Request, Response


router = APIRouter()


@router.get("/resources/path/{file}")
@router.post("/resources/path/{file}")
@router.put("/resources/path/{file}")
@router.delete("/resources/path/{file}")
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