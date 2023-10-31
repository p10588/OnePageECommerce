from models.order.interface_cart_repo import ICartRepo
from models.order.cart_model import CartItemData
from service.cookie_service import CookieService
from typing import List
import json

class CartRepo(ICartRepo):
    
    def __init__(self):
        self.cookie_service = CookieService()

    def set(self, cart_items:List[CartItemData]):
        cart_json = json.dumps(cart_items)
        # get cart from cookie
        self.cookie_service.set_cookie('cart', cart_json, 3600)

    def get(self):
        data = self.cookie_service.get_cookie('cart')
        if data is None or len(data)<=0:
            return 'Cart is empty'
        return data
    
    def delete_all_cart_items(self):
        self.cookie_service.RemoveCookie('cart')