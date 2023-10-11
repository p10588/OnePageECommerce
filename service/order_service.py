from db.order_repo_postgres import OrderRepo
from service.cookie_service import CookieService

class OrderService:

    def __init__(self):
        #connect ro order repo
        self.order_repo = OrderRepo() 
        self.cookie_service = CookieService()
    
    def get_cart(self):
        # get order item from cookie
        data = self.cookie_service.GetCookie('cart')
        if data is None or len(data)<=0:
            return 'Cart is empty'
        return data

    def add_to_cart(self, product_id):
        # get cart from cookie
        cart = self.cookie_service.GetCookie('cart')

        # null check
        if cart is None:
            cart = []

        # add order item and set to cookie
        cart.append(product_id)   
        response = self.cookie_service.SetCookie('cart', cart, 3600)
        return response

    def remove_from_cart(self, product_id):
        # get cart from cookie
        cart = self.cookie_service.GetCookie('cart')

        # null check and print message
        if cart is None:
            return 'Product not found in cart', 404
        
        # check product is exist then remove, and set back to cookie
        if product_id in cart:
            cart.remove(product_id)
            response = self.cookie_service.SetCookie('cart', cart, 3600)
            return response
        
        return 'Product not found in cart', 404

    def delete_cart(self):
        response = self.cookie_service.RemoveCookie('cart')
        return response

    def order_placement(self, user_id, order_items, shipping_data, payment_type):
        # check user is login
        # true: create new user order 
        #       check order id == 0 and update order item order id
        # false: 
        pass

    def get_user_orders():
        # get user orders by user id
        pass
        
    def __check_user_is_logn():
        pass
