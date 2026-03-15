from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_user_service
from app.schemas.user import (
    TokenResponse,
    UserCreate,
    UserResponse,
    UserUpdate,
    UserWithToken,
)
from app.services.user_service import UserService

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post(
    "",
    response_model=UserWithToken,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
async def create_user(
    body: UserCreate,
    service: UserService = Depends(get_user_service),
):
    user, token = await service.create_user(body.name)
    return UserWithToken(
        user=UserResponse(**user),
        access_token=token,
    )


@router.get(
    "/{user_id}/token",
    response_model=TokenResponse,
    summary="Get token by user ID (for testing)",
)
async def get_token(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    token = await service.get_token(user_id)
    return TokenResponse(access_token=token)


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user name",
)
async def update_user(
    user_id: int,
    body: UserUpdate,
    service: UserService = Depends(get_user_service),
):

    user = await service.update_name(user_id, body.name)
    return UserResponse(**user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
)
async def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):


    await service.delete_user(user_id)
