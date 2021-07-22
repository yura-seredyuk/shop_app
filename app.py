from admin import Admin
from customer import Customer
from pprint import pprint
import datetime
from custom import respprint

admin1 = Admin('Admin2', '1111')
# admin1.register_self()

orders = admin1.get_order_info(category='status', selector=False)

respprint(orders)


# print(admin1.login_self())


# customer2 = Customer('kate', '1111')
# # customer2.register_self('Kate', 'Kat', 2)
# customer2.login_self()
# # print(customer2.first_name)
# customer2.create_order([('Apple',2,), ('Meat', 5)])