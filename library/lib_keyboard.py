"""
Copyright 2022 kensoi
"""

from vkbotkit.objects import callback, filters, keyboard, LibraryModule


class Main(LibraryModule):
    """
    Пример плагина с клавиатурой
    """

    @callback(filters.IsCommand({"keyboard", "клавиатура"}))
    async def send_keyboard(self, package):
        """
        Команда для отправки команды
        """
        keyboard_test = keyboard.Keyboard(one_time = False, inline = True)

        keyboard_test.add_button("Кнопка 1", keyboard.KeyboardColor.PRIMARY)
        keyboard_test.add_line()
        keyboard_test.add_button("A")
        keyboard_test.add_button("B")
        keyboard_test.add_line()
        keyboard_test.add_button("C")

        await package.toolkit.api.messages.send(
            random_id = package.toolkit.gen_random(),
            peer_id = package.peer_id,
            message = "Пример клавиатуры",
            keyboard = keyboard_test.get_keyboard()
        )
