from src.secrets import (
    DB_HOST,
    DB_USER,
    DB_PASS,
    DB_NAME,
    DB_PORT
)

from src.singleton import MySQLConnection
from src.logger import logger

import time

def main() -> None:
    try:
       credentials = {
          "DB_HOST": DB_HOST,
          "DB_USER": DB_USER,
          "DB_PASS": DB_PASS,
          "DB_NAME": DB_NAME,
          "DB_PORT": DB_PORT
       }
       conn_mysql = MySQLConnection.get_instance(credentials)
       logger.info(f'MySQL database connected successfully: {conn_mysql}')
       time.sleep(10)
       MySQLConnection.close_instance()
       logger.info(f'MySQL database closed successfully: {conn_mysql}')
    except TypeError as error:
       logger.error(f'Error to connect to MySQL database: {error}')

if __name__ == "__main__":
   main()