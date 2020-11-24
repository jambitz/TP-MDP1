from clase1.practica1 import *
from clase2.iterable import *
from clase2.iteradorDeConjuntos import *
from clase2.iteradorDeDiccionarios import *
from clase2 import estrategiaDeComparacion
from clase2.estrategiaPorLegajo import EstrategiaPorLegajo
from clase2.estrategiaPorPromedio import EstrategiaPorPromedio
from clase2.estrategiaPorNombre import EstrategiaPorNombre
from clase2.estrategiaPorDNI import EstrategiaPorDNI

#2 Modifique el ejercicio 16 de la clase anterior para crear alumnos con alguna estrategia
#implementada en el ejercicio anterior.

def llenarAlumnos(coleccionable):
    if isinstance(coleccionable, Pila):
        global estrategiaDeComparacion
        while True:
            seleccion = int(input("desea comparar por: \n 1) Legajo\n 2) Promedio\n"))
            if seleccion == 1:
                estrategiaDeComparacion = EstrategiaPorLegajo()
                break
            elif seleccion == 2:
                estrategiaDeComparacion = EstrategiaPorPromedio()
                break
            else:
                print("Ingrese una opcion validad por favor..")

    nombres = ["Pedro", "Ana", "Jose", "Marcos", "Pablo", "Ramiro", "Mirna", "Mirta", "Susana", "Felipe", "Camila", "Agustin", "Agostina"]
    for x in range(20):
        comparable = Alumno(nombres[random.randint(0, len(nombres)-1)], random.randint(10000000, 45000000), random.randint(0,99999), random.randint(1,10))
        comparable.setEstrategia(estrategiaDeComparacion)
        if isinstance(coleccionable, Diccionario):
            coleccionable.agregar(comparable.getLegajo(),comparable)
        else:
            coleccionable.agregar(comparable)

# Use el método main del ejercicio 17 de la clase anterior para comprobar el funcionamiento
# correcto de la estrategia seleccionada. Note que este método main NO debería ser modificado

# def main():
#     pila = Pila()
#     cola = Cola()
#     multiple = ColeccionMultiple(pila, cola)
#     llenarAlumnos(pila)
#     llenarAlumnos(cola)
#     informar(multiple)
#     cla = ClaveValor(22, "asd")
#     print(cla.clave)
#     cla.clave = 49
#     print(cla.clave)


# 3. Implemente  la clase Conjunto.  Un Conjunto es  una  colección  que  almacena  elementos  sin repetición.  
# Es  decir,  si  se  intenta  almacenar  un  elemento  que  ya  está  en  el  conjunto,  
# éste elemento no se almacena ya que sino estaría repetido


class Conjunto(Coleccionable, Iterable):
    
    def __init__(self):
        self.__coleccion = set( )

    def agregar(self, elemento):
        self.__coleccion.add(elemento)

    def pertenece(self, elemento):
        return elemento in self.__coleccion
    
    def cuantos(self):
        return len(list(self.__coleccion))
        
    def minimo(self):
        menor = self.__coleccion[0]
        for num in self.__coleccion:
            if num.sosMenor(menor):
                menor = num
        return menor.getValor()

    def maximo(self):
        mayor = self.__coleccion[0]
        for num in self.__coleccion:
            if num.sosMayor(mayor):
                mayor = num
        
        return mayor.getValor()
    
    def contiene(self, comparable):
        for num in self.__coleccion:
            if num.sosIgual(comparable):
                return True
        return False
    
    def crearIterador(self):
        return IteradorDeConjuntos(self)

    @property
    def coleccion(self):
        return self.__coleccion

    @coleccion.setter
    def coleccion(self, coleccion):
        self.__coleccion = coleccion



#   4. Implemente  la  clase Diccionario.  Un Diccionarioes  una  colección  que  almacena
#   elementos,  donde cada elemento tiene una clave asociada. Las claves no pueden repetirse. 

# Usando diccionarios de Python
# class Diccionario:

#     def agregar(self, clave, valor):
#         self.__diccionario[clave] = valor
        

#     def valorDe(self, clave):
#         #return self.__diccionario.get(clave)
        
#         try:
#             return self.__diccionario[clave]
#         except:
#             return False


# Variante sin usar diccionarios de Python.

class ClaveValor:
               
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave):
        self.__clave = clave

    
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

class Diccionario(Coleccionable, Iterable):
    def __init__(self):
        self.__conjunto  = Conjunto()
        self.__coleccion = self.__conjunto.coleccion

    def agregar(self, clave, valor):
        for claveValor in self.__conjunto.coleccion:
            if claveValor.clave == clave:
                print("Esa clave se encuentra en uso, debe ingresar una nueva")
                return None
        self.__claveValor = ClaveValor(clave, valor) 
        self.__conjunto.agregar(self.__claveValor)
    
    def valorDe(self, clave):  
        for diccionario in self.__conjunto:
            if diccionario.clave == clave:
                return diccionario.valor
            else:
                print("No se encuentra valor para esa clave")

    def minimo(self):
        minimo = self.__conjunto[0].valor
        for diccionario in self.__conjunto:
            minimo = diccionario.valor if  diccionario.valor < minimo else None
        return minimo

    def maximo(self):
        maximo = self.__conjunto[0].valor
        for diccionario in self.__conjunto:
            maximo = diccionario.valor if  diccionario.valor > maximo else None
        return minimo
        
    def cuantos(self):
        return len(list(self.__conjunto.coleccion))
    
    def contiene(self, comparable):
        for num in self.__coleccion:
            if num.sosIgual(comparable):
                return True
        return False

    def crearIterador(self):
        return IteradorDeDiccionarios(self)

    @property
    def coleccion(self):
        return self.__coleccion

    @coleccion.setter
    def coleccion(self, coleccion):
        self.__coleccion = coleccion
    

