import random

num = random.randint(0,9)
#inicializo variables

print("a continuacion debes adivinar el numero secreto")

aleat = int(input(""))
cant = 1
#inicializo variables

if aleat == num:
    #caso especial, acierto a la primera
    cant = cant
else:
    while aleat != num:
        print("intente de nuevo")
        aleat = int(input(""))
        cant += 1
        #solicito un numero al usuario, si es distinto al numero aleatorio, vuelve a pedirlo y en cada intento suma 1 al contador de intentos
print (f"CORRECTO, se necesitaron {cant} intentos")