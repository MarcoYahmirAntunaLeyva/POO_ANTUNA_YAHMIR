def abstraccion():
    print("La abstracción es la capacidad de identificar y separar los conceptos y características generales de un objeto, proceso o situación, de sus detalles específicos.")
    
def encapsulacion():
    print("La encapsulación es la capacidad de ocultar o esconder detalles internosde un objeto o sistema, para que solo se puedan acceder a ellos a través de una interfaz pública bien definida.")
    
def herencia():
    print("La herencia es la capacidad de crear una nueva clase a partir de una clase existente, de modo que la nueva clase herede las propiedades y métodos de la clase original, y pueda agregar nuevas propiedades y métodos o sobreescribir los existentes.")
    
def polimorfismo():
    print("El polimorfismo es la capacidad de un objeto o método de tener diferentes formas o comportamientos en función del contexto en el que se utilice, de modo que se pueda utilizar de manera flexible y adaptable en diferentes situaciones.")
    
while True:
    x = input("¿Cual definicion desea conocer?\na)Abstraccion \nb)Encapsulamiento\nc)Herencia\nd)Polimorfismo\ne)salir\n: ")  
    match x:
          case "a":
                abstraccion()
          case "b":
                encapsulacion()
          case "c":
                herencia()
          case "d":
                polimorfismo()
          case "e":
               print("Hasta luego")
               break
          case _:
             print("Opción no válida. Por favor, ingrese una opción válida.")