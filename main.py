from inicioseccion import *
from peliculas import *
import os


        
print('1. Iniciar Sesión')
print('2. Registrar Usuario')
print('3. Ver Listado de Peliculas')
menu = input()
if menu == '1':
    ruta = iniciar_sesion(usuarios)

elif menu == '2':
    print('registro')
elif menu == '3':
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
else:
    print("Opcion no valida")


