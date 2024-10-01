import asyncio

from mono_bot.application.bot.bot_thread import bot_main
from mono_bot.application.mediator.mediator import Mediator
from mono_bot.application.server import run_server


async def main():
    mediator = Mediator()
    await asyncio.gather(bot_main(mediator), run_server(mediator))


if __name__ == '__main__':
    asyncio.run(main())
