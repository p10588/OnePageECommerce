import os
from db.interface_user_repo import IUserRepo
from models.user_model import User
from psycopg2 import pool

class UserRepo_postgres(IUserRepo):
    
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
        self.connect_pool = pool.ThreadedConnectionPool(**self.DB_DATA_POOL)


    def add_new_user(self, user:User):
        connection = self.connect_pool.getconn()
        try:
            if self.__check_user_exist(connection, user.user_id):
                print('User is exist')
            else:
                self.__insert_user_data(connection, user)
        except Exception as e:
            print(f'Error: {e}')
            raise Exception(e)
    
    def __check_user_exist(self, connection, user_id):
        with connection.cursor() as cursor:
            sql_select = 'SELECT * FROM users WHERE user_id = %s'
            cursor.execute(sql_select, (user_id, ))
            connection.commit()
            users = cursor.fetchone()
            if users is None:
                return False
            else :
                return True

    def __insert_user_data(self, connection, user:User):
        with connection.cursor() as cursor:
            sql_insert = 'INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql_insert, 
                           (user.user_id, user.account, user.full_name,
                           user.email, user.shipping_address, user.contact_phone))
            connection.commit()

    def get_user(self, user_id):
        connection = self.connect_pool.getconn()
        try:
            return self.__get_single_user_by_id(connection, user_id)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)

    def __get_single_user_by_id(self, connection, user_id ):
        with connection.cursor() as cursor:
            sql_select_user = 'SELECT * FROM users WHERE user_id = %s'
            cursor.execute(sql_select_user, user_id)
            connection.commit()
            user_data = cursor.fetchone()
            user = User(user_data[0], user_data[1], user_data[2],
                        user_data[3], user_data[4], user_data[5])
            return user

    def update_user_data(self, user_id, column, data):
        connection = self.connect_pool.getconn()
        try:
            if self.__check_user_exist(connection, user_id) :
                self.__update_user_colume(connection, user_id, column, data)
            else:
                raise Exception('User doesnt exsit!!!')
        except Exception as e:
            print(f'Error: "{e}')
            raise Exception(e)

    def __update_user_colume(self,connection,user_id, column, data):
        with connection.cursor() as cursor:
            sql_update = 'UPDATE users SET {} = %s WHERE user_id = %s'.format(column)
            cursor.execute(sql_update, (data, user_id,))
            connection.commit()
    
    def remove_user(self, user_id):
        connection = self.connect_pool.getconn()
        try:
            self.__delete_product(connection, user_id)
        except Exception as e:
            print(f'An error occurred: {e}')
            raise Exception(e)
            

    def __delete_product(self, connection, user_id):
        with connection.cursor() as cursor:
            cursor.execute('''
                DELETE FROM users WHERE user_id = %s
            ''', (user_id, )
            )
            connection.commit()