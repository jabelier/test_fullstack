from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import asyncpg
import redis.asyncio as aioredis

from app.core.config import Settings, settings
from app.core.security import decode_access_token
from app.repositories.user_repo import UserRepository
from app.repositories.publication_repo import PublicationRepository
from app.services.user_service import UserService
from app.services.publication_service import PublicationService

bearer_scheme = HTTPBearer()


def get_settings() -> Settings:
    return settings


async def get_db_pool(request: Request) -> asyncpg.Pool:
    return request.app.state.db_pool


async def get_redis(request: Request) -> aioredis.Redis:
    return request.app.state.redis


async def get_user_repo(
    pool: asyncpg.Pool = Depends(get_db_pool),
) -> UserRepository:
    return UserRepository(pool)


async def get_publication_repo(
    pool: asyncpg.Pool = Depends(get_db_pool),
) -> PublicationRepository:
    return PublicationRepository(pool)


async def get_user_service(
    repo: UserRepository = Depends(get_user_repo),
) -> UserService:
    return UserService(repo)


async def get_publication_service(
    repo: PublicationRepository = Depends(get_publication_repo),
    redis: aioredis.Redis = Depends(get_redis),
    cfg: Settings = Depends(get_settings),
) -> PublicationService:
    return PublicationService(repo, redis, cfg)


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    repo: UserRepository = Depends(get_user_repo),
) -> int:
    _unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_id = decode_access_token(credentials.credentials)
    if user_id is None:
        raise _unauthorized
    user = await repo.get_by_id(user_id)
    if not user:
        raise _unauthorized
    return user_id
