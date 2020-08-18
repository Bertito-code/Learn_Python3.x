# El polimorfismo es una variable que puede apuntar a un objeto de tipo padre o hijo, 
# y dependiendo al que esta apuntando en tiempo de ejecucion, va a ser el metodo que se va a ejecutar
# Una misma variable puede ejecutar el metodo de la clase padre o de la clase hija.
# Son multiples formas de ejecutar un metodo que este definido en la clase padre o hija
# Y el metodo que se ejecute va a depender de a la clase que esta apuntando
# Con esto buscamos crear metodos mas genericos y reutilizables

class Empleado:
    def __init__ (self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __str__(self):
        return " Nombre: " + self.nombre + " Sueldo: " + str(self.sueldo)


