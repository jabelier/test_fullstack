from datetime import datetime

from pydantic import BaseModel, Field


class PublicationCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=500)
    text: str = Field(..., min_length=1)


class PublicationUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=500)
    text: str | None = Field(None, min_length=1)


class PublicationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    text: str
    created_at: datetime
    updated_at: datetime
    source: str = "database"


class PaginatedPublications(BaseModel):
    items: list[PublicationResponse]
    total: int
    limit: int
    offset: int
