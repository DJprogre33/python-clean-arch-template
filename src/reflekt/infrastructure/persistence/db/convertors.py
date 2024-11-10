from sqlalchemy import Row

from reflekt.application.user.dto import UserInfo


def convert_row_to_user_info_dto(row: Row) -> UserInfo | None:
    return UserInfo(
        name=row.name,
        surname=row.username,
    )
