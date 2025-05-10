compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

#agregar jugo a la lista del 3er cliente
compras[2].append("jugo")

#reemplazar fideos por tallarines en 2do cliente
compras[1][1] = "tallarines"

#eliminar pan de la lista del 1er cliente
compras[0].remove("pan")

print(compras)