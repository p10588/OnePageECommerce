from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class PaymentType(Enum):
    TEST_PAYMENT = 'TestPayment'
    COD = 'COD'
    LINE_PAY = 'LinePay'
    GOOGLE_PAY = 'GooglePay'

class PaymentStatus(Enum):
    PENDING = 1
    PAID = 2
    FAIL = 3
    REFUNDING = 4
    REFUNDED = 5

@dataclass(frozen=True)
class PaymentInfo():
    total_amount : int

class PaymentFactory:
    @staticmethod
    def create_payment(class_name):
        try:
            subclasses = IPayment.__subclasses__()
            for subclass in subclasses:
                if subclass.__name__ == class_name:
                    return subclass             
            raise AttributeError(f"Class {class_name} not found!!")
        except  AttributeError as e:
            print(f"Error creating payment: {e}")
            return None

class PaymentService:
    def process_payment(self, payment_method, total_amount, callback, fallback):
        payment_class = PaymentFactory.create_payment(payment_method)
        payment = payment_class()
        payment_info = self.__new_payment_info(total_amount)
        result = payment.process_payment(payment_info, callback, fallback)
        return result

    def __new_payment_info(self, total_amount):
        payment_info = PaymentInfo(
            total_amount=total_amount
        )
        return payment_info
    

class IPayment(ABC): 
    @abstractmethod
    def process_payment(self, payment_info, callback, fallback):
        pass

class TestPayment(IPayment):
    def process_payment(self, payment_info:PaymentInfo, callback, fallback):
        
        response = payment_info.total_amount # connection with payment sdk
        
        if response:
            if callback: callback()
            return 'Payment Success' 
        else:
            if fallback: fallback()
            return 'Payment Fail'