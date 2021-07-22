import psycopg2
from settings import *
from connection import Connection
from datetime import datetime

class Customer(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.first_name = ''
        self.last_name = ''
        self.city_id = ''
        self.id = ''

    def register_self(self,first_name, last_name, city ):
        self.register( self.login, self.password, 'cus')
        data=[{
            'city_id': city,
            'first_name': first_name,
            'last_name': last_name,
            'reg_id': self.getNextId('reg_base')-1
        }]
        self._postData('customer', data)
    
    def login_self(self):
        id = self.login_check(self.login,self.password, 'cus')
        if id:
            self.first_name = self.getData(('customer',),('first_name',),f"where reg_id = {id}")[0][0]
            self.last_name = self.getData(('customer',),('last_name',),f"where reg_id = {id}")[0][0]
            self.city_id = self.getData(('customer',),('city_id',),f"where reg_id = {id}")[0][0]
            self.id = self.getData(('customer',),('id',),f"where reg_id = {id}")[0][0]
            # print(self.first_name,  self.last_name, self.city_id)
            return True
        return False

    def get_order_info(self, category = '', selector = '', ):
        """
        category must be one of the item from the list:
        ['city_name','date_of_order', 'product_name']

        date format for selector: 2020-6-12
        """
        if self.login_self():
            categoryes = ['city_name','date_of_order', 'product_name']
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name, o.date_of_order, concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price """,)
            if category and category in categoryes and selector:
                where = f"""where {category} = '{selector}'"""
            else:
                where = ''
            selector = f""" inner JOIN employee e on e.id = o.employee_id 
                            inner JOIN city c on c.id = o.city_id 
                            inner JOIN customer c2 on c2.id = o.customer_id 
                            inner JOIN product p on p.id = o.product_id {where}"""
            result = self.getData(table, fields, selector)
            fieldNames = ["id", "employee", "city_name","date_of_order", "customer", "product_name", "price" ]
            changeRes = []
            for item in result:
                cort = {}
                for index,element in enumerate(item):
                    cort[fieldNames[index]]=element
                changeRes.append(cort)
        else:
            changeRes = "Invalid loging!"
        return changeRes



    def create_order(self, products):
        if  self.login_self():
            table = 'orders'
            data = []
            for item in products:
                order = {
                    "customer_id": self.id,
                    "city_id": self.city_id,
                    "date_of_order": datetime.today().strftime('%Y-%m-%d'),
                    "product_id": self.getData(('product',),('id',),f"where product_name = '{item[0]}'")[0][0],
                    "price": self.getData(('product',),('unit_price',),f"where product_name = '{item[0]}'")[0][0] * item[1]
                    }
                data.append(order)
            result = self._postData(table, data)
            return result





if __name__ == '__main__':
    pass


