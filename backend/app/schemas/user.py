from datetime import datetime

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)


class UserUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)


class UserResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime


class UserWithToken(BaseModel):
    user: UserResponse
    access_token: str
    token_type: str = "bearer"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
