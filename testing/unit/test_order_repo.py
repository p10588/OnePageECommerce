import pytest
from models.order.order_model import Order, OrderItem, OrderData, OrderItemData
from db.order_repo_postgres import OrderRepo
from testing.conftest import *

def test_get_next_order_id():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        order_repo = OrderRepo(test_db_connection_pool.getconn())
        order_id = order_repo.get_next_order_id()
        print(order_id)
        assert True
    except Exception as e:
        print(e)
        assert False

@pytest.mark.parametrize('test_data',
                         [(test_testuser1_order_data),
                          (test_testuser1_order_data_1)
                          ])
def test_add_order(test_data):
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order = conftest_order(test_data)
        order_repo.add_order(order)
        connection.commit()
        assert True
    except Exception as e:
        print(e)
        assert False
    
@pytest.mark.parametrize('test_data',
                         [(test_testuser1_order_data),
                          (test_testuser1_order_data_1)
                          ])
def test_update_order_data(test_data):
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order = conftest_order(test_data)
        order_repo.update_order_data(order.order_id,'total_amount', 2000)
        connection.commit()
        assert True
    except Exception as e:
        print(e)
        assert False

@pytest.mark.parametrize('test_data',
                         [(test_testuser1_order_data)])
def test_list_order_by_user_id(test_data):
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order = conftest_order(test_data)
        orders = order_repo.list_order_by_user_id(order.user_id)
        for o in orders:
            print(o)
            assert o.__dict__['user_id'] == order.user_id
    except Exception as e:
        print(e)
        assert False

def test_get_order():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        order_repo = OrderRepo(test_db_connection_pool.getconn())
        order = order_repo.get_order(4)
        assert order.order_id == 4
    except Exception as e:
        print(e)
        assert False

def test_get_next_order_item_id():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        order_repo = OrderRepo(test_db_connection_pool.getconn())
        order_item_id = order_repo.get_next_order_item_id()
        print(order_item_id)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_add_order_item():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order_repo.add_order_item(order_item_1)
        connection.commit()
        assert True
    except Exception as e:
        print(e)
        assert False

def test_list_order_items_by_order_id():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        orderitems = order_repo.list_order_items_by_order_id(-1)
        for o in orderitems:
            print(o)
            assert o.__dict__['order_id'] == -1

    except Exception as e:
        print(e)
        assert False


def test_update_order_item_data():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order_repo.update_order_item_data(-1,'quantity', 3)
        connection.commit()
        assert True
    except Exception as e:
        print(e)
        assert False

def test_remove_order_item():
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order_repo.remove_order_item(-1)
        connection.commit()
        assert True
    except Exception as e:
        print(e)
        assert False

@pytest.mark.parametrize('test_data',
                         [(test_testuser1_order_data),
                          (test_testuser1_order_data_1)
                          ])
def test_remove_order(test_data):
    try:
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        connection = test_db_connection_pool.getconn()
        order_repo = OrderRepo(connection)
        order = conftest_order(test_data)
        order_repo.remove_order(order.order_id)
        connection.commit()
        assert True
    except Exception as e:
        print(e)
        assert False
