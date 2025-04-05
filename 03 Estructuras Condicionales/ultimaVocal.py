palabra = input("ingrese palabra a verificar: ")

ultima = palabra[-1].lower() #funciona con mayusculas tambien

if ultima in "aeiou":
    print(palabra+"!")
else:
    print(palabra)