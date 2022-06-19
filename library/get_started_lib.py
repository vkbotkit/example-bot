"""
Copyright 2022 kensoi
"""
from vkbotkit.utils import VERSION
from vkbotkit.objects import (
    filters,
    callback,
    LibraryModule
    )

HELLO_ME = """
Hello, world
Programmed to work and not to feel
Not even sure that this is real
"""
VKBOTKIT_INFO = f"""
Построено на VKBotKit
Версия библиотеки: {VERSION}
"""

class Main(LibraryModule):
    """
    Пример плагина для VKBotKit
    Все плагины, сгружаемые с каталога библиотеки, взаимодействуют только с Longpoll событиями.
    """
    def __init__(self):
        LibraryModule.__init__(self)
        self.canary_att = None

    @callback(filters.IsCommand({"начать", "привет", "старт"}))
    async def send_hello(self, package):
        """
        Приветствие бота
        """
        await package.toolkit.send_reply(package, HELLO_ME)


    @callback(filters.IsCommand({"канари", "движок"}))
    async def send_engine_info(self, package):
        """
        Приветствие бота
        """
        if not self.canary_att:
            self.canary_att = await package.toolkit.uploader.photo_messages("preview.png")

        await package.toolkit.send_reply(package, VKBOTKIT_INFO, self.canary_att)
        