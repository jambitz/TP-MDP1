#5 Implemente  con  el  patrón  Factory  Method  la  capacidad  de  crear  
#  instancias  de  comparables(sólo  las  clases Numeroy Alumno).  
# Implemente  las  fabricas  concretas FabricaDeNumeros y FabricaDeAlumnos

from clase3.fabricaDeComparables import FabricaDeComparables
from clase3.generadorDeDatosAleatorios import GeneradorDeDatosAleatorios
from clase3.lectorDeDatos import LectorDeDatos
from clase2.Alumno import Alumno
class FabricaDeAlumnos(FabricaDeComparables):
    
    def crear_aleatorio(self):
        self.__random = GeneradorDeDatosAleatorios()
        return Alumno(self.__random.string_aleatorio(6),
                      self.__random.numero_aleatorio(99999999), 
                      self.__random.numero_aleatorio(9999), 
                      self.__random.numero_aleatorio(10))

    def crear_por_teclado(self):
        self.__lector_de_datos = LectorDeDatos()
        return Alumno(self.__lector_de_datos.string_por_teclado(), 
                      self.__lector_de_datos.numero_por_teclado(),
                      self.__lector_de_datos.numero_por_teclado(), 
                      self.__lector_de_datos.numero_por_teclado())
        
        