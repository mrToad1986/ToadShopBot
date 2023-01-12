import os
from emoji import emojize

# регистрационный токен
TOKEN = ''
# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до БД (в директории /settings)
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

NAME_DB = 'products.sqlite'
VERSION = '0.0.1'
AUTHOR = 'User'

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLY': '✅ Оформить заказ',
    'COPY': '©️'
}

# категории продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICECREAM': 3,
}

# команды
COMMANDS = {
    'START': 'start',
    'HELP': 'help',
}

