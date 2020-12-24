from src.secrets import (
    DB_HOST,
    DB_USER,
    DB_PASS,
    DB_NAME,
    DB_PORT
)

import mysql.connector as mysql

class MySQLConnection:

    __instance = mysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, database=DB_NAME, port=DB_PORT)

    def __init__(self):
        if MySQLConnection.__instance is None:
            MySQLConnection.__instance = self
        else:
            raise Exception('You cannot create another MySQL connection')

    @staticmethod
    def get_instance():
        if not MySQLConnection.__instance:
            MySQLConnection()
        return MySQLConnection.__instance