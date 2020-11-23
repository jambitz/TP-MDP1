from clase2.estrategiaDeComparacion import *
from clase1.practica1 import *

class EstrategiaPorPromedio(EstrategiaDeComparacion):
    def sosMenor(self, comparableA, comparableB):
        return comparableA.promedio < comparableB.promedio
    
    def sosIgual(self, comparableA, comparableB):
        if isinstance(comparableB, Numero):
            return comparableA.promedio == comparableB.getValor()
        return comparableA.promedio == comparableB.promedio

    def sosMayor(self, comparableA, comparableB):
        return comparableA.promedio > comparableB.promedio

    def getValor(self, comparable):
        return comparable.promedio