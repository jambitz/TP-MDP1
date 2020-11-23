from abc import ABCMeta, abstractmethod

class Iterable(metaclass=ABCMeta):
    
    @abstractmethod
    def crearIterador(self):
        pass

