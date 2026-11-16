from enum import Enum
class EstadoPedido(Enum):
    En_espera = "En espera"
    Asignado = "Asignado"
    Entregado = "Entregado"
    Cancelado = "Cancelado"

class Nodo:
    def __init__ (self, dato):
        self.dato = dato
        self.siguiente = None

class Colas: 
    def __init__ (self):
        self.frente = None
        self.final = None

    def encolar (self, dato):
        nueva_persona = Nodo(dato)

        if self.final is None:
            self.frente = nueva_persona
            self.final = nueva_persona

        else:
            self.final.siguiente = nueva_persona
            self.final = nueva_persona
      
        print (f"{dato} ahora esta en la fila")

    def desencolar (self):
        if self.frente is None:
            return "la fila está vacía"

        atendido = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        print (f"{atendido} compro su boleto y salio de la fila") 
        return atendido

    def mostrar (self):
        elementos = []
        actual = self.frente
        while actual is not None:
            elementos.append (str(actual.dato))
            actual = actual.siguiente

        print ("estado de la fila" .join(elementos))

class pilas:
    def __init__ (self):
        self.cima = None

    def apilar (self, dato):
        nueva_caja = Nodo(dato)
        nueva_caja.siguiente = self.cima
        self.cima = nueva_caja
        
        print (f"se apilo {dato} en la cima")

    def desapilar (self):
        if self.cima is None:
            return "la pila esta vacia"
        cumbre  = self.cima.dato
        self.cima = self.cima.siguiente

        print (f"se quito {cumbre} de la pila")
        return cumbre
    def mostrar (self):
        elementos = []
        actual = self.cima
        while actual is not None:
            elementos.append (str(actual.dato))
            actual = actual.siguiente

        print ("estado de la pila" .join(elementos))

class Colaprioridad:
    
    def __init__(self):
        self.urgentes = Colas()
        self.normales = Colas()

    def encolar (self, dato, urgente=False):
    
       if urgente:
        self.urgentes.encolar(dato)
        print ("El pedido tiene prioridad urgente")
       else:
           self.normales.encolar(dato)
           print ("El pedido tiene prioridad Normal")

class Pedido:
    def __init__(self, id, codigo_cliente, descripcion, valor, barrio_destino,
                  urgente=False):
       self.id = id
       self.codigo_cliente = codigo_cliente
       self.descripcion = descripcion
       self.valor = valor
       self.barrio_destino = barrio_destino
       self.urgente = urgente
       self.estado = EstadoPedido.En_espera

    def cambiar_estado(self, nuevo_estado):
       self.estado = nuevo_estado
       