# Una lista es una coleccion de elementos, un conjunto de elementos que podemos alamacenar en una variable
# Las listas van entre corchetes, se pueden utilizar comillas simples o dobles, 
# El primer elemento de la lista tiene el valor de 0 dentro del indice
nombres = ["Juan", "Karla", "Ricardo", "Maria"]    
# len muestra el numero de elementos que contienen nuestra lista
print(len(nombres)) 
# Imprimimos el primer elemento de la lista 
print(nombres[0]) 
# Imprimimos el segundo elemento de la lista 
print(nombres[1])  

# Si imprimimos un elemento que no exite, nos devulve el error, el indice esta fuera de rango
# print(nombres[9])

# Navegacion inversa, con este metodo accedemos al ultimo elemento de la lista primero.
print(nombres[-1])
# Accedemos al penultimo elemento de la lista 
print(nombres[-2])  
# Imprimir un rango. SIN INCLUIR EL INDICE 2
print(nombres[0:2])
# Imprime desde el elemento de inicio hasta el indice indicado, sin incluir el indice indicado. No imprime el indice 3.  
print(nombres[:3])
# Imprime desde el indice proporcionado hasta el indice final   
print(nombres[1:])   
# Cambiar el valor de un elemento en una lista
nombres[3] = "Ivone"    
print(nombres)
# Listamos la lista con un for
for nombre in nombres:
    print(nombre) 

# Revisar si exite un elemento dentro de la lista
if "Karla" in nombres:
    print("Karla si existe en al lista")
else:
    print("El elemento buscado no existe en la lista")

# Agregar un nuevo elemento a la lista
# Ponemos el nombre de la lista seguido de .append con esto se agrega el nuevo elemento al final de la lista
nombres.append("Lorenzo")     
print(nombres)

# Insertar un nuevo elemento en el indice proporcionado
# Para insertar un elemento en una lista se utiliza .insert(x, y) 
# x es el indice delante del cual se va a insertar e y es el valor del nuevo elemento
nombres.insert(1, "Octavio")  
print(nombres)

# Eliminar un elemento de la lista
# Eliminamos un elemento de la lista mediante el comando .remove y el nombre del elemento a remover
nombres.remove("Octavio")  
print(nombres)

# Eliminar el ultimo elemento de la lista
# Por defecto elimina el ultimo elemento de la lista
nombres.pop() 
print(nombres)

# Eliminar el indice indicado de la lista
del nombres[0]
print(nombres)

# Limpiar todos los elementos de nuestra lista, la deja en blanco
nombres.clear()
print(nombres)

# Eliminar por completo la lista
# Elimina la lista por completo, incluso la variable, es una manera de eliminar variables
del nombres
# Nos devuelve un error ya que ni siquiera existe la variable, a sido eliminada por el comando del
print(nombres) 

    