# 5 Haga que las clases Conjunto y Diccionario implementen la interface Coleccionable. 
# En  el  caso  de  Diccionario, los  métodos minimo, máximo y contiene deben hacer  
# referencia  a los  valores  asociados,  no  a  las  claves. En  el  método agregar puede
# usar  una  clave única  por defecto, que maneja el propio diccionario para ir agregando los 
# valores asociados a esas claves únicas.

#lo resuelvo en el punto anterior.

# 6. Haga que las clases Pila, Cola, Conjunto y Diccionarioimplementen 
# la interface Iterablevista en teoría.

# Agrego las interfaces en sus respectivas clases.

#7 Implemente una función imprimirElementos que  reciba  un  coleccionable  y  
#  usando  el  iterador del coleccionable imprima todos los elementos del coleccionable

def imprimirElementos(coleccionable):
    iterador = coleccionable.crearIterador()
    while not iterador.fin():
        print(iterador.actual())
        iterador.siguiente()



# 8. Implementeunmódulo main para  crear  una pila,  una  cola,  un  conjunto  y  
#  un diccionariode alumnos y luego invoque la función imprimirElementospara cada coleccionable.

# def main():
#     pila = Pila()
#     cola = Cola()
#     conjunto = Conjunto()
#     diccionario = Diccionario()
#     llenarAlumnos(pila)
#     llenarAlumnos(cola)
#     llenarAlumnos(conjunto)
#     llenarAlumnos(diccionario)
#     imprimirElementos(pila)
#     imprimirElementos(cola)
#     imprimirElementos(conjunto)
#     imprimirElementos(diccionario)

#9. Implemente  una  función cambiarEstrategia que  reciba  
# un  coleccionable  y  una  estrategia  de comparación (implementada en el ejercicio 1) 
# y asigne esa estrategia a todos los elementos del coleccionable

def cambiarEstrategia(coleccionable, estrategiaComparacion):
    for elemento in coleccionable:
        elemento.setEstrategia(estrategiaComparacion)

#10. Modifique el módulo main para que cambie  la estrategia de comparación 
#a los elementos de un coleccionable e informe minimo y máximo elemento



# def main():
#     pila = Pila()
#     llenarAlumnos(pila)
#     cambiarEstrategia(pila.coleccion, EstrategiaPorNombre())
#     informar(pila)
#     cambiarEstrategia(pila.coleccion, EstrategiaPorLegajo())
#     informar(pila)
#     cambiarEstrategia(pila.coleccion, EstrategiaPorPromedio())
#     informar(pila)
#     cambiarEstrategia(pila.coleccion, EstrategiaPorDNI())
#     informar(pila)
    
# 11. Si  se  implementara  una  nueva  clase AlumnoEgresado,  
# subclase  de  Alumno, que agrega como estado el atributo fecha_de_egreso.
#  Además   de   agregar la clase AlumnoEgresado
# ¿qué otras modificaciones hay que hacer a todo lo desarrollado hasta acá.

class AlumnoEgresado(Alumno):
    def __init__(self, n, d, l, p, fecha_de_egreso):
        super().__init__(n, d, l, p)
        self.__fecha_de_egreso = fecha_de_egreso

# R: no se necesitaria realizar alguna otra modificacion


# 12 y  Si  se  posee  un  alumno  con  promedio 7.00 como “alumno promedio” y se desea  usar  
# para  compararlo  con  alumnos  que  están  en  un  conjunto  (donde  algunos  tienen mejor  
# promedio  y  otro  un  promedio  más  bajo),  además  se  desea  usar  la  misma  
# función  del ejercicio  7  sin  modificarla  en  absoluto.  ¿Qué cambios  se  deben  
# hacer  al  sistema  desarrollado hasta ahora para imprimir solo los alumnos que tengan 
# mejor promedio que mi “alumno promedio”?

# def main():
#     conjunto = Conjunto()
#     llenarAlumnos(conjunto)
#     imprimirElementos(conjunto)

# 13.  Implemente  el iterador pensado en el ejercicio 12. Piense en que el iterador pueda compararel “alumno promedio” 
# con los criterios promedio, nombre, legajo o dni, donde en los cuatro 
# casos solo se deben recorrer los alumnos “mayores” al alumno promedio con el criterio elegido

from clase2.AlumnoPromedio import *

# def main():
#     conjunto = Conjunto()
#     alumno_promedio = AlumnoPromedio()
#     llenarAlumnos(conjunto)
#     conjunto.agregar(alumno_promedio)
#     imprimirElementos(conjunto)
    

#14. Desarrolle  una  función multiplesIteradoresque permita que tres “clientes” 
#    iteren sobre la misma colección
def multiplesIteradores():
    pila = Pila()
    llenarAlumnos(pila)
    iteradores = []
    fin = []
    for i in range(3):
        iteradores.append(pila.crearIterador())
        fin.append(False)
    while not fin[0] and not fin[1] and not fin[2]:
        randomIndex = random.randint(0, 2)
        ite = iteradores[randomIndex]
        if (not ite.fin()):
            print(ite.actual())
            ite.siguiente()
        else:
            fin[randomIndex] = True

def main():
    multiplesIteradores()

# R: Si, a costo de rendimento, codigo menos legible y escalable, si usara un diccionario no tendria 
# que cambiar nada gracias al uso de iteradores



