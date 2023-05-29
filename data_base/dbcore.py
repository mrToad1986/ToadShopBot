'''
инициализация декларативного стиля для БД
важно, чтобы вся работа осуществлялась через один и тот же объект Base.
с последующим импортом во все исползующие его файлы
'''
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()