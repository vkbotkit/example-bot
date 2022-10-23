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


NO_ADMIN_RIGHTS = """
У бота нет прав администратора для выполнения этой команды.
"""
NO_ADMIN_RIGHTS_AT_USER = """
У вас нет прав администратора для выполнения этой команды.
"""
ONLY_CHAT_COMMAND = """
Эта команда предназначена для беседы.
"""
KICK_START = """
Исключаю пользователей...
"""
KICK_FINISH = """
Пользователи исключены.
"""
KICK_EXCEPT_NO_USER = """
Нет выделенных пользователей. Для выделения пользователей отправьте команду "@canarybot кик" со списком упоминаний в любой форме, списком пересланных сообщений или ответом на сообщение.
"""
KICK_EXCEPT_ADMIN = """
Невозможно исключить {}: пользователь имеет права администратора.
"""
KICK_EXCEPT_NO_MEMBER = """
Невозможно исключить {}: не состоит в беседе.
"""


class Main(LibraryModule):
    """
    Плагин для управления беседой при помощи VKBotKit
    Команды в этом плагине:
    @botname созвать
    @botname кик
    """


    @callback(filters.IsCommand({"кик", "исключить", "выкинуть"}))
    async def kick(self, package, toolkit):
        """
        Функция для исключения пользователей
        """
        
        if package.peer_id == package.from_id:
            await toolkit.send_reply(package, ONLY_CHAT_COMMAND)

        if not toolkit.is_admin(package.peer_id, package.from_id):
            await toolkit.send_reply(package, NO_ADMIN_RIGHTS_AT_USER)
            return
          
        user_map = []

        if hasattr(package, "fwd_messages"):
            fwd_messages = map(lambda message: message.from_id, package.fwd_messages)
            user_map.extend(fwd_messages)

        if hasattr(package, "reply_message"):
            user_map.append(package.reply_message.from_id)

        if len(user_map) == 0:
            await toolkit.send_reply(package, KICK_EXCEPT_NO_USER)

        else:
            try:
                user_list = await toolkit.get_chat_members(package.peer_id)
                admin_list = await toolkit.get_chat_admins(package.peer_id)

            except exceptions.MethodError as response_error:
                await toolkit.log(response_error, log_level = enums.LogLevel.DEBUG)
                await toolkit.send_reply(package, NO_ADMIN_RIGHTS)

            await toolkit.send_reply(package, KICK_START)

            for i in user_map:
                mention = Mention(i)

                if i in user_list:
                    if i in admin_list:
                        await toolkit.send_reply(
                            package,
                            KICK_EXCEPT_ADMIN.format(mention.repr)
                            )

                    else:
                        await toolkit.api.messages.removeChatUser(
                            chat_id = package.peer_id - 2000000000,
                            user_id = i
                        )
                else:
                    await toolkit.send_reply(
                        package,
                        KICK_EXCEPT_NO_MEMBER.format(mention)
                        )
