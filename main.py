from src.singleton import MySQLConnection
from src.logger import logger

def main() -> None:
    try:
       conn_mysql = MySQLConnection.get_instance()
       logger.info(f'Connected to MySQL database successfully: {conn_mysql}')
    except TypeError as error:
       logger.error(f'Error to connect to MySQL database: {error}')

if __name__ == "__main__":
   main()