from datetime import datetime
from models.order_model import Order, OrderItem
from db.order_repo_postgres import OrderRepo

def test_create_new_order():
    order = Order(
        order_id=0,
        user_id='0',
        order_date=datetime.now(),
        order_status=-1,
        total_amount=1000,
        shipping_address='qwertyuiop',
        contact_phone='886123456789',
        shippping_method=-1,
        payment_method=-1
    )
    try:
        order_repo = OrderRepo()
        order_repo.create_new_order(order)
        assert True
    except Exception as e:
        print(e)
        assert False


def test_update_order_data():
    try:
        order_repo = OrderRepo()
        order_repo.update_order_data(0,'total_amount', 2000)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_remove_order():
    try:
        order_repo = OrderRepo()
        order_repo.remove_order(0)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_get_user_all_orders():
    try:
        order_repo = OrderRepo()
        orders = order_repo.get_user_all_orders('0')
        for o in orders:
            print(o)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_create_order_item():
    order_item = OrderItem(
        order_item_id=0,
        order_id=0,
        user_id=0,
        product_id=0,
        quantity=1,
    )
    try:
        order_repo = OrderRepo()
        order_repo.create_order_items(order_item)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_update_order_item_data():
    try:
        order_repo = OrderRepo()
        order_repo.update_order_item_data(0,'quantity', 3)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_remove_order_item_data():
    try:
        order_repo = OrderRepo()
        order_repo.remove_order_item(0)
        assert True
    except Exception as e:
        print(e)
        assert False