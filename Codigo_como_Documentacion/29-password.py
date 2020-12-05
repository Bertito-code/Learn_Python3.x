import random
import string
import io

# Crear un password con letras,numeros y simbolos aleatorio
# De una longitud proporcionada por el usuario

# Funciones
def create_password(n):
    allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    passphrase = []

    for i in range(n):
        tmp = random.choice(allChars)
        passphrase.append(tmp)
    
    out = io.StringIO()
    out.writelines(passphrase)
    return out.getvalue()

# Programa
n = int(input("Longitud del Password: "))

passwd = create_password(n)

try:
    print(passwd)
except:
    print("Falta la longitud del password")
