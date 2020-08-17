# Dada la longitud, altura y anchura, calcula el resultado de las siguientes formulas
# Los valores los debe de introducir el usuario

a = 5
b = 10
c = 15

# s = 4(a + b + c)

# S = 2(ab + bc + ac)

# V = abc







# SOLUCION

a1 = input()
b1 = input()
c1 = input()
a1 = int(a1)
b1 = int(b1)
c1 = int(c1)
print(int((a1 + b1 + c1) * 4))  # 120
print(int(((a1 * b1) + (b1 * c1) + (a1 * c1)) * 2))  # 550
print(int(c1 * b1 * a1))  # 750