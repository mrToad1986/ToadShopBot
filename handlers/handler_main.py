from handlers.handler_com import HandlerCommands
from handlers.handler_all_text import HandlerAllText


# класс-компоновщик
class HandlerMain:
    # инициализация обработчиков
    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # непосредственно инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)

    # запуск обработчиков
    def handle(self):
        self.handler_commands.handle()
        self.handler_all_text.handle()
