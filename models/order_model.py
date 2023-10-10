from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Order:
    order_id : int
    user_id : str
    order_date :datetime
    order_status : int
    total_amount : int
    shipping_address : str
    contact_phone : str
    shippping_method : int
    payment_method : int

@dataclass(frozen=True)
class OrderItem:
    order_item_id: int 
    user_id : int
    order_id : int
    product_id : int
    quantity : int



