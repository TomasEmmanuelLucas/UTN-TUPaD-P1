#se crea el diccionario para trabajar
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

#se agregan elementos al diccionario
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300

#print(precios_frutas)

#actualizo los valores del dicc
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melon"] = 2800

#print(precios_frutas)

#creo una lista con solo los nombres de los elementos, sin los precios
lista = []

lista = precios_frutas.keys()
print(lista)