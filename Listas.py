class Pelicula:
    def __init__(self, titulo, director, anio, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.siguiente = None
        

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.primera_pelicula = None
        self.siguiente_categoria = None

    def agregar_pelicula(self, pelicula):
        if self.primera_pelicula is None:
            self.primera_pelicula = pelicula
        else:
            actual = self.primera_pelicula
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = pelicula

class ListaCategorias:
    def __init__(self):
        self.primera_categoria = None

    def agregar_categoria(self, categoria):
        if self.primera_categoria is None:
            self.primera_categoria = categoria
        else:
            actual = self.primera_categoria
            while actual.siguiente_categoria is not None:
                actual = actual.siguiente_categoria
            actual.siguiente_categoria = categoria

    def buscar_pelicula_por_nombre(self, nombre_pelicula):
        actual_categoria = self.primera_categoria
        while actual_categoria is not None:
            actual_pelicula = actual_categoria.primera_pelicula
            while actual_pelicula is not None:
                if actual_pelicula.titulo.lower() == nombre_pelicula.lower():
                    return actual_categoria, actual_pelicula
                actual_pelicula = actual_pelicula.siguiente
            actual_categoria = actual_categoria.siguiente_categoria

        # Si no se encontró la película, retornar None
        return None, None

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class NodoBoleto:
    def __init__(self, boleto):
        self.boleto = boleto
        self.siguiente = None
        
class ListaBoletos:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.longitud = 0  # Agregamos un atributo para almacenar la longitud de la lista

    def agregar_boleto(self, boleto):
        nuevo_nodo = NodoBoleto(boleto)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.longitud += 1  # Incrementamos la longitud al agregar un boleto

    def imprimir_boletos(self):
        actual = self.primero
        while actual is not None:
            print("Número de boleto:", actual.boleto["numero_boleto"])
            print("Película:", actual.boleto["pelicula"])
            print("Fecha y hora de función:", actual.boleto["fecha_funcion"], actual.boleto["hora_funcion"])
            print("---")
            actual = actual.siguiente