# OPEREADORES ARITMETICOS
a = 3
b = 2
suma = a + b
print(suma)
resta = a - b
print(resta)
multi = a * b
print(multi)
division = a / b
print(division)
modulo = a % b  # El operador de modulo es el resto de la division
print(modulo)
exponente = a ** b  # El operador exponente es elevar a una potencia, a elevado a b.
print(exponente)


# OPERADORES DE ASIGNACION
x = 3
print(x)
x += 2  # Esto equivale a x = x + 2
print(x)
x -= 1  # Esto equivale a x = x - 1 
print(x)
x *= 3  # Esto equivale a x = x * 3
print(x)
x /= 2  # Esto equivale a x = x / 2
print(x)


# OPERADORES DE COMPARACION
c = 3
d = 2
# Estamos preguntando si c es igual a d. Los parentesis no son necesarios, 
# simplemente dan prioridad a la operacion que contienen. 
# Las respuestas a los operadores de comparacion son de tipo booleano.
resultado = ( c == d )  
print(resultado)
resultado = c != d  # Estamos preguntando si la variable c es diferente de d.
print(resultado)
resultado = c > d  # Preguntamos si  c es mayor que d.
print(resultado)
resultado = c >= d  # Preguntamos si c es mayor o igual que d.
print(resultado)
resultado = c < d  # Preguntamos si c es menor que d.
print(resultado)
resultado = c <= d  # Preguntamos si c es menor o igual que d.
print(resultado)


# Vamos a saber si a es un numero par, para ello utilizamos el condicional if, 
# diciendole que saque el resto de la division de c entre 2 ( operador modulo) 
# y si el resto es igual a 0 ( true) es un numero par. 
if c%2 == 0:   
    print("Es par") # Si el resultado de lo anterior es verdadero (True) (El resto de la division es 0) 
else:
    print("Es impar") # Si el resultado anterior es falso (False) (El resto de la division es distinto a 0)


edadlimite = 18
edadpersona = 5
# Utilizamos el condicional if Comparando la variable, 
# Como al tener 18 años se es mayor de edad, la comparacion que utilizamos es mayor o igual que.
if (edadpersona >= edadlimite):  
    print("Es un adulto")
else:
    print("Es menor de edad")


# OPERADORES LOGICOS
e = 3 
#e = int(input("Proporciona un valor:  "))  # Solicitamos la introduccion de un numero entero 
valorMinimo = 0  
valorMaximo = 5
# Queremos saber si la variable e esta dentro del rango que hemos creado con las variables valorMinimo y valorMaximo.
#  En este caso el rango va del 0 al 5, lo primero que preguntamos es si es mayor o igual a 0 
# y con el operdor logico and le preguntaremos si tambien es menor o igual que 5. 
# Para que se cumpla la condicion ambas variables deben de ser True.
dentrodeRango = (e >= valorMinimo and e <= valorMaximo) 
print(dentrodeRango)  # El resultado que nos dan los operadores logicos son de tipo booleano.


# Utilizamos un condicional para sacar un mensaje personalizado. 
# Si la Variable dentrodeRango es verdadera (True) nos sacara un mensaje y si es falsa (False) nos sacara otro mensaje.
if (dentrodeRango):  
    print("Esta dentro del Rango")
else:
    print("No esta dentro del rango")


# variables del tipo booleano ( True,False)
vacaciones = False 
diadescanso = True
# El operador logico or equivale a "o". Si es verdadera la variable 1 "o" es verdadera la variable 2, 
# la condicion es verdadera (True) con cumplir una de las 2 variables la condicion es verdaddera  
if (vacaciones or diadescanso):   
    print("Puedes ir al parque")
else:
    print("Tienes que trabajar, no puedes ir al parque")
# El operador logico not invierte los valores booleanos.
# En este la variable vacaciones es False, pero al usar not imprimira por pantalla que vacaciones en True.
print(not(vacaciones)) 
# Al utilizar not, la condicion cambia a si no son vacaciones o diadedescanso...
#  Hemos cambiado el si se cumple la condicion, a si no se cumple la condicion.  
if (not(vacaciones or diadescanso)): 
    print("Tienes que trabajar, no puedes ir al parque")  # Se coloca alreves que en el if. Se ha invertido la logica 
else:
    print("Puedes ir al Parque")
