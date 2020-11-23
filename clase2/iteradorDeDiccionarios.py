from .iterator import *

class IteradorDeDiccionarios(Iterator):
    
    def __init__(self, iterable):
        self.__coleccion = list(iterable.coleccion)
        self.primero()        
        
    def primero(self):
        self.__indexActual = 0

    def siguiente(self):
        self.__indexActual += 1

    def fin(self):
        return self.__indexActual >= len(self.__coleccion)

    def actual(self):
        return self.__coleccion[self.__indexActual].valor
    