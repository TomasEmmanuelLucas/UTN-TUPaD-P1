nombre = input("ingrese su nombre: ")

print("opciones:")
print("opcion 1: nombre en mayusculas")
print("opcion 2: nombre en minusculas")
print("opcion 3: primera letra en mayusculas")

opcion = int(input("ingrese la opcion deseada: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.capitalize())
else:
    print("opcion incorrecta")