# Se rompe el bucle for cuando se cumple la condicion if. Rompe con el Bucle que se esta ejectuando en este momento.
# Pasa a la siguiente linea fuera del ciclo.
# Cuando se usa break se rompe el bucle y pasa directamente a la siguiente linea que este fuera del bucle
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break            
else:
    print("Fin ciclo for")

print("Continua el programa")     


# Utilizamos range() para definir un rango, en este caso del 0 al 5.
for i in range(6):     
    if i%2 == 0:
        print(i)


# En este caso le decimos que el resultado no sea 0 al dividirlo entre dos,
# y mediante el continue sigue con el siguiente numero
# Si la expresion es falsa salta al print, si es verdadero continua con el siguiente valor.
for i in range(6):     
    if i%2 != 0:       
        continue       
    print(i)    

