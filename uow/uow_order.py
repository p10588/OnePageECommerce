from uow.interface_uow import IUow
from db.order_repo_postgres import OrderRepo
from models.order.order_model import Order

class UowOrder(IUow):

    def __init__(self, connection_pool):
        super().__init__(connection_pool)
    
    def __enter__(self):
        super().__enter__()
        self.order_repo = OrderRepo(self.connection)
     
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

    def commit(self):
        super().commit()

    def rollback(self):
        super().rollback()

    # def create_savepoint(self, name):
    #     super().create_savepoint(name)
    
    # def release_savepoint(self):
    #     super().release_savepoint()
    
    

    
    
    