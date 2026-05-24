from dataclasses import dataclass
from interfaces import GameObject

@dataclass
class Sector:
    nombre: str
    dificultad: int

class Item(GameObject):
    def __init__(self, nombre: str, potencia: int, precio: int = 0):
        super().__init__(nombre)
        self.potencia: int = potencia
        self.precio: int = precio

    def obtener_reporte(self) -> str:
        return f"[ITEM] {self.nombre} (Poder: {self.potencia})"

