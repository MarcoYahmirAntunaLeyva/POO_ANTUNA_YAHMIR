#Utilizando llaves
N1 = {"Cinco", 8, 3.1415}
print(N1)

#Método add()
N2 = {"uno", 2, 3.1415}
N2.add("cuatro")
print(N2)

#Método remove()
N3 = {"uno", 2, 3.1415}
N3.remove(2)
N3.discard("uno")
print(N3)

'OPERACIONES'
#Union de conjuntos
union = N1 | N2
N1.union(N2)
print ("Union N1,N2",union)

#Intersección de conjuntos
interseccion = N1 & N2
N1.intersection(N2)
print("interseccion", interseccion)

#Diferencia de conjuntos
diferencia = N1 - N2
N1.difference(N2)
print(diferencia)

'MÉTODOS COMUNES'
#len(conjunto)
print("Numero_elementos_en_N1", len(N1))
print("Numero_elementos_en_N2", len(N2))
print("Numero_elementos_en_N3", len(N3))

# in
print(2 in N1)
print("Cinco" in N1)

# Clear()
N2.clear()
print(N2)
print(N3)

# copy()
N1.copy()
print(N1)

'TUPLAS'
#Utilizando paréntesis
tupla = (3, "nueve", -4.2)
print(tupla)

#Utilizando índices con []
tupla[0]
print(tupla[0])

#Utilizando operador +
tupla1 = (2, "tres", .99)
tupla2 = (9, "uno", -9.8)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

#Utilizando operador *
mi_tupla = (2, 4, 5)
tupla_repetida = mi_tupla * 2
print(tupla_repetida)

#Asignar elementos de una tupla a diferentes variables
tupla_nueva = (1, 2, 3)
a, b, c = tupla_nueva
print(a)
print(b)
print(c)