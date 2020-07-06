# Definir una funcion
def mi_funcion():
    print("Ejecutando mi funcion")    
    # Cuerpo de la funcion
    # Cuerpo de la funcion
    # Cuerpo de la funcion

# Llamar a una funcion
mi_funcion()

# PARAMETROS: Es una variable definida entre los parentesis de la funcion
# ARGUMENTO (arg): Es el valor enviado a la funcion

# Introducimos el dato que queramos en la llamada a la funcion, se lo pasamos como argumento,
#  y se le envia como parametro a la funcion
def funcion_arg(nombre):
    print(" El nombre introducido es:  ", nombre)
    
funcion_arg("Juan")         

def funcion_arg2(nombre, apellido):
    print( "El nombre introducido es:  ", nombre)
    print("El apellido introducido es:  ", apellido)

# Las funciones se pueden llamar todas las veces que se necesiten   
funcion_arg2("Juan", "Perez")    
funcion_arg2("Susana", "Dominguez")
funcion_arg2("Eduardo", "Garcia")


# Return devulve el resultado de los argumentos que le pasemos. 
# El valor se devuelve a la linea de codigo que hizo la llamada a la funcion
# No es necesario usar ; para terminar la linea
def suma(a, b):
    return a + b;       

print(suma(5, 3))       
print("El resultado de la suma es:  ", suma(5, 3))


# Se pueden poner valores por defecto
def suma2(a=20, b=7):
    return a + b

# En este caso no pasamos argumentos, ya que a y b tiene valor en el parametro
print("El resultado de la suma es:  ", suma2()) 
# Si la funcion tiene valores en el parametro y le pasamos argumentos, 
# se sustituiran los de por defecto por los que introducimos
print("El resultado de la suma es:  ", suma2(5, 3)) 


