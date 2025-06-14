#inicializo set
parcial1 = {1,7,2,5,8,9}
parcial2 = {1,2,3,5,6}

#para saber quienes aprobaron ambos haga la interseccion de los set
ambos = {}
ambos = parcial1 & parcial2

print(f"los que aprobaron ambos: {ambos}")

#para los que aprobaron 1 hago diferencia simetrica entre sets
uno_solo = {}
uno_solo = parcial1 ^ parcial2

print(f"los que aprobaron 1 de los parciales: {uno_solo}")

#para la lista total que aprobaron al menos 1 parcial sin repetirlos hago la union
uno = {}
uno = parcial1 | parcial2

print(f"la lista total de estudiantes que aprobaron al menos 1: {uno}")