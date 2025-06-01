print("ingrese numero que desea sumar, para finalizar ingrese el numero 0: ")

num = int(input(""))
aux = 0
#inicializo variables

while num != 0:
    aux += num
    num = 0
    num = int(input(""))
    #mientras que el numero ingresado no sea "0" entro al bucle y cada vez que ingreso un numero se suma con los anteriores
print(f"la sumatoria de los numeros ingresados fue {aux}")
