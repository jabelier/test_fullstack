from datetime import datetime, timezone

import asyncpg


class PublicationRepository:
    def __init__(self, pool: asyncpg.Pool):
        self._pool = pool

    async def create(self, user_id: int, title: str, text: str) -> dict:
        query = """
            INSERT INTO publications (user_id, title, text)
            VALUES ($1, $2, $3)
            RETURNING id, user_id, title, text, created_at, updated_at
        """
        async with self._pool.acquire() as conn:
            row = await conn.fetchrow(query, user_id, title, text)
        return dict(row)

    async def get_by_id(self, pub_id: int) -> dict | None:
        query = """
            SELECT id, user_id, title, text, created_at, updated_at
            FROM publications WHERE id = $1
        """
        async with self._pool.acquire() as conn:
            row = await conn.fetchrow(query, pub_id)
        return dict(row) if row else None

    async def get_ids_by_user(
        self, user_id: int, limit: int, offset: int
    ) -> list[int]:
        query = """
            SELECT id FROM publications
            WHERE user_id = $1
            ORDER BY created_at DESC
            LIMIT $2 OFFSET $3
        """
        async with self._pool.acquire() as conn:
            rows = await conn.fetch(query, user_id, limit, offset)
        return [row["id"] for row in rows]

    async def get_by_ids(self, ids: list[int]) -> list[dict]:
        query = """
            SELECT id, user_id, title, text, created_at, updated_at
            FROM publications
            WHERE id = ANY($1::int[])
            ORDER BY created_at DESC
        """
        async with self._pool.acquire() as conn:
            rows = await conn.fetch(query, ids)
        return [dict(row) for row in rows]

    async def count_by_user(self, user_id: int) -> int:
        query = "SELECT count(*) FROM publications WHERE user_id = $1"
        async with self._pool.acquire() as conn:
            return await conn.fetchval(query, user_id)

    async def update(self, pub_id: int, title: str, text: str) -> dict | None:
        now = datetime.now(timezone.utc)
        query = """
            UPDATE publications
            SET title = $1, text = $2, updated_at = $3
            WHERE id = $4
            RETURNING id, user_id, title, text, created_at, updated_at
        """
        async with self._pool.acquire() as conn:
            row = await conn.fetchrow(query, title, text, now, pub_id)
        return dict(row) if row else None

    async def delete(self, pub_id: int) -> bool:
        query = "DELETE FROM publications WHERE id = $1"
        async with self._pool.acquire() as conn:
            result = await conn.execute(query, pub_id)
        return result == "DELETE 1"
