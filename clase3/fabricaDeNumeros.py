#5 Implemente  con  el  patrón  Factory  Method  la  capacidad  de  crear  
#  instancias  de  comparables(sólo  las  clases Numeroy Alumno).  
# Implemente  las  fabricas  concretas FabricaDeNumeros y FabricaDeAlumnos

from clase3.fabricaDeComparables import FabricaDeComparables
from clase3.generadorDeDatosAleatorios import GeneradorDeDatosAleatorios
from clase1.practica1 import Numero
from clase3.lectorDeDatos import LectorDeDatos
class FabricaDeNumeros(FabricaDeComparables):
    
    def crear_aleatorio(self):
        self.__num_random = GeneradorDeDatosAleatorios().numero_aleatorio(9999)
        return Numero(self.__num_random)

    def crear_por_teclado(self):
        self.__num_teclado = LectorDeDatos().numero_por_teclado()
        return Numero(self.__num_teclado)
        
