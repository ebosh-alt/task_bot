import asyncio
import sys

sys.path.append('D:/telegram_bot/contract_bot')

from contextlib import suppress
import logging

from bot.config import bot, dp


async def main() -> None:
    for router in routers:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        # filename="logger.log",
                        filemode="w",
                        format="%(levelname)s %(asctime)s %(message)s",
                        encoding='utf-8')

    with suppress(KeyboardInterrupt):
        asyncio.run(main())
