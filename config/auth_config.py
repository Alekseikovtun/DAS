import os

from dotenv import load_dotenv

load_dotenv('./.env')

KEY = os.getenv('KEY')
ALGORITHMS = os.getenv('ALGORITHMS')