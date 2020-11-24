#12. Implemente el patrón Observer haciendo que los vendedores 
# sean los observables y el gerente el observador de todos los vendedores.
from abc import ABCMeta, abstractmethod

class IObservador(metaclass=ABCMeta):

    @abstractmethod
    def actualizar(self, observado):
        pass


