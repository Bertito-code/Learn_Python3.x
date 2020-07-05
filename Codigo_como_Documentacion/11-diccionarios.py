# Un Diccionario esta compuesto por llave,valor (key,value)

diccionario = {
    "IDE": "Integrated Development Environment ",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
        
}

print(diccionario)

# Total del elementos en el diccionario
print(len(diccionario))
# Acceder a un elemento del diccionario
# Se accede al elmento mediante su key
print(diccionario["IDE"])   
# Otra forma de acceder al elemento es usando .get y la key del elemento
print(diccionario.get("IDE")) 
# Modificar valores del diccionario
# Cambiamos las mayusculas a minusculas
diccionario["IDE"] = "integrated development environment" 
print(diccionario)
#Iterar elementos del diccionario
# En este caso nos imprimira el key de cada elemento en el diccionario
for termino in diccionario:
    print(termino)            

# En este caso nos imprime el value de cada elemento en el diccionario   
for termino in diccionario:
    print(diccionario[termino])  

# Al añadir .values nos sacara directamente el valor de los elementos del diccionario    
for valor in diccionario.values():  
    print(valor)
    
# Comprobar existencia de un elemento en el diccionario, devuelve un valor booleano
print("IDE" in diccionario)         
# Agregar un elemento al diccionario
diccionario["PK"] = "Primary Key"
print(diccionario)
# Eliminar elementos del diccionario
diccionario.pop("DBMS")
print(diccionario)
# Limpiar el diccionario
diccionario.clear()
print(diccionario)
# Eliminar el diccionario
del diccionario
