class Producto:
    # Creamos una variable para contar los objetos que se crean
    contador_productos = 0
    
    def __init__(self, nombre, precio):
        # La variable que cuenta los objetos que creamos de la clase Producto suma 1 por cada Objeto creado
        Producto.contador_productos +=1
        # El id del producto sera igual al orden que se haya creado el objeto. 
        # Asi si es el primer objeto su id sera 1, si es el segundo el 2...  Esto hara que sea un valor unico
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio 

    def __str__(self):
        return "Id Producto: " + str(self.__id_producto) + " Nombre: " + self.__nombre + " Precio: " + str(self.__precio)
