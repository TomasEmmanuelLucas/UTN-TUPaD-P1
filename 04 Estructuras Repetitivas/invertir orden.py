num = int(input("ingrese numero a invertir: "))

digito = 0
invertido = 0
original = abs(num)

while original !=0:
    digito = original % 10
    invertido = invertido * 10 + digito
    original = original // 10 
if num < 0:
    invertido = - invertido

print(f"el numero invertido es {invertido}")