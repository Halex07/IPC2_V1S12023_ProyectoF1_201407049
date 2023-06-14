import xml.etree.ElementTree as ET
import os 
from peliculas import *
from Listas import *

# Definir la clase para el nodo de la lista enlazada
class NodoUsuario:
    def __init__(self, nombre, contrasena, rol):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol
        self.siguiente = None

# Definir la clase para la lista enlazada
class ListaUsuarios:
    def __init__(self):
        self.cabeza = None

    def agregar_usuario(self, nombre, contrasena, rol):
        nuevo_usuario = NodoUsuario(nombre, contrasena, rol)
        if self.cabeza is None:
            self.cabeza = nuevo_usuario
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_usuario

    def buscar_usuario(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

def iniciar_sesion(lista_usuarios):
    os.system ("clear") 
    # Solicitar nombre de usuario y contraseña al usuario
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Buscar el usuario en la lista enlazada
    usuario_encontrado = lista_usuarios.buscar_usuario(usuario)

    if usuario_encontrado and usuario_encontrado.contrasena == contrasena:
        os.system ("clear") 
        print(f"Inicio de sesión exitoso. Rol: {usuario_encontrado.rol}")
        # Imprimir el menú correspondiente según el rol
        
        if usuario_encontrado.rol == 'administrador': 
            mostrar_menu_admin()
        elif usuario_encontrado.rol == 'cliente':
            mostrar_menu_client()
        else:
            print("Rol no reconocido.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def mostrar_menu_admin():
    print("Bienvenido " )
    print("1. Gestionar usuarios")
    print("2. Gestionar Categorías y películas ")
    print("3. Gestionar Salas")
    print("4. Gestionar boletos comprados")
    print("5. Salir")
    menua = input()
    

def mostrar_menu_client():
    menu()
        
      





# Crear una instancia de la lista enlazada
usuarios = ListaUsuarios()

# Leer el archivo XML y almacenar la información en la lista enlazada
tree = ET.parse('users.xml')
root = tree.getroot()

for usuario_xml in root.findall('usuario'):
    nombre = usuario_xml.find('nombre').text
    contrasena = usuario_xml.find('contrasena').text
    rol = usuario_xml.find('rol').text
    usuarios.agregar_usuario(nombre, contrasena, rol)

# Llamar a la función para iniciar sesión
#iniciar_sesion(usuarios)
