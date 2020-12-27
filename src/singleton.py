from typing import Dict

import mysql.connector as mysql

class MySQLConnection:

    __instance = None

    def __init__(self, host: str, user: str, password: str, name: str, port: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.name = name
        self.port = port
        if MySQLConnection.__instance is None:
            MySQLConnection.__instance = mysql.connect(host=self.host, user=self.user, passwd=self.password, database=self.name, port=self.port)
        else:
            raise Exception('You cannot create another MySQL connection')

    @staticmethod
    def get_instance(credentials: Dict[str, str]) -> object:
        if not MySQLConnection.__instance:
            MySQLConnection(credentials['DB_HOST'], credentials['DB_USER'], credentials['DB_PASS'], credentials['DB_NAME'], credentials['DB_PORT'])
        return MySQLConnection.__instance

    @staticmethod
    def close_instance() -> None:
        MySQLConnection.__instance.close()