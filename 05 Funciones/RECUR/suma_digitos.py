# Función recursiva que suma los dígitos de un número
def suma_digitos(n):
    # Caso base: si el número tiene un solo dígito, se devuelve ese dígito
    if n < 10:
        return n
    else:
        # Tomamos el último dígito (n % 10) y lo sumamos con la llamada recursiva
        return (n % 10) + suma_digitos(n // 10)

# Ejemplos de uso
print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8
