"""
Bot application
"""
import asyncio
from os import (
    environ,
    getenv
    )
from sys import argv
from dotenv import load_dotenv
from vkbotkit import Librabot
from vkbotkit.objects import (
    #decorators,
    #filters,
    enums,
    #library_module
)


async def main():
    """
    главная функция приложения
    """
    if "-d" in argv:
        token = environ['DEBUG_TOKEN']
        log_level = enums.LogLevel.DEBUG

    else:
        token = environ['PUBLIC_TOKEN']
        log_level = enums.LogLevel.INFO

    config_log = getenv("CONFIG_LOG", default = "")

    bot = Librabot(token)
    bot.toolkit.configure_logger(log_level, "f" in config_log, "c" in config_log)
    bot.library.import_library()

    # START POLLING
    await bot.start_polling()

if __name__ == "__main__":
    load_dotenv()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
