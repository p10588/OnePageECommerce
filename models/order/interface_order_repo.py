import abc
from abc import abstractmethod
from typing import List
from datetime import datetime
from dataclasses import dataclass
from models.order.order_model import Order, OrderItem, OrderData

@dataclass(frozen=True)
class OrderRepoData:
    order_id : int
    user_id : str
    order_date : datetime 
    total_amount : int
    order_status : int
    shipping_status : int
    payment_status : int
    payment_date : datetime
    shipping_method: str
    shipping_address : str
    contact_phone : str
    email : str
    payment_method : str

@dataclass(frozen=True)
class OrderItemRepoData:
    order_item_id : int
    user_id : str
    order_id : int
    product_id : str
    quantity : int
    price : int


class IOrderRepo(abc.ABC):
        
    @abstractmethod
    def get_next_order_id(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_order(self, order_id):
        raise NotImplementedError
    
    @abstractmethod
    def add_order(self, order: Order):
        raise NotImplementedError

    @abstractmethod
    def update_order_data(self, order_id, column, data):
        raise NotImplementedError

    @abstractmethod
    def list_order_by_user_id(self, order_id):
        raise NotImplementedError

    @abstractmethod
    def remove_order(self, order_id):
        raise NotImplementedError

    @abstractmethod
    def get_next_order_item_id(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_order_item(self, order_item_id):
        raise NotImplementedError
    
    @abstractmethod
    def add_order_item(self, order_item:OrderItem):
        raise NotImplementedError
    
    @abstractmethod
    def list_order_items_by_order_id(self, order_id):
        raise NotImplementedError

    @abstractmethod
    def update_order_item_data(self, order_item_id, column, data):
        raise NotImplementedError

    @abstractmethod
    def remove_order_item(self,order_item_id):
        raise NotImplementedError
    

class FakeOrderRepo(IOrderRepo):
    
    order_item_repo_data_1 = OrderItemRepoData(
        order_item_id=1,
        user_id='bbb@bbb.com', 
        order_id=0,
        product_id='1',
        quantity=1,
        price = 1000
    )
    order_item_repo_data_2 = OrderItemRepoData(
        order_item_id=2,
        user_id='bbb@bbb.com', 
        order_id=0,
        product_id='2',
        quantity=1,
        price = 2000
    )
    order_item_repo_data_3 = OrderItemRepoData(
        order_item_id=3,
        user_id='bbb@bbb.com', 
        order_id=0,
        product_id='3',
        quantity=1,
        price = 3000
    )

    def get_next_order_id(self):
        pass
    
    def get_order(self, order_id):
        pass
    
    def add_order(self, order: Order):
        pass

    def update_order_data(self, order_id, column, data):
        pass
    
    def get_user_all_orders(self, user_id):
        pass

    def list_order_by_user_id(self, order_id):
        order_items : List[OrderItem]
        order_items = [
            FakeOrderRepo.order_item_repo_data_1,
            FakeOrderRepo.order_item_repo_data_2,
            FakeOrderRepo.order_item_repo_data_3,
        ]
        return order_items
    

    def remove_order(self, order_id):
        pass

    def get_next_order_item_id(self):
        pass
    
    def get_order_item(self, order_item_id):
        pass
    
    def add_order_item(self, order_item:OrderItem):
        pass
    
    def list_order_items_by_order_id(self, order_id):
        pass

    def update_order_item_data(self, order_item_id, column, data):
        pass

    def remove_order_item(self,order_item_id):
        pass


