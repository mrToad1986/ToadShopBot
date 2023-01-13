# используем паттерн Singleton для создания единственного объекта класса
# с предоставлением глобальной точки доступа
class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


# класс-менеджер для работы с БД
class DBManager(metaclass=Singleton):
    def __init__(self):
        pass
