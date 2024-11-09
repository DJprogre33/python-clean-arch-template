import asyncio

from reflekt.config import create_config
from reflekt.presentation.web.factory import create_app, run_app


async def main() -> None:
    config = create_config()
    app = create_app()
    await run_app(app=app, config=config.api)


if __name__ == "__main__":
    asyncio.run(main())
