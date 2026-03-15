from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "trendsee"

    redis_host: str = "localhost"
    redis_port: int = 6379

    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 24

    publication_hot_ttl: int = 600
    cold_query_delay: float = 2.0


settings = Settings()
