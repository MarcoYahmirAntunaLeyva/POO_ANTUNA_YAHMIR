class Biblioteca:
    def __init__(self, nombre, ubicacion, num_libros, horario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_libros = num_libros
        self.horario = horario
        self.libros = []

    def abrir(self):
        print(self.nombre, "está abierta.")

    def cerrar(self):
        print(self.nombre, "está cerrada.")

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Número de libros:", self.num_libros)
        print("Horario:", self.horario)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.num_libros += 1

    def mostrar_libros(self):
        print("Libros en", self.nombre,":")
        for libro in self.libros:
            libro.mostrar_informacion()

#Asociación
class Libro:
    def __init__(self, titulo, autor, año_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año de Publicación:", self.año_publicacion)
        print("Género:", self.genero)


biblio1 = Biblioteca("Biblioteca Central", "Calle Principal 123", 20000, "9:00 - 18:00")
biblio2 = Biblioteca("Biblioteca de Barrio", "Calle Secundaria 456", 5000, "10:00 - 17:00")
biblio3 = Biblioteca("Biblioteca Universitaria", "Campus Universitario", 100000, "8:00 - 20:00")


libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Realismo Mágico")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela")
libro3 = Libro("1984", "George Orwell", 1949, "Distopía")


biblio1.agregar_libro(libro1)
biblio1.agregar_libro(libro2)
biblio1.agregar_libro(libro3)


print(biblio1.nombre)
print(biblio2.ubicacion)
biblio1.abrir()
biblio1.mostrar_informacion()
biblio1.mostrar_libros()