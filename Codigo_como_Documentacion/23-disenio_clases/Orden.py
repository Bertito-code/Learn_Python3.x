# En Python los tipos de la variables son muy flexibles, esto se conoce como tipado dinamico

class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
    
    def agregar_producto(self, producto):
        self.__productos.append(producto)

    # Sumamos el precio de los productos dentro de una orden, para poder imprimirlos
    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total

    def __str__(self):
        productos_str =""
        for producto in self.__productos:
            productos_str += producto.__str__() + " | "
            # La linea 24 y 26 son dos maneras de escribir lo mismo. Cambia la sintaxis
            # productos_str = productos_str + producto.__str__() + " | "
        return "Id Orden: " + str(self.__id_orden) + " Productos: " + productos_str
    