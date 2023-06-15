import xml.etree.ElementTree as ET
import os

# Definición de clases
class Pelicula:
    def __init__(self, titulo, director, anio, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora

class NodoPelicula:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class PeliculasListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar(self, pelicula):
        nuevo_nodo = NodoPelicula(pelicula)

        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = self.ultimo
            self.primero.anterior = nuevo_nodo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def eliminar(self, pelicula):
        if self.esta_vacia():
            return

        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato == pelicula:
                if nodo_actual == self.primero:
                    self.primero = nodo_actual.siguiente
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
                elif nodo_actual == self.ultimo:
                    self.ultimo = nodo_actual.anterior
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
                else:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                break
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break

    def imprimir(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        nodo_actual = self.primero
        while nodo_actual:
            print("Título:", nodo_actual.dato.titulo)
            print("Director:", nodo_actual.dato.director)
            print("Año:", nodo_actual.dato.anio)
            print("Fecha:", nodo_actual.dato.fecha)
            print("Hora:", nodo_actual.dato.hora)
            print("")

            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break


# Funciones de manipulación del XML
def leer_xml():
    try:
        tree = ET.parse("peliculas.xml")
        return tree.getroot()
    except FileNotFoundError:
        print("El archivo XML no existe.")
        return None

def escribir_xml(root):
    tree = ET.ElementTree(root)
    tree.write("peliculas.xml", encoding="utf-8")

def agregar_pelicula_xml(root, categoria_nombre, titulo, director, anio, fecha, hora):
    categoria_element = ET.SubElement(root, "categoria")
    nombre_element = ET.SubElement(categoria_element, "nombre")
    nombre_element.text = categoria_nombre

    peliculas_element = ET.SubElement(categoria_element, "peliculas")
    pelicula_element = ET.SubElement(peliculas_element, "pelicula")

    titulo_element = ET.SubElement(pelicula_element, "titulo")
    titulo_element.text = titulo

    director_element = ET.SubElement(pelicula_element, "director")
    director_element.text = director

    anio_element = ET.SubElement(pelicula_element, "anio")
    anio_element.text = str(anio)

    fecha_element = ET.SubElement(pelicula_element, "fecha")
    fecha_element.text = fecha

    hora_element = ET.SubElement(pelicula_element, "hora")
    hora_element.text = hora

    escribir_xml(root)
    print("La película se ha agregado al XML.")


# Funciones del menú
def mostrar_menu():
    os.system ("clear") 
    print("----- MENÚ -----")
    print("1. Agregar película")
    print("2. Modificar película")
    print("3. Eliminar película")
    print("4. Imprimir lista de películas")
    print("5. Salir")

def ejecutar_menu(): 
    peliculas_lista = PeliculasListaCircular()
    xml_root = leer_xml()

    if xml_root is None:
        return

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            os.system ("clear") 
            categoria_nombre = input("Ingrese el nombre de la categoría: ")
            titulo = input("Ingrese el título de la película: ")
            director = input("Ingrese el director de la película: ")
            anio = int(input("Ingrese el año de la película: "))
            fecha = input("Ingrese la fecha de la película (formato: YYYY-MM-DD): ")
            hora = input("Ingrese la hora de la película: ")

            pelicula = Pelicula(titulo, director, anio, fecha, hora)
            peliculas_lista.agregar(pelicula)
            agregar_pelicula_xml(xml_root, categoria_nombre, titulo, director, anio, fecha, hora)

            print("La película se ha agregado correctamente.")

        elif opcion == "2":
            print("Funcionalidad en desarrollo.")

        elif opcion == "3":
            titulo = input("Ingrese el título de la película a eliminar: ")

            peliculas_lista.eliminar(titulo)
            print("La película se ha eliminado correctamente.")

        elif opcion == "4":
            peliculas_lista.imprimir()

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Ejecución del programa
#ejecutar_menu()
