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


SOZYV = """
ВНИМАНИЕ, ПОЛЬЗОВАТЕЛИ! 
Обратите внимание на сообщения {sender}!
{members}
"""
NO_ADMIN_RIGHTS = """
У бота нет прав администратора для выполнения этой команды.
"""
NO_ADMIN_RIGHTS_AT_USER = """
У вас нет прав администратора для выполнения этой команды.
"""
ONLY_CHAT_COMMAND = """
Эта команда предназначена для беседы.
"""


class Main(LibraryModule):
    """
    Плагин для управления беседой при помощи VKBotKit
    Команды в этом плагине:
    @botname созвать
    @botname кик
    """

    @callback(filters.IsCommand({"созвать", "позвать", "созыв"}))
    async def sozyv(self, package, toolkit):
        """
        при получении команды '@botname созвать' => отправлять текст SOZYV
        """
        
        if package.peer_id == package.from_id:
            await toolkit.send_reply(package, ONLY_CHAT_COMMAND)
            return
        
        if not await toolkit.is_admin(package.peer_id, package.from_id):
            await toolkit.send_reply(package, NO_ADMIN_RIGHTS_AT_USER)
            return
        
        else:
            try:
                chat_members = await toolkit.get_chat_members(package.peer_id)
                chat_members.remove(package.from_id)
                chat_members_mapped = map(lambda x: Mention(x, "."), chat_members)
                chat_members_repred = map(lambda x: x.repr, user_list)
                chat_members = " ".join(list(chat_members_repred))

                user_mention = await toolkit.create_mention(package.from_id)
                response = SOZYV.format(
                        sender = user_mention.repr,
                        members = chat_members)
                toolkit.send_reply(package, response,
                    attachment = "photo-195675828_457242153")

            except exceptions.MethodError as response_error:
                await toolkit.log(response_error, log_level = enums.LogLevel.DEBUG)
                await toolkit.send_reply(package, NO_ADMIN_RIGHTS)
        else:
