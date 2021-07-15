import psycopg2
from settings import *
from connection import Connection

class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self):
        pass

    def get_order_info(self, selector = ''):
        table = ('orders',)
        fields = ('*',)
        selector = ''
        result = self.getData(table, fields, selector)
        return result
       

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


