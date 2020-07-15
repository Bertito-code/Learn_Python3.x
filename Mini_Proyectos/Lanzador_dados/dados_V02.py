# Autor: Alberto González
# Version: 0.2



# Librerias
from random import randint, uniform, random

# Funciones

def dx():
    aleatorio = randint(1,tipo_dado_in)
    print(aleatorio)

# Programa
numero_introducido = 1
print("Bienvenido al lanzador de dados")
while numero_introducido == 1:
    numero_introducido = int(input(" Si quieres lanzar dados pulsa 1, si quieres salir pulsa 2     "))
    if numero_introducido == 1:
        tipo_dado_in = int(input("Introduce el numero de caras que tiene el dado: "))
        numero_dados = int(input("Introduce el numero de dados que se lanzaran"))
        contador = numero_dados + 1
        while contador > 1:
            contador = contador -1
            if tipo_dado_in != 0:
                dx()
            else:
                print("ERROR:  Has introducido " + str(tipo_dado_in) + " el valor tiene que ser superior a 1")   