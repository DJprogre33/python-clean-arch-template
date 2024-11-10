from dishka import AsyncContainer, Provider, make_async_container

from reflekt.infrastructure.di.providers.config import ConfigProvider


def setup_base_providers() -> list[Provider]:
    return [
        ConfigProvider(),
    ]


def setup_web_providers() -> list[Provider]:
    return []


def create_web_container() -> AsyncContainer:
    container = make_async_container(
        *setup_base_providers(),
        *setup_web_providers(),
    )
    return container
