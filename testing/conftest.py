import os
from psycopg2 import pool
from models.order.order_model import OrderData, OrderItemData, Order, OrderItem
from models.order.cart_model import CartItemData
from datetime import datetime

test_user_id = None
test_user_id_1 = 'test_user_1'
test_user_id_2 = 'test_user_2'
test_user_id_3 = 'test_user_3'
test_user_id_4 = 'test_user_4'

test_cart_item_data1 = CartItemData(
    product_id=-1, quantity=1
)

test_order_item_data1 = OrderItemData(
    product_id=-1, quantity=1, price=1000
)
test_order_item_data2 = OrderItemData(
    product_id=-2, quantity=2, price = 2000
)
test_order_item_data3 = OrderItemData(
    product_id=-3, quantity=3, price=3000
)

order_item_1 = OrderItem(
    order_item_id=-1, order_id=-1, user_id=test_user_id_1, 
    product_id=-1, quantity=1, price = 1000
)
order_item_2 = OrderItem(
    order_item_id=-2, order_id=-1, user_id=test_user_id_1, 
    product_id=-2, quantity=2, price = 2000
)
order_item_3 = OrderItem(
    order_item_id=-3, order_id=-1, user_id=test_user_id_1, 
    product_id=-3, quantity=3, price = 3000
)

test_price = [1000,2000,3000]

test_order_item_datas = [
    test_order_item_data1, test_order_item_data2, test_order_item_data3
]

test_order_data = OrderData(
    order_items=test_order_item_datas,
    shipping_method = 'TestLogistics',
    contact_phone='88612345678',
    email='aaa@aaa.com',
    payment_method='TestPayment',
    shipping_address='qwertyuiop'
)

test_testuser1_order_data = {
    'order_id': -1,
    'user_id': test_user_id_1,
    'order_date': datetime.now(),
    'total_amount': 14000,
    'order_status': 1,
    'shipping_status': 1,
    'payment_status': 1,
    'payment_date': None,
    'shipping_method': 'TestLogistics',
    'shipping_address': 'wertyuio',
    'contact_phone': '886234567890',
    'email': 'bbb@bbb.com',
    'payment_method': 'TestPayment'
}
test_testuser1_order_data_1 = {
    'order_id': -2,
    'user_id': test_user_id_1,
    'order_date': datetime.now(),
    'total_amount': 14000,
    'order_status': 1,
    'shipping_status': 1,
    'payment_status': 1,
    'payment_date': None,
    'shipping_method': 'TestLogistics',
    'shipping_address': 'wertyuio',
    'contact_phone': '886234567890',
    'email': 'bbb@bbb.com',
    'payment_method': 'TestPayment'
}

test_testuser1_order_data_2 = {
    'order_id': -3,
    'user_id': test_user_id_1,
    'order_date': datetime.now(),
    'total_amount': 14000,
    'order_status': 1,
    'shipping_status': 1,
    'payment_status': 1,
    'payment_date': None,
    'shipping_method': 'TestLogistics',
    'shipping_address': 'wertyuio',
    'contact_phone': '886234567890',
    'email': 'bbb@bbb.com',
    'payment_method': 'TestPayment'
}

test_testuser_order_data_3 = {
    'order_id': -4,
    'user_id': test_user_id,
    'order_date': datetime.now(),
    'total_amount': 14000,
    'order_status': 1,
    'shipping_status': 1,
    'payment_status': 1,
    'payment_date': None,
    'shipping_method': 'TestLogistics',
    'shipping_address': 'wertyuio',
    'contact_phone': '886234567890',
    'email': 'bbb@bbb.com',
    'payment_method': 'TestPayment'
}

test_place_order_data = {
    "order_items" : [
        {
            "product_id" : -2,
            "quantity" : 2,
            "price" : 2000
        },
        {
            "product_id" : -1,
            "quantity" : 1,
            "price" : 1000
        }
    ],
    "shipping_method" : "TestLogistics",
    "shipping_address" : "wertyuio",
    "contact_phone" : "8863456789",
    "email" : "aaa@aaa.com",
    "payment_method" : "TestPayment"
}

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_DATA_POOL = {
    'host': DB_HOST,
    'database': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'port' : DB_PORT,
    'minconn' : 1,
    'maxconn' : 20,
}
test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)

def conftest_order(test_data):
    order = Order(**test_data)
    order_items = conftest_setup_order_items(order, test_order_item_datas)
    order.set_order_items(order_items)
    return order


def conftest_setup_order_items(order, order_item_datas):
    order_items = []
    id = 1
    for item in order_item_datas:
        order_item = OrderItem(
            order_item_id= id, 
            user_id=order.user_id, 
            order_id=order.order_id, 
            product_id=item.product_id,
            quantity=item.quantity, 
            price=item.price)
        order_items.append(order_item)
        id += 1
    return order_items    