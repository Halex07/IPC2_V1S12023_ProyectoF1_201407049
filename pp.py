import xml.etree.ElementTree as ET
import os  

def pelis():
    os.system ("clear") 
    treecl = ET.parse('peliculas.xml')
    rootcl = treecl.getroot() 
    for peliculas_xml in rootcl.findall('categoria'):
            categoria = peliculas_xml.find('nombre').text
            #print(f"Categoria: {categoria.strip()}")
            pelicula = peliculas_xml.find('peliculas')

    for peli in pelicula.findall('pelicula'):
        titulo = peli.find('titulo').text
        #print('Titulo: '+titulo)
    for peliculass in peliculas_xml:
         print("Categoria: "+peliculass.categoria)

        
    
