import os
from emoji import emojize

NAME_DB = 'products.sqlite'
VERSION = '0.0.1'
AUTHOR = 'mrToad86'
# регистрационный токен
TOKEN = '5947031195:AAGBN6tF6FnsvIK328Vf35S7L7WVPgeLbp4'
# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до БД (в директории /settings)
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

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
    'DOWN': emojize('🔽'),
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
    'ICE_CREAM': 3,
}

# команды
COMMANDS = {
    'START': 'start',
    'HELP': 'help',
}
