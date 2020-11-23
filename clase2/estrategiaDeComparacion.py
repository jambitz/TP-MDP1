# 1.Implemente cuatro estrategias de comparación para la clase Alumno definida en la práctica
# anterior. Realice una estrategia para que compare alumnos por nombre, otra para que
# compare por DNI, otra para que compare por promedio y una última estrategia que compare
# por legajo

from abc import ABCMeta, abstractmethod

class EstrategiaDeComparacion(metaclass=ABCMeta):
    @abstractmethod
    def sosMenor(self, comparableA, comparableB):
       pass

    @abstractmethod
    def sosMayor(self,  comparableA, comparableB):
       pass

    @abstractmethod
    def sosIgual(self, comparableA, comparableB):
        pass