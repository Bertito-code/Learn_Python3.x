# Las clases abstractas no permiten crear objetos
# ABC: Abstract Basic Class
# Importamos un modulo definido en las librerias de Python para clases abstractas
# Vamos a usar tambien un decorador, los decoradores agregan funcionalidades a nuestros metodos, 
# en este caso va a añadir la funcionalidad de abstracto

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    # Para usar decoradores se pone @ y el nombre del decorador    
    @abstractmethod                    
    def area(self):
        pass
    
        
# Las clases que heredan de FiguraGeometrica estan obligadas a definir el metodo area,
# de lo contrario tambien se convierten en clases abstractas.
# Esto es una caracteristica muy importante cuando estamos trabajando con la programacion orientada a objetos en Python  