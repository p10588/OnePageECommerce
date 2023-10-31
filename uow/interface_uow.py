import abc
from abc import abstractmethod


class IUow(abc.ABC):

    @abstractmethod
    def __init__(self, connection_pool):
        # self.savepoint = None
        self.connection_pool = connection_pool
        self.committed:bool = False

    @abstractmethod
    def __enter__(self):
        self.connection = self.connection_pool.getconn()
        self.committed = False
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        if self.committed == False:
            self.rollback()
        self.connection.close()

    @abstractmethod
    def commit(self):
        self.connection.commit()
        self.committed = True
    
    @abstractmethod
    def rollback(self):
        self.connection.rollback()
        # if self.savepoint is not None:
        #     self.__rollback_savepoint()
    
    # @abstractmethod
    # def create_savepoint(self, name):
    #     if self.savepoint is not None:
    #         self.release_savepoint(self.savepoint)

    #     self.connection.cursor().execute(f"SAVEPOINT {name}")
    #     self.savepoint = name

    # @abstractmethod
    # def release_savepoint(self):
    #     if self.savepoint is None: return 
    #     self.connection.cursor().execute(f"RELEASE {self.savepoint}")
    #     self.savepoint = None

    # def __rollback_savepoint(self):
    #     if self.savepoint is None: return 
    #     self.connection.execute(f"ROLLBACK TO {self.savepoint}")
    #     self.savepoint = None


    