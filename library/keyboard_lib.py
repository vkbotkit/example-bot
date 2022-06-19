"""
Copyright 2022 kensoi
"""

from vkbotkit.utils import VERSION
from vkbotkit.objects import (
    callback,
    filters,
    enums,
    LibraryModule)

from vkbotkit.objects.keyboard import (
    Keyboard, KeyboardColor
)


class Main(LibraryModule):
    """
    Пример плагина с клавиатурой
    """

    def __init__(self):
        LibraryModule.__init__(self)
        self.keyboard_test = None
        self.keyboard_test2 = None


    async def start(self, toolkit):
        """
        Функция, выполняющаяся при запуске бота
        """
        self.keyboard_test = Keyboard(one_time = False, inline = True)
        self.keyboard_test2 = Keyboard(one_time = False, inline = True)

        self.keyboard_test.add_button("Кнопка 1", KeyboardColor.PRIMARY)
        self.keyboard_test.add_line()
        self.keyboard_test.add_button("A")
        self.keyboard_test.add_button("B")
        self.keyboard_test.add_line()
        self.keyboard_test.add_button("C")

        self.keyboard_test2.add_button("Кнопка 2", KeyboardColor.PRIMARY)
        self.keyboard_test2.add_line()
        self.keyboard_test2.add_location_button()
        toolkit.log(
            "keyboardlib loaded"
        )

    @callback(filters.WhichUpdate({enums.Events.MESSAGE_NEW,}))
    async def send_keyboard(self, package):
        """
        Команда для отправки команды
        """
        await package.toolkit.api.messages.send(
            random_id = package.toolkit.gen_random(),
            peer_id = package.peer_id,
            message = "Пример клавиатуры",
            keyboard = self.keyboard_test.get_keyboard()
        )
