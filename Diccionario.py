#Utilizando llaves
diccionario = {
    "Nombre" : "Yahmir",
    "Edad" : 18,
    "Grupo" : "A"
}

print(diccionario)

#Utilizando dict
diccionario2 = dict(nombre="Yahmir", Edad=18, Grupo="A")

print(diccionario2)

#Utlizando corchetes
diccionario3 = {
    "Nombre" : "Yahmir",
    "Edad" : 18,
    "Grupo" : "A"
}

print(diccionario3["Nombre"])

#Se asigna valor a clave existente
diccionario4 = {
    "Nombre" : "Yahmir",
    "Edad" : 18,
    "Grupo" : "A"
}

diccionario4["Nombre"] = "Marco"

#Se asigna nueva clave y valor
#Eliminar clave

diccionario4["Carrera"] = "TI"
del diccionario4["Grupo"]
print(diccionario4)


'METODOS COMUNES'
#keys
diccionario5 = {
    "Nombre" : "Yahmir",
    "Edad" : 18,
    "Grupo" : "A"
}

print(diccionario5.keys())

#values
values = diccionario5.values()
print(values)

#items
items = diccionario5.items()
print(items)
