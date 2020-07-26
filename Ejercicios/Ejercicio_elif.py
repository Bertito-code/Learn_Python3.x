# Escribe un programa que recomiende peliculas segun la edad que introduzca el usuario
# <= 16 "Lion King"
# 17−25 "La vida de Brian"
# 26−40 "Indiana Jones"
# 41-60 "Pulp Fiction"
# > 60 "La muerte tenia un precio"





# SOLUCION

edad = int(input())
if edad <= 16:
    print("Lion King")
elif edad >= 17 and edad <= 25:
    print("La vida de Brian")
elif edad >= 26 and edad <= 40:
    print("Indiana Jones")
elif edad >= 41 and edad <= 60:
    print("Pulp Fiction")
elif edad > 60:
    print("La muerte tenia un precio")
    

# OTRA SOLUCION

edad = int(input())
if edad <= 16:
    print("Lion King") 
elif 17 <= edad <= 25:
    print("La vida de Brian")
elif 26 <= edad <= 40:
    print("Indiana Jones") 
elif 41 <= edad <= 60:
    print("Pulp Fiction")
else:
    print("La muerte tenia un precio")
    