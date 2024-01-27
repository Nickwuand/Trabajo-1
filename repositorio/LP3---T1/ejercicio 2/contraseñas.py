import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud=8))
    return contraseña

print(generar_contraseña())