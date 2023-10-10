import os
import datetime
import psycopg2
from db.interface_order_repo import IOrderRepo
from models.order_model import Order, OrderItem
from psycopg2 import pool

class OrderRepo(IOrderRepo):

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
        'maxconn' : 5,
    }

    def __init__(self):
        self.connection_pool = pool.ThreadedConnectionPool(**self.DB_DATA_POOL)


    def create_new_order(self, order:Order):
        connection = self.connection_pool.getconn()
        try:
            if self.__check_order_exist(connection, order.order_id):
                print('Order is exist!!')
            else:
                self.__insert_order(connection, order)
        except Exception as e:
            print('Error: {e}')
            raise Exception(e)
    
    def __check_order_exist(self, connection, order_id):
        with connection.cursor() as cursor:
            sql_select_order = 'SELECT * FROM orders WHERE order_id = %s'
            cursor.execute(sql_select_order, (order_id, ))
            connection.commit()
            order_data = cursor.fetchone()
            if order_data is None: return False
            else: return True

    def __insert_order(self, connection, order:Order):
        with connection.cursor() as cursor:
            sql_insert_order = 'INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s)'
            sql_timestamp = order.order_date.strftime('%Y-%m-%d %H:%M:%S')

            cursor.execute(sql_insert_order,(order.order_id, order.user_id ,sql_timestamp, 
                                             order.total_amount, order.shipping_address, 
                                             order.contact_phone))
            connection.commit()


    def update_order_data(self, order_id, column, data):
        connection = self.connection_pool.getconn()
        try:
            if self.__check_order_exist(connection,order_id):
                self.__update_order_column(connection, order_id, column, data)
            else:
                exception = f'Order {order_id} doesnt exist'
                print(exception)
                raise Exception(exception)
        except Exception as e:
            print('Error: {e}')
            raise Exception(e)
    
    def __update_order_column(self, connection, order_id, column, data):
        with connection.cursor() as cursor:
            sql_update_column = 'UPDATE orders SET {} = %s WHERE order_id = %s'.format(column)
            cursor.execute(sql_update_column,(data, order_id))
            connection.commit()


    def remove_order(self, order_id):
        connection = self. connection_pool.getconn()
        try:
            self.__delete_order(connection, order_id)
        except Exception as e:
            print('Error: {e}')
            raise Exception(e)
    
    def __delete_order(self, connection, order_id):
        with connection.cursor() as cursor:
            sql_delete_order = 'DELETE FROM orders WHERE order_id = %s'
            cursor.execute(sql_delete_order, (order_id, ))
            connection.commit()
  

    def get_user_all_orders(self, user_id):
        connection = self.connection_pool.getconn()
        try:
            return self.__select_order_by_user_id(connection, user_id)
        except Exception as e:
            print('Error: {e}')
            raise Exception(e)

    
    def __select_order_by_user_id(self, connection, user_id):
        orders =[]
        with connection.cursor() as cursor:
            sql_select_order_by_user_id = 'SELECT * FROM orders WHERE user_id = %s'
            cursor.execute(sql_select_order_by_user_id, (user_id,))
            connection.commit()
            order_data = cursor.fetchall()
            for o in order_data:
                data = Order(o[0], o[1], o[2], -1 ,o[3] ,o[4] ,o[5] , -1, -1)
                orders.append(data)

            return orders


    def create_order_items(self, order_item:OrderItem):
        connection = self.connection_pool.getconn()
        try:
            if(self.__check_order_item_exist(connection, order_item.order_item_id)):
                print('Order item is exist')
            else:
                self.__insert_order_item(connection, order_item)
        except Exception as e:
             print('Error: e')
             raise Exception(e)

    def __check_order_item_exist(self, connection, order_item_id):
        with connection.cursor() as cursor:
            sql_select_item = '''SELECT * FROM orderitems WHERE order_item_id = %s'''
            cursor.execute(sql_select_item, (order_item_id, ))
            connection.commit()
            data = cursor.fetchone()
            if data is None: return False
            else: return True


    def __insert_order_item(self,connection, order_item:OrderItem):
        with connection.cursor() as cursor:
            sql_insert_item = '''INSERT INTO orderitems (order_item_id, order_id, user_id, product_id, quantity) 
                                 VALUES (%s, %s, %s, %s, %s)'''
            cursor.execute(sql_insert_item, (order_item.order_item_id,order_item.order_id,
                                             order_item.user_id, order_item.product_id, 
                                             order_item.quantity))
            connection.commit()
    
    def update_order_item_data(self, order_item_id, column, data):
        connection = self.connection_pool.getconn()
        try:
            if self.__check_order_item_exist(connection, order_item_id):
                self.__update_order_item_column_data(connection, order_item_id, column, data)
            else:
                print('Order Item isnt exsit!!!')
        except Exception as e:
            print('Error: {e}')
            raise Exception(e)


    def __update_order_item_column_data(self, connection, order_item_id, column, data):
        with connection.cursor() as cursor:
            sql_update_data = ' UPDATE orderitems SET {} = %s WHERE order_item_id = %s'.format(column)
            cursor.execute(sql_update_data, (data, order_item_id))
            connection.commit()

    def remove_order_item(self, order_item_id):
        connection = self.connection_pool.getconn()
        try:
            self.__delete_order_item(connection, order_item_id)
        except Exception as e: 
            print('Error: {e}')
            raise Exception(e)
    
    def __delete_order_item(self, connection, order_item_id):
        with connection.cursor() as cursor:
            sql_delete = 'DELETE FROM orderitems WHERE order_item_id = %s'
            cursor.execute(sql_delete, (order_item_id, ))
            connection.commit()

    def __del__(self):
        self.connection_pool.closeall()

