#2. Implemente la clase GeneradorDeDatosAleatorios

import random
import string

class GeneradorDeDatosAleatorios():

    def numero_aleatorio(self, max):
        return random.randint(0, max)
    
    def string_aleatorio(self, cant):
        letras = string.ascii_letters
        return  ''.join(random.choice(letras) for i in range(cant))