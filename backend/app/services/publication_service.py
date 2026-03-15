import asyncio
import json
from datetime import datetime

import redis.asyncio as aioredis

from app.core.config import Settings
from app.core.exceptions import NotFoundError
from app.repositories.publication_repo import PublicationRepository


def _parse_dt(value: datetime | str) -> datetime:
    """Normalize created_at to datetime for reliable sorting.

    asyncpg returns datetime objects; values deserialized from Redis JSON
    are ISO-format strings — both need to be comparable.
    """
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(value)


class PublicationService:
    def __init__(
        self,
        repo: PublicationRepository,
        redis: aioredis.Redis,
        settings: Settings,
    ):
        self._repo = repo
        self._redis = redis
        self._settings = settings

    def _cache_key(self, pub_id: int) -> str:
        return f"publication:{pub_id}"

    async def _cache_publication(self, pub: dict) -> None:
        await self._redis.setex(
            self._cache_key(pub["id"]),
            self._settings.publication_hot_ttl,
            json.dumps(pub, default=str),
        )

    async def create(self, user_id: int, title: str, text: str) -> dict:
        pub = await self._repo.create(user_id, title, text)
        await self._cache_publication(pub)
        pub["source"] = "cache"
        return pub

    async def update(
        self,
        pub_id: int,
        title: str | None,
        text: str | None,
    ) -> dict:
        pub = await self._repo.get_by_id(pub_id)
        if not pub:
            raise NotFoundError("Publication not found")

        new_title = title if title is not None else pub["title"]
        new_text = text if text is not None else pub["text"]
        updated = await self._repo.update(pub_id, new_title, new_text)

        ttl = await self._redis.ttl(self._cache_key(pub_id))
        if ttl > 0:
            await self._redis.setex(
                self._cache_key(pub_id),
                ttl,
                json.dumps(updated, default=str),
            )
            updated["source"] = "cache"
        else:
            updated["source"] = "database"

        return updated

    async def delete(self, pub_id: int) -> None:
        pub = await self._repo.get_by_id(pub_id)
        if not pub:
            raise NotFoundError("Publication not found")

        await self._repo.delete(pub_id)
        await self._redis.delete(self._cache_key(pub_id))

    async def get_user_publications(
        self, user_id: int, limit: int = 20, offset: int = 0
    ) -> tuple[list[dict], int]:
        pub_ids = await self._repo.get_ids_by_user(user_id, limit, offset)
        total = await self._repo.count_by_user(user_id)

        if not pub_ids:
            return [], total

        keys = [self._cache_key(pid) for pid in pub_ids]
        cached_values = await self._redis.mget(*keys)

        hot: list[dict] = []
        cold_ids: list[int] = []

        for pid, raw in zip(pub_ids, cached_values):
            if raw is not None:
                pub_data = json.loads(raw)
                pub_data["source"] = "cache"
                hot.append(pub_data)
            else:
                cold_ids.append(pid)

        cold: list[dict] = []
        if cold_ids:
            await asyncio.sleep(self._settings.cold_query_delay)
            cold_rows = await self._repo.get_by_ids(cold_ids)
            for row in cold_rows:
                row["source"] = "database"
                cold.append(row)

        all_pubs = hot + cold
        all_pubs.sort(key=lambda p: _parse_dt(p["created_at"]), reverse=True)
        return all_pubs, total
