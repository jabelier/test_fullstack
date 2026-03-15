import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.publications import router as publications_router
from app.api.users import router as users_router
from app.cache.redis import create_redis
from app.core.exceptions import ForbiddenError, NotFoundError
from app.db.postgres import create_pool, init_schema

logger = logging.getLogger(__name__)


async def _wait_for_postgres(retries: int = 30, delay: float = 1.0):
    """Retry loop — PostgreSQL may not be ready immediately in Docker."""
    for attempt in range(retries):
        try:
            pool = await create_pool()
            await init_schema(pool)
            return pool
        except Exception:
            if attempt == retries - 1:
                raise
            logger.warning("Postgres not ready, retrying in %ss…", delay)
            await asyncio.sleep(delay)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db_pool = await _wait_for_postgres()
    app.state.redis = await create_redis()
    logger.info("Backend started — PG and Redis connected")
    yield
    await app.state.db_pool.close()
    await app.state.redis.close()


app = FastAPI(
    title="Publications API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(NotFoundError)
async def not_found_handler(_request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": exc.detail})


@app.exception_handler(ForbiddenError)
async def forbidden_handler(_request: Request, exc: ForbiddenError):
    return JSONResponse(status_code=403, content={"detail": exc.detail})


app.include_router(users_router)
app.include_router(publications_router)


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}
