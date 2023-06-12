from inicioseccion import *
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
    print("hola")
else:
    print("Opcion no valida")


