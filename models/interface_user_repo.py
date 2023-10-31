from models.auth_model import User
from abc import abstractmethod

class IUserRepo:
    
    @abstractmethod
    def add_new_user(self, user:User):
        pass
    
    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def update_user_data(self, user_id, column, data):
        pass