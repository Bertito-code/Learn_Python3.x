# La posibilidad de definir cuál será el comportamiento de los operadores básicos 
# (+, -, *, /), se llama sobrecarga de operadores.

a = 2
b = 3
# Aqui el + se comporta como un operador matematico
print( a + b)

str1 = "Hola"
str2 = "Mundo"
# Aqui el + concatena las variables al ser del tipo str
print( str1 + str2)   

list1 = [2,4]
list2 = [5,7]
# Aqui el + une las listas, generando una sola, que incluye los elementos de la lista 1 y la lista 2
print(list1 + list2)