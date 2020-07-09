# Con las clases el importar de otros archivos funciona un poco distinto
# from nombre_fichero import nombre_clase
from Modulo_persona import Persona

p1 = Persona("Alberto", 33)
print(p1)

# Y si esta en otra ruta distinta el modulo
# from carpeta.nombre_fichero import nombre_clase

from Modulos.Modulo_persona import Persona

p2 = Persona("Pichon", 22)
print(p2)