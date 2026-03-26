# from abc import ABC, abstractmethod
#
# class GameObject(ABC):
#     def __init__(self, nombre: str):
#         self._nombre : str = nombre
#
#     @property
#     def nombre(self):
#         return self._nombre
#
#     @abstractmethod
#     def obtener_reporte(self) -> str:
#         pass
#

class GameObject:
    def __init__(self, nombre: str):
        self.nombre : str = nombre

    def obtener_reporte(self) -> str:
        pass