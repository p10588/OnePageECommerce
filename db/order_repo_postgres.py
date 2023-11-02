import os
from datetime import datetime
from models.order.interface_order_repo import IOrderRepo
from models.order.order_model import Order, OrderItem

from psycopg2.extensions import connection


class OrderRepo(IOrderRepo):

    def __init__(self, connection:connection):
        self.connection = connection

    def get_next_order_id(self):
        with self.connection.cursor() as cursor:
            query = "SELECT MAX(order_id) FROM orders"
            cursor.execute(query)
            result = cursor.fetchone()

            if result and result[0] is not None:
                next_id = result[0] + 1
            else:
                next_id = 1

            return next_id

    def get_order(self, order_id):
        with self.connection.cursor() as cursor:
            sql_select_order = 'SELECT * FROM orders WHERE order_id = %s'
            cursor.execute(sql_select_order, (order_id, ))
            data = cursor.fetchone()
            order_data = Order(*data)
            return order_data

    def add_order(self, order:Order):
        with self.connection.cursor() as cursor:
            sql_insert_order = '''INSERT INTO orders (order_id, user_id, order_date, total_amount, 
                                                      shipping_address, contact_phone, 
                                                      order_status, shipping_status, 
                                                      shipping_method, payment_method, 
                                                      payment_status, payment_datetime,
                                                      email) 
                                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                  RETURNING order_id'''
            order_date = self.__sql_timestamp(order.order_date)
            payment_date = self.__sql_timestamp(order.order_date)
            cursor.execute(sql_insert_order,(order.order_id, order.user_id ,order_date, 
                                             order.total_amount, order.shipping_address, 
                                             order.contact_phone, order.order_status,
                                             order.shipping_status, order.shipping_method,
                                             order.payment_method, order.payment_status,
                                             payment_date, order.email))

    def __sql_timestamp(self, datetime:datetime):
        return datetime.strftime('%Y-%m-%d %H:%M:%S')

    def update_order_data(self, order_id, column, data):
        with self.connection.cursor() as cursor:
            sql_update_column = 'UPDATE orders SET {} = %s WHERE order_id = %s'.format(column)
            cursor.execute(sql_update_column,(data, order_id))

    def remove_order(self, order_id):
        with self.connection.cursor() as cursor:
            sql_delete_order = 'DELETE FROM orders WHERE order_id = %s'
            cursor.execute(sql_delete_order, (order_id, ))
    
    def list_order_by_user_id(self, user_id):
        orders =[]
        with self.connection.cursor() as cursor:
            sql_select_order_by_user_id = 'SELECT * FROM orders WHERE user_id = %s'
            cursor.execute(sql_select_order_by_user_id, (user_id,))
            order_data = cursor.fetchall()
            orders = [Order(*o) for o in order_data]
            return orders

    # def __convert_order_repo_date_to_order(self, order_repo_data:OrderRepoData):
    #     return Order(
    #         order_id= order_repo_data.order_id,
    #         user_id= order_repo_data.user_id,
    #         order_data = OrderData(
    #             order_items= self.get_order_items_by_order_id(order_repo_data.order_id),
    #             shipping_method=order_repo_data.shipping_method,
    #             shipping_address=order_repo_data.shipping_address,
    #             contact_phone=order_repo_data.contact_phone,
    #             email=order_repo_data.email,
    #             payment_method=order_repo_data.payment_method
    #         ),
    #         order_repo=self
    #     )

    def get_next_order_item_id(self):
        with self.connection.cursor() as cursor:
            query = 'SELECT MAX(order_item_id) FROM orderitems'
            cursor.execute(query)
            result = cursor.fetchone()

            if result and result[0] is not None:
                next_id = result[0] + 1
            else:
                next_id = 1

            return next_id

    def get_order_item(self, order_item_id):
        with self.connection.cursor() as cursor:
            sql_select_item = '''SELECT * FROM orderitems WHERE order_item_id = %s'''
            cursor.execute(sql_select_item, (order_item_id, ))
            data = cursor.fetchone()
            return data

    def add_order_item(self, order_item:OrderItem):
        with self.connection.cursor() as cursor:
            sql_insert_item = '''INSERT INTO orderitems (order_item_id, order_id, user_id, product_id, quantity, price) 
                                 VALUES (%s, %s, %s, %s, %s, %s)'''
            cursor.execute(sql_insert_item, (order_item.order_item_id,order_item.order_id,
                                             order_item.user_id, order_item.product_id, 
                                             order_item.quantity, order_item.price))  

    def list_order_items_by_order_id(self, order_id):
        with self.connection.cursor() as cursor:
            sql_select_order_by_user_id = 'SELECT * FROM orderitems WHERE order_id = %s'
            cursor.execute(sql_select_order_by_user_id, (order_id,))
            order_itme_data = cursor.fetchall()
            orders = [OrderItem(*o) for o in order_itme_data]
            return orders

    # def __convert_order_item_repo_data_to_order_item(self, 
    #                                                order_item_repo_data:OrderItemRepoData):
    #     return OrderItem(
    #         order_item_repo_data.order_item_id,
    #         order_item_repo_data.user_id,
    #         order_item_repo_data.order_id,
    #         order_item_repo_data.product_id,
    #         order_item_repo_data.quantity
    #     )

    def update_order_item_data(self, order_item_id, column, data):
        with self.connection.cursor() as cursor:
            sql_update_data = ' UPDATE orderitems SET {} = %s WHERE order_item_id = %s'.format(column)
            cursor.execute(sql_update_data, (data, order_item_id))

    def remove_order_item(self, order_item_id):
        with self.connection.cursor() as cursor:
            sql_delete = 'DELETE FROM orderitems WHERE order_item_id = %s'
            cursor.execute(sql_delete, (order_item_id, ))


