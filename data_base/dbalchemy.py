# формирование пути к файлу базы данных
from os import path
# создания подключения к базе данных
from sqlalchemy import create_engine
# создание сессии, через сессии ORM-библиотека SQLAlchemy взаимодействует с БД
from sqlalchemy.orm import sessionmaker

from settings import config
from models.product import Products
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
