from flask import Blueprint, request, jsonify
from db.cart_repo_cookies import CartRepo
from service.order_service import OrderService
import os
from psycopg2 import pool
from uow.uow_order import UowOrder
import json

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
    'maxconn' : 20,
}
connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)

orders_bp = Blueprint('orders_v1', __name__)
order_service = OrderService()

# Process Cart 
@orders_bp.route('/orders/addtocart', methods =['POST'])
def AddToCart():
    try:
        data = request.get_json(force=True)  
        response = order_service.add_to_cart(data)
        return response 
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error' : e}), 400

@orders_bp.route('/orders/removefromcart' , methods =['POST'])
def RemoveFromCart():
    try:
        data = request.get_json(force=True)
        response = order_service.remove_from_cart(data)
        return response
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error' : e}), 400

@orders_bp.route('/orders/deletecart', methods =['POST'])
def DeleteCart():
    try:
        response = order_service.delete_cart()
        return response
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error' : e}), 400

@orders_bp.route('/orders/getcart', methods =['GET'])
def GetCart():
    try:
        data = order_service.get_cart()
        return data
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error' : e}), 400

# Process Order
@orders_bp.route('/orders/getuserorders', methods =['GET'])
def GetUserOrders():
    try:
        data = 'aaa@aaa.com'
        uow = UowOrder(connection_pool)
        respone = order_service.get_user_orders(data, uow)
        return jsonify(json.loads(respone))
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error' : e}), 400

@orders_bp.route('/orders/placeorder', methods =['POST'])
def PlaceOrder():
    try:
        data = request.get_json(force=True) #force request data is json
        uow = UowOrder(connection_pool)
        respone = order_service.place_order(data, uow)
        return jsonify(json.loads(respone))
    except Exception as e:
        print(f'Error: {e}')
        error_message = f'{e}'
        return jsonify({'error' : error_message}), 400
    

@orders_bp.route('/orders/AdvanceLogisticsStatus', methods =['POST'])
def AdvanceLogisticsStatus():
    return 'AdvanceLogisticsStatus'

@orders_bp.route('/orders/AdvancePaymentStatus', methods =['POST'])
def UpdatePaymentStatus():
    return 'AdvancePaymentStatus'

@orders_bp.route('/orders/PreparedOrderItems', methods =['POST'])
def ReadyForShipment():
    return 'AdvancePaymentStatus'