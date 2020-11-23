from clase2.estrategiaDeComparacion import *
from clase1.practica1 import * 

class EstrategiaPorNombre(EstrategiaDeComparacion):
    def sosMenor(self, comparableA, comparableB):
        return comparableA.nombre < comparableB.nombre
    
    def sosIgual(self, comparableA, comparableB):
        if isinstance(comparableB, Numero):
            return "no se puede comparar un nombre con un numero"
        return comparableA.nombre == comparableB.nombre

    def sosMayor(self, comparableA, comparableB):
        return comparableA.nombre > comparableB.nombre

    def getValor(self, comparable):
        return comparable.nombre
