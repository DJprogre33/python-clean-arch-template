from abc import ABC

from sqlalchemy.ext.asyncio import AsyncConnection


class SQLAlchemyDataMapper(ABC):
    def __init__(self, connection: AsyncConnection) -> None:
        self._connection = connection
