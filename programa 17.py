while True:
  #menu
  print("\nMenú de conversión de temperatura:")
  print("1. Celsius a Fahrenheit")
  print("2. Fahrenheit a Celsius")
  print("3. Salir")

  opcion = input("Ingrese su opción: ")

  if opcion == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")
  elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}°F equivalen a {celsius:.2f}°C")
  elif opcion == "3":
    print("Saliendo del programa...")
    break
  else:
    print("Opción inválida. Intente nuevamente.")

