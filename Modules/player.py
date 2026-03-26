# from actor import Actor
# from item import Item
#
# class Player(Actor):
#     def __init__(self, nombre: str):
#         super().__init__(nombre, 100)
#         self.energia : int = 50
#         self.bits : int = 0
#         self.morral: list[Item] = [] # SE CAMBIÓ MOCHILA POR MORRAL
#
#     def obtener_reporte(self) -> str:
#         return f" {self.nombre} |  {self._integridad} % Integridad |  {self.energia}  Energía |  {self.bits} Bits"


from actor import Actor
from item import Item

class Player(Actor):
    def __init__(self, nombre: str):
        super().__init__(nombre, 100)
        self.energia : int = 50
        self.bits : int = 0
        self.morral : list[Item] = []

    def obtener_reporte(self) -> str:
        return f" {self.nombre} |  {self.integridad} % Integridad |  {self.energia}  Energía |  {self.bits} Bits"