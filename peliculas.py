import xml.etree.ElementTree as ET
from Listas import *


def cargar_peliculas_desde_xml():
    root = ET.parse('peliculas.xml')
    lista_categorias = ListaCategorias()
    etiquetas_categoria = root.findall('categoria')

    for etiqueta_categoria in etiquetas_categoria:
        nombre_categoria = etiqueta_categoria.find('nombre').text
        categoria = Categoria(nombre_categoria)
        etiquetas_pelicula = etiqueta_categoria.findall('.//pelicula')

        for etiqueta_pelicula in etiquetas_pelicula:
            titulo = etiqueta_pelicula.find('titulo').text
            director = etiqueta_pelicula.find('director').text
            anio = etiqueta_pelicula.find('anio').text
            fecha = etiqueta_pelicula.find('fecha').text
            hora = etiqueta_pelicula.find('hora').text
            pelicula = Pelicula(titulo, director, anio, fecha, hora)
            categoria.agregar_pelicula(pelicula)

        lista_categorias.agregar_categoria(categoria)

    return lista_categorias

def mostrar_listado_peliculas(lista_categorias):
    print("----- Listado de Películas -----")
    print("1. Listado general")
    print("2. Listado por categoría")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Listado general:")
        actual_categoria = lista_categorias.primera_categoria
        while actual_categoria is not None:
            print("Categoría:", actual_categoria.nombre)
            actual_pelicula = actual_categoria.primera_pelicula
            while actual_pelicula is not None:
                print("Título:", actual_pelicula.titulo)
                print("Director:", actual_pelicula.director)
                print("Año:", actual_pelicula.anio)
                print("Fecha:", actual_pelicula.fecha)
                print("Hora:", actual_pelicula.hora)
                print("-------------------------")
                actual_pelicula = actual_pelicula.siguiente
            actual_categoria = actual_categoria.siguiente_categoria

    elif opcion == '2':
        print("Listado por categoría:")
        actual_categoria = lista_categorias.primera_categoria
        while actual_categoria is not None:
            print("Categoría:", actual_categoria.nombre)
            actual_pelicula = actual_categoria.primera_pelicula
            while actual_pelicula is not None:
                print("Título:", actual_pelicula.titulo)
                print("Director:", actual_pelicula.director)
                print("Año:", actual_pelicula.anio)
                print("Fecha:", actual_pelicula.fecha)
                print("Hora:", actual_pelicula.hora)
                print("-------------------------")
                actual_pelicula = actual_pelicula.siguiente
            actual_categoria = actual_categoria.siguiente_categoria

def marcar_pelicula_favorita(lista_categorias):
    print("----- Marcar Película como Favorita -----")
    categoria_favorita = input("Ingrese la categoría de la película favorita: ")
    titulo_pelicula = input("Ingrese el título de la película favorita: ")

    actual_categoria = lista_categorias.primera_categoria
    while actual_categoria is not None:
        if actual_categoria.nombre.lower() == categoria_favorita.lower():
            actual_pelicula = actual_categoria.primera_pelicula
            while actual_pelicula is not None:
                if actual_pelicula.titulo.lower() == titulo_pelicula.lower():
                    print("¡Película marcada como favorita!")
                    
                    return
                actual_pelicula = actual_pelicula.siguiente
            break
        actual_categoria = actual_categoria.siguiente_categoria

    print("La película no se encontró en la categoría especificada.")


def comprar_boleto(lista_categorias, lista_boletos):
    print("----- Comprar Boleto -----")

    # Mostrar listado de películas disponibles
    mostrar_listado_peliculas(lista_categorias)

    # Solicitar al usuario que ingrese el nombre de la película
    nombre_pelicula = input("Ingrese el nombre de la película: ")

    # Buscar la película en la lista de categorías
    categoria, pelicula = ListaCategorias.buscar_pelicula_por_nombre(lista_categorias, nombre_pelicula)

    if pelicula is None:
        print("La película no se encuentra disponible.")
        return

    # Obtener los detalles de la película
    fecha_funcion = pelicula.fecha
    hora_funcion = pelicula.hora

    # Generar número de boleto en el formato #USACIPC2_Carnet_Incremental
    carnet = "201407049"
    numero_boleto_str = str(lista_boletos.longitud + 1).zfill(6)
    #numero_boleto_str = str(lista_boletos.longitud() + 1).zfill(6)
    numero_boleto_final = f"#USACIPC2_{carnet}_{numero_boleto_str}"

    # Crear un diccionario con los detalles de la compra
    boleto = {
        "numero_boleto": numero_boleto_final,
        "pelicula": nombre_pelicula,
        "fecha_funcion": fecha_funcion,
        "hora_funcion": hora_funcion
    }

    # Agregar el boleto a la lista de boletos
    lista_boletos.agregar_boleto(boleto)

    # Imprimir detalles de la compra
    print("----- Detalles de la compra -----")
    print("Número de boleto:", numero_boleto_final)
    print("Película:", nombre_pelicula)
    print("Fecha de función:", fecha_funcion)
    print("Hora de función:", hora_funcion)


def mostrar_historial_compras(lista_boletos):
    print("----- Historial de Compras -----")
    lista_boletos.imprimir_boletos()

def obtener_categoria_seleccionada(lista_categorias, categoria_seleccionada):
    actual_categoria = lista_categorias.primera_categoria
    while actual_categoria is not None:
        if actual_categoria.nombre == categoria_seleccionada:
            return actual_categoria
        actual_categoria = actual_categoria.siguiente_categoria
    return None

def obtener_pelicula_seleccionada(categoria, pelicula_seleccionada):
    actual_pelicula = categoria.primera_pelicula
    contador = 1
    while actual_pelicula is not None:
        if contador == pelicula_seleccionada:
            return actual_pelicula
        contador += 1
        actual_pelicula = actual_pelicula.siguiente
    return None

lista_categorias = cargar_peliculas_desde_xml()
lista_boletos = ListaBoletos()


lista_categorias = cargar_peliculas_desde_xml()
def menu():
    while True:
        print("----- MENU -----")
        print("1. Ver listado de películas")
        print("2. Marcar película como favorita")
        print("3. Comprar boletos")
        print("4. Mostrar historial de compras")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_listado_peliculas(lista_categorias)
        elif opcion == '2':
            marcar_pelicula_favorita(lista_categorias)
        elif opcion == '3':
            comprar_boleto(lista_categorias, lista_boletos)
        elif opcion == '4':
            mostrar_historial_compras(lista_boletos)
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")
