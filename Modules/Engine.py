import random
from models import Player, Boss, Sector, Item
from exceptions import (
    InsufficientEnergyError,
    InsufficientBitsError,
    EmptyInventoryError,
    LowIntegrityError,
    AllSectorsRepairedError
)


class Engine:
    def __init__(self):
        self.jugador = Player("Admin_User")
        self.sectores = [
            Sector("Kernel_Core", 25),
            Sector("Firewall_Node", 50)
        ]
        self.jefe_final = Boss(nombre="GIGA VIRUS", escudo=100)
        self.nivel_actual = 0
        self.ejecutando = True
        self.parche_pro = Item(nombre="Parche_Ultra", potencia=70, precio=35)

    def explorar(self) -> str:
        if self.jugador.energia < 5:
            raise InsufficientEnergyError("¡Energía insuficiente para explorar! (Mínimo 5).")

        self.jugador.energia -= 5
        if random.random() > 0.4:
            bits_encontrados = random.randint(20, 40)
            self.jugador.bits += bits_encontrados
            return f"Exploración exitosa. ¡Encontraste {bits_encontrados} Bits!"
        else:
            self.jugador.integridad -= 10
            return "¡Error de Sistema detectado! Perdiste 10 de Integridad."

    def comprar_parche(self) -> str:
        if self.jugador.bits < self.parche_pro.precio:
            raise InsufficientBitsError("Saldo insuficiente. Consigue más bits explorando.")

        self.jugador.bits -= self.parche_pro.precio
        self.jugador.morral.append(self.parche_pro)
        return f"Compra exitosa: {self.parche_pro.nombre} añadido al morral."

    def reparar_sector(self) -> str:
        if self.nivel_actual >= len(self.sectores):
            raise AllSectorsRepairedError("Todos los sectores ya han sido reparados con éxito.")
        if not self.jugador.morral:
            raise EmptyInventoryError("El morral está vacío. Compra un parche en la tienda.")

        parche = self.jugador.morral.pop(0)
        sector_actual = self.sectores[self.nivel_actual]

        if parche.potencia > sector_actual.dificultad:
            self.nivel_actual += 1
            return f"Sector [{sector_actual.nombre}] reparado exitosamente."
        else:
            return f"X El parche no tiene potencia suficiente para [{sector_actual.nombre}]."

    def recargar_sistema(self) -> str:
        if self.jugador.integridad <= 15:
            raise LowIntegrityError("Integridad demasiado baja para recargar de forma segura.")

        self.jugador.integridad -= 15
        self.jugador.energia += 40
        if self.jugador.energia > 100:
            self.jugador.energia = 100
        return "Energía recargada (+40 Energía, -15 Integridad)."

    def batalla_jefe(self) -> str:
        if not self.jugador.morral:
            self.jugador.integridad -= 20
            raise EmptyInventoryError("¡Sin herramientas en el morral! Recibiste 20 de daño directo del jefe.")

        ataque = self.jugador.morral.pop(0)
        self.jefe_final.recibir_danio(ataque.potencia)

        if self.jefe_final.escudo <= 0:
            self.ejecutando = False
            return "¡SISTEMA RECUPERADO! HAS ELIMINADO EL GIGA VIRUS. ¡GANASTE!"

        return f"Atacaste al jefe con {ataque.nombre}. Escudo restante del jefe: {self.jefe_final.escudo}."