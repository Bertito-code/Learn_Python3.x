'''
Estamos creando un personaje para un videojuego y queremos modificar las caracteristicas que este tiene con funciones.
Utilizaremos el modificador global, para cambiar el valor de la varaiable que esta fuera de las funciones.
'''

pj_damage = 100
pj_life = 120
pj_shield = 20

# Queremos que la primera funcion multiplique por 2 el damage
# La segunda funcion sumaria 100 al valor life
# Y por ultimo reduciriamos a un 10% el valor shield
# Imprimir los resultados en una linea



# SOLUCION

def up_damage():
    global pj_damage
    pj_damage *= 2
def shield():
    global pj_shield
    pj_shield *= 0.1
def up_life():
    global pj_life
    pj_life += 100


up_damage()
shield()
up_life()
print(pj_damage, pj_shield, pj_life)
