"""
Copyright 2022 kensoi
"""

from vkbotkit.objects import callback, filters, Library


HELLO_MESSAGE = """
Hello, world
Programmed to work and not to feel
Not even sure that this is real
"""
HELP_MESSAGE = """
HELP INSTRUCTIONS HERE
"""


class NewUser(filters.Filter):
    """
    Фильтр оповещений о новых участниках
    """

    async def check(self, package):
        if not hasattr(package, "action"):
            return

        if not hasattr(package.action, "type"):
            return

        return package.action == "chat_invite_user"


class Main(Library):
    """
    Библиотека с командами, предназначенными для приветствия пользователей
    """

    @callback(filters.IsCommand({"start",}) | NewUser())
    async def send_hello(self, package, toolkit):
        """
        при получении команды '@your_bot_id start' => отправлять текст HELLO_ME
        """

        await toolkit.send_reply(package, HELLO_MESSAGE)


    @callback(filters.IsCommand({"help",}))
    async def send_help(self, package, toolkit):
        """
        при получении команды '@your_bot_id start' => отправлять текст HELLO_ME
        """

        await toolkit.send_reply(package, HELP_MESSAGE)
