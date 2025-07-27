# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Estás desarrollando una parte básica del sistema de una biblioteca. Queremos permitir que un usuario pueda
pedir prestado un libro, siempre que haya stock. En caso de no haber stock disponible, se debe lanzar una
excepción clara que el sistema pueda capturar.

Consigna:
Implementa en Python las siguientes clases y funcionalidades:

    - Clase Libro con atributos titulo, autor y stock.
    - Clase Biblioteca con un método prestar_libro(titulo) que:
        - Verifique si hay stock del libro.
        - Reduzca el stock si hay ejemplares disponibles.
        - Lance una excepción LibroNoDisponibleError si no hay stock.

Captura la excepción e imprime un mensaje que indique el error al usuario.

Paso a paso:
    1- Crea la clase Libro con constructor e inicialización de atributos.
    2- Crea la clase LibroNoDisponibleError heredando de Exception.
    3- Define la clase Biblioteca con un diccionario de libros.
    4- Agrega el método prestar_libro(titulo) que:
        - Verifique si el libro está en el catálogo.
        - Verifique si hay stock.
        - Reste uno al stock si hay.
        - Lance la excepción si no hay stock.
        - Prueba el funcionamiento en un bloque try-except.
"""

# Se define la clase Libro
class Libro:
    def __init__(self, titulo, autor, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

# Se crea una clase para la Excepción
class LibroNoDisponibleError(Exception):
    pass

# Se define la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, libro):
        self.catalogo[libro.titulo] = libro

    def prestar_libro(self, titulo):
        if titulo not in self.catalogo:
            raise ValueError(f"El libro '{titulo}' no está incluido en este catálogo.")
        
        libro = self.catalogo[titulo]
        
        if libro.stock > 0:
            libro.stock -= 1
            print(f"Se ha prestado el libro: '{libro.titulo}' del autor {libro.autor}. El stock restante es: {libro.stock}")
        else:
            raise LibroNoDisponibleError(f"No hay stock disponible para el libro: '{titulo}'.")

# Programa principal
if __name__ == "__main__":
    # Se crean 2 libros.
    libro1 = Libro("La casa de los espíritus", "Isabel Allende", 4)
    libro2 = Libro("Sub Terra", "Baldomero Lillo", 0)

    # Se crea la biblioteca y se agregan los 2 libros.
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Se ejecuta el método para prestar distintos libros y se prueba el funcionamiento en un bloque try-except.
    try:
        biblioteca.prestar_libro("Sub Terra")
    except LibroNoDisponibleError as e:
        print(e)
    except ValueError as e:
        print(e)

    try:
        biblioteca.prestar_libro("La casa de los espíritus")
    except Exception as e:
        print(e)

    try:
        biblioteca.prestar_libro("Desolación")
    except Exception as e:
        print(e)