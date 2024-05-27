promedio1 = float(input("Ingrese el primer promedio: "))
promedio2 = float(input("Ingrese el segundo promedio: "))
promedio3 = float(input("Ingrese el tercer promedio: "))

mayor = promedio1

if promedio2 > mayor:
  mayor = promedio2
elif promedio3 > mayor:
  mayor = promedio3

print(f"El mayor promedio es: {mayor}")
