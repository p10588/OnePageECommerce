from flask import Blueprint

orders_bp = Blueprint('orders_v1', __name__)

@orders_bp.route('/orders/GetUserOrders')
def GetUserOrders():
    return 'GetUserOrders' 

@orders_bp.route('/orders/GetUserOrders')
def AddToCart():
    return 'AddToCart' 

@orders_bp.route('/orders/GetUserOrders')
def OrderPlacement():
    return 'OrderPlacement' 