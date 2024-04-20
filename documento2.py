import random
import string

def generar_contrasena(palabra):
    # Longitud mínima de la contraseña
    longitud_minima = 8

    # Listas de números y símbolos para elegir
    numeros = '0123456789'
    simbolos = '!*()_+-;:'
    
    # Verificar que la palabra tenga al menos una letra
    if not any(char.isalpha() for char in palabra):
        raise ValueError("La palabra debe contener al menos una letra.")
    
    # Verificar longitud mínima
    while len(palabra) < longitud_minima:
        palabra += random.choice(string.ascii_letters)
    
    # Convertir la palabra en una lista para manipularla
    caracteres = list(palabra)

    # Añadir 3 números al azar
    for _ in range(3):
        caracteres.append(random.choice(numeros))

    # Añadir 2 símbolos al azar
    for _ in range(2):
        caracteres.append(random.choice(simbolos))

    # Mezclar todos los caracteres para que los números y símbolos no estén al final
    random.shuffle(caracteres)

    # Convertir la lista de caracteres de vuelta a una cadena
    contrasena = ''.join(caracteres)

    return contrasena

# Uso de la función
while True:
    palabra_usuario = input("Ingresa la palabra para generar tu contraseña: ")
    try:
        contrasena_generada = generar_contrasena(palabra_usuario)
        print(f"Tu nueva contraseña es: {contrasena_generada}")
        break
    except ValueError as e:
        print(e)
