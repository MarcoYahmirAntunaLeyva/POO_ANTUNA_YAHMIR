class Biblioteca:
    def __init__(self, nombre, ubicacion, num_libros, horario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_libros = num_libros
        self.horario = horario
        self.libros = []
        self.bibliotecarios = []
        self.secciones = []  

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
        print("Libros en", self.nombre, ":")
        for libro in self.libros:
            libro.mostrar_informacion()

    def agregar_bibliotecario(self, bibliotecario):
        self.bibliotecarios.append(bibliotecario)

    def mostrar_bibliotecarios(self):
        print("Bibliotecarios en", self.nombre, ":")
        for bibliotecario in self.bibliotecarios:
            bibliotecario.mostrar_informacion()

    def agregar_seccion(self, nombre, tipo):
        seccion = Seccion(nombre, tipo)
        self.secciones.append(seccion)

    def mostrar_secciones(self):
        print("Secciones en", self.nombre, ":")
        for seccion in self.secciones:
            seccion.mostrar_informacion()


# Agregación
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

# Asociación
class Bibliotecario:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.bibliotecas = []

    def asignar_a_biblioteca(self, biblioteca):
        if biblioteca not in self.bibliotecas:
            self.bibliotecas.append(biblioteca)
            biblioteca.agregar_bibliotecario(self)

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("ID Empleado:", self.id_empleado)

# Composición
class Seccion:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_informacion(self):
        print("Sección:", self.nombre)
        print("Tipo:", self.tipo)


biblio1 = Biblioteca("Biblioteca Central", "Calle Principal 123", 20000, "9:00 - 18:00")
biblio2 = Biblioteca("Biblioteca de Barrio", "Calle Secundaria 456", 5000, "10:00 - 17:00")
biblio3 = Biblioteca("Biblioteca Universitaria", "Campus Universitario", 100000, "8:00 - 20:00")


libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Realismo Mágico")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela")
libro3 = Libro("1984", "George Orwell", 1949, "Distopía")

biblio1.agregar_libro(libro1)
biblio1.agregar_libro(libro2)
biblio1.agregar_libro(libro3)


bibliotecario1 = Bibliotecario("Ana Pérez", 101)
bibliotecario2 = Bibliotecario("Juan Gómez", 102)


bibliotecario1.asignar_a_biblioteca(biblio1)
bibliotecario2.asignar_a_biblioteca(biblio2)


biblio1.agregar_seccion("Ficción", "Literatura")
biblio1.agregar_seccion("Ciencia", "Educación")


print(biblio1.nombre)
print(biblio2.ubicacion)
biblio1.abrir()
biblio1.mostrar_informacion()
biblio1.mostrar_libros()
biblio1.mostrar_bibliotecarios()
biblio1.mostrar_secciones()

bibliotecario1.mostrar_informacion()
bibliotecario2.mostrar_informacion()