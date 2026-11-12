"""Pila (LIFO) con nodos enlazados."""
from typing import Generic, TypeVar

from estructuras.nodo import Nodo

T = TypeVar("T")


class Pila(Generic[T]):
    """Pila: el último en entrar es el primero en salir."""

    def __init__(self):
        self._cima = None
        self._tamano = 0

    def apilar(self, dato: T):
        """Pone un dato en la cima."""
        
        nuevo = Nodo(dato)
        nuevo._siguiente = self._cima
        self._cima = nuevo
        self._tamano += 1

    def desapilar(self) -> T:
        """Quita y retorna la cima. Lanza error si está vacía."""
        
        if self._cima is None:
            return "La pila está vacía"
        dato = self._cima._dato
        self._cima = self._cima._siguiente
        self._tamano -= 1
        return dato

    def cima(self) -> T:
        """Retorna la cima sin quitarla. Lanza error si está vacía."""
        
        if self._cima is None:
            return "La pila está vacía"
        return self._cima._dato

    def esta_vacia(self):

        """True si no tiene elementos."""

        if self.cima is None:
            return True
        return False

