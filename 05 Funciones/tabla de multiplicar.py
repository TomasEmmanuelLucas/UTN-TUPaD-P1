def tabla_multiplicar(numero):
    # Inicializamos el contador en 1
    i = 1
    # Creamos una lista vacía para almacenar las líneas de la tabla
    resultados = []
    
    # Usamos un ciclo while para iterar desde 1 hasta 10
    while i <= 10:
        # Construimos la línea de multiplicación y la agregamos a la lista
        resultados.append(f"{numero} x {i} = {numero * i}")
        # Incrementamos el contador para pasar al siguiente número
        i += 1
    
    # Recorremos la lista con las líneas guardadas
    for linea in resultados:
        # Imprimimos cada línea de la tabla de multiplicar
        print(linea)

# Pedimos al usuario que ingrese un número y lo convertimos a entero
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Llamamos a la función y le pasamos el número ingresado
tabla_multiplicar(num)