# from game_object import GameObject
#
# class Item(GameObject):
#     def __init__(self, nombre: str, potencia: int, precio: int = 0):
#         super().__init__(nombre)
#         self.__potencia : int  = potencia
#         self.__precio : int = precio
#
#     @property
#     def potencia(self):
#         return self.__potencia
#
#     def obtener_reporte(self) -> str:
#         return f"[ITEM] {self.nombre} (Poder: {self.potencia})"


from game_object import GameObject

class Item(GameObject):
    def __init__(self, nombre: str, potencia: int, precio: int = 0):
        super().__init__(nombre)
        self.potencia : int = potencia
        self.precio : int = precio

    def obtener_reporte(self) -> str:
        return f"[ITEM] {self.nombre} (Poder: {self.potencia})"

