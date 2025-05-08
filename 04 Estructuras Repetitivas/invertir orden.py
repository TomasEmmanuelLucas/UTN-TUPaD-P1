num = int(input("ingrese numero a invertir: "))
#solicita ingresar un numero

digito = 0
invertido = 0
original = abs(num)
#inicializo variables

while original !=0:
    digito = original % 10
    #realiza modulo a 10 para poder tomar esa ultima unidad
    invertido = invertido * 10 + digito
    #multiplica por 10 para subir un nivel el digito anterior y sumarle el nuevo como unidad
    original = original // 10 
    #trunca el numero para reducir una unidad y asi en la vuelta al bucle seguir con la continua
    
if num < 0:
    invertido = - invertido
    #caso especial por si el numero ingresado era negativo, asi respeta el signo

print(f"el numero invertido es {invertido}")