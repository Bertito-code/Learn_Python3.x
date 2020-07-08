# Importamos el modulo de aritmetica y le asignamos un alias para utilizarlo mas facilmente. 
# Esto es si esta en el mismo directorio, si no hay que indicarle la ruta de el modulo
import Modulo_aritmetica as aritmetica
# Creamos una variable que sea igual al alias que hemos creado del modulo y la funcion que queremos usar
# variable = modulo.funcion(parametros)
resultado = aritmetica.sumar(2, 2)
# Imprimimos el resultado para ver que lo realiza correctamente
print(resultado)

resultado = aritmetica.restar(2,1)
print(resultado)

resultado = aritmetica.multiplicar(2,2)
print(resultado)

resultado = aritmetica.dividir(4,2)
print(resultado)


# Si queremos importar desde otra ubicacion, usamos from, en este caso el archivo esta dentro de la carpeta modulos
# from nombre_directorio import nombre_modulo as alias
from modulos import Modulo_aritmetica as aritmetica

resultado = aritmetica.sumar(3, 2)
print(resultado)

resultado = aritmetica.restar(3,1)
print(resultado)

resultado = aritmetica.multiplicar(3,2)
print(resultado)

resultado = aritmetica.dividir(6,2)
print(resultado)

# Tambien se puede hacer de esta manera:
# import carpeta.nombre_modulo as alias
import Modulos.Modulo_aritmetica as aritmetica

resultado = aritmetica.sumar(4, 2)
print(resultado)

resultado = aritmetica.restar(4,1)
print(resultado)

resultado = aritmetica.multiplicar(4,2)
print(resultado)

resultado = aritmetica.dividir(8,2)
print(resultado)

