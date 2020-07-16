# Dado el siguiente texto:
# "En el Verano hace muchisimo calor en Madrid!"
# Elimina los simbolos de puntuacion ( comas, puntos, exclamaciones, interrogaciones)
# Convierte el texto a minusculas
# Imprime el texto









# SOLUCION

# frase = str(input())  # Si el texto lo introduciese el usuario
frase = "En el Verano hace muchisimo calor en Madrid!"
frase2 = frase.replace("!", "").replace("?", "").replace(",", "").replace(".", "").lower()
print(frase2)