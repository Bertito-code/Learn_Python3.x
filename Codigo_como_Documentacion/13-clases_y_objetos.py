# Una clase es una plantilla de la cual vamos a poder crear objetos, 
# en python las clases en si mismas son objetos
# Una clase se compone de atributos y metodos
# ATRIBUTOS: Son las caracteristicas de nuestras clases en python
# METODOS: Nos permiten ejecutar las funcionalidades de nuestras clases

# Se recomienda que los nombres de las clases empiecen con mayuscula
class Persona:        
    
    def __init__(self, nombre, edad):
        # Para diferenciar entre el atributo y el argumento se utiliza la paralabra reservada self.
        # self hace referencia al objeto que se esta ejecutando en este momento
        self.nombre = nombre   
        self.edad = edad
        
# pass  # Se utiliza para que no nos de error la clase si no la rellenamos



###############################PARA VERIFICAR QUE UNA CLASE ES UN OBJETO#################
# Modificar los valores
Persona.nombre = "Alberto"
Persona.edad = 33
# Acceder a los valores
print(Persona.nombre)
print(Persona.edad)
#########################################################################################

# Creacion de un nuevo objeto
persona = Persona("Bertito", 33)
print(persona.nombre)
print(persona.edad)
# Creacion de un segundo objeto
persona2 = Persona("Belen", 40)
print(persona2.nombre)
print(persona2.edad)
# Saber la direccion de memoria
print(id(persona))
print(id(persona2))  
# Podemos ver que cada objeto apunta a una direccion de memoria distinta
# Esto quiere decir que apartir de nuestra clase Persona creamos dos objetos
# La clase Persona tiene un objeto en la memoria 49901896 al que apunta la variable persona
# La clase Persona tiene un objeto en la memoria 49902040 al que apunta la varibale persona2
# Cada objeto contiene su propia informacion



# Metodos dentro de una clase
# El usar """ """ es otra manera de poner comentarios en python
class Aritmetica:
    """Clase Aritmetica para realizar las operaciones de suma,resta..."""
    def __init__(self, operador1, operador2):
        self.operador1 = operador1    # El nombre del parametro no tiene por que ser igual al nombre del atributo, pero es lo comun.
        self.operador2 = operador2
    
    def suma(self):
        """Se realiza la operacion con los atributos de la clase"""   
        return    self.operador1 + self.operador2
    
    def resta(self):
        return self.operador1 - self.operador2
    
    def multi(self):
        return self.operador1 * self.operador2
    
    def divi(self):
        return self.operador1 / self.operador2
    
# Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)
print("El resultado de la suma es:  ", aritmetica.suma())

# Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)
print("El resultado de la suma es:  ", aritmetica.resta())

# Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)
print("El resultado de la suma es:  ", aritmetica.multi())

# Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)
print("El resultado de la suma es:  ", aritmetica.divi())




# NO HAY PORQUE USAR SELF, Y LOS PARAMETROS NO TIENEN QUE LLAMARSE IGUAL QUE LOS ATRIBUTOS
# TUPLA *
# DICCIONARIO **
# Ponemos this, en vez de self. Tambien añadimos una tupla con *v y tambien añadimos un diccionario con **d
class Individuo:
    def __init__(this, n, e, *v, **d):            
        this.nombre = n                  
        this.edad = e
        this.valores = v  
        this.diccionario = d               
        
    def desplegar(this):
        print("Nombre:  ", this.nombre)
        print("Edad:  ", this.edad)    
        print("Valores (Tupla):  ", this.valores)
        print("Diccionario:  ", this.diccionario)
        
p1 = Individuo("Alberto", 33)
print(p1.nombre)
print(p1.edad)
print(p1.valores)
p1.desplegar()
# Imprimir linea en blanco
print() 
p2 = Individuo("Lucio", 28, 3, 5, 9, 11)
p2.desplegar()
print()
# El diccionario se introduce con llave,valor (Key="Value")
p3 = Individuo("Andrea", 43, 2, 7, 1, 22, man="manzana", per="pera", nan="naranja")    
p3.desplegar()
