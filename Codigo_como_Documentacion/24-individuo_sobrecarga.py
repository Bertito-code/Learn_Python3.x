class Individuo(object):
    def __init__(self, nombre):
        self.__nombre = nombre
    # SOBRESCRITURA ES MODIFICAR EL COMPORTAMIENTO DE UN METODO DEFINIDO EN LA CLASE PADRE
    # Metodo sobre escrito de la clase padre object
    def __add__(self, otro_objeto):
        return self.__nombre + otro_objeto.__nombre
    # En este caso no tiene mucho sentido sobrecargar el operador - en nuestra clase
    def __sub__(self, otro_objeto):
        return "Operacion no soportada"

individuo1 = Individuo("Alberto")
individuo2 = Individuo("Pedro")
# Sobrecargar el operador para darle una nueva forma de trabajar al operador +
print(individuo1 + individuo2)
# En este caso habria que definir que se quiere hacer, 
# ya que la suma es normal que concatene los valores, 
# pero en el caso de la resta habria que definirlo, 
# ya que no tiene sentido el - en este caso
print(individuo1 - individuo2)
