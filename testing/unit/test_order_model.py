import pytest
from models.order.order_model import Order, OrderItem, OrderStatusType
from testing.conftest import *

 

@pytest.mark.parametrize('test_data, user_id_result', 
                         [(test_testuser_order_data_3, 'bbb@bbb.com'), 
                          (test_testuser1_order_data, 'test_user_1')])
def test_order_initalize(test_data, user_id_result):
    try:
        order = Order(**test_data)
        assert order.order_id != None
        assert order.user_id == user_id_result
        assert order.contact_phone == '886234567890'
        assert order.email == 'bbb@bbb.com'
        assert order.order_items == []
    except Exception as e:
        print(e)
        assert False   

@pytest.mark.parametrize('test_data, user_id_result', 
                         [(test_testuser_order_data_3, 'bbb@bbb.com'),
                          (test_testuser1_order_data, 'test_user_1')])
def test_set_order_items(test_data, user_id_result):
    try:
        order = Order(**test_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        assert order.order_items[0].user_id == user_id_result
    except Exception as e:
        print(e)
        assert False  
 

@pytest.mark.parametrize('test_price, total_amount_result', 
                         [(test_price, 14000), ([1000,2000], 0)])
def test_calculate_total_amount(test_price, total_amount_result):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.calculate_total_amount()
        assert order.total_amount == total_amount_result
    except Exception as e:
        print(e)
        if len(order.order_items) != len(test_price):
            assert True
        else: assert False


@pytest.mark.parametrize('order_status', 
                         [(OrderStatusType.PROCESSING), (OrderStatusType.CANCELED)])
def test_update_order_status( order_status: OrderStatusType):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_order_status(order_status)
        assert order.order_status == order_status.value
    except Exception as e:
        print(e)
        assert False  

@pytest.mark.parametrize('contact_phone', 
                         [('8860987654')])
def test_update_contact_phone(contact_phone:str):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_contact_phone(contact_phone)
        assert order.contact_phone == contact_phone
    except Exception as e:
        print(e)
        assert False  

@pytest.mark.parametrize('contact_phone', 
                         [('8860987654')])
def test_update_contact_phone_Exception(contact_phone:str):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_order_status(OrderStatusType.SHIPPED)
        order.update_contact_phone(contact_phone)
        assert order.contact_phone == contact_phone
        assert False
    except Exception as e:
        print(e)
        assert True 

@pytest.mark.parametrize('shipping_address', 
                         [('poiuytrew')])
def test_update_shipping_address(shipping_address:str):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_shipping_address(shipping_address)
        assert order.shipping_address == shipping_address
    except Exception as e:
        print(e)
        assert False  
 
@pytest.mark.parametrize('shipping_address', 
                         [('poiuytrew')])
def test_update_shipping_address_Exception(shipping_address:str):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_order_status(OrderStatusType.SHIPPED)
        order.update_shipping_address(shipping_address)
        assert order.shipping_address == shipping_address
        assert False
    except Exception as e:
        print(e)
        assert True 

@pytest.mark.parametrize('shipping_status', 
                         [(5)])
def test_update_shipping_status(shipping_status):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_shipping_status(shipping_status)
        assert order.shipping_status == shipping_status
    except Exception as e:
        print(e)
        assert False  

@pytest.mark.parametrize('payment_status', 
                         [(2)])
def test_update_payment_status(payment_status):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_payment_status(payment_status)
        assert order.payment_status == payment_status
    except Exception as e:
        print(e)
        assert False  

@pytest.mark.parametrize('amount, quantity_result', 
                         [(1,2),(10,11),(-10,1),(1000,999)])
def test_update_order_item_quantity(amount, quantity_result):
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.update_order_item_quantity(order.order_items[0].order_item_id, amount)
        assert order.order_items[0].quantity == quantity_result
    except Exception as e:
        print(e)
        assert False 

def test_remove_order_item():
    try:
        order = Order(**test_testuser1_order_data)
        order_items = conftest_setup_order_items(order, test_order_item_datas)
        order.set_order_items(order_items)
        order.remove_order_item(order.order_items[0].order_item_id)
        assert len(order.order_items) == 2
    except Exception as e:
        print(e)
        assert False 
