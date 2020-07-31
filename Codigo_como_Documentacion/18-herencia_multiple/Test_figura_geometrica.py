from Cuadrado import Cuadrado

cuadrado = Cuadrado(4, "Rojo")
print(cuadrado.area())
print(cuadrado.color)


# Method Resolution Order
# .mro nos muestra el orden de las clases
print(Cuadrado.mro())     

