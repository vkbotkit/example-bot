"""
Copyright 2022 kensoi
"""

from vkbotkit.objects import data,
    filters,
    exceptions,
    enums,
    callback,
    Library,
    Mention)


END_POLLING = """
Завершаю прослушку сервера.
"""


class Main(LibraryModule):
    """
    Плагин для управления беседой при помощи VKBotKit
    Команды в этом плагине:
    @botname созвать
    @botname кик
    """

    
    @callback(filters.IsCommand({"стоп", "остановить"}))
    async def end(self, package, toolkit):
        """
        при получении команды '@kyokoubot стоп' => выключать бота
        """
        
        await toolkit.send_reply(package, END_POLLING)
        toolkit.stop_polling()
