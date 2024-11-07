from dishka import Provider, Scope, from_context, provide

from reflekt.config import Config, PostgresConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    config = from_context(provides=Config)

    @provide
    def postgres_config(self, config: Config) -> PostgresConfig:
        return config.postgres
