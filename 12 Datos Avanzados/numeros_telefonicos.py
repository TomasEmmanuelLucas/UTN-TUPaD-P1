#inicializo variables
contactos = {}
nombre = 0
num = 0
contac = ""

#solicito 5 valores al usuario
for i in range (1,6):
    print(f"introduzca nombre {i}")
    nombre = input()
    print(f"introduzca el numero de {nombre}")
    num = input()
    contactos [nombre] = num

#solicito el numero del contacto
contac = input("introduzca nombre de contacto para ver su numero ")
print(contactos[contac])

