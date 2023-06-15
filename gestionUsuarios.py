import xml.etree.ElementTree as ET
import os


class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasena):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.siguiente = None


class ListaUsuarios:
    def __init__(self):
        self.cabeza = None

    def agregar_usuario(self, usuario):
        if self.cabeza is None:
            self.cabeza = usuario
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = usuario

    def leer_usuarios(self):
        actual = self.cabeza
        while actual is not None:
            print("Rol:", actual.rol)
            print("Nombre:", actual.nombre)
            print("Apellido:", actual.apellido)
            print("Teléfono:", actual.telefono)
            print("Correo:", actual.correo)
            print("Contraseña:", actual.contrasena)
            print("-------------------------")
            actual = actual.siguiente

    def buscar_usuario(self, correo):
        actual = self.cabeza
        while actual is not None:
            if actual.correo == correo:
                return actual
            actual = actual.siguiente
        return None

    def modificar_usuario(self, correo, nuevo_nombre):
        usuario = self.buscar_usuario(correo)
        if usuario is not None:
            usuario.nombre = nuevo_nombre

    def eliminar_usuario(self, correo):
        if self.cabeza is None:
            return

        if self.cabeza.correo == correo:
            self.cabeza = self.cabeza.siguiente
            return

        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.correo == correo:
                anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

    def generar_archivo_xml(self):
        usuarios_root = ET.Element("usuarios")

        actual = self.cabeza
        while actual is not None:
            usuario_elem = ET.SubElement(usuarios_root, "usuario")
            rol_elem = ET.SubElement(usuario_elem, "rol")
            rol_elem.text = actual.rol
            nombre_elem = ET.SubElement(usuario_elem, "nombre")
            nombre_elem.text = actual.nombre
            apellido_elem = ET.SubElement(usuario_elem, "apellido")
            apellido_elem.text = actual.apellido
            telefono_elem = ET.SubElement(usuario_elem, "telefono")
            telefono_elem.text = actual.telefono
            correo_elem = ET.SubElement(usuario_elem, "correo")
            correo_elem.text = actual.correo
            contrasena_elem = ET.SubElement(usuario_elem, "contrasena")
            contrasena_elem.text = actual.contrasena

            actual = actual.siguiente

        usuarios_tree = ET.ElementTree(usuarios_root)
        usuarios_tree.write("usuarios.xml")


# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    os.system("clear")
    print("----- MENÚ -----")
    print("1. Agregar usuario")
    print("2. Leer usuarios")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


# Función principal
def usr():
    lista_usuarios = ListaUsuarios()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            rol = input("Rol: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasena)
            lista_usuarios.agregar_usuario(usuario)
            lista_usuarios.generar_archivo_xml()

            print("Usuario agregado y archivo XML actualizado")

        elif opcion == "2":
            print('Lectura: ')
            lista_usuarios.leer_usuarios()

        elif opcion == "3":
            correo = input("Correo del usuario a modificar: ")
            nuevo_nombre = input("Nuevo nombre: ")

            lista_usuarios.modificar_usuario(correo, nuevo_nombre)
            lista_usuarios.generar_archivo_xml()

            print("Usuario modificado y archivo XML actualizado")

        elif opcion == "4":
            correo = input("Correo del usuario a eliminar: ")

            lista_usuarios.eliminar_usuario(correo)
            lista_usuarios.generar_archivo_xml()

            print("Usuario eliminado y archivo XML actualizado")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar la función principal
#usr()

