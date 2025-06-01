# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Pedimos al usuario un número entero positivo
limite = int(input("Ingrese un número entero positivo: "))

# Mostramos los factoriales desde el número ingresado hasta 1
for i in range(limite, 0, -1):
    print(f"{i}! = {factorial(i)}")
