# El simbolo de almohadilla sirve para hacer comentarios en Python
# Tambien se puede usar triple comilla ''' comentario '''


# Mediante el comando print sacaremos por pantalla lo que introduzcamos dentro de ()
print("Hola mundo")
print("Hola Mundo desde Python")


x = 3
print(x)
y = 5
print(y)
z = x + y
print(z)
w = z
print(w)
# id() muestra a que direccion de memoria ram esta apuntando la variable. En la direccion de memoria ram es donde se guarda el valor de la variable. 
# En el caso de w al ser igual que y ambas apuntan a la misma direccion de memoria, ya que el valor es el mismo
id(w)     
print(id(w))  # Muestra el valor de la direccion de memoria a la que apunta la variable.
print(id(z))  
# Podemos comprobar que la direccion de memoria de w,z es la misma ya que w=z el dato se guarda en una sola direccion de memoria ram.

e = True
print(type(e)) # Saber tipo de variable, int, float, bool, str, NoneType. Los tipos de variable pueden ser de tipo entero, de tipo decimal,de tipo booleano (True,False),de tipo cadena ("Saludos") y de tipo sin valor (None)
f = "Pruebas"
print(type(f))
g = None
print(type(g))
# Una equivalencia de una variable a otra
cadena = f
# Se pueden concatenar variables de tipo str, para concatenar junto con texto "Texto" + Variable
print("Esto es una prueba de concatenacion de variables: " + cadena + "  Esto es otra prueba:  " + cadena) 
# Para poder concatenar texto con numeros debemos de usar el simbolo de , 
print("Esto es una operacion de suma: ", x + z) 
print("Gracias al simbolo de , podemos concatenar datos de tipo str y de tipo int o float: ", z )
# Al forzar el cambio de tipo de variable a str ya no nos dara el error de que no se pueden mezclar tipos, ya que hemos convertido la variable a tipo str
print("Otro metodo es cambiar modificar el tipo de variable y pasarla a str:  " + str(y + z)) 
