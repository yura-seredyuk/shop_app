import psycopg2
from settings import *

class Connection():

    @classmethod
    def openDB(cls):
        connection = psycopg2.connect(user = USER, password = PASSWORD,
                                host = HOST, port = PORT, 
                                database = 'shop_db')
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def closeDB(cls, connection, cursor):
        cursor.close()
        connection.close()

    def getData(self, table:tuple, fields:tuple, selector = ''):
        connection, cursor = self.openDB()
        select_query = f"""SELECT {','.join(fields)} FROM {','.join(table)} {selector} ORDER BY id;"""
        cursor.execute(select_query)
        connection.commit()
        result = cursor.fetchall()
        self.closeDB(connection, cursor)
        return result
        

    def _postData(self, table, data:list):
        connection, cursor = self.openDB()
        next_id = self.getNextId(table)
        fields = list(data[0].keys())
        fields.append('id')
        values = ''
        for row in data:
            value = f"""({','.join(map(lambda item: f"'{item}'" ,row.values()))}, {next_id}),"""
            next_id += 1
            values += value
        insert_query = f"""INSERT INTO {table} ({','.join(fields)}) VALUES {values[:-1]};"""
        cursor.execute(insert_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Insert done!'

        

    def updateData(self,table, data:dict, selector:str):
        connection, cursor = self.openDB()
        set_items = ''
        for key in data:
            set_items += f"{key} = '{data[key]}',"

        update_query = f"""UPDATE {table} SET {set_items[:-1]} WHERE {selector}"""
        cursor.execute(update_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Update done!'

    def deleteData(self, table, selector = ''):
        connection, cursor = self.openDB()
        delete_query = f"""DELETE FROM {table} WHERE {selector};"""
        cursor.execute(delete_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Item was deleted!'

    
    def getNextId(self, table):
        table = (table,)
        fields = ('id',)
        print(self.getData(table, fields))
        if self.getData(table, fields) == []:
            return 1
        result = self.getData(table, fields)[-1][0] + 1
        return result

    def register(self, login, password, role):
        data = [{
            'login': login,
            'password': password,
            'role': role
        }]
        find_login =  self.getData(('reg_base',),('login',), f" where login = '{login}'")
        if not find_login:
            self._postData('reg_base',data)
        else:
            print('Login is exist!')
    
    def login_check(self, login, password, role):
        find_login =  self.getData(('reg_base',),('*',), f" where login = '{login}'")
        if find_login and password == find_login[0][2] and find_login[0][3] == role:
            return True
        else: 
            return False






