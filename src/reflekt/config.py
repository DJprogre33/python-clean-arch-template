import os
from dataclasses import dataclass


@dataclass
class PostgresConfig:
    username: str
    password: str
    host: str
    port: str
    database: str

    @classmethod
    def from_env(cls) -> "PostgresConfig":
        return cls(
            username=os.environ["POSTGRES_USERNAME"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
            database=os.environ["POSTGRES_DATABASE"],
        )


@dataclass
class Config:
    postgres: PostgresConfig


def create_config() -> Config:
    return Config(postgres=PostgresConfig.from_env())
