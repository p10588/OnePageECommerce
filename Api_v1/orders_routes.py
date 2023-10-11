from flask import Blueprint
from service.cookie_service import CookieService
from service.order_service import OrderService
orders_bp = Blueprint('orders_v1', __name__)
cookie_service = CookieService()
order_service = OrderService()

@orders_bp.route('/orders/GetUserOrders')
def GetUserOrders():
    return 'GetUserOrders' 

@orders_bp.route('/orders/addtocart/<product_id>')
def AddToCart(product_id):
    response = order_service.add_to_cart(product_id)
    return response 

@orders_bp.route('/orders/removefromcart/<product_id>')
def RemoveFromCart(product_id):
    response = order_service.remove_from_cart(product_id)
    return response

@orders_bp.route('/orders/deletecart')
def DeleteCart():
    response = order_service.delete_cart()
    return response

@orders_bp.route('/orders/getcart')
def GetCart():
    data = order_service.get_cart()
    return data


@orders_bp.route('/orders/GetUserOrders')
def OrderPlacement():
    return 'OrderPlacement' 