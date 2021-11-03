import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import *

connection = psycopg2.connect(user = USER, password = PASSWORD,
                                host = HOST, port = PORT)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE shop_db")
cursor.close()
connection.close()