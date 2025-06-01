def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Solicitar datos al usuario
nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("¿Dónde vivís?: ")

# Llamar a la función con los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)
