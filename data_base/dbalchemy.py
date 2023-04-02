# формирование пути к файлу базы данных
from os import path
from datetime import datetime
# создания подключения к базе данных
from sqlalchemy import create_engine
# создание сессии, через сессии ORM-библиотека SQLAlchemy взаимодействует с БД
from sqlalchemy.orm import sessionmaker

from settings import config, utility
from models.product import Products
from models.order import Order
from data_base.dbcore import Base


class Singleton(type):
    '''
    используем паттерн Singleton для создания единственного объекта класса
    c предоставлением глобальной точки доступа
    '''

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


# класс-менеджер для работы с БД
class DBManager(metaclass=Singleton):
    # инициализация сессии и подключения к БД
    def __init__(self):
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    # Возвращает все все товары категории
    def select_all_products_category(self, category):
        result = self._session.query(Products).filter_by(category_id=category).all()
        self.close()
        return result

    # закрытие сессии
    def close(self):
        self._session.close()

    # заполнение заказа
    def _add_orders(self, quantity, product_id, user_id, ):
        # получаем список всех product_id
        all_id_product = self.select_all_product_id()
        # обновление таблиц заказа и продуктов, если данные есть в списке
        if product_id in all_id_product:
            quantity_order = self.select_order_quantity(product_id)
            quantity_order += 1
            self.update_order_value(product_id, 'quantity', quantity_order)
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)
            return
        # создаем новый объект заказа, если нет данных
        else:
            order = Order(quantity=quantity, product_id=product_id,
                          user_id=user_id, data=datetime.now())
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)
        self._session.add(order)
        self._session.commit()
        self.close()

    def select_all_products_id(self):
        '''
        :return: все id товара в заказе и конвертирует
        результат выбрки в список c помощью функции _convert модуля utility
        '''
        result = self._session.query(Order.product_id).all()
        self.close()
        return utility._convert(result)

    def select_order_quantity(self, product_id):
        '''
        :return: количество товара из заказа
        в соответствии с номером товара
        '''
        result = self._session.query(Order.quantity).filter_by(
            product_id=product_id).one()
        self.close()
        return result.quantity

    def update_order_value(self, product_id, name, value):
        '''
        Обновляет данные указанное позиции заказа
        в соответствии с номером товара(rownum)
        '''
        self._session.query(Order).filter_by(
            product_id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_quantity(self, rownum):
        '''
        :param rownum: номер товара, определяется при выборе товара в интерфейсе
        :return: количество товара на складе
        '''
        result = self._session.query(
            Products.quantity).filter_by(id=rownum).one()
        self.close()
        return result.quantity

    def update_product_value(self, rownum, name, value):
        '''
        Обновляет количество товара на складе
        '''
        self._session.query(Products).filter_by(
            id=rownum).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_name(self, rownum):
        '''
        :return: название товара в соответствии с номером товара
        '''
        result = self._session.query(Products.name).filter_by(id=rownum).one()
        self.close()
        return result.name

    def select_single_product_title(self, rownum):
        '''
        :return: торговую марку товара в соответствии с номером товара
        '''
        result = self._session.query(Products.title).filter_by(id=rownum).one()
        self.close()
        return result.title

    def select_single_product_price(self, rownum):
        '''
        :return: цену товара в соответствии с номером товара
        '''
        result = self._session.query(Products.price).filter_by(id=rownum).one()
        self.close()
        return result.price

    def count_rows_orders(self):
        '''
        :return: количество позиций в заказе
        '''
        result = self._session.query(Order).count()
        self.close()
        return result

    def delete_order(self, product_id):
        '''
        Удаляет данные указанной строки заказа
        '''
        self._session.query(Order).filter_by(product_id=product_id).delete()
        self._session.commit()
        self.close()
