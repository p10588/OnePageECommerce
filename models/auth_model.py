from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class User:
    user_id : str
    account : str
    full_name : str
    email : str
    shipping_address : str
    contact_phone : str

class AuthFactory:

    @staticmethod
    def create_auth(class_name):
        try:
            subclasses = IAuth.__subclasses__()
            for subclass in subclasses:
                if subclass.__name__ == class_name:
                    return subclass             
            raise AttributeError(f"Class {class_name} not found!!")
        except  AttributeError as e:
            print(f"Error creating auth: {e}")
            return None


class IAuth(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass 
    @abstractmethod
    def signin(self):
        pass
    
class Auth_Google(IAuth):
    def login(self):
        return super().login()
    def logout(self):
        return super().logout()
    def signin(self):
        return super().signin()

class Auth_Line(IAuth):
    def login(self):
        return super().login()
    def logout(self):
        return super().logout()
    def signin(self):
        return super().signin()