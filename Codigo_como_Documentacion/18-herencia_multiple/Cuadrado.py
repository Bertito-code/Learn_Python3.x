# En primer lugar tomara prioridad la clase padre de FiguraGeometrica,
# en segundo lugar la clase color y por ultimo la clase Cuadrado
# FiguraGeometrica y Color son clases Object
# Ponemos las clases de las que va a heredar, la prioridad la tiene la clase mas a la izquierda, 
# El orden de busqueda de atributos o metodos sera primero la clase hija(Cuadrado), 
# posteriormente en la clase padre definida en el lado izquierdo(FiguraGeometrica), 
# luego en la clase padre definida en el lado derecho(Color) 
# y por ultimo en la clase padre de las clases padres que hemos utilizado(Object), es decir la clase abuela. 
# Esto es cuando creemos objetos de la clase Cuadrado

# Importamos las clases Padre, ya que se encuentran en otro fichero, dentro de este directorio
from Figura_geometrica import FiguraGeometrica
from Color import Color

'''Inicializamos los atributos de las clases Padre
Como los cuadrados tienen el mismo ancho que largo, vamos a pedir solo un valor a la clase Padre FiguraGeometrica,
que va a ser el atributo lado. Y de la clase Padre Color, solicitamos el atributo color'''

class Cuadrado(FiguraGeometrica, Color):  
      def __init__(self, lado, color):
# Se utiliza esta sintaxis para llamar a la clase padre que esta en el lado izquierdo
            FiguraGeometrica.__init__(self, lado, lado)
      # super().__init__(lado, lado)  # No se usa esta sintaxis porque genera confusion
            Color.__init__(self, color)
# Definimos este metodo a esta altura porque cada figura geometrica tiene una formula para su area,
# asi que se define en la clase hija Cuadrado y no en la clase padre FiguraGeometrica        
      def area(self):
            return self.alto * self.ancho