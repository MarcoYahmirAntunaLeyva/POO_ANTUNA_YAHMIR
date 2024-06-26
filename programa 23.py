class Biblioteca:
    def __init__(self, nombre, ubicacion, num_libros, horario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_libros = num_libros
        self.horario = horario

    def abrir(self):
        print(self.nombre, "está abierta.")

    def cerrar(self):
        print(self.nombre, "está cerrada.")

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Número de libros:", self.num_libros)
        print("Horario:", self.horario)

biblio1 = Biblioteca("Biblioteca Central", "Calle Principal 123", 20000, "9:00 - 18:00")
biblio2 = Biblioteca("Biblioteca de Barrio", "Calle Secundaria 456", 5000, "10:00 - 17:00")
biblio3 = Biblioteca("Biblioteca Universitaria", "Campus Universitario", 100000, "8:00 - 20:00")

print(biblio1.nombre)
print(biblio2.ubicacion)
biblio1.abrir()
biblio1.mostrar_informacion()