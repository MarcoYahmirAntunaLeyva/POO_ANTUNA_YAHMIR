print("#Estructura basica")
def saludar():
    print("hola")
saludar()

print("#Parametros y arumentos")
def saludar(nombre):
    print("hola", nombre)
saludar("Yahmir")
    
print("#Valores de retorno")
def suma(a, b):
    suma = a + b
    return(suma)
resultado = suma(2, 3)
print("El resultado de la suma es: ",resultado)

print("#Parametros por defecto")
def suma(a=5, b=1):
    suma = a + b
    return(suma)
resultado = suma()
print("El resultado de la suma es: ",resultado)
   