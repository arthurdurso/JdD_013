from abc import ABC, abstractmethod

class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractmethod
    def transform_to_df(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")