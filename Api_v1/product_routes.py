from flask import Blueprint

product_bp = Blueprint('product_v1', __name__)

@product_bp.route('/product/getproducts')
def GetProduct():
    return 'GetProduct' 