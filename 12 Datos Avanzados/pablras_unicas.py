# Pedimos al usuario que escriba una frase
frase = input("Escribí una frase: ")

# Dividimos la frase en palabras
palabras = frase.split()

# Mostramos las palabras únicas con un set
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Creamos un diccionario para contar las palabras
conteo = {}

# Recorremos cada palabra y la contamos
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

# Mostramos el diccionario con el conteo
print("Conteo de palabras:", conteo)
