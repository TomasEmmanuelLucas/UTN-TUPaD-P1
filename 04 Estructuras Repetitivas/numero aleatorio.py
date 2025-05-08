import random

num = random.randint(0,9)

print("a continuacion debes adivinar el numero secreto")

aleat = int(input(""))
cant = 1

if aleat == num:
    #caso especial, acierto a la primera
    cant = cant
else:
    while aleat != num:
        print("intente de nuevo")
        aleat = int(input(""))
        cant += 1
print (f"CORRECTO, se necesitaron {cant} intentos")