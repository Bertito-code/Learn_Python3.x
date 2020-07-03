# Los elementos dentro del Set son unicos, y no mantienen ningun orden. 
# No podemos modificar sus elementos, pero si podemos agregar elementos o eliminar elementos
# Set es una coleccion sin orden y sin indice

planetas = {"Marte", "Jupiter", "Venus"}
# Al imprimir el set, podemos ver que no siguen ningun orden, 
# cada vez que se ejecuta el orden puede cambiar
print(planetas)  
#Numero de elementos
print(len(planetas))
# Ver si un elemento esta presente
# Nos devuelve un valor Booleano (True/False)
print ("Tierra" in planetas)  
# Agregar un nuevo elemento
planetas.add("Tierra")
print(planetas)
# No se pueden agregrar elementos duplicados, 
# con lo cual solo imprimira un elemento con el mismo nombre, 
# como podemos ver en la siguiente linea
planetas.add("Tierra") 
print(planetas)
# Eliminar elementos
# Si pusieramos un elemento que no existe nos daria un error
planetas.remove("Tierra")  
print(planetas)
# Con Discard si no existe el elemento a eliminar no nos arroja un error
planetas.discard("Jupiter") 
print(planetas)
# Limpiar el set
planetas.clear
print(planetas)
# Eliminar el set, con esto se elimina totalmente la variable
del planetas






