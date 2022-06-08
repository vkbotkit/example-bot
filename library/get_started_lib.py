"""
Пример плагина для vkbotkit
"""
from vkbotkit.objects import (
    decorators,
    filters,
    #enums,
    LibraryModule)


HELLO_ME = """
Hello, world
Programmed to work and not to feel
Not even sure that this is real
"""


class Main(LibraryModule):
    """
    docstring fix
    """

    @decorators.callback(filters.IsCommand({"start",}))
    async def send_hello(self, package):
        """
        при получении команды '@your_bot_id start' => отправлять текст HELLO_ME
        """
        await package.toolkit.send_reply(package, HELLO_ME)
        