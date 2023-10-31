from models.order.cart_model import Cart, CartItemData
from service.cookie_service import CookieService
class CartService:

    def __init__(self):
        self.cart = Cart()
        self.cookie_service = CookieService()

    def get_cart(self):
        # get order item from cookie
        data = self.cookie_service.get_cookie('cart')

        if data is None or len(data)<=0:
            return 'Cart is empty'
        
        return data

    def add_to_cart(self, data):
        # verify data
        cart_item = CartItemData(**data)

        self.cart.add_to_cart(cart_item)

        cart_items_json = [item.__dict__ for item in self.cart.cart_items]

        response = self.cookie_service.set_cookie('cart', cart_items_json, 3600)
        return response

    def remove_from_cart(self, data):
        if not isinstance(data['product_id'], int):
            raise Exception('Data is invalid')
        
        product_id = data['product_id']
        self.cart.remove_from_cart(product_id)
        cart_items_json = [item.__dict__ for item in self.cart.cart_items]
        response = self.cookie_service.set_cookie('cart', cart_items_json, 3600)
        return response

    def delete_cart(self):
        response = self.cookie_service.delete_cookie('cart')
        self.cart.clear_cart()
        return response
 
    
# Process Cart 
# @orders_bp.route('/orders/addtocart', methods =['POST'])
# def AddToCart():
#     try:
#         data = request.get_json(force=True)  
#         response = order_service.add_to_cart(data)
#         return response 
#     except Exception as e:
#         print(f'Error: {e}')
#         return jsonify({'error' : e}), 400

# @orders_bp.route('/orders/removefromcart' , methods =['POST'])
# def RemoveFromCart():
#     try:
#         data = request.get_json(force=True)
#         response = order_service.remove_from_cart(data)
#         return response
#     except Exception as e:
#         print(f'Error: {e}')
#         return jsonify({'error' : e}), 400

# @orders_bp.route('/orders/deletecart', methods =['POST'])
# def DeleteCart():
#     try:
#         response = order_service.delete_cart()
#         return response
#     except Exception as e:
#         print(f'Error: {e}')
#         return jsonify({'error' : e}), 400

# @orders_bp.route('/orders/getcart', methods =['GET'])
# def GetCart():
#     try:
#         data = order_service.get_cart()
#         return data
#     except Exception as e:
#         print(f'Error: {e}')
#         return jsonify({'error' : e}), 400


