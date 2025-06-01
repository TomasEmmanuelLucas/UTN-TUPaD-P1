# Función recursiva para contar cuántos bloques se necesitan
def contar_bloques(n):
    # Si solo hay un nivel, se necesita un solo bloque
    if n == 1:
        return 1
    else:
        # Sumamos los bloques de este nivel con los del nivel de arriba
        return n + contar_bloques(n - 1)

# Pedimos al usuario que ingrese cuántos bloques quiere en la base
nivel_base = int(input("¿Cuántos bloques tiene el nivel más bajo? "))

# Calculamos el total de bloques con la función
total = contar_bloques(nivel_base)

# Mostramos el resultado
print("Para construir la pirámide se necesitan", total, "bloques.")
