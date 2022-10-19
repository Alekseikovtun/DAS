import os

from dotenv import load_dotenv

load_dotenv('./.env')

POSTGRES_OUT_PORT = os.getenv('DB_OUT_PORT')
POSTGRES_USER = os.getenv('DB_USER')
POSTGRES_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
