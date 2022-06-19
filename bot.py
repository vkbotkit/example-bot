"""
Copyright 2022 kensoi
"""

import asyncio
from os import environ, getenv
from sys import argv
from dotenv import load_dotenv

from vkbotkit import Librabot
from vkbotkit.objects import enums

load_dotenv()

if "-d" in argv:
    TOKEN = environ['DEBUG_TOKEN']
    LOG_LEVEL = enums.LogLevel.DEBUG

else:
    TOKEN = environ['PUBLIC_TOKEN']
    LOG_LEVEL = enums.LogLevel.INFO

GROUP_ID = environ['GROUP_ID']
CONFIG_LOG = getenv("CONFIG_LOG", default = "")

async def main():
    """
    Главная функция приложения
    """

    bot = Librabot(TOKEN, GROUP_ID)
    bot.toolkit.configure_logger(LOG_LEVEL, "f" in CONFIG_LOG, "c" in CONFIG_LOG)

    # START POLLING
    await bot.toolkit.start_polling()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.create_task(main())
    loop.run_forever()
