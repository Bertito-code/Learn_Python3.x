# Convertir un diccionario en un fichero JSON

# Libreria Json
import json

# Diccionario
colores = {"arcoiris": ["rojo", "naranja", "amarillo", "verde", "azul", "indigo", "violeta"],
          "CMYK": ["azul", "magenta", "amarillo", "key color"],
          "RBG": ["rojo", "azul", "verde"]}


# Creacion del fichero json con los datos del diccionario
with open("colores.json", "w") as archivo_json:
    json.dump(colores, archivo_json)