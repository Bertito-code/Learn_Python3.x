# Autor: Alberto González
# Version: 0.1
# En desarrollo


# Librerias
from random import randint, uniform, random


# Variables 


# Funciones

def d4():
    aleatorio = randint(1,tipo_dado_in)
    print(aleatorio)

def d6():
    aleatorio = randint(1,tipo_dado_in)
    print(aleatorio)

def d8():
    aleatorio = randint(1,tipo_dado_in)
    print(aleatorio)

def d12():
    aleatorio = randint(1,tipo_dado_in)
    print(aleatorio)

def d20():
    
    aleatorio = randint(1,tipo_dado_in)
    if aleatorio == tipo_dado_in:
        print("20   CRITICO")
    elif aleatorio == 1:
        print("1    PIFIA")
    else:
        print(aleatorio)

def d100():
    
    aleatorio = randint(1,tipo_dado_in)
    print(aleatorio)

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
        contador = numero_dados
        while contador > 1:
            contador = contador -1
            if tipo_dado_in == 4:
                d4()
            elif tipo_dado_in == 6:
                d6()
            elif tipo_dado_in == 8:
                d8()
            elif tipo_dado_in == 12:
                d12()
            elif tipo_dado_in == 20:
                d20()
            elif tipo_dado_in == 100:
                d100()
        else:
            dx()   



