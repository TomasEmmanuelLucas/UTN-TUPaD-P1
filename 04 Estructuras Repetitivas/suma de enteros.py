num1 = int(input("introducir primer numero entero: "))
num2 = int(input("introducir segundo numero entero: "))

suma = 0

for i in range (num1+1,num2):
    suma += i
    
    
print(f"la sumatoria de los numeros enteros es {suma}")