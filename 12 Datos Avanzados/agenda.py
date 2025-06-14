# Creamos la agenda con claves (día, hora) y valores evento
agenda = {
    ("Lunes", 9): "Matemáticas",
    ("Lunes", 11): "Programación 1",
    ("Martes", 10): "Física",
    ("Miércoles", 15): "Programación 2",
    ("Jueves", 9): "Química",
    ("Viernes", 14): "Proyecto Final"
}

# Pedimos al usuario el día para consultar
dia = input("Ingresá el día (por ejemplo: Lunes): ").capitalize()
# .capitalize() convierte la primera letra a mayúscula y el resto a minúscula
# Esto ayuda a que el formato coincida con las claves del diccionario, que tienen el primer caracter en mayúscula

# Pedimos al usuario la hora para consultar
hora = int(input("Ingresá la hora (número entero, por ejemplo 9): "))

# Buscamos el evento usando la tupla (día, hora) como clave en el diccionario
evento = agenda.get((dia, hora))  # .get() busca la clave y devuelve el valor si existe, o None si no

if evento:
    print(f"En {dia} a las {hora} hs hay: {evento}")
else:
    print(f"No hay actividades programadas para {dia} a las {hora} hs.")
