from settings.message import MESSAGES
from settings import config
from handlers.handler import Handler

# Класс для обработки входящих текстовых сообщений от нажатия на кнопки
class HandlerAllText(Handler):
    def __init__(self, bot):
        super().__init__(bot) # что есть super() ???
        # шаг в заказе
        self.step = 0

    # обработка нажития на кнопку "О магазине"
    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.info_menu())

    # обработка нажития на кнопку "Настройки"
    def pressed_btn_settings(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.settings_menu())

    # обработка нажития на кнопку "Назад"
    def pressed_btn_back(self, message):
        self.bot.send_message(message.chat.id, 'Вы вернулись назад',
                              reply_markup=self.keyboards.start_menu())

    # обработчик(декоратор) сообщений,
    # который обрабатывает входящие текстовые сообщения
    # от нажатия кнопок.
    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)
            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)
            # if message.text == config.KEYBOARD['<<']:
            #     self.pressed_btn_back()
            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)