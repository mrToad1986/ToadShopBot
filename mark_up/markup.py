# типы телеграм-бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton
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

    def set_inline_btn(self, name):
        '''
        Создает и возвращает инлайн кнопку (товарная позиция)
        по входным параметрам
        '''
        return InlineKeyboardButton(str(name), callback_data=str(name.id))
        # где id  - идентификатор товара

    def set_select_category(self, category):
        '''
        создает разметку кнопок в выбранной категории товара
        возвращает разметку
        '''
        self.markup = InlineKeyboardMarkup(row_width=1)
        # загружаем в названия кнопок данные из БД
        for itm in self.DB.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(itm))
        return self.markup

    @staticmethod
    def remove_menu():
        '''
        Удаление меню
        '''
        return ReplyKeyboardRemove()

    def category_menu(self):
        '''
        Создание разметки кнопок в меню категорий товара
        и возвращение разметки
        '''
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    def orders_menu(self, step, quantity):
        '''
        создает разметку кнопок в заказе товара и возвращает разметку
        '''
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('X', step, quantity)
        itm_btn_2 = self.set_btn('DOWN', step, quantity)
        itm_btn_3 = self.set_btn('AMOUNT_PRODUCT', step, quantity)
        itm_btn_4 = self.set_btn('UP', step, quantity)
        itm_btn_5 = self.set_btn('BACK_STEP', step, quantity)
        itm_btn_6 = self.set_btn('AMOUNT_ORDERS', step, quantity)
        itm_btn_7 = self.set_btn('NEXT_STEP', step, quantity)
        itm_btn_8 = self.set_btn('APPLAY', step, quantity)
        itm_btn_9 = self.set_btn('<<', step, quantity)
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_6, itm_btn_7)
        self.markup.row(itm_btn_9, itm_btn_8)

        return self.markup
