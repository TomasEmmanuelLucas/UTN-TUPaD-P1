magnitud = int(input("ingrese la magnitud del terremoto: "))

if magnitud > 0:
    if magnitud < 3:
        print("Muy leve")
    elif magnitud >= 3 and magnitud < 4:
        print("leve")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")
else:
    print("ingrese magnitud correcta")