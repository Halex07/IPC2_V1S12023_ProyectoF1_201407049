from Listas import *  
import xml.etree.ElementTree as ET

# Resto del código...

def principal():
    

# Función para cargar los datos del archivo XML
    def cargar_datos():
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

# Función para mostrar el listado de películas
    def mostrar_listado_peliculas(lista_categorias):
        opcion = input("Seleccione una opción:\n1. Listado general\n2. Listado por categoría\n")

        if opcion == '1':
            print("Listado general de películas:")
            categoria_actual = lista_categorias.primera_categoria
            while categoria_actual is not None:
                print(f"Categoría: {categoria_actual.nombre}")
                pelicula_actual = categoria_actual.primera_pelicula
                while pelicula_actual is not None:
                    print(f"Título: {pelicula_actual.titulo}")
                    print(f"Fecha: {pelicula_actual.fecha}")
                    print(f"Hora: {pelicula_actual.hora}")
                    print()
                    pelicula_actual = pelicula_actual.siguiente
                categoria_actual = categoria_actual.siguiente
        elif opcion == '2':
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
            pelicula_actual = lista_categorias.obtener_peliculas_por_categoria(nombre_categoria)
            if pelicula_actual is not None:
                print(f"Listado de películas de la categoría '{nombre_categoria}':")
                while pelicula_actual is not None:
                    print(f"Título: {pelicula_actual.titulo}")
                    print(f"Fecha: {pelicula_actual.fecha}")
                    print(f"Hora: {pelicula_actual.hora}")
                    print()
                    pelicula_actual = pelicula_actual.siguiente
            else:
                print(f"No se encontraron películas en la categoría '{nombre_categoria}'")
        else:
            print("Opción inválida.")

# Función para marcar una película como favorita
    def marcar_como_favorita(pelicula):
        pelicula.favorita = True

# Función para mostrar el listado de películas favoritas
    def mostrar_listado_peliculas_favoritas(lista_categorias):
        print("Listado de películas favoritas:")
        categoria_actual = lista_categorias.primera_categoria
        while categoria_actual is not None:
            pelicula_actual = categoria_actual.primera_pelicula
            while pelicula_actual is not None:
                if getattr(pelicula_actual, "favorita", False):
                    print(f"Título: {pelicula_actual.titulo}")
                    print(f"Fecha: {pelicula_actual.fecha}")
                    print(f"Hora: {pelicula_actual.hora}")
                    print()
                pelicula_actual = pelicula_actual.siguiente
            categoria_actual = categoria_actual.siguiente

# Cargar los datos del archivo XML
    lista_categorias = cargar_datos()

