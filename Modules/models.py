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

class Actor(GameObject):
    def __init__(self, nombre: str, integridad: int):
        super().__init__(nombre)
        self.integridad: int = integridad

    def esta_vivo(self) -> bool:
        return self.integridad > 0

    @abstractmethod
    def obtener_reporte(self) -> str:
        pass

class Player(Actor):
    def __init__(self, nombre: str):
        super().__init__(nombre, integridad=100)
        self.energia: int = 50
        self.bits: int = 0
        self.morral: list[Item] = []

    def obtener_reporte(self) -> str:
        return f"Jugador: {self.nombre} | Integridad: {self.integridad}% | Energía: {self.energia} | Bits: {self.bits}"

