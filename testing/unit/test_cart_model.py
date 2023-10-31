from models.order.cart_model import Cart
from testing.conftest import *

def test_add_to_cart():
    try:
        cart = Cart()
        cart.add_to_cart(test_cart_item_data1)
        assert len(cart.cart_items) == 1
        cart.add_to_cart(test_cart_item_data1)
        assert cart.cart_items[0].quantity == 2
        cart = None
    except Exception as e:
        print(e)
        assert False

def test_remove_from_cart():
    try:
        cart = Cart()
        cart.add_to_cart(test_cart_item_data1)
        assert len(cart.cart_items) == 1
        cart.remove_from_cart(test_cart_item_data1.product_id)
        assert len(cart.cart_items) == 0
    except Exception as e:
        print(e)
        assert False

def test_update_cart_item_quantity():
    try:
        cart = Cart()
        cart.add_to_cart(test_cart_item_data1)
        assert len(cart.cart_items) == 1
        cur_amount = cart.cart_items[0].quantity
        cart.update_cart_item_quantity(test_cart_item_data1.product_id, 10)
        assert cart.cart_items[0].quantity == (cur_amount+10)
    except Exception as e:
        print(e)
        assert False
