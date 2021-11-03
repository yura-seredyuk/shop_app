import psycopg2
from settings import *

connection = psycopg2.connect(user = USER, password = PASSWORD,
                                host = HOST, port = PORT, 
                                database = 'shop_db')

cursor = connection.cursor()
cursor.execute('SELECT * FROM employee WHERE city_id = 3;')

response = cursor.fetchall()
# print(response)
for item in response:
    print(item)

cursor.close()
connection.close()