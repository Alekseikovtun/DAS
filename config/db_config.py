import os

from dotenv import load_dotenv

load_dotenv('./.env')

DB_OUT_PORT = os.getenv('DB_OUT_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST',  default='localhost')
