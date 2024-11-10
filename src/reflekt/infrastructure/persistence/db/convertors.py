from sqlalchemy import CursorResult

from reflekt.application.user.dto import UserInfo


def convert_cursor_result_to_user_dto(result: CursorResult) -> UserInfo | None:
    for row in result:
        return UserInfo(
            name=row.name,
            surname=row.username,
        )
