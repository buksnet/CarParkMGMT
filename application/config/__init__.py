from dotenv import load_dotenv
from os import getenv
from uuid import uuid4

load_dotenv('application/config/.env')

DEBUG = True if getenv('DEBUG') == 'True' else False
TESTING = True if getenv('TESTING') == 'True' else False
SECRET_KEY = uuid4().hex
MAX_REQUESTS_PER_HR = int(getenv('MAX_REQUESTS_PER_HR'))
DATABASE_URL = getenv('DATABASE_URL')
DATABASE_PORT = getenv('DATABASE_PORT')
DATABASE_PASSWORD = getenv('DATABASE_PASSWORD')
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_USER = getenv('DATABASE_USER')