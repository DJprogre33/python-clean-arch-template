from sqlalchemy import TEXT, Column, MetaData, Table
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()


user_table = Table(
    "users",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("name", TEXT, nullable=False),
    Column("surname", TEXT, nullable=False),
)
