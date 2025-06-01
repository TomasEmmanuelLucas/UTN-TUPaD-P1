# Función recursiva que verifica si una palabra es un palíndromo
def es_palindromo(palabra):
    # Si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y última letra son distintas, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Si son iguales, revisamos el resto de la palabra (sin primera ni última letra)
    return es_palindromo(palabra[1:-1])

# Pedimos al usuario que ingrese una palabra
texto = input("Ingresá una palabra sin espacios ni tildes: ")

# Pasamos todo a minúscula por si hay mayúsculas
texto = texto.lower()

# Mostramos si es palíndromo o no
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
