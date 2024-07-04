class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ':', sep='')
        print('Fuerza:', self.fuerza)
        print('Inteligencia:', self.inteligencia)
        print('Defensa:', self.defensa)
        print('Vida:', self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, 'ha muerto')

    def usar_pocion(self):
        self.vida += 10
        print(f"{self.nombre} ha recuperado 10 puntos de vida. Vida actual: {self.vida}")

# Herencia
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma

    def atacar(self):
        print(f"{self.nombre} ataca con {self.arma}!")

# Asociación
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, personaje):
        self.miembros.append(personaje)
    
    def mostrar_miembros(self):
        print(f"Equipo {self.nombre}:")
        for miembro in self.miembros:
            print('-' * 20)
            miembro.atributos()

# Agregación
class Arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.danio = daño

class GuerreroConArma:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        self.personaje = Guerrero(nombre, fuerza, inteligencia, defensa, vida, arma)
        self.arma = arma

# Composición
class Escuadron:
    def __init__(self, nombre):
        self.nombre = nombre
        self.guerrero = Guerrero("Default", 10, 5, 5, 100, "Espada")
    
    def asignar_guerrero(self, guerrero):
        self.guerrero = guerrero
    
    def mostrar_escuadron(self):
        print(f"Escuadrón {self.nombre} compuesto por:")
        self.guerrero.atributos()

# Dependencia
class Batalla:
    def __init__(self, guerrero1, guerrero2):
        self.guerrero1 = guerrero1
        self.guerrero2 = guerrero2

    def iniciar_batalla(self):
        print(f"Batalla entre {self.guerrero1.nombre} y {self.guerrero2.nombre}")
        while self.guerrero1.esta_vivo() and self.guerrero2.esta_vivo():
            self.guerrero1.vida -= self.guerrero2.fuerza
            self.guerrero2.vida -= self.guerrero1.fuerza
            print(f"{self.guerrero1.nombre}: {self.guerrero1.vida} HP")
            print(f"{self.guerrero2.nombre}: {self.guerrero2.vida} HP")
        if self.guerrero1.esta_vivo():
            print(f"{self.guerrero1.nombre} gana la batalla!")
        else:
            print(f"{self.guerrero2.nombre} gana la batalla!")

# Clase con estructura de control y estructura de datos
class Inventario:
    def __init__(self):
        self.items = {"Poción": 0}

    def agregar_item(self, nombre, cantidad):
        if nombre in self.items:
            self.items[nombre] += cantidad
        else:
            self.items[nombre] = cantidad

    def usar_pocion(self):
        if self.items["Poción"] > 0:
            self.items["Poción"] -= 1
            return True
        else:
            print("No hay pociones disponibles.")
            return False

    def mostrar_inventario(self):
        for nombre, cantidad in self.items.items():
            print(f"{nombre}: {cantidad}")

# Crear objetos
personaje1 = Personaje("Ivan", 10, 5, 5, 100)
personaje2 = Personaje("Ernesto", 12, 3, 4, 90)
arma1 = Arma("Espada", 10)
arma2 = Arma("Arco", 7)
equipo = Equipo("Los DobleP")
escuadron = Escuadron("Alfa")
inventario = Inventario()

# Función para crear un personaje
def crear_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    fuerza = int(input("Ingrese la fuerza del personaje (0-10): "))
    inteligencia = int(input("Ingrese la inteligencia del personaje (0-10): "))
    defensa = int(input("Ingrese la defensa del personaje (0-10): "))
    vida = 100
    return Personaje(nombre, fuerza, inteligencia, defensa, vida)

# Menú interactivo
def menu():
    personajes = [personaje1, personaje2]
    while True:
        print("\nMenú:")
        print("1. Mostrar atributos de un personaje")
        print("2. Subir de nivel un personaje")
        print("3. Crear un nuevo personaje")
        print("4. Agregar miembro a un equipo")
        print("5. Mostrar miembros del equipo")
        print("6. Iniciar batalla")
        print("7. Agregar item al inventario")
        print("8. Mostrar inventario")
        print("9. Usar poción")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for i, p in enumerate(personajes):
                print(f"{i+1}. {p.nombre}")
            seleccion = int(input("Seleccione un personaje: ")) - 1
            personajes[seleccion].atributos()
        elif opcion == "2":
            for i, p in enumerate(personajes):
                print(f"{i+1}. {p.nombre}")
            seleccion = int(input("Seleccione un personaje: ")) - 1
            personajes[seleccion].subir_nivel(5, 3, 2)
            personajes[seleccion].atributos()
        elif opcion == "3":
            nuevo_personaje = crear_personaje()
            personajes.append(nuevo_personaje)
            print("Personaje creado exitosamente.")
        elif opcion == "4":
            for i, p in enumerate(personajes):
                print(f"{i+1}. {p.nombre}")
            seleccion = int(input("Seleccione un personaje para agregar al equipo: ")) - 1
            equipo.agregar_miembro(personajes[seleccion])
            equipo.mostrar_miembros()
        elif opcion == "5":
            equipo.mostrar_miembros()
        elif opcion == "6":
            for i, p in enumerate(personajes):
                print(f"{i+1}. {p.nombre}")
            seleccion1 = int(input("Seleccione el primer guerrero: ")) - 1
            seleccion2 = int(input("Seleccione el segundo guerrero: ")) - 1
            batalla = Batalla(personajes[seleccion1], personajes[seleccion2])
            batalla.iniciar_batalla()
        elif opcion == "7":
            inventario.agregar_item("Poción", 5)
            inventario.mostrar_inventario()
        elif opcion == "8":
            inventario.mostrar_inventario()
        elif opcion == "9":
            for i, p in enumerate(personajes):
                print(f"{i+1}. {p.nombre}")
            seleccion = int(input("Seleccione un personaje para usar la poción: ")) - 1
            if inventario.usar_pocion():
                personajes[seleccion].usar_pocion()
        elif opcion == "10":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()
