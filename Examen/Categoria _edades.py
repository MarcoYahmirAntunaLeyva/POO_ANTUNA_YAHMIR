edades = [5, 12, 8, 18, 22, 4, 30, 45, 26, 15]

infancia = []
adolescentes = []
adultos_jovenes = []
adultos = []

for edad in edades:
  if edad < 11:
    infancia.append(edad)
  elif edad < 17:
    adolescentes.append(edad)
  elif edad < 26:
    adultos_jovenes.append(edad)
  else:
    adultos.append(edad)

print(f"Menores de edad: {infancia}")
print(f"Menores de edad: {adolescentes}")
print(f"Adultos jóvenes: {adultos_jovenes}")
print(f"Mayores de edad: {adultos}")
