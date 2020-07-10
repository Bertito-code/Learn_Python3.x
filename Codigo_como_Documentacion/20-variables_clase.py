# VARIABLE DE CLASE: Es cualquier variable definida fuera del los metodos, 
# pero dentro de nuestra clase
# VARIABLE DE INSTANCIA: Es cualquier variable definida dentro del metodo __init__ 
# y de la cual estamos inicializando el valor dentro del metodo __init__, 
# esta variable se asocia con los objetos que vamos a crear

class Miclase:
    variable_clase = "Esto es una variable de clase"   
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
        
# Para acceder a la variable de clase, no hay necesidad de crear un objeto, 
# ya que podemos acceder al valor usando simplemente el nombre de la clase
print(Miclase.variable_clase)

# Para acceder a la variable de instancia hay que crear un objeto
objeto1 = Miclase("Variable de instancia")
print(objeto1.variable_instancia)
Miclase.variable_instancia = "Modificando variable instancia"
print(Miclase.variable_instancia)

# Podemos acceder a la variables de clase desde los objetos
print(objeto1.variable_clase)

# Podemos acceder a la varibles con el nombre de la clase
print(Miclase.variable_clase)

# No estamos modificando realmente la variable de clase, 
# si no que se crea un nuevo atributo que se asocia con esta instancia.
objeto1.variable_clase = "Modificando variable de clase"
print(objeto1.variable_clase)
# Comprobamos que si mandamos imprimir la misma variable, 
# nos da resultados distintos, ya que la variable solo se ha modificado para el objeto
print(Miclase.variable_clase)  

# Si modificamos la variable de clase, todos los objetos que creemos despues de la modificacion y accedan
# a la variable clase, obtendra el valor de la modificacion, pero los objetos que creamos antes
# seguiran teniendo el valor inicial



