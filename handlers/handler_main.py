# обработка комманд
from handlers.handler_com import HandlerCommands
# обработка нажатия на кнопки и иные сообщения
from handlers.handler_all_text import HandlerAllText
# обработка нажатия на инлайн кнопки
from handlers.handler_inline_query import HandlerInlineQuery


# класс-компоновщик
class HandlerMain:
    # инициализация обработчиков
    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # непосредственно инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    # запуск обработчиков
    def handle(self):
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()
