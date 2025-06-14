# Diccionario original: países como claves, capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima"
}

# Creamos un nuevo diccionario invertido
capitales_paises = {}

# Recorremos el diccionario original para invertir claves y valores
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

# Mostramos el nuevo diccionario
print(capitales_paises)
