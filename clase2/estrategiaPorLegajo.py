from clase2.estrategiaDeComparacion import *
from clase1.practica1 import *

class EstrategiaPorLegajo(EstrategiaDeComparacion):
    def sosMenor(self, comparableA, comparableB):
        return comparableA.legajo < comparableB.legajo
    
    def sosIgual(self, comparableA, comparableB):
        if isinstance(comparableB, Numero):
            return comparableA.legajo == comparableB.getValor()
        return comparableA.legajo == comparableB.legajo

    def sosMayor(self, comparableA, comparableB):
        return comparableA.legajo > comparableB.legajo

    def getValor(self, comparable):
        return comparable.legajo

