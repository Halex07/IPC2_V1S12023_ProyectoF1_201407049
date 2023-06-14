
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)


# Función para la operación matemática
def evaluar_operacion(operacion):
    # Eliminar espacios en blanco
    operacion = operacion.replace(" ", "")


    pila_operadores = Pila()
    cola_operandos = Cola()

    # Diccionario de prioridades de operadores
    prioridad = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Función para realizar una operación y actualizar la cola de operandos
    def realizar_operacion():
        operador = pila_operadores.desapilar()
        operand2 = cola_operandos.desencolar()
        operand1 = cola_operandos.desencolar()

        if operador == '+':
            resultado = operand1 + operand2
        elif operador == '-':
            resultado = operand1 - operand2
        elif operador == '*':
            resultado = operand1 * operand2
        elif operador == '/':
            resultado = operand1 / operand2

        cola_operandos.encolar(resultado)

    # Recorrer la operación
    i = 0
    while i < len(operacion):
        token = operacion[i]

        if token.isdigit():
            # Leer el número completo
            numero = token
            while i + 1 < len(operacion) and operacion[i + 1].isdigit():
                i += 1
                numero += operacion[i]
            cola_operandos.encolar(int(numero))
        elif token == '(':
            pila_operadores.apilar(token)
        elif token == ')':
            while not pila_operadores.esta_vacia() and pila_operadores.ver_tope() != '(':
                realizar_operacion()
            pila_operadores.desapilar() 
        else:  
            while not pila_operadores.esta_vacia() and pila_operadores.ver_tope() != '(' and prioridad[token] <= prioridad.get(pila_operadores.ver_tope(), 0):
                realizar_operacion()
            pila_operadores.apilar(token)

        i += 1

    
    while not pila_operadores.esta_vacia():
        realizar_operacion()

    
    return cola_operandos.desencolar()



operacion = input("Ingrese la operación matemática: ")
resultado = evaluar_operacion(operacion)
print("El resultado es:", resultado)
