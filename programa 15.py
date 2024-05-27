edades = [15, 23, 17, 28, 32, 12, 19, 25]

mayores_de_edad = []
menores_de_edad = []

for edad in edades:
  if edad >= 18:
    mayores_de_edad.append(edad)
  else:
    menores_de_edad.append(edad)

print(f"Mayores de edad: {mayores_de_edad}")
print(f"Menores de edad: {menores_de_edad}")
