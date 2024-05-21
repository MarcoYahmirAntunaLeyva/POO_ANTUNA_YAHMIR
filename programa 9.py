contraseña_correcta = "POO123"

while True:
    contraseña = input("Ingrese su contraseña: ")
    if contraseña == contraseña_correcta:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, Porfavor vuelva a ingresarla")