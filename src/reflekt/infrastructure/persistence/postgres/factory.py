from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from reflekt.config import PostgresConfig


def create_postgres_url(config: PostgresConfig) -> str:
    driver_name = "psycopg3"
    username = config.username
    password = config.password
    host = config.host
    port = config.port
    database = config.database

    return f"postgresql+{driver_name}://{username}:{password}@{host}:{port}/{database}"


def create_engine(url: str) -> AsyncEngine:
    engine = create_async_engine(url=url)
    return engine
