num = int(input("introduzca un numero entero: "))

cant = 0
original = num

if (num // 10 == 0):
    cant += 1
    
else:
    while num != 0:
        cant += 1
        num = num // 10
print(f"la cantidad de digitos del numero ingresado {original} es {cant} digitos")
        