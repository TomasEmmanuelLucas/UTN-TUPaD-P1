contraseña = str(input("ingrese una contraseña entre 8 y 14 caracteres: "))

cant = len(contraseña)

if cant >= 8 and cant <= 14:
    print("ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")