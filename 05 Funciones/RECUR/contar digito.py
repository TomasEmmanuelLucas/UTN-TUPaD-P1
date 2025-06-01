 def contar_digito(numero, digito):
    if numero == 0:  # Si no queda nada para mirar, terminamos
        return 0
    else:
        if numero % 10 == digito:  # Si el último número es el que buscamos
            return 1 + contar_digito(numero // 10, digito)  # Sumamos 1 y seguimos con el resto
        else:
            return contar_digito(numero // 10, digito)  # No sumamos nada, seguimos con el resto

# Ejemplo:
print(contar_digito(123456, 7))  # Esto imprime 0 porque no hay 7 en el número
