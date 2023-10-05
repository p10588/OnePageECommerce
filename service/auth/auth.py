from abc import ABC, abstractmethod

class Auth(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass 
    @abstractmethod
    def signin(self):
        pass
    
class Auth_Google(Auth):
    def login(self):
        return super().login()
    def logout(self):
        return super().logout()
    def signin(self):
        return super().signin()

class Auth_Line(Auth):
    def login(self):
        return super().login()
    def logout(self):
        return super().logout()
    def signin(self):
        return super().signin()