#11. Implemente la clase Gerente. Un Gerentetiene una colección con sus vendedores.

from clase1.practica1 import Pila
from clase3.iObservador import IObservador

class Gerente(IObservador):
    def __init__(self):
        self.__mejores = Pila()

    def cerrar(self):
        for mejor in self.__mejores.coleccion:
            print(f"Nombre: {mejor.nombre} Apellido: {mejor.apellido} -- Bonus Acumulado: {mejor.bonus}" ) 

    def venta(self, monto, vendedor):
        if monto > 5000:
            if not self.__mejores.contiene(vendedor):
                self.__mejores.agregar(vendedor)
            vendedor.aumenta_bonus()
        
    def actualizar(self, observado):
        self.venta(observado.monto_venta, observado)