from dataclasses import dataclass
from pydantic import BaseModel
from typing import List

class CartItemData(BaseModel):
    product_id : int
    quantity : int


class Cart:
    def __init__(self):
        self.cart_items:List[CartItemData] = []

    def add_to_cart(self, cart_item:CartItemData):
        cart_item_incart = self.__get_item(cart_item.product_id)
        if cart_item_incart is not None:
            cart_item_incart.quantity += cart_item.quantity
        else: 
            self.cart_items.append(cart_item)

        return cart_item_incart

    def remove_from_cart(self, product_id:int):
        if len(self.cart_items)<=0: return 

        for item in self.cart_items:
            if item.product_id == product_id:
                self.cart_items.remove(item)
                break
            
    
    def update_cart_item_quantity(self, product_id:int, amount:int):
        cart_item = self.__get_item(product_id)
        if cart_item is not None:
            cart_item.quantity += amount

    def clear_cart(self):
        self.cart_items = []
    
    def __get_item(self, product_id):
        for item in self.cart_items:
            if item.product_id == product_id:
                return item
        return None

    def __del__(self):
        self.cart_items = None
        
    
