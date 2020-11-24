#1 ¿Cuál   es   la   única   diferencia   entre   los   métodos llenar, 
#  llenarPersonasy llenarAlumnosimplementados en la práctica 1 (ejercicios 5, 12 y 16)?
# ¿Qué tuvo que hacer conel método informar(ejercicio 6)a medida que ejecutaba los métodos main(ejercicios 13 y 17)? 
# ¿Qué  sucedería  con  todos  estos  métodos  si  apareciera  una  nueva  clase Vendedor 
# la  cual  se desea comparar por cantidad de ventas realizadas?

#R: La unica diferencia entre los metodos es que cambia el objeto que se instancia y se guarda en la coleccion.
# Tuve que adaptar el metodo Informar segun el tipo de dato que se busca contenido en la coleccion.
# Para una nueva clase vendedor se tendria que adaptar el metodo llenar, creando un llenarVendedores para instanciar vendedores.
# y adaptar la logica de informar para buscar un valor pasado por teclado.

#6. implemente una única función llenar(práctica 1, ejercicios 5 y 16) y una única 
# función informar(práctica  1,  ejercicios  6 y  17) que  reciban  una opción por  
# parámetro que  indique  que comparable instanciar
from clase1.practica1 import Cola, ColeccionMultiple, Coleccionable, Numero, Pila
from clase3.fabricaDeComparables import FabricaDeComparables
import random


def llenar(coleccionable, opcion):
    if isinstance(coleccionable, Coleccionable): 
        for x in range(20):
            comparable = FabricaDeComparables.crear_aleatorio(opcion)
            coleccionable.agregar(comparable)

def informar(coleccionable, opcion):
    print(coleccionable.cuantos())
    print(coleccionable.minimo())
    print(coleccionable.maximo())
    comparable = FabricaDeComparables.crear_por_teclado(opcion)
    if coleccionable.contiene(comparable):
        print("el elemento leido esta en la coleccion")
    else:
        print("el elemento leido no esta en la coleccion")

# Adapte, modifique y compruebe el correcto funcionamiento de los métodos main de los ejercicios 9 y 17 
# de la práctica 1. Unifique ambos métodos en un único main.


# def main():
#     pila = Pila()
#     cola = Cola()
#     multiple = ColeccionMultiple(pila, cola)
#     llenar(pila, "Vendedor")
#     llenar(cola, "Vendedor")
#     informar(multiple, "Vendedor")


#7. Para  reflexionar.  ¿Qué  debería  hacer  si se quiere  tener en  el método main la  opción  
# de almacenar los comparables en una pila, en una cola, en una colección múltiple, 
# en un conjunto o en un diccionario?

# Se podria crear sus respectivas fabricas para instanciar el coleccionable deseado adaptando
# el metodo llenar para el caso del diccionario o implementando un llenar diferente en cada fabrica. 

#10. ¿Qué tienen en común las fábricas de la clase Vendedor y de la clase Alumno? 
# ¿Podría ampliarse la jerarquía de clases de las fábricas?¿Cómo?

# Ambas fabricas instancias hijos de la clase Persona, se podria crear una fabrica persona

#13. Implemente la función jornadaDeVentas

def jornada_de_ventas(coleccionable_vendedores):
    for _ in range(20):
        for vendedor in coleccionable_vendedores.coleccion:
            monto = random.randint(0, 7000)
            vendedor.venta(monto)


# 14. implemente la siguiente  funcion main
from clase3.gerente import Gerente

def main():
    coleccion = Pila()
    llenar(coleccion, "Vendedor")
    gerente = Gerente()
    for vendedor in coleccion.coleccion:
        vendedor.agregar_observador(gerente)
    jornada_de_ventas(coleccion)
    gerente.cerrar()
    

main()