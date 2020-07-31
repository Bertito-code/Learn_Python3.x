from Cuadrado import Cuadrado
from Figura_geometrica_clase_abstracta import FiguraGeometrica

cuadrado = Cuadrado(4, "Rojo")
print(cuadrado.area())
print(cuadrado.color)


#Method Resolution Order
print(Cuadrado.mro())     # .mro nos muestra el orden de las clases
# Si nos damos cuenta la clase abc figura en la lista
'''[<class 'Cuadrado.Cuadrado'>, <class 'Figura_geometrica_clase_abstracta.FiguraGeometrica'>, <class 'abc.ABC'>, <class 'Color.Color'>, <class 'object'>]'''



# No es posible crear objetos de una clase abstracta, da el siguiente error: TypeError: Can't instantiate abstract class FiguraGeometrica with abstract methods area
#figurageometrica = FiguraGeometrica()