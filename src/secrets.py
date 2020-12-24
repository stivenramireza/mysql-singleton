import os
from dotenv import load_dotenv

ENV = os.environ.get('ENV')
if ENV == 'production':
    dotenv_path = '.env'
else:
    dotenv_path = '.env.dev'

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files do not exist')

load_dotenv(dotenv_path)

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')