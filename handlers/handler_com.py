# импорт класса-родителя
from handlers.handler import Handler


# класс-обработчик входящих комманд /start и т.п.
class HandlerCommands(Handler):
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        self.bot.send_message(message.chat.id,
                              f'Здравствуйте, {message.from_user.first_name}.'
                              f' Добро пожаловать в наш магазин!',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(message)
            print(type(message))
            if message.text == '/start':
                self.pressed_btn_start(message)
