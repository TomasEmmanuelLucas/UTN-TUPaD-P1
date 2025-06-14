alumnos = {}

# Pedimos los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")

    # Pedimos 3 notas y las guardamos como tupla de enteros
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))

    alumnos[nombre] = (nota1, nota2, nota3)

# Mostramos el promedio de cada alumno
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:}")
