def celsius_a_fahrenheit(celsius):
    # Calcula y devuelve la temperatura en Fahrenheit
    return (celsius * 9/5) + 32

# Pide al usuario que ingrese la temperatura en grados Celsius
print("Ingrese la temperatura en grados Celsius:")

# Lee el valor ingresado y lo convierte a número decimal (float)
temp_celsius = float(input())

# Llama a la función para convertir y muestra el resultado
print(celsius_a_fahrenheit(temp_celsius))
