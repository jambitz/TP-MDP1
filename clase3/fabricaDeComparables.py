#4. Implemente la interface FabricaDeComparables

from abc import ABCMeta, abstractmethod

class FabricaDeComparables(metaclass=ABCMeta):

    @abstractmethod
    def crear_aleatorio(self):
        pass
    
    @abstractmethod
    def crear_por_teclado(self):
        pass

    @staticmethod
    def crear_aleatorio(opcion):
        if opcion == "Numero":
            fabrica = FabricaDeNumeros()
        elif opcion == "Alumno":
            fabrica = FabricaDeAlumnos()
        elif opcion == "Vendedor":
            fabrica = FabricaDeVendedores()
            
        return fabrica.crear_aleatorio()


    @staticmethod
    def crear_por_teclado(opcion):
        if opcion == "Numero":
            fabrica = FabricaDeNumeros()
        elif opcion == "Alumno":
            fabrica = FabricaDeAlumnos()
        elif opcion == "Vendedor":
            fabrica = FabricaDeVendedores()

        return fabrica.crear_por_teclado()    
    
from clase3.fabricaDeNumeros import FabricaDeNumeros
from clase3.fabricaDeAlumnos import FabricaDeAlumnos
from clase3.fabricaDeVendedores import FabricaDeVendedores