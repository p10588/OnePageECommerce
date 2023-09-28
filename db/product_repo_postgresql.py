import os
import psycopg2
from model.product_model import Product, Product_Spec, Product_Spec_Detail
from psycopg2 import pool
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

    def AddProduct(self, product:Product):
        connection = self.connection_pool.getconn()
        try:
            with connection.cursour() as cursor:
                cursor.execute("""
                    INSERT INTO products 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING product_id
                """, product.product_id, product.product_name, product.product_description,
                    product.price, product.sales_price, product.image_url
                )
                connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def UpdateProduct(self, table_name, data):
        return super().UpdateProduct(table_name, data)
    
    def GetAllProduct(self, table_name, data):
        return super().GetAllProduct(table_name, data)

    def GetProduct(self, table_name, data):
        return super().GetProduct(table_name, data)

    def ImportProductList(self, path):
        return super().ImportProductList(path)
     

