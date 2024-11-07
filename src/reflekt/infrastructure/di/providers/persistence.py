from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine

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
