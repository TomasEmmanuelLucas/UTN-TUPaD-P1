# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Pedimos al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validamos que sea positivo
if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
