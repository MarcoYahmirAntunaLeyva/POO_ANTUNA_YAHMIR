while True:
  print("Seleccione una figura geométrica:")
  print("A) Cuadrado")
  print("B) Triángulo")
  print("C) Rectángulo")
  print("D) Salir")

  opcion = input("Introduce una opcion: ").upper()

  if opcion == "A":
    try:
      lado = float(input("Introduce el lado del cuadrado: "))
      area = lado * lado
      print(f"El área del cuadrado es: {area}")
    except ValueError:
      print("Error: Ingresa un valor numérico válido para el lado.")

  elif opcion == "B":
    try:
      base = float(input("Ingrese la base del triángulo: "))
      altura = float(input("Ingrese la altura del triángulo: "))
      area = (base * altura) / 2
      print(f"El área del triángulo es: {area}")
    except ValueError:
      print("Error: Ingresa valores numéricos válidos para la base y la altura.")

  elif opcion == "C":
    try:
      base = float(input("Ingrese la base del rectángulo: "))
      altura = float(input("Ingrese la altura del rectángulo: "))
      area = base * altura
      print(f"El área del rectángulo es: {area}")
    except ValueError:
      print("Error: Ingresa valores numéricos válidos para la base y la altura.")

  elif opcion == "D":
    print("¡Hasta luego!")
    break

  else:
    print("Opción inválida. Intente nuevamente.")
