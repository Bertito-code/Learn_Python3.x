# ATRIBUTOS PRIVADOS
# El encapsulamiento es el impedir que podemos acceder a la informacion de los atributos de manera directa. 
# Como la palabra indica lo que se hace es encapsular u ocultar el acceso a los atributos de nuestras clases
# Convertir un atributo en privado: Poner __ antes del atributo (Doble guion bajo)
# GET: Para leer informacion del atributo
# SET: Para modificar el valor del atributo asignado
# Hay que definir un metodo get y set para cada atibuto privado
# Es una buena practica que el nombre del parametro sea igual que el del atributo. ejemplo: nombre = nombre o edad = edad
# No es necesario ni obligatorio pasar todos los parametros, con pasar uno para inicializarlo es suficiente. 
# Lo normal es que se pasen parametros y no valores internos 

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        # Se pasa de manera interna, si no se pasara asi, habria que ponerlo en el init(self, nombre, edad)    
        self.__edad = 18            
        
    def get_nombre(self):
        # Usamos return porque def es para acceder a datos privados y es el que nos va a devolver los datos cuando usemos print          
        return self.__nombre        
    
    def set_nombre(self, nombre):   
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad   



# Modificamos el valor del atributo        
p1 = Persona("Alberto")   
print(p1.get_nombre())    
print(p1.get_edad())      

p2 = Persona("Pichon")
print(p2.get_nombre())
print(p2.get_edad())

# Modificamos el valor del atributo privado existente
p1.set_nombre("Veronica")  
print(p1.get_nombre())
# Modificamos el valor por defecto de 18 que tiene edad        
p1.set_edad(47)            
print(p1.get_edad())



# self.atributo     el atributo es publico
# self._atributo    el atributo es protegido o parcialmente privado
# self.__atributo   el atributo es privado  ( Es necesario crear get y set )
# Al crear un metodo privado no podemos acceder a sus valores, 
# con lo cual debemos crear un metodo publico que acceda al metodo privado.
# Y a la hora de acceder al metodo privado deberemos de hacerlo por el metodo publico que llama al privado.


class Ciudadano:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre
        self._ape_paterno = ape_paterno
        self.__ape_materno = ape_materno
    
    def metodo_publico(self):  # Se crea este metodo publico para llamar al metodo privado y poder acceder a el
        self.__metodo_privado()  # Llamada al metodo privado
        
        # Definimos un metodo privado poniendo __ delante, 
        # este metodo se va a encargar de imprimir cada uno de los atributos
    def __metodo_privado(self):  
        print(self.nombre)
        print(self._ape_paterno)
        print(self.__ape_materno)
        
    '''__ape_materno  al ser un atributo privado hay que crear el get y set para poder acceder a el'''
    def get_ape_materno(self):
        return self.__ape_materno
    def set_ape_materno(self, ape_materno):
        self.__ape_materno = ape_materno
        
            
# Creamos un nuevo objeto
c1 = Ciudadano("Juan", "Lopez", "Perez")    
# c1.__metodo_privado() # No se puede acceder a este metodo directamente porque es privado
# Al mandar imprimir el metodo publico, que a la vez manda llamar al metodo privado, podemos imprimir sus valores
c1.metodo_publico() 

print(c1.nombre)
print(c1._ape_paterno)
# print(c1.__ape_materno)  # Da error al imprimir al ser un atributo privado
# Nos permite imprimir el atributo privado al usar get, no pasamos ningun atributo al metodo()
print(c1.get_ape_materno())



