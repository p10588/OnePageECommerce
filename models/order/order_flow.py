from abc import abstractmethod
from models.order.order_model import Order
from enum import Enum

class OrderFlowType(Enum):
    COD = 'COD'
    PREPAID = 'Prepaid'

class OrderFlowFactory:
    @staticmethod
    def create_orderflow(class_name):
        try:
            subclasses = IOrderFlow.__subclasses__()
            for subclass in subclasses:
                if subclass.__name__ == class_name:
                    return subclass             
            raise AttributeError(f"Class {class_name} not found!!")
        except  AttributeError as e:
            print(f"Error creating payment: {e}")
            return None
        
        

class IOrderFlow:
    @abstractmethod
    def process_orderflow(self, order:Order):
        pass

class COD(IOrderFlow):

    def __init__(self, payment, inventory, 
                 logistics):
        self.payment_service = payment
        self.inventory_service = inventory
        self.logistics_service = logistics

    def process_orderflow(self, order:Order):
        # process inventory 
        self.inventory_service.process_inventory(order.order_items, None, None)

class Prepaid(IOrderFlow):

    def __init__(self, payment, inventory, 
                 logistics):
        self.payment_service = payment
        self.inventory_service = inventory
        self.logistics_service = logistics
    
    def process_orderflow(self, order:Order):
        # process payment
        self.payment_service.process_payment(order.payment_method, order.total_amount, None, None)
        # process inventory 
        self.inventory_service.process_inventory(order.order_items, None, None)
