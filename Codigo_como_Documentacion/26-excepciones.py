# Si dividimos 10/0 nos dara un error, ya que estamos dividiendo un valor entre 0

#10/0  # Descomentar la linea para ver el error inicial: ZeroDivisionError: division by zero

# Para que nos devuelva un mensaje personalizado de error
try:
    10/0
except:
    print("Se ha producido un error")

# En Python existen tipos de errores, para mostrar el tipo de error en nuestro mensaje personalizado
# Ponemos el tipo Exception que es el mas generico y le asignamos una variable error
try:
    10/0
except Exception as error:
    print("Se ha producido un error", error)
    
# Es importante que nuestro programa tenga control de excepciones para que asi cuando haya una pueda seguir ejecutandose
# Si no se tiene control de excepciones, cuando surja un error nuestro programa se detendra
try:
    10/0
except Exception as error:
    print("Se ha producido un error", error)

print(" El programa continua despues de los errores anteriores gracias al control de errores ")

# En este caso usamos variables, al dar el error la variable no obtiene resultado,
# por eso cuando imprimimos el resultado no sale None
# Si no estuviera el control de errores no nos llegaria a arrojar el valor None,
# ya que el programa se terminaria en la operacion que no puede realizar
resultado = None
a = 10
b = 0
try:
    resultado = a / b
except Exception as error:
    print("Se ha producido un error", error)
# Imprimimos el tipo de error para saber su tipo
    print(type(error))
# Imprimimos el resultado de la operacion
print("Resultado: ", resultado)


# Al saber el tipo de exacto de error podriamos contemplar directamente ese error, 
# pero quedarian excluidos los errores de otro tipo
resultado = None
a = 10
b = 0
try:
    resultado = a / b
except ZeroDivisionError as error:
    print("Se ha producido un error", error)
    print(type(error))
print("Resultado: ", resultado)


# Si ponemos el tipo de error muy especifico y da otro tipo de error no lo contemplara, y no habra control de errores
# En este caso el error es: TypeError: unsupported operand type(s) for /: 'str' and 'int'
# Al no ser del tipo especifico no hay control de errores y el programa se detiene
resultado = None
# a = "10"  # Se comenta la linea, para que no de el error, si quereis verlo, descomentar la linea y ejecutar
b = 0
try:
    resultado = a / b
except ZeroDivisionError as error:
    print("Se ha producido un error", error)
    print(type(error))
print("Resultado: ", resultado)


# Para el caso anterior voy a usar el tipo generico Exception, para que funcione el control de errores
resultado = None
a = "10"  
b = 0
try:
    resultado = a / b
except Exception as error:
    print("Se ha producido un error", error)
    print(type(error))
print("Resultado: ", resultado)


# Podemos usar varios tipos de errores a la vez para devolver mensajes personalizados para cada tipo de error
resultado = None
a = "10"
b = 0
try:
    resultado = a / b
except ZeroDivisionError as error:
    print("Se ha producido un error, no se puede dividir para 0", error)
    print(type(error))
except TypeError as error:
    print("Se ha producido un error, la variable 'a' no es un numero", error)
    print(type(error))
print("Resultado: ", resultado)

# Hay que ponerlas de menor jeraquia a mayor jerarquia, 
# si ponemos la de mayor jerarquia primero, el resto no se pocesaran
resultado = None
a = "10"
b = 0
try:
    resultado = a / b
except ZeroDivisionError as error:
    print("Se ha producido un error, no se puede dividir para 0", error)
    print(type(error))
except TypeError as error:
    print("Se ha producido un error, la variable 'a' no es un numero", error)
    print(type(error))
except Exception as error:
    print("Se ha producido un error: ", error)
    print(type(error))
print("Resultado: ", resultado)

# Si las variables se van a utilizar en mas sitios se definen fuera del bloque try
# Si el valor de las variables se va a definir mas adelante les ponemos el valor de None
'''
resultado = None
a = 10
b = 0
try:
resultado = a / b
except  as  :
'''
# Si las variables se van a utilizar solo en el blpque try se pueden definir dentro de el
'''
try:
a = 10
b = 0
resultado = a / b
except  as  :
'''


# Vamos a pedir datos al usuario para las variables
# Ponemos la variables dentro del try, ya que solo las vamos a usar aqui
try:
    a = 10  # int(input("Primer numero"))
    b = 2  # int(input("Segundo numero"))
    resultado = a / b
except ZeroDivisionError as error:
    print("Se ha producido un error, no se puede dividir para 0", error)
    print(type(error))
except TypeError as error:
    print("Se ha producido un error, la variable 'a' no es un numero", error)
    print(type(error))
except ValueError as error:
    print("Se ha producido un error con el tipo de valor: ", error)
    print(type(error))
except Exception as error:
    print("Se ha producido un error: ", error)
    print(type(error))
# En el caso de que no haya ninguna excepcion podemos usar el bloque else, para que nos devulva un mensaje personalizado
# El bloque else no es obligatorio usarlo
else:
    print("Todo esta OK")    
# El bloque finally se ejecuta haya o no un error, y siempre se ejecuta
# El bloque finally no es obligatorio usarlo
finally:
    print("Programa desarrollado por Alberto")   
print("Resultado: ", resultado)


# Dependiendo de las necesidades de nuestro programa, podemos crear nuestras propias clases de excepcion
# La clase que he creado personalizada para la excepcion esta en el archivo excepcion_personalizada.py
# Para lanzar la excepcion personalizada se utiliza raise
# Importamos el modulo de la Excepcion personalizada para poder utilizarlo
from excepcion_personalizada import ExcepcionPersonalizada

try:
    a = 20
    b = 20
    if a == b:
        raise ExcepcionPersonalizada("Los numeros son iguales")
    resultado = a / b
except ZeroDivisionError as error:
    print("Se ha producido un error, no se puede dividir para 0", error)
    print(type(error))
except TypeError as error:
    print("Se ha producido un error, la variable 'a' no es un numero", error)
    print(type(error))
except ValueError as error:
    print("Se ha producido un error con el tipo de valor: ", error)
    print(type(error))
except Exception as error:
    print("Se ha producido un error: ", error)
    print(type(error))
else:
    print("Todo esta OK")    
finally:
    print("Programa desarrollado por Alberto")   
print("Resultado: ", resultado)



# Jerarquia de errores mas comunes, existen mas tipos que los mostrados, el mas generico es Exception
'''
                                          BaseException
                                              |  
                                          Exception
                                              |
ArithmeticError   ----   OSError    ---   RuntimeError    ---       LookupError   ---    SyntaxError
        |                   |                                            |                     |
ZeroDivisionError           |                                            |               IdentationError                                               
                          /   \                                        /   \
          FileNotFoundError   PermissionError                IndexError    KeyError
'''         
         