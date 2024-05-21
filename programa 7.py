Kg = int(input("Ingrese los kilogramos que desea enviar: "))

if Kg <= 1:
    print("$50")
elif Kg  <= 5:
    print("$100")
elif Kg <= 10:
    print("$200")
elif Kg >= 10:
    print("$500")
else:
    print("No puede enviarse")