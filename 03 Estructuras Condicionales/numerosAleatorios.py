import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

from statistics import mode, median, mean 

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print ("Hay sesgo Negativo")
else:
    print("Sin sesgo")