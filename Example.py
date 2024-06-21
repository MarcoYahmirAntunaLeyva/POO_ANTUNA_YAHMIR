#Clase
class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre #Atributo
        self.raza = raza #Atributos
        self.edad = edad #Atributos
        
    def ladrar(self):
        print("GUAF")
        
    def comer(self):
        print("Comiendo...")
    
    def describir(self):
        print("Soy un perro llamado", self.nombre, "soy de raza", self.raza,"y tengo", self.edad, "años.")
        
        

class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        
    def añadir_perro(self, perro):
        self.perros.append(perro)
        print(perro.nombre, "añadido a la lista de perros de", self.nombre)
        
    def listar_perros(self):
        print(self.nombre, "tiene los siguientes perros")
        for perro in self.perros:
            print(perro.nombre)
    
    def pasear_perros(self):
        print(self.nombre, "esta paseando a sus perros: ")
        for perro in self.perros:
            perro.ladrar()

#Objetos

perro1 = Perro("Firualis", "Chihuahua", 3)
perro2 = Perro("Max", "Pitbull", 5)

#Usar atributos del objeto
print(perro1.nombre)
print(perro1.edad)
print(perro2.nombre, perro2.edad)

#Usar metodos de la clase para mis objetos
perro1.ladrar()
perro1.comer()

dueño = Dueño("Yahmir")

dueño.añadir_perro(perro1)
dueño.añadir_perro(perro2)

dueño.listar_perros()

dueño.pasear_perros()