import os
import psycopg2
from models.product_model import Product, Product_Spec, Product_Spec_Detail
from psycopg2 import pool, sql, extensions
from db.interface_product_repo import IProductRepo

class ProductRepo_Postgreaql(IProductRepo):

    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    DB_DATA_POOL = {
        'host': DB_HOST,
        'database': DB_NAME,
        'user': DB_USER,
        'password': DB_PASSWORD,
        'port' : 5432,
        'minconn' : 1,
        'maxconn' : 5,
    }

    def __init__(self):
        self.connection_pool = pool.ThreadedConnectionPool(**self.DB_DATA_POOL)


    def add_product(self, product:Product):
        connection = self.connection_pool.getconn()
        try:
            check = self.__check_product_exist(connection, product.product_id)
            if(check):
                print('Product Data is exist')
            else:
                self.__insert_single_product(connection, product)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)

    def __check_product_exist(self, connection, product_id):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products WHERE product_id = %s', (product_id,))
            if cursor.fetchone() is not None: return True
            else : return False 
        
    def __insert_single_product(self, connection, product:Product):
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s)
            ''', 
                (product.product_id, product.product_name, product.product_description,
                product.price, product.sales_price, product.image_url)
            )
            connection.commit()
    

    def update_product_data(self, product_id, column, data):
        connection = self.connection_pool.getconn()
        try:
            if(self.__check_product_exist(connection, product_id)):
                self.__update_product_column(connection, product_id, column, data)
            else:
                print(f'{product_id} isnt exist')
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)

    def __update_product_column(self, connection, product_id, column, data):
        with connection.cursor() as cursor:
            update_syntax = '''
                UPDATE products
                SET {} = %s
                WHERE product_id = %s
            '''.format(column)
            cursor.execute(update_syntax, (data, product_id))
            connection.commit()

    def get_all_products(self):
        connection = self.connection_pool.getconn()
        try:
            return self.__select_all_data_in_products(connection)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)

    def __select_all_data_in_products(self, connection):
        products = []
        with connection.cursor() as cursor :
            cursor.execute('SELECT * FROM products')
            connection.commit()
            all_product_data = cursor.fetchall()
            for p in all_product_data:
                product = Product(p[0], p[1], p[2], p[3], p[4], p[5])
                products.append(product)
    
        return products

        
    def get_product(self, product_id):
        connection = self.connection_pool.getconn()
        try:
            return self.__select_single_product_by_id(connection, product_id)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)


    def __select_single_product_by_id(self, connection, product_id):
        product = None
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT * FROM products
                WHERE product_id = %s
            ''', (product_id, )
            )
            connection.commit()
            product_data = cursor.fetchall()
            for p in product_data:
                product = Product(p[0], p[1], p[2], p[3], p[4], p[5])
        return product

    def import_product_list(self, path):
        connection = self.connection_pool.getconn()
        try:
            self.__copy_data_to_table(connection, path)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)

    def __copy_data_to_table(self, connection, path):

        with open(path, 'r') as file:
            data = file.readlines()
            for line in data:
                data = line.split(',')
                product_data = Product(
                    product_id=data[0],
                    product_name=data[1],
                    product_description=data[2],
                    price=data[3],
                    sales_price=data[4],
                    image_url=data[5]
                )
                if(self.__check_product_exist(connection, product_data.product_id)):
                    self.__update_product_data(connection, product_data)
                else:
                    self.__insert_single_product(connection, product_data)

    def __update_product_data(self,connection, product:Product): 
        try:
            self.__update_product_column(
                connection, product.product_id, 'product_name', product.product_name )
            self.__update_product_column(
                connection, product.product_id, 'product_description', product.product_description )
            self.__update_product_column(
                connection, product.product_id, 'price', product.price )
            self.__update_product_column(
                connection, product.product_id, 'sales_price', product.sales_price )
            self.__update_product_column(
                connection, product.product_id, 'image_url', product.image_url )
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e) 

    
    def remove_product(self, product_id):
        connection = self.connection_pool.getconn()
        try:
            self.__delete_product(connection, product_id)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)
            

    def __delete_product(self, connection, product_id):
        with connection.cursor() as cursor:
            cursor.execute('''
                DELETE FROM products WHERE product_id = '%s'
            ''', (product_id, )
            )
            connection.commit()
    
     

