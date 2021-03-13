import  sqlite3
import SQLQuerys as querys
from sqlite3 import Error
import configparser

config= configparser.ConfigParser()
config.read('config.ini')

path=config['DataBase']['testPath']

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection



connection=create_connection(path)
querys.create_Tables(connection)
querys.insert_snapshots(connection)


