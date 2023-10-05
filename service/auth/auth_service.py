from service.auth.auth import Auth

class AuthFactory:

    @staticmethod
    def get_subclass(base_class):
        subclasses = base_class.__subclasses__()
        return subclasses

    @staticmethod
    def create_auth(class_name):
        try:
            subclasses = AuthFactory.get_subclass(Auth)
            for subclass in subclasses:
                if subclass.__name__ == class_name:
                    return subclass             
            raise AttributeError(f"Class {class_name} not found!!")
        except  AttributeError as e:
            print(f"Error creating auth: {e}")
            return None
        
    

            



