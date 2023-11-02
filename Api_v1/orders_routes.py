from flask import Blueprint, request, jsonify
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
    

@orders_bp.route('/orders/updateshippingstatus', methods =['POST'])
def UpdateLogisticsStatus():
    try:
        data = request.get_json(force=True) #force request data is json
        uow = UowOrder(connection_pool)
        respone = order_service.update_shipping_stauts(data, uow)
        return jsonify(json.loads(respone))
    except Exception as e:
        print(f'Error: {e}')
        error_message = f'{e}'
        return jsonify({'error' : error_message}), 400

@orders_bp.route('/orders/updatepaymentstatus', methods =['POST'])
def UpdatePaymentStatus():
    try:
        data = request.get_json(force=True) #force request data is json
        uow = UowOrder(connection_pool)
        respone = order_service.update_payment_status(data, uow)
        return jsonify(json.loads(respone))
    except Exception as e:
        print(f'Error: {e}')
        error_message = f'{e}'
        return jsonify({'error' : error_message}), 400

@orders_bp.route('/orders/updateorderstatus', methods =['POST'])
def UpdateOrderStatus():
    try:
        data = request.get_json(force=True) #force request data is json
        uow = UowOrder(connection_pool)
        respone = order_service.update_order_status(data, uow)
        return jsonify(json.loads(respone))
    except Exception as e:
        print(f'Error: {e}')
        error_message = f'{e}'
        return jsonify({'error' : error_message}), 400