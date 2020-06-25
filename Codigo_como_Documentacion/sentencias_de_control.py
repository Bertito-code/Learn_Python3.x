# LAS SENTENCIAS DE CONTROL NOS PERMITEN CONTROLAR EL FLUJO DE NUESTROS ALGORITMOS

condicion = True
if condicion == True:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")


if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:  # Preguntamos si la condicion es falsa de manera explicita.
    print("La condicion es falsa")
else:  # Si no se cumple ninguna de las 2 condiciones anteriores entonces imprime "Condicion no reconocida"
    print("Condicion no reconocida")


numero = int(input("Introduce un numero entre 1 y 3:   "))
if numero == 1:
    numerotexto = "Numero uno"
elif numero == 2:
    numerotexto = "Numero dos"
elif numero == 3:
    numerotexto = "Numero tres"
else:
    numerotexto = "Valor fuera de rango"

print("Numero proporcionado:   " + numerotexto)


# OPERADOR TERNARIO, SOLO SI ES MUY SENCILLO LO QUE SE VA A ANALIZAR.
condicion = True
print("Condicion verdadera") if condicion else print("Condicion falsa")
# Lo anterior equivale a lo siguiente
if condicion == True:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")
