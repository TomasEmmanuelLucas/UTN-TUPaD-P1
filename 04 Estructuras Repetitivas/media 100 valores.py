cant = 0
media = 0
suma = 0

for i in range (100):
    num = int(input("ingrese numero: "))
    cant += 1
    suma += num

media = suma/cant

print(f"la media de los numeros ingresados fue de {media}")
    