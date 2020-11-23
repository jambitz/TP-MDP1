from clase2.estrategiaPorNombre import *
from clase2.estrategiaPorDNI import *
from clase2.estrategiaPorLegajo import *
from clase2.estrategiaPorPromedio import *
from clase2.Alumno import *

class AlumnoPromedio(Alumno):
    def __init__(self):
        nombre = input("ingrese nombre de alumno promedio: ")
        dni = int(input("ingrese dni de alumno promedio: "))
        legajo = int(input("ingrese legajo de alumno promedio: "))
        super().__init__(nombre, dni, legajo, 7)
        self.definir_estrategia()
        
    def definir_estrategia(self):
        while True:
            seleccion = int(input("desea comparar por: \n 1) Legajo\n 2) Promedio\n 3) DNI\n 4) Nombre\n"))
            if seleccion == 1:
                estrategiaDeComparacion = EstrategiaPorLegajo()
                break
            elif seleccion == 2:
                estrategiaDeComparacion = EstrategiaPorPromedio()
                break
            elif seleccion == 3:
                estrategiaDeComparacion = EstrategiaPorDNI()
                break
            elif seleccion == 4:
                estrategiaDeComparacion = EstrategiaPorNombre()
                break
            else:
                print("Ingrese una opcion validad por favor..")
        self.setEstrategia(estrategiaDeComparacion)

