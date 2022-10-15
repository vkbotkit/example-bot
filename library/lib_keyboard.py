"""
Copyright 2022 kensoi
"""

from vkbotkit.objects import callback, filters, keyboard, LibraryModule

# важное замечание для клавиатуры
# для работы этого плагина необходимо включить возможности чат-ботов
# vk.com/your_bot_id?act=messages&tab=bots

keyboard_test = keyboard.Keyboard(one_time = False, inline = True)

keyboard_test.add_button("Кнопка 1", keyboard.KeyboardColor.PRIMARY)
keyboard_test.add_button("A")
keyboard_test.add_button("B")
keyboard_test.add_line()
keyboard_test.add_button("Кнопка 2", keyboard.KeyboardColor.PRIMARY)
keyboard_test.add_button("C")
keyboard_test.add_button("D")


class Main(LibraryModule):
    """
    Пример плагина с клавиатурой
    """

    @callback(filters.IsCommand({"keyboard", "клавиатура"}))
    async def send_keyboard(self, package, toolkit):
        """
        Команда для отправки команды
        """

        await toolkit.send_reply(
            package, "Пример клавиатуры",
            keyboard = keyboard_test.get_keyboard())
