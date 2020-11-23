# 6. Haga que las clases Pila, Cola, Conjunto y Diccionario
#    implementen la interface Iterablevista en teoría

from abc import ABCMeta, abstractmethod

class Iterator(metaclass=ABCMeta):
    
    @abstractmethod
    def primero(self):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def fin(self):
        pass

    @abstractmethod
    def actual(self):
        pass

