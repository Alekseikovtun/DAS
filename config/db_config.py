import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_OUT_PORT = os.getenv('POSTGRES_OUT_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
