import xml.etree.ElementTree as ET
import os
from Listas import *
# Definición de clases y funciones

class Cine:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salas = ListaDoblementeEnlazada()


class Sala:
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos
        self.siguiente = None
        self.anterior = None

lista_salas = None  # Variable global para la lista de salas
ultimo_numero_sala = 0  # Variable global para el último número de sala

class Nodoc:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_final(self, dato):
        nuevo_nodo = Nodoc(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                if nodo_actual.anterior is None:
                    self.cabeza = nodo_actual.siguiente
                else:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente

                if nodo_actual.siguiente is None:
                    self.cola = nodo_actual.anterior
                else:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior

                return True

            nodo_actual = nodo_actual.siguiente

        return False

    def buscar(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                return nodo_actual

            nodo_actual = nodo_actual.siguiente

        return None

def leer_xml():
    if not os.path.exists("cines.xml"):
        crear_xml()
    
    try:
        tree = ET.parse("cines.xml")
        return tree.getroot()
    except ET.ParseError:
        print("Error al leer el archivo XML.")
        return None

def escribir_xml(xml_root):
    try:
        tree = ET.ElementTree(xml_root)
        tree.write("cines.xml")
        print("Se ha guardado el archivo XML correctamente.")
    except ET.ParseError:
        print("Error al escribir el archivo XML.")

def crear_xml():
    cine_element = ET.Element("cine")
    nombre_element = ET.Element("nombre")
    nombre_element.text = "Cine ABC"
    cine_element.append(nombre_element)
    salas_element = ET.Element("salas")
    cine_element.append(salas_element)
    xml_root = cine_element
    escribir_xml(xml_root)
    print("Se ha creado un nuevo archivo XML.")

def cargar_datos():
    global lista_salas
    global ultimo_numero_sala

    # Cargar datos desde el archivo XML
    try:
        xml_tree = ET.parse("cines.xml")
        xml_root = xml_tree.getroot()

        cines = xml_root.findall("cine")
        for cine in cines:
            nombre_cine = cine.find("nombre").text
            if nombre_cine == "Cine ABC":
                salas = cine.find("salas")
                for sala in salas.findall("sala"):
                    numero = sala.find("numero").text
                    asientos = sala.find("asientos").text
                    agregar_sala_lista(numero, asientos)

                    # Actualizar el contador de último número de sala
                    numero_sala = int(numero.split("_")[-1])
                    if numero_sala > ultimo_numero_sala:
                        ultimo_numero_sala = numero_sala

        print("Datos cargados desde el archivo XML.")

    except FileNotFoundError:
        print("El archivo XML no existe. Se creará uno nuevo.")

def ejecutar_menu_salas():
    while True:
        os.system ("clear") 
        print("\n=== GESTIÓN DE SALAS ===")
        print("1. Ver salas")
        print("2. Agregar sala")
        print("3. Modificar sala")
        print("4. Eliminar sala")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            imprimir_salas()
        elif opcion == "2":
            agregar_sala()
        elif opcion == "3":
            modificar_sala()
        elif opcion == "4":
            eliminar_sala()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")



def agregar_sala():
    global ultimo_numero_sala

    numero_asientos = input("Ingrese el número de asientos: ")

    # Generar el número de sala automáticamente
    numero_sala = f"#USACIPC2_201407049{ultimo_numero_sala + 1}"

    agregar_sala_lista(numero_sala, numero_asientos)

    # Actualizar el archivo XML
    xml_tree = ET.ElementTree()
    xml_root = None

    try:
        xml_tree = ET.parse("cines.xml")
        xml_root = xml_tree.getroot()
    except FileNotFoundError:
        xml_root = ET.Element("cines")
        xml_tree._setroot(xml_root)

    cine_xml = None

    for cine in xml_root.findall("cine"):
        cine_nombre = cine.find("nombre").text
        if cine_nombre == "Cine ABC":
            cine_xml = cine
            break

    if cine_xml is None:
        cine_xml = ET.Element("cine")
        nombre_xml = ET.SubElement(cine_xml, "nombre")
        nombre_xml.text = "Cine ABC"
        salas_xml = ET.SubElement(cine_xml, "salas")
        xml_root.append(cine_xml)
    else:
        salas_xml = cine_xml.find("salas")

    sala_xml = ET.Element("sala")
    numero_xml = ET.SubElement(sala_xml, "numero")
    numero_xml.text = numero_sala
    asientos_xml = ET.SubElement(sala_xml, "asientos")
    asientos_xml.text = numero_asientos

    salas_xml.append(sala_xml)

    xml_tree.write("cines.xml")

    print("XML actualizado con la nueva sala.")

    # Imprimir la lista de salas
    imprimir_salas()

def agregar_sala_lista(numero, asientos):
    global lista_salas
    global ultimo_numero_sala

    sala = Sala(numero, asientos)

    if lista_salas is None:
        lista_salas = sala
        lista_salas.siguiente = lista_salas
        lista_salas.anterior = lista_salas
    else:
        ultima_sala = lista_salas.anterior
        ultima_sala.siguiente = sala
        sala.anterior = ultima_sala
        sala.siguiente = lista_salas
        lista_salas.anterior = sala

    ultimo_numero_sala += 1

    print("Sala agregada con éxito.")



def imprimir_salas():
    global lista_salas

    if lista_salas is None:
        print("No hay salas registradas.")
        return

    sala_actual = lista_salas
    while True:
        print(f"Número de sala: {sala_actual.numero}")
        print(f"Número de asientos: {sala_actual.asientos}")
        print("-----------")

        sala_actual = sala_actual.siguiente
        if sala_actual == lista_salas:
            break

# Cargar datos desde el archivo XML
cargar_datos()

def modificar_sala():
    xml_root = leer_xml()
    if xml_root is None:
        return

    nombre_cine = xml_root.find(".//nombre").text
    print("Cine:", nombre_cine)

    numero_sala = input("Ingrese el número de la sala a modificar: ")

    sala = xml_root.find(".//sala[numero='" + numero_sala + "']")
    if sala is not None:
        nuevo_numero = input("Ingrese el nuevo número de la sala: ")
        nuevo_asientos = input("Ingrese la nueva cantidad de asientos: ")

        numero_element = sala.find("numero")
        numero_element.text = nuevo_numero
        asientos_element = sala.find("asientos")
        asientos_element.text = nuevo_asientos

        escribir_xml(xml_root)
        print("La sala se ha modificado correctamente.")
    else:
        print("No se encontró la sala especificada.")

def eliminar_sala():
    global lista_salas

    numero_sala = input("Ingrese el número de sala que desea eliminar: ")

    if lista_salas is None:
        print("No hay salas registradas.")
        return

    sala_actual = lista_salas
    sala_encontrada = False

    while True:
        if sala_actual.numero == numero_sala:
            sala_encontrada = True
            break

        sala_actual = sala_actual.siguiente
        if sala_actual == lista_salas:
            break

    if sala_encontrada:
        if sala_actual == lista_salas and lista_salas.siguiente == lista_salas:
            lista_salas = None
        else:
            sala_anterior = sala_actual.anterior
            sala_siguiente = sala_actual.siguiente
            sala_anterior.siguiente = sala_siguiente
            sala_siguiente.anterior = sala_anterior

            if sala_actual == lista_salas:
                lista_salas = sala_siguiente

        print("Sala eliminada con éxito.")
    else:
        print("No se encontró la sala con ese número.")

    # Actualizar el XML
    xml_tree = ET.ElementTree()
    xml_root = None

    try:
        xml_tree = ET.parse("cines.xml")
        xml_root = xml_tree.getroot()
    except FileNotFoundError:
        print("No se encontró el archivo XML 'cines.xml'.")
        return

    cines = xml_root.findall("cine")
    for cine in cines:
        salas = cine.find("salas")
        salas_elementos = salas.findall("sala")
        for sala_element in salas_elementos:
            numero_element = sala_element.find("numero")
            numero = numero_element.text
            if numero == numero_sala:
                salas.remove(sala_element)
                break

    xml_tree.write("cines.xml")

    print("XML actualizado después de eliminar la sala.")

    # Imprimir la lista de salas actualizada
    imprimir_salas()


# Ejecución del programa
ejecutar_menu_salas()
