# Diccionario inicial con productos y stock
stock = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}
# Aquí definimos un diccionario llamado 'stock' con algunos productos y la cantidad que hay de cada uno.

while True:  # Inicia un ciclo infinito para mostrar el menú hasta que el usuario elija salir.
    print("\nOpciones:")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Elegí una opción (1-4): ")  
    # Pide al usuario que elija una opción del menú.

    if opcion == "1":
        producto = input("Ingresá el nombre del producto para consultar: ").lower()
        # Pide el nombre del producto y lo convierte a minúsculas para evitar problemas con mayúsculas.
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]} unidades")
            # Si el producto está en el diccionario, muestra la cantidad disponible.
        else:
            print(f"El producto '{producto}' no está en el stock.")
            # Si no está, avisa que no existe.

    elif opcion == "2":
        producto = input("Ingresá el nombre del producto para agregar unidades: ").lower()
        # Pide el nombre del producto para agregar stock, y lo convierte a minúsculas.
        if producto in stock:
            cantidad = int(input("Ingresá la cantidad a agregar: "))
            # Pide cuántas unidades quiere agregar.
            stock[producto] += cantidad  # Suma esa cantidad al stock actual del producto.
            print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
        else:
            print(f"El producto '{producto}' no está en el stock.")
            # Si el producto no existe, avisa.

    elif opcion == "3":
        producto = input("Ingresá el nombre del nuevo producto: ").lower()
        # Pide el nombre del nuevo producto y lo convierte a minúsculas.
        if producto in stock:
            print(f"El producto '{producto}' ya existe en el stock.")
            # Si ya existe, avisa que no se puede agregar porque ya está.
        else:
            cantidad = int(input("Ingresá la cantidad inicial: "))
            stock[producto] = cantidad  # Agrega el producto nuevo con la cantidad que ingresa el usuario.
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break  # Sale del ciclo y termina el programa.

    else:
        print("Opción inválida. Por favor, elegí entre 1 y 4.")
        # Si el usuario ingresa algo que no está en el menú, muestra este mensaje.
