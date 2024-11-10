from dataclasses import dataclass
from uuid import UUID

from reflekt.application.common.query import Query, QueryHandler
from reflekt.application.user.dto import UserInfo
from reflekt.application.user.exceptions import UserNotFoundError
from reflekt.application.user.interfaces import UserReader


@dataclass(frozen=True)
class GetUserInfoById(Query):
    user_id: UUID


class GetUserInfoByIdHandler(QueryHandler[GetUserInfoById, UserInfo]):
    def __init__(self, user_reader: UserReader) -> None:
        self._user_reader = user_reader

    async def __call__(self, query: GetUserInfoById) -> UserInfo:
        user_info = await self._user_reader.get_user_info_by_id(query.user_id)
        if not user_info:
            raise UserNotFoundError(query.user_id)

        return user_info
