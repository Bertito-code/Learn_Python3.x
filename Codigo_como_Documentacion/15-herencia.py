# Clase padre llamada Persona
# Clase hija llamada Empleado 
# La clase Empleado va a heredar las caracteristicas y metodos de la clase Persona.
# Pero la clase Empleado puede agregar sus propios atributos y metodos
# No es necesario ponerlo, pero para tener mas informacion esta clase seria (object), 
# la clase object es la clase padre de todas las clases en python

class Persona:                     
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# El metodo __str__ se utiliza para que al usar print(Persona) 
# en vez de imprimirnos la direccion de memoria a la que apunta, nos imprima los valores de la clase        
    def __str__(self):
# Usamos return para pasar los valores que tiene que devolver, 
# convertimos el valor de la edad a texto, para que no nos devuelva un error                      
        return "Nombre: " + self.nombre + "  Edad: " + str(self.edad)          
        
# Se pone entre parentesis () de la clase que hereda, en este caso va a heredar de Persona            
class Empleado(Persona):
# Aqui ponemos los parametros de la clase padre y añadimos los que queramos para la clase hija                      
    def __init__(self,nombre, edad, sueldo):
# Con super() accedemos a los metodos o atributos de la clase padre.
# Ponemos despues .__init__() y dentro del parentesis los atributos a los que queremos acceder  
        super().__init__(nombre, edad)
# Definimos el atributo de la clase hijo                         
        self.sueldo = sueldo                    
    def __str__(self):
# Llamamos con super() al metodo str de la clase padre y añadimos solo la parte de la clase hija
        return super().__str__() + " Sueldo: " + str(self.sueldo)   
        


# Creamos algunos objetos de prueba

persona = Persona("Alberto", 33)
print(persona)       
        
empleado = Empleado("Pichon", 30, 1200)
print(empleado)

# Estamos cambiando valores de la clase padre, desde la clase hija
# Cambiamos un valor de la clase hija
# Imprimimos los valores para ver que se ha realizado el cambio
empleado.nombre = "Natalia"   
empleado.sueldo = 1300        
print(empleado)               