from flask import Blueprint

shop_bp = Blueprint('shop_v1', __name__)

@shop_bp.route('/product/GetLogo')
def GetLogo():
    return 'GetProduct' 