DB_HOST='206.189.197.253'
DB_USER='webnuti'
DB_PASS='internonuti123'
DB_NAME='webdb'
DB_PORT='9306'

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