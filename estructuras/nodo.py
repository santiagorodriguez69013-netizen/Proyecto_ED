"""Nodos para las estructuras enlazadas."""
from typing import Generic, TypeVar

T = TypeVar("T")


class Nodo(Generic[T]):
    """Nodo con un dato y un enlace al siguiente nodo."""

    def __init__(self, dato: T):
        self._dato = dato
        self._siguiente = None


class NodoDoble(Generic[T]):
    """Nodo con enlace al siguiente y al anterior."""

    def __init__(self, dato: T):
        self._dato = dato
        self._siguiente = None
        self._anterior = None