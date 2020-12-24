import mysql.connector as mysql

class MySQLConnection:

    __instance = None

    def __init__(self, host: str, user: str, pwd: str, database : str, port: str):
        if MySQLConnection.__instance is None:
            MySQLConnection.__instance = mysql.connect(host, user, pwd, database, port)
        else:
            raise Exception('You cannot create another MySQL connection')

    @staticmethod
    def get_instance(host: str, user: str, pwd: str, database : str, port: str):
        if not MySQLConnection.__instance:
            MySQLConnection(host, user, pwd, database, port)
        return MySQLConnection.__instance