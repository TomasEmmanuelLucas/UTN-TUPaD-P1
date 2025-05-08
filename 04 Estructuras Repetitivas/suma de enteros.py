num1 = int(input("introducir primer numero entero: "))
num2 = int(input("introducir segundo numero entero: "))
suma = 0
#inicializo variables

for i in range (num1+1,num2):
    suma += i
    #realizo la suma de todos los numeros enteros entre los 2 ingresados, haciendo un juego con el bucle for y la variable    
    
print(f"la sumatoria de los numeros enteros es {suma}")