# Las tuplas a diferencias de las listas no permiten modificar los elementos una vez que las hemos inicializado (inmutables)
# Las tuplas como las listas siguen un orden

frutas = ( "Naranja", "Platano", "Manazana")
print(frutas)
# Saber el numero de elementos de la tupla
print(len(frutas)) 
# Acceder a un elemento de la tupla, se utiliza el numero de indice como en las listas
print(frutas[0])
# Navegacion inversa
print(frutas[-1])
# Rango dentro de la tupla
print(frutas[0:2])
# Convertir una Tupla en una Lista, esto lo usamos para poder modificar un elemento, 
# ya que las tuplas no lo permiten con lo cual transformamos la tupla en una lista 
# y modificamos el el elemento en la lista
frutaslista = list(frutas)
# Al convertir en el paso anterior la tupla en lista ya podemos modificar elementos
frutaslista[1] = "Fresa"    
# Ahora convertimos la Lista en Tupla, para dejarlo como estaba despues de haber añadido los elementos
frutas = tuple(frutaslista)
print(frutas)
# Iterar elementos de la tupla, 
# al hacer una iteracion mostramos los elementos individualmente
for fruta in frutas:
    print(fruta)
# Lo mismo que lo anterior, pero quitamos el salto de linea entre los elementos, 
# haciendo que la separacion sea un espacio entre ellos
for fruta in frutas:
    print(fruta, end=" ")

#No podemos agregar ni modificar elementos de la tupla, lo unico que podemos hacer es eliminar la tupla
del frutas
