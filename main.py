from src.secrets import (
    DB_HOST,
    DB_USER,
    DB_PASS,
    DB_NAME,
    DB_PORT
)

from src.singleton import MySQLConnection
from src.logger import logger

if __name__ == "__main__":
   try:
       conn_mysql = MySQLConnection.get_instance(DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT)
       logger.info(f'Connected to MySQL database successfully: {conn_mysql}')
   except Exception as error:
       logger.error(f'Error to connect to MySQL database: {error}')