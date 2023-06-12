# создание объекта бота
from telebot import TeleBot
# константы и настройки
from settings import config
# класс-обработчик
from handlers.handler_main import HandlerMain


# сервер бота на основе pyTelegramBotAPI
class TelBot:
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    # запуск обработчика событий
    def start(self):
        self.handler.handle()

    # запуск основных событий сервера
    def run_bot(self):
        self.start()
        self.bot.polling(none_stop=True)

# # эхо для тестирования
# bot = TeleBot(config.TOKEN)
#
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
    # bot.infinity_polling()
