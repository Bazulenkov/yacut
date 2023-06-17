import os
import secrets


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex())


LINK_LENGTH = 6

# messages
NEW_LINK_MESSAGE = "Ваша новая ссылка готова:"

# error messages
DUPLICATE_MESSAGE = "Имя {} уже занято!"
NO_REQUIRED_FIELDS_GIVEN_MESSAGE = "В запросе отсутствуют обязательные поля"
NO_BODY_MESSAGE = "Отсутствует тело запроса"
NOT_FOUND_MESSAGE = "Ссылка с указанным коротким путем не найдена"
