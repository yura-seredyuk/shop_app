import psycopg2
from settings import *
from connection import Connection
import datetime

class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self):
        self.register( self.login, self.password, 'adm')
    
    def login_self(self):
        return self.login_check(self.login,self.password, 'adm')

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
            selector = f"""  inner JOIN employee e on e.id = o.employee_id 
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



    def add_pr_category(self, data):
        table = 'product_category'
        result = self._postData(table, data)
        return result

    def edit_pr_category(self, data, selector):
        table = 'product_category'
        result = self.updateData(table, data, selector)
        return result

    def delete_pr_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(table,selector)
        return result





if __name__ == '__main__':

    admin1 = Admin('Admin1', '1234')
    # orders = admin1.get_order_info()
    # print(orders)
    data = [{
            'category_name': "Beer"
        },
    ]
    put = admin1.add_pr_category(data)
    print(put)

    
    # data = {
    #         'category_name': "Water"
    #     }
    # edit = admin1.edit_pr_category(data, "category_name = 'Rom'")
    # print(edit)
    # id = admin1.getNextId('product_category')
    # print(id)

    # dele = admin1.delete_pr_category('Beer')
    # print(dele)


