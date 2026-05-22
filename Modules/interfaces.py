from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

@runtime_checkable
class Reportable(Protocol):
    """Protocolo para cualquier objeto que deba generar un reporte textual."""
    def obtener_reporte(self) -> str:
        ...

class GameObject(ABC):
    """Clase abstracta base para todos los elementos del juego."""
    def __init__(self, nombre: str):
        self.nombre: str = nombre

    @abstractmethod
    def obtener_reporte(self) -> str:
        pass
