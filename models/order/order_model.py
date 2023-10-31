from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel
from typing import List
from enum import Enum

class OrderStatusType(Enum):
    PENDING = 1 
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELED = 5

@dataclass(frozen=True)
class OrderItemData(BaseModel):
    product_id : int 
    quantity : int
    price : int
    # sample json
    # {
    #     "product_id" : "123123"
    #     "quantity" : 1
    #     "price":1000
    # }

@dataclass(frozen=True)
class OrderData(BaseModel):
    order_items : List[OrderItemData]
    shipping_method: str
    shipping_address : str
    contact_phone : str
    email : str
    payment_method : str
    # sample json
    # {
    #     "order_items" : [
    #         {
    #             "product_id" : "4532",
    #             "quantity" : 2
    #         },
    #     ],
    #     "shipping_method" : "TestLogistics",
    #     "shipping_address" : "wertyuio",
    #     "contact_phone" : "8863456789",
    #     "email" : "aaa@aaa.com",
    #     "payment_method" : "TestPayment"
    # }

class OrderItem:
    def __init__(self, order_item_id:int, order_id:int, product_id:int,
                  quantity:int, user_id:str, price:int ):
        self.order_item_id = order_item_id
        self.user_id = user_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def update_order_item_quantity(self, amount:int):
        if self.order_item_id is not None:
            raise Exception('Order Item has been created')  
          
        self.quantity += amount
        



class Order:

    def __init__(self, order_id: int, user_id: str, order_date : datetime, 
                 total_amount : int, shipping_address: str, contact_phone: str, 
                 shipping_status : int, shipping_method: str,  payment_status : int, 
                 payment_method : str, payment_date : datetime, order_status : int,
                 email: str):
        self.order_id = order_id
        self.shipping_method = shipping_method
        self.shipping_address = shipping_address
        self.contact_phone = contact_phone
        self.email = email
        self.payment_method = payment_method
        self.order_date = order_date
        self.total_amount = total_amount
        self.order_status = order_status
        self.shipping_status = shipping_status
        self.payment_status = payment_status
        self.payment_date = payment_date
        
        self.user_id = self.__get_user_id(user_id)

        self.order_items:List[OrderItem] = []
        

    def set_order_items(self, order_items:List[OrderItem]):
        self.order_items = order_items

    def __get_user_id(self, user_id):
        if user_id is None:
            return self.email
        else: 
            return user_id 

    def calculate_total_amount(self):
        total_amount = 0

        for i in range(len(self.order_items)):
            total_amount += (self.order_items[i].quantity * self.order_items[i].price)

        self.total_amount = total_amount

    def update_order_status(self, order_status:OrderStatusType):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')
           
        self.order_status = order_status.value

    def update_contact_phone(self, contact_phone:str):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')
        
        if self.order_status >= OrderStatusType.SHIPPED.value:
            raise Exception('Order is shipped')
        
        self.contact_phone = contact_phone
    
    def update_shipping_address(self, shipping_address:str):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')
        
        if self.order_status >= OrderStatusType.SHIPPED.value:
            raise Exception('Order is shipped')
        
        self.shipping_address = shipping_address

    def update_shipping_status(self, shipping_status):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')

        self.shipping_status = shipping_status

    def update_payment_status(self, payment_status):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')

        self.payment_status = payment_status


    def update_order_item_quantity(self, order_item_id, amount:int):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')
        
        updated_item = None

        for item in self.order_items:
            if item.order_item_id == order_item_id:
                item.quantity += amount
                item.quantity = max(min(item.quantity, 999), 1)
                updated_item = item
                break

        if updated_item is None:
             raise Exception('Item doesnt exsit!!')

    def remove_order_item(self, order_item_id):
        if self.order_id is None:
            raise Exception('Order hasnt been creat yet !')
        
        self.order_items = [item for item in self.order_items if item.order_item_id != order_item_id]
        


    




