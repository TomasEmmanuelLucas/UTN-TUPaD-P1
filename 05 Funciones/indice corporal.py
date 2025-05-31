def calcular_imc(peso, altura):
    # Fórmula del IMC: peso dividido por la altura al cuadrado
    imc = peso / (altura ** 2)
    return imc

# Pedimos al usuario que ingrese su peso en kilogramos
peso_usuario = float(input("Ingrese su peso en kilogramos: "))

# Pedimos al usuario que ingrese su altura en metros
altura_usuario = float(input("Ingrese su altura en metros: "))

# Calculamos el IMC llamando a la función
resultado_imc = calcular_imc(peso_usuario, altura_usuario)

# Mostramos el resultado con dos decimales
print(f"Su índice de masa corporal (IMC) es: {resultado_imc:.2f}")
