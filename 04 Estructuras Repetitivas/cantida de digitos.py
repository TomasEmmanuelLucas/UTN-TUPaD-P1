num = int(input("introduzca un numero entero: "))
#solicita al usuario que ingrese numero

cant = 0
original = num
#inicializo variables 

if (num // 10 == 0):
    cant += 1
#caso especial por si ingresa un numero de una sola unidad    
else:
    while num != 0:
        cant += 1
        num = num // 10
        #trunca la division por 10 quitando una unidad y volviendo al bucle hasta que la unidad es "0" y en cada vuelta suma 1 al contador de digitos
print(f"la cantidad de digitos del numero ingresado {original} es {cant} digitos")
        