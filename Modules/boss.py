# from actor import Actor
#
# class Boss(Actor):
#     def __init__(self, nombre: str, escudo: int):
#         super().__init__(nombre, 100)
#         self.escudo : int = escudo
#
#     def recibir_danio(self, cantidad: int):
#         self.escudo -= cantidad
#
#     def obtener_reporte(self) -> str:
#         return f" {self.nombre} | Escudo: {self.escudo}"


from actor import Actor

class Boss(Actor):
    def __init__(self, nombre: str, escudo: int):
        super().__init__(nombre, 100)
        self.escudo : int = escudo

    def recibir_danio(self, cantidad: int):
        self.escudo -= cantidad

    def obtener_reporte(self) -> str:
        return f" {self.nombre} | Escudo: {self.escudo}"


