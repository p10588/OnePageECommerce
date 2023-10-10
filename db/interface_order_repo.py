from abc import abstractmethod
from models.order_model import Order, OrderItem

class IOrderRepo:

    @abstractmethod
    def create_new_order(self, order:Order):
        pass

    @abstractmethod
    def update_order_data(self, order_id, column, data):
        pass
    
    @abstractmethod
    def get_user_all_orders(self, user_id):
        pass

    @abstractmethod
    def remove_order(self, order_id):
        pass

    @abstractmethod
    def create_order_items(self, order_item:OrderItem):
        pass

    @abstractmethod
    def update_order_item_data(self,order_item_id, column, data):
        pass

    @abstractmethod
    def remove_order_item(self,order_item_id):
        pass



