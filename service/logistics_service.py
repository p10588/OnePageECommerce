from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class LogisticsType(Enum):
    TEST_LOGISTICS = 'TestLogistics'
    HOME_DELIVERY = 'HomeDelivery'
    STORE_PICKUP = 'StorePickup'

class LogisticsStatus(Enum):
    PENDING = 1
    IN_TRANSIT = 2
    DELIVERED = 3
    PICKED_UP = 4
    RETURNING = 5
    RETURNED = 6
    CANCELLED = 7


@dataclass(frozen=True)
class Logistics:
    logistics_type : LogisticsType
    shipping_address : str

class LogisticsFactory:

    @staticmethod
    def create_Logistics(class_name):
        try:
            subclasses = ILogistics.__subclasses__()
            for subclass in subclasses:
                if subclass.__name__ == class_name:
                    return subclass             
            raise AttributeError(f"Class {class_name} not found!!")
        except  AttributeError as e:
            print(f"Error creating payment: {e}")
            return None

class LogisticsService:

    def process_logistics(self, shipping_method:LogisticsType, shipping_address): 
        logistics_data = self.__new_logistics(shipping_method, shipping_address)

        logistics_class = LogisticsFactory.create_Logistics(shipping_method.value)
        logistics = logistics_class()
        logistics.process_logistics(logistics_data, None, None)

    def __new_logistics(self, shipping_method:LogisticsType, shipping_address):
        logistics = Logistics(
            logistics_type = shipping_method,
            shipping_address = shipping_address
        )
        return logistics

class ILogistics(ABC): 
    @abstractmethod
    def process_logistics(self, logistics_info, callback, fallback):
        pass

    @abstractmethod
    def logistics_complete(selfr):
        pass

class TestLogistics(ILogistics):
    def process_logistics(self, logistics_info:Logistics, callback, fallback):

        response = logistics_info  # connection with logistics sdk

        if response:
            return 'Start Logistics' 
        else:
            return 'Logistics Fail'
    
    def logistics_complete(self):
        print('logistics complete')