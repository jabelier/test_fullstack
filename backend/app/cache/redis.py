import redis.asyncio as aioredis

from app.core.config import settings


async def create_redis() -> aioredis.Redis:
    client = aioredis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        decode_responses=True,
    )
    await client.ping()
    return client
