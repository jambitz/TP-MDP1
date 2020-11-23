from .iterator import *
from clase2.practica2 import *
from clase2.AlumnoPromedio import *

class IteradorDeConjuntos(Iterator):
    
    def __init__(self, iterable):
        self.__coleccion = list(iterable.coleccion)
        # 12.
        # alumnos = []
        # if isinstance(self.__coleccion[0], Alumno):
        #     for alumno in self.__coleccion:
        #         if alumno.promedio >= 7:
        #             alumnos.append(alumno)
        #     self.__coleccion = alumnos
    
        # 13.
        if isinstance(self.__coleccion[0], Alumno):
            for alumno in self.__coleccion:
                if isinstance(alumno, AlumnoPromedio):
                    alumno_promedio = self.__coleccion.pop(self.__coleccion.index(alumno))
            print(alumno_promedio)
            alumnos_filtrados = []
            for alumno in self.__coleccion:
                if alumno_promedio.sosMenor(alumno) or alumno_promedio.sosIgual(alumno):
                    alumnos_filtrados.append(alumno)
            self.__coleccion = alumnos_filtrados
            
        self.primero()        
        
    def primero(self):
        self.__indexActual = 0

    def siguiente(self):
        self.__indexActual += 1

    def fin(self):
        return self.__indexActual >= len(self.__coleccion)

    def actual(self):
        return self.__coleccion[self.__indexActual]
    