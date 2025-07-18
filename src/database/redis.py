import redis.asyncio as redis
from redis.exceptions import ConnectionError, TimeoutError


# 配置redis连接池
# 后续放.env文件中
redis_pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    decode_responses=True,
    encoding='utf-8',
)


async def redis_connect():
    try:
        redis_client = redis.Redis(connection_pool=redis_pool)
        sig = await redis_client.ping()  # 测试连接
        print(f"Redis connection established: {sig}")
        return redis_client
    except ConnectionError as e:
        print(f"Redis connection error: {e}")
    except TimeoutError as e:
        print(f"Redis connection timed out: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")