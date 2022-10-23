"""
Copyright 2022 kensoi
"""

from vkbotkit.objects import callback, filters, Library


SHORTING_START = """
{mention}, отправьте в ответ вашу ссылку
"""

SHORTING_RESULT = """
{mention}, ваша ссылка: {link}
"""

class Main(Library):
    """
    Сокращатель ссылок
    """

    @callback(filters.IsCommand({"сократить"}))
    async def get_short(self, package, toolkit):
        """
        при получении команды '@your_bot_id start' => отправлять текст HELLO_ME
        """
        
        user_mention = await toolkit.create_mention(package.from_id, None, "nom")
        await toolkit.send_reply(package, SHORTING_START.format(mention = mention.repr))

        reply = await toolkit.replies.get(package)
        link = await toolkit.api.utils.getShortLink(url = reply.text)
        response = SHORTING_RESULT.format(mention = repr(user_mention), link = link.short_url)
        
        await toolkit.send_reply(package, response)
