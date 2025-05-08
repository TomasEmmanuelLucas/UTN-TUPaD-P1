print("ingrese numero que desea sumar, para finalizar ingrese el numero 0: ")

num = int(input(""))
aux = 0

while num != 0:
    aux += num
    num = 0
    num = int(input(""))
print(f"la sumatoria de los numeros ingresados fue {aux}")
