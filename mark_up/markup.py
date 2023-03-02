# типы телеграм-бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
# константы и настройки
from settings import config
# класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


# класс для создания и разметки интерфейса бота
class Keyboards:
    # инициализируем менеджер для работы с БД
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    # Создает и возвращает кнопку по входным параметрам
    def set_btn(self, name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD[name])

    # Создает разметку кнопок в основном меню и возвращает разметку
    # Определение рассположение кнопок в меню
    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        # Создает разметку кнопок в меню 'О магазине'
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        # Создает разметку кнопок в меню 'Настройки'
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup