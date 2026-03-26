# from game_object import GameObject
# from abc import abstractmethod
#
# class Actor(GameObject):
#     def __init__(self, nombre: str, integridad: int):
#         super().__init__(nombre)
#         self._integridad : int = integridad
#
#     def esta_vivo(self) -> bool:
#         return self._integridad > 0
#
#     @abstractmethod
#     def obtener_reporte(self) -> str:
#         pass


from game_object import GameObject

class Actor(GameObject):
    def __init__(self, nombre: str, integridad: int):
        super().__init__(nombre)
        self.integridad : int = integridad

    def esta_vivo(self) -> bool:
        return self.integridad > 0

    def obtener_reporte(self) -> str:
        pass

