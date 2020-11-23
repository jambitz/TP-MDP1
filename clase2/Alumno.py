from clase2.estrategiaPorLegajo import *
from clase1.Persona import *

class Alumno(Persona):
    def __init__(self, n, d, l, p):
        super().__init__(n, d)
        self.__legajo = l
        self.__promedio = p
        self.__estrategia = EstrategiaPorLegajo()

    def setEstrategia(self, estrategiaDeComparacion):
        self.__estrategia = estrategiaDeComparacion
                  
    @property
    def estrategia(self):
        return self.__estrategia

    def getLegajo(self):
        return self.__legajo

    def getPromedio(self):
        return self.__promedio
    
    def sosIgual(self, comparable):
        return self.__estrategia.sosIgual(self, comparable)

    def sosMenor(self, comparable):
        return self.__estrategia.sosMenor(self, comparable)

    def sosMayor(self, comparable):
        return self.__estrategia.sosMayor(self, comparable)
    
    def getValor(self):
        return self.__estrategia.getValor(self)
    
    @property
    def promedio(self):
        return self.__promedio
    
    @promedio.setter
    def promedio(self, legajo):
        self.__promedio = promedio

    @property
    def legajo(self):
        return self.__legajo

    @legajo.setter
    def legajo(self, legajo):
        self.__legajo = legajo