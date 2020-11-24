# 8. Implemente la clase Vendedor
from clase1.Persona import Persona
from clase3.iObservado import IObservado

class Vendedor(Persona, IObservado):

    def __init__(self, nombre, apellido, dni, sueldo_basico):
        super().__init__(nombre, dni)
        self.__sueldo_basico = sueldo_basico
        self.__bonus = 1
        self.__apellido = apellido
        self.__observadores = []

    def venta(self, monto):
        self.__monto_venta = monto
        self.notificar()
    
    def aumenta_bonus(self):
        self.__bonus += 0.1

    def agregar_observador(self, observador):
        self.__observadores.append(observador)
    
    def quitar_observador(self, observador):
        self.__observadores.remove(observador)
    
    def notificar(self):
        for observador in self.__observadores:
            observador.actualizar(self)
    
    def sosIgual(self, comparable):
        #return self.__bonus == comparable
        return self == comparable

    def sosMenor(self, comparable):
        return self.__bonus > comparable.__bonus

    def sosMayor(self, comparable):
        return self.__bonus < comparable.__bonus
    
    def getValor(self):
        return self.__bonus 

    @property
    def apellido(self):
        return self.__apellido

    @property
    def bonus(self):
        return self.__bonus

    @property
    def monto_venta(self):
        return self.__monto_venta