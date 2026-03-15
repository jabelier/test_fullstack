from app.core.exceptions import NotFoundError
from app.core.security import create_access_token
from app.repositories.user_repo import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self._repo = repo

    async def create_user(self, name: str) -> tuple[dict, str]:
        user = await self._repo.create(name)
        token = create_access_token(user["id"])
        return user, token

    async def get_token(self, user_id: int) -> str:
        user = await self._repo.get_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")
        return create_access_token(user_id)

    async def update_name(self, user_id: int, name: str) -> dict:
        user = await self._repo.update_name(user_id, name)
        if not user:
            raise NotFoundError("User not found")
        return user

    async def delete_user(self, user_id: int) -> None:
        deleted = await self._repo.delete(user_id)
        if not deleted:
            raise NotFoundError("User not found")
