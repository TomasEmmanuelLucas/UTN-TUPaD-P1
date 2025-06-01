def calcular_promedio(a, b, c):
    # Calcula el promedio de los tres números y lo devuelve
    return (a + b + c) / 3

# Pedimos los tres números al usuario y convertimos a float
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Llamamos a la función para calcular el promedio
promedio = calcular_promedio(num1, num2, num3)

# Mostramos el resultado
print(f"El promedio es: {promedio}")
