cant = 0
media = 0
suma = 0
#inicializo variables 

for i in range (100):
    num = int(input("ingrese numero: "))
    cant += 1
    suma += num
    #recorre los numeros desde 0 a 99 (100 numeros), suma 1 a la cantidad de numeros para utilizarlos luego en el calculo matematico y realiza la suma de cada numero con el siguiente
media = suma/cant
#realiza el calculo matematico de promedio

print(f"la media de los numeros ingresados fue de {media}")
    