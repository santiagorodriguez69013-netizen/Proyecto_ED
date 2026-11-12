"""Cola (FIFO) con nodos enlazados."""
from typing import Generic, TypeVar

from estructuras.nodo import Nodo

T = TypeVar("T")


class Cola(Generic[T]):
    """Cola: el primero en entrar es el primero en salir."""

    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    def encolar(self, dato: T):
        """Agrega un dato al final de la cola."""
        
        nuevo = Nodo(dato)
        if self._final is None:
            self._frente = nuevo
        else:
            self._final._siguiente = nuevo
        self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        """Quita y retorna el primero. Lanza error si está vacía."""
    
        if self._frente is None:
            return ("La cola está vacía")
        dato = self._frente._dato
        self._frente = self._frente._siguiente
        if self._frente is None:
            self._final = None
        self._tamano -= 1
        return dato

    def frente(self) -> T:
        """Retorna el primero sin quitarlo. Lanza error si está vacía."""
        
        if self._frente is None:
            return("La cola está vacía")
        return self._frente._dato

    def esta_vacia(self):
        """True si no tiene elementos."""
        if self.frente is None:
            return True
        return False
    