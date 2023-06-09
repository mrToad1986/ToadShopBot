# типы телеграм-бота для создания элементов интерфейса
from telebot.types import KeyboardButton
# константы и настройки
from settings import config
# класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


# класс для создания и разметки интерфейса бота
class Keyboard:
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])
