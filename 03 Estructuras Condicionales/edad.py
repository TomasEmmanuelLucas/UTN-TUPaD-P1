edad = float(input("ingrese su edad: "))

if edad > 0:
    if edad < 12:
        print("usted es un niño")
    elif edad >= 12 and edad < 18:
        print("usted es un adolecente")
    elif edad >= 18 and edad < 30:
        print("usted es un adulto/a joven")
    else:
        print("usted es adulto/a")
else:
    print("por favor ingrese una edad real")
