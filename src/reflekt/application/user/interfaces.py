from typing import Protocol
from uuid import UUID

from reflekt.application.user.dto import UserInfo


class UserReader(Protocol):
    async def get_user_info_by_id(self, user_id: UUID) -> UserInfo: ...
