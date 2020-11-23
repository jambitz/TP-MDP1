from .iterator import *

class IteradorDeColecciones(Iterator):
    
    def __init__(self, iterable):
        self.__coleccion = iterable.coleccion
        self.primero()        
        
    def primero(self):
        self.__indexActual = 0

    def siguiente(self):
        self.__indexActual += 1

    def fin(self):
        return self.__indexActual >= len(self.__coleccion)

    def actual(self):
        return self.__coleccion[self.__indexActual]
    