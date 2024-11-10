from collections.abc import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine

from reflekt.config import PostgresConfig
from reflekt.infrastructure.persistence.postgres.factory import (
    create_async_engine,
    create_postgres_url,
)


class PostgresProvider(Provider):
    scope = Scope.APP

    @provide
    def get_engine(self, config: PostgresConfig) -> AsyncEngine:
        url = create_postgres_url(config=config)
        engine = create_async_engine(url=url)
        return engine

    @provide(scope=Scope.REQUEST)
    async def get_connection(self, engine: AsyncEngine) -> AsyncIterable[AsyncConnection]:
        async with engine.connect() as connection:
            yield connection


class DataMapperProviders(Provider):
    scope = Scope.REQUEST
