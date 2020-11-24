#3. Implemente la clase LectorDeDatos

class LectorDeDatos():

    def numero_por_teclado(self):
        self.__numero = int(input("Ingrese un numero: "))
        return self.__numero

    def string_por_teclado(self):
        self.__string = input("Ingrese un string: ")
        return self.__string


