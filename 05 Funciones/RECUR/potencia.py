# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return base * potencia(base, exponente - 1)

# Pedimos al usuario los valores de base y exponente
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero positivo): "))

# Llamamos a la función y mostramos el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")
