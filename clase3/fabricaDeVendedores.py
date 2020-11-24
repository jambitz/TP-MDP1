# 9. Implemente una   fábrica   concreta   para   la   clase Vendedory   compruebe   el   correcto 
# funcionamiento  del  método maindel  ejercicio  6.Compare  a  los  vendedores  por  el  campo bonus

from clase3.fabricaDeComparables import FabricaDeComparables
from clase3.generadorDeDatosAleatorios import GeneradorDeDatosAleatorios
from clase3.lectorDeDatos import LectorDeDatos
from clase1.numero import Numero
from clase3.vendedor import Vendedor

class FabricaDeVendedores(FabricaDeComparables):
    
    def crear_aleatorio(self):
        self.__random = GeneradorDeDatosAleatorios()
        return Vendedor(self.__random.string_aleatorio(6),
                        self.__random.string_aleatorio(6),
                        self.__random.numero_aleatorio(99999999),
                        self.__random.numero_aleatorio(99999))

    def crear_por_teclado(self):
        self.__lector_de_datos = LectorDeDatos()
        return Vendedor(self.__lector_de_datos.string_por_teclado(),
                        self.__lector_de_datos.string_por_teclado(), 
                        self.__lector_de_datos.numero_por_teclado(),
                        self.__lector_de_datos.numero_por_teclado())