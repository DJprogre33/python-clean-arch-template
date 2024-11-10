from uuid import UUID

from sqlalchemy import select

from reflekt.application.user.dto import UserInfo
from reflekt.application.user.interfaces import UserReader
from reflekt.infrastructure.persistence.db.convertors import convert_cursor_result_to_user_dto
from reflekt.infrastructure.persistence.db.mappers.base import SQLAlchemyDataMapper
from reflekt.infrastructure.persistence.db.tables import user_table


class UserReaderMapper(SQLAlchemyDataMapper, UserReader):
    async def get_user_info_by_id(self, user_id: UUID) -> UserInfo | None:
        query = select(user_table).where(user_table.c.id == user_id)
        result = await self._connection.execute(query)
        return convert_cursor_result_to_user_dto(result)
