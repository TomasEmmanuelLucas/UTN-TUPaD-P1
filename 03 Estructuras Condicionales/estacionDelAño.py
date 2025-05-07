emis = str(input("ingrese el emisferio, N para norte o S para sur: "))
mes = int(input("ingrese el mes del año: "))
dia = int(input("ingrese el dia actual: "))

emis = emis.lower()

if emis == "n":
    if (mes == 12 and dia > 20) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
         print("usted se encuentra en invierno")
    if (mes == 3 and dia > 20) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
         print("usted se encuentra en primavera")
    if (mes == 6 and dia > 20) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
         print("usted se encuentra en Verano")
    if (mes == 9 and dia > 20) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
         print("usted se encuentra en Otoño")     
elif emis == "s":
    if (mes == 12 and dia > 20) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
         print("usted se encuentra en Verano")
    if (mes == 3 and dia > 20) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
         print("usted se encuentra en Otoño")
    if (mes == 6 and dia > 20) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
         print("usted se encuentra en Invierno")
    if (mes == 9 and dia > 20) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
         print("usted se encuentra en Primavera")  
else:
     print("algun valor no corresponde con lo solicitado")  