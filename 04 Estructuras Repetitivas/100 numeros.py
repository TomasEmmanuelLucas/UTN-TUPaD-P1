neg = 0
posi = 0
impar = 0
par = 0
cero = 0
#inicializo variables

for i in range(0,100):
    print("ingrese numero para evaluar: ")
    num = int(input(""))
    #solicito el ingreso del numero 
    if num < 0:
        #verifica si es negativo
        neg += 1
        if num % 2 == 0:
            par += 1
            #verifica si es par haciendo el modulo a 2 del numero
        else:
            impar += 1
    elif num == 0:
        cero += 1
        #caso especial por si ingresa un "0"
    else:
        posi += 1
        #verifica si es positivo
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"la cantidad de numeros negativos ingresados fue {neg}")
print(f"la cantidad de numeros positivos ingresados fue {posi}")
print(f"la cantidad de numeros pares ingresados fue {par}")
print(f"la cantidad de numeros impares ingresados fue {impar}")
print(f"usted ingreso {cero} veces el numero 0")