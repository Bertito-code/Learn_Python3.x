from Constantes import *
# Si no queremos usar el *, deberemos importar por separado
# from Constantes import MI_CONSTANTE
# from Constantes import Matematicas
# Al importarlas por separado podemos renombrar una clase
# from Constantes import Matematicas as Mate

print(MI_CONSTANTE)
print(Matematicas.PI)



# En Python se pueden modificar las constantes
MI_CONSTANTE = "NUEVO Valor de mi constante"
Matematicas.PI = 3.14
print(MI_CONSTANTE)
print(Matematicas.PI)