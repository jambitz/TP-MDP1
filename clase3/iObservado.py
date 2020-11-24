#12. Implemente el patrón Observer haciendo que los vendedores 
# sean los observables y el gerente el observador de todos los vendedores.
from abc import ABCMeta, abstractmethod

class IObservado(metaclass=ABCMeta):

    @abstractmethod
    def agregar_observador(self, observador):
        pass
    
    @abstractmethod
    def quitar_observador(self, observador):
        pass

    @abstractmethod    
    def notificar(self):
        pass
    
