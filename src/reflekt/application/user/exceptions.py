from dataclasses import dataclass
from uuid import UUID

from reflekt.application.common.exceptions import ApplicationLayerError


@dataclass
class UserNotFoundError(ApplicationLayerError):
    _user_id: UUID

    @property
    def title(self) -> str:
        return f"A user with {self._user_id} doesn't exist"
