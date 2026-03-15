from fastapi import APIRouter, Depends, Query, status

from app.core.dependencies import get_current_user_id, get_publication_service
from app.schemas.publication import (
    PaginatedPublications,
    PublicationCreate,
    PublicationResponse,
    PublicationUpdate,
)
from app.services.publication_service import PublicationService

router = APIRouter(prefix="/api/publications", tags=["Publications"])


@router.post(
    "",
    response_model=PublicationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create publication",
)
async def create_publication(
    body: PublicationCreate,
    current_user_id: int = Depends(get_current_user_id),
    service: PublicationService = Depends(get_publication_service),
):
    pub = await service.create(current_user_id, body.title, body.text)
    return PublicationResponse(**pub)


@router.patch(
    "/{publication_id}",
    response_model=PublicationResponse,
    summary="Update publication",
)
async def update_publication(
    publication_id: int,
    body: PublicationUpdate,
    service: PublicationService = Depends(get_publication_service),
):
    pub = await service.update(publication_id, body.title, body.text)
    return PublicationResponse(**pub)


@router.delete(
    "/{publication_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete publication",
)
async def delete_publication(
    publication_id: int,
    service: PublicationService = Depends(get_publication_service),
):
    await service.delete(publication_id)


@router.get(
    "/user/{user_id}",
    response_model=PaginatedPublications,
    summary="Get user publications (paginated)",
)
async def get_user_publications(
    user_id: int,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    service: PublicationService = Depends(get_publication_service),
):
    items, total = await service.get_user_publications(user_id, limit, offset)
    return PaginatedPublications(
        items=[PublicationResponse(**p) for p in items],
        total=total,
        limit=limit,
        offset=offset,
    )
