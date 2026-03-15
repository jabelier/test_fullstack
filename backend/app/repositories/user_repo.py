from datetime import datetime, timezone

import asyncpg


class UserRepository:
    def __init__(self, pool: asyncpg.Pool):
        self._pool = pool

    async def create(self, name: str) -> dict:
        query = """
            INSERT INTO users (name)
            VALUES ($1)
            RETURNING id, name, created_at, updated_at
        """
        async with self._pool.acquire() as conn:
            row = await conn.fetchrow(query, name)
        return dict(row)

    async def get_by_id(self, user_id: int) -> dict | None:
        query = "SELECT id, name, created_at, updated_at FROM users WHERE id = $1"
        async with self._pool.acquire() as conn:
            row = await conn.fetchrow(query, user_id)
        return dict(row) if row else None

    async def update_name(self, user_id: int, name: str) -> dict | None:
        query = """
            UPDATE users
            SET name = $1, updated_at = $2
            WHERE id = $3
            RETURNING id, name, created_at, updated_at
        """
        now = datetime.now(timezone.utc)
        async with self._pool.acquire() as conn:
            row = await conn.fetchrow(query, name, now, user_id)
        return dict(row) if row else None

    async def delete(self, user_id: int) -> bool:
        query = "DELETE FROM users WHERE id = $1"
        async with self._pool.acquire() as conn:
            result = await conn.execute(query, user_id)
        return result == "DELETE 1"
