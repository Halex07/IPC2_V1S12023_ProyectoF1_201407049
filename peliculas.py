import xml.etree.ElementTree as ET
import os  

def pelis():
    os.system ("clear") 
    treecl = ET.parse('peliculas.xml')
    rootcl = treecl.getroot() 
    for peliculas_xml in rootcl.findall('categoria'):
            categoria = peliculas_xml.find('nombre').text
        
    print("Categoria: "+categoria)
