# Definimos una función que convierte segundos a horas
def segundos_a_horas(s):
    return s / 3600  # 1 hora tiene 3600 segundos

# Solicitamos al usuario que ingrese una cantidad de segundos
s = int(input("Segundos: "))  # Convertimos el valor ingresado a entero

# Llamamos a la función y mostramos el resultado
print("Horas:", segundos_a_horas(s))  # Mostramos las horas resultantes