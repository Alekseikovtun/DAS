import os

from dotenv import load_dotenv

load_dotenv('./.env')

POSTGRES_OUT_PORT = os.getenv('POSTGRES_OUT_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST',  default='localhost')
