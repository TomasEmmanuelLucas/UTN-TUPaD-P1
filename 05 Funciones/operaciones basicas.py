def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Para evitar error de división por cero
    if b != 0:
        division = a / b
    else:
        division = None  # O puedes usar "division = 'No se puede dividir por cero'"
    
    # Devuelve una tupla con los resultados
    return (suma, resta, multiplicacion, division)

# Pedimos los dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamamos a la función y guardamos la tupla resultado
resultados = operaciones_basicas(num1, num2)

# Mostramos los resultados de forma clara
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
if resultados[3] is not None:
    print(f"División: {resultados[3]}")
else:
    print("División: No se puede dividir por cero")
