from models.order.cart_model import CartItemData
from abc import abstractmethod,ABC

#interface
class ICartRepo(ABC):

    @abstractmethod
    def set(self, cart_item:CartItemData):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def delete_all_cart_items(self):
        raise NotImplementedError
        