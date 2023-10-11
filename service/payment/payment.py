from abc import abstractmethod

class PaymentFactory:
    @staticmethod
    def get_subclass(base_class):
        subclasses = base_class.__subclasses__()
        return subclasses

    @staticmethod
    def create_payment(class_name):
        try:
            subclasses = PaymentFactory.get_subclass(IPayment)
            for subclass in subclasses:
                if subclass.__name__ == class_name:
                    return subclass             
            raise AttributeError(f"Class {class_name} not found!!")
        except  AttributeError as e:
            print(f"Error creating payment: {e}")
            return None

class IPayment: 
    @abstractmethod
    def process_payment(self, payment_info):
        pass

class TestPayment(IPayment):
    def process_payment(self, payment_info):
        if payment_info:
            return 'Payment Success' 
        else:
            return 'Payment Fail'