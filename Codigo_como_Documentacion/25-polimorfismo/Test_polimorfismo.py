from Empleado import Empleado
from Gerente import Gerente


# Se puede definir en un archivo a parte, para no tener que depender del orden, solo hay que importarlo
def imprimir_detalles(tipo):
    print(tipo)
    # Usamos type para que nos diga que metodo se esta ejecutando
    # Ponemos el end="\n\n" para que imprima dos lineas en blanco al final de la salida
    print(type(tipo), end="\n\n")
    # Podemos utilizar if isinstance para que nos devuelva un valor de un metodo si es verdadero.
    # En este caso le decimos que es la clase hija, nos imprima el valor de departamento
    if isinstance(tipo, Gerente):
        print(tipo.departamento)
    
    
# Llamamos al metodo de la clase padre
# Esto es asi porque la variable "tipo" esta apuntando a un objeto de clase "empleado"
# asi que el metodo que se hace llamar es el de la clase padre
empleado = Empleado("Alberto", 1200)
imprimir_detalles(empleado)

# Llamamos al metodo de la clase hija
# Podemos ver que es verdad ya que esta incluyendo el atributo de "departamento"
empleado = Gerente("Pichon", 2000, "Todos")
imprimir_detalles(empleado)
