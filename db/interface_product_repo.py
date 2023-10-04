from models.product_model import Product
from abc import abstractmethod

#interface
class IProductRepo():

    @abstractmethod
    def add_product(self, product:Product):
        pass

    @abstractmethod
    def update_product_data(self, data):
        pass

    @abstractmethod
    def import_product_list(self, path):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass
