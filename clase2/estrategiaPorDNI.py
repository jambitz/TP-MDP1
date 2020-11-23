from clase2.estrategiaDeComparacion import *
from clase1.practica1 import *

class EstrategiaPorDNI(EstrategiaDeComparacion):
    def sosMenor(self, comparableA, comparableB):
        return comparableA.dni < comparableB.dni
    
    def sosIgual(self, comparableA, comparableB):
        if isinstance(comparableB, Numero):
            return comparableA.dni == comparableB.getValor()
        return comparableA.dni == comparableB.dni

    def sosMayor(self, comparableA, comparableB):
        return comparableA.dni > comparableB.dni

    def getValor(self, comparable):
        return comparable.dni