num = int(input("ingrese un numero entero positivo"))
#el usuario ingresa un numero
sum = 0
for i in range (0,num):
    sum +=i
    #utiliza un for para recorrer los numeros solicitados por el ejercicio y luego utiliza la variable para ir acumulando cada valor nuevo
print(f"la sumatoria de los numeros comprendidos entre 0 y {num} es: {sum}")