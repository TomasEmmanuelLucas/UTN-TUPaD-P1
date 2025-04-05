nota = float(input("introduzca la nota del estudiante: "))
notaminima = 6

if nota < notaminima and nota > 0:
    print("el estudiante reprobo la materia")
elif nota >= notaminima and nota <= 10:
    print("el estudiante aprobo la materia")
else:
    print("la nota ingresada no es valida")