from admin import Admin
from pprint import pprint
import datetime
from custom import respprint

admin1 = Admin('Admin2', '1111')

orders = admin1.get_order_info(category='date_of_order', selector='2020-6-12')

respprint(orders)

# admin1.register_self()
# print(admin1.login_self())