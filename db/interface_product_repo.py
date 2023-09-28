from abc import ABC, abstractmethod

#interface
class IProductRepo():

    @abstractmethod
    def AddProduct(self, table_name, data):
        pass

    @abstractmethod
    def UpdateProduct(self, table_name, data):
        pass

    @abstractmethod
    def ImportProductList(self, path):
        pass

    @abstractmethod
    def GetProduct(self, table_name, data):
        pass

    @abstractmethod
    def GetAllProduct(self, table_name, data):
        pass
