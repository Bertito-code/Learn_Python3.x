from Orden import Orden
from Producto import Producto

producto1 = Producto("Teclado", 41)
producto2 = Producto("Raton", 14)
producto3 = Producto("Alfombrilla", 5)

productos = [producto1, producto2]

# Aqui se encuentra la relacion de agregacion ya que los objetos de la tipo producto pueden existir
# sin los objetos de tipo orden, cuando estos objetos no pueden existir fuera de la clase orden
# entonces se conoce como una relacion de composicion
orden1 = Orden(productos)
print(orden1)
print(orden1.calcular_total())

# Usamos .append para agregar un producto a nuestra lista
productos.append(producto3)
orden2 = Orden(productos)
print(orden2)
# Mandamos imprimir el precio total de los articulos contenidos en la orden2
print(orden2.calcular_total())