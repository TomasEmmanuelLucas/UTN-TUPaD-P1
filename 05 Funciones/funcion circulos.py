import math  # Importamos para usar pi

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar el radio al usuario
radio = float(input("Ingresá el radio del círculo: "))

# Calcular área y perímetro
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostrar los resultados
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")