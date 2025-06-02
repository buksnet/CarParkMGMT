from dotenv import load_dotenv
from os import getenv
from uuid import uuid4

load_dotenv('application/config/.env')

# ------------------------------- Загрузка конфигурации приложения -------------------------------------

DEBUG = True if getenv('DEBUG') == 'True' else False
TESTING = True if getenv('TESTING') == 'True' else False
SECRET_KEY = uuid4().hex
TEMPLATES_AUTO_RELOAD = getenv('TEMPLATES_AUTO_RELOAD')

# ------------------------ Загрузка конфигурации модулей приложения -------------------------------------

MAX_REQUESTS_PER_HR = int(getenv('MAX_REQUESTS_PER_HR'))

# -------------------------------- Прочие переменные ----------------------------------------------------

DATABASE_PASSWORD = getenv('DATABASE_PASSWORD')
DATABASE_PORT = getenv('DATABASE_PORT')
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_USER = getenv('DATABASE_USER')
DATABASE_URL = getenv('DATABASE_URL')
