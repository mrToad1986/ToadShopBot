# реализация абстрактных классов
import abc
# разметка клавиатуры и клавиш
from markup.markup import Keyboards
# класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager

# базовый абстрактный класс-обработчик
class Handler(metaclass=abc.ABCMeta):
    def __init__(self, bot):
        self.bot = bot
        self.keyboards = Keyboards()
        self.DB = DBManager()

    # задекорированный метод будет переопределен в классах-наследниках
    @abc.abstractmethod
    def handle(self):
        pass