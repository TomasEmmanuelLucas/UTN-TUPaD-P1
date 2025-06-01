# Función recursiva para calcular el valor de Fibonacci en una posición
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario la posición máxima de la serie
posicion_max = int(input("Ingrese la cantidad de términos de la serie de Fibonacci: "))

# Mostramos la serie completa desde la posición 0 hasta la indicada
print("Serie de Fibonacci:")
for i in range(posicion_max):
    print(f"F({i}) = {fibonacci(i)}")
