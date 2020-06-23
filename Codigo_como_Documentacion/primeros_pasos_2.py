# Creamos dos variables de tipo booleano. Sacamos el valor de las variables por pantalla 
# y sacamos tambien el tipo de variable que son por pantalla. 
x = True
print(x)
y = False
print(y)
print(type(x))
print(type(y))

num1 = 1
num2 = 5
# Creamos una variable en la que preguntamos si num1 es mayor que num2 y sacamos el valor por pantalla. 
# En este caso el valor resultante es si es verdadero o falso, el que num1 sea mayor que num2.
pregunta = num1 > num2
# Como el valor de num1 no es mayor que num2, al imprimir la variable nos devulve un False. 
# Si cambiasemos el valor de num1 y pusieramos un valor mayor que num2, nos devolveria True. 
print(pregunta) 
pregunta2 = num1 < num2
print(pregunta2)

# Creamos un condicional con las variables num1 y num2, si se cumple la condicion de que num1 es menor que num2, 
# sacara por pantalla el mensaje A, 
# si no se cumple la condicion sacara por pantalla el mensaje B
if(num1 < num2):
    print("El primer numero es menor que el segundo numero")  # Mensaje A, se cumple la condicion.
else:    
    print("El primer numero es mayoe que el segundo numero")  # Mensaje B, no se cumple la condicion.

# El comado input sirve para que solicite la entrada de datos por parte del usuario
dato = input() 
# Sacamos por pantalla lo que le hemos escrito a la variable dato cuando nos lo ha solicitado.
print(dato)  

# Como los datos introducidos mediante input son de tipo str, lo que hacemos es convertir el dato a int, 
# para poder hacer operaciones matematicas, ya que lo que vamos a introducir es un numero.
num3 = int(input()) 
num4 = int(input()) 
print(num3)
print(num4)
# Sumamos los valores num3 y num4 esto es posible porque los hemos convertido a tipo int, 
# si no se hubieran convertido al ser de tipo str se imprimira su valor individual pero no se realizaria la operacion matematica. 
print(num3 + num4)
# Podemos escribir un mensaje para que le salga al usuario antes de introducir el dato.
num5 = int(input("Introduce un numero entero")) 
nom = input("Introduce tu nombre")
# Ponemos la , para poder concatenar texto con numeros.
print("El numero que has elegido " + nom + "es:  ", + num5) 
