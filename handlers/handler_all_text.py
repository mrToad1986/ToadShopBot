from settings.message import MESSAGES
from settings import config
from handlers.handler import Handler


# Класс для обработки входящих текстовых сообщений от нажатия на кнопки
class HandlerAllText(Handler):
    def __init__(self, bot):
        super().__init__(bot)  # что есть super() ???
        # шаг в заказе
        self.step = 0

    # обработка нажатия на кнопку "О магазине"
    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.info_menu())

    # обработка нажатия на кнопку "Настройки"
    def pressed_btn_settings(self, message):
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode='HTML',
                              reply_markup=self.keyboards.settings_menu())

    # обработка нажатия на кнопку "Назад"
    def pressed_btn_back(self, message):
        self.bot.send_message(message.chat.id, 'Вы вернулись назад',
                              reply_markup=self.keyboards.start_menu())

    # обработка нажатия на кнопку "Выбрать товар"
    def pressed_btn_category(self, message):
        # удаляем старую разметку
        self.bot.send_message(message.chat.id, 'Каталог категорий товара',
                              reply_markup=self.keyboards.remove_menu())
        # добавляем новую разметку
        self.bot.send_message(message.chat.id, 'Сделайте свой выбор',
                              reply_markup=self.keyboards.category_menu())

    # обработка выбора товара из категории
    def pressed_btn_product(self, message, product):
        self.bot.send_message(message.chat.id, 'Категория ' +
                              config.KEYBOARD[product],
                              reply_markup=self.keyboards.set_select_category(config.CATEGORY[product]))
        self.bot.send_message(message.chat.id, 'OK',
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_order(self, message):
        '''
        Обрабатывает входящие текстовые сообщения
        от нажатия на кнопку "Заказ"
        '''
        # обнуляем шаг
        self.step = 0
        # список всех товаров в заказе
        count = self.DB.select_all_products_id()
        # количество по каждой позиции товара
        quantity = self.DB.select_order_quantity(count[self.step])
        # овтет пользователю
        self.send_message_order(count[self.step], quantity, message)

    def send_message_order(self, product_id, quantity, message):
        '''
        :return: отправляет ответ пользователю при
        выполнении различных действий
        '''
        self.bot.send_message(message.chat.id, MESSAGES['order_number'].format(
            self.step + 1), parse_mode="HTML")
        self.bot.send_message(message.chat.id, MESSAGES['order'].format(
            self.DB.select_single_product_name(product_id),
            self.DB.select_single_product_title(product_id),
            self.DB.select_single_product_price(product_id),
            self.DB.select_order_quantity(product_id)), parse_mode="HTML",
                              reply_markup=self.keyboards.orders_menu(self.step, quantity))

    def pressed_btn_up(self, message):
        '''
        Обработка нажатия кнопки увеличения
        количества определенного товара в заказе
        '''
        # список всех товаро в заказе
        count = self.DB.select_all_products_id()
        # количество конкретной позиции в заказе
        quantity_order = self.DB.select_order_quantity(count[self.step])
        # количество конкретной позиции в запасе
        quantity_product = self.DB.select_single_product_quantity(count[self.step])
        # если товар есть в наличии
        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1
            # вносим изменения в БД orders
            self.DB.update_order_value(count[self.step], 'quantity', quantity_order)
            # вносим изменения в БД product
            self.DB.update_product_value(count[self.step], 'quantity', quantity_product)
        # отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity_order, message)


    def handle(self):
        '''
        обработчик(декоратор) сообщений,
        который обрабатывает входящие текстовые сообщения
        от нажатия кнопок.
        '''
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # основеное меню
            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)
            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)
            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)
            # категории товара
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')
            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')
            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')
            if message.text == config.KEYBOARD['ORDER']:
                # если есть заказ
                if self.DB.count_rows_order() > 0:
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(message.chat.id, MESSAGES['no_orders'],
                                          parse_mode='HTML',
                                          reply_markup=self.keyboards.category_menu())
            # меню работы с заказом
            if message.text == config.KEYBOARD['UP']:
                self.pressed_btn_up(message)

