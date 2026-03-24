import random
from abc import ABC, abstractmethod

class GameObject(ABC):

    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def obtener_reporte(self) -> str:
        pass

class Item(GameObject):

    def __init__(self, nombre: str, potencia: int, precio: int = 0):  # CORREGIDO
        super().__init__(nombre)  # CORREGIDO: super().__init__
        self.__potencia = potencia  # Atributo privado
        self.__precio = precio

    @property
    def potencia(self):
        return self.__potencia

    def obtener_reporte(self) -> str:
        return f"[ITEM] {self.nombre} (Poder: {self.potencia})"

class Actor(GameObject):
    def __init__(self, nombre: str, integridad: int):  # CORREGIDO
        super().__init__(nombre)  # CORREGIDO
        self._integridad = integridad

    def esta_vivo(self) -> bool:
        return self._integridad > 0

    @abstractmethod
    def obtener_reporte(self) -> str:
        pass

class Player(Actor):
    def __init__(self, nombre: str):  # CORREGIDO
        super().__init__(nombre, 100)  # CORREGIDO
        self.energia = 50
        self.bits = 0
        self.mochila: list[Item] = []

    def obtener_reporte(self) -> str:
        return f"🤖 {self.nombre} | ❤️ {self._integridad}% | ⚡ {self.energia} | 💰 {self.bits} Bits"


class Boss(Actor):
    def __init__(self, nombre: str, escudo: int):  # CORREGIDO
        super().__init__(nombre, 100)  # CORREGIDO
        self.escudo = escudo

    def recibir_danio(self, cantidad: int):
        self.escudo -= cantidad

    def obtener_reporte(self) -> str:
        return f"👾 {self.nombre} | 🛡️ Escudo: {self.escudo}"

class Engine:
    def __init__(self):
        self.jugador = Player("Admin_User")
        self.sectores = [
            {"nombre": "Kernel_Core", "dificultad": 25},
            {"nombre": "Firewall_Node", "dificultad": 50}
        ]
        self.jefe_final = Boss("GIGA_VIRUS", 100)
        self.nivel_actual = 0
        self.ejecutando = True

    def tienda(self):
        print("\n--- 🛒 TIENDA DE SISTEMA ---")
        parche_pro = Item("Parche_Ultra", 70, 50)
        print(f"1. Comprar {parche_pro.nombre} (50 Bits)")
        op = input("Seleccione: ")
        if op == "1" and self.jugador.bits >= 50:
            self.jugador.bits -= 50
            self.jugador.mochila.append(parche_pro)
            print("✅ Compra exitosa.")
        else:
            print("❌ Saldo insuficiente o cancelado.")

    def batalla_jefe(self):
        print(f"\n🔥 COMBATIENDO AL JEFE: {self.jefe_final.nombre}")
        if not self.jugador.mochila:
            print("⚠️ Sin herramientas. Recibes daño directo.")
            self.jugador._integridad -= 30
            return

        ataque = self.jugador.mochila.pop(0)
        self.jefe_final.recibir_danio(ataque.potencia)

        if self.jefe_final.escudo <= 0:
            print("✨ ¡SISTEMA RECUPERADO! HAS GANADO.")
            self.ejecutando = False
        else:
            print(f"🛡️ Escudo restante: {self.jefe_final.escudo}")
            self.jugador._integridad -= 20

    def jugar(self):
        print(">>> CORE-DUMP: SYSTEM RECOVERY INICIADO <<<")

        while self.ejecutando and self.jugador.esta_vivo():
            print(f"\n{self.jugador.obtener_reporte()}")
            print("\n📋 COMANDOS:")
            print("1. 🔍 Explorar (-10⚡)")
            print("2. 🛠️ Reparar sector")
            print("3. 🛒 Tienda")
            print("4. 🔋 Recargar (-20❤️ , +40⚡)")
            print("5. 👊 Combatir Jefe")
            print("6. ❌ Salir")

            try:
                op = input("\nSeleccione acción: ")

                if op == "1":
                    self.jugador.energia -= 10
                    if random.random() > 0.4:
                        bits = random.randint(20, 40)
                        self.jugador.bits += bits
                        print(f"💰 Bits encontrados: {bits}")
                    else:
                        print("👾 Error detectado: -15 Integridad")
                        self.jugador._integridad -= 15

                elif op == "2":
                    if self.nivel_actual < len(self.sectores) and self.jugador.mochila:
                        parche = self.jugador.mochila.pop(0)
                        if parche.potencia >= self.sectores[self.nivel_actual]["dificultad"]:
                            print(f"✨ Sector {self.sectores[self.nivel_actual]['nombre']} reparado.")
                            self.nivel_actual += 1
                        else:
                            print("❌ Potencia insuficiente.")
                    else:
                        print("🎒 Mochila vacía o sectores ya reparados.")

                elif op == "3":
                    self.tienda()

                elif op == "4":
                    self.jugador._integridad -= 20
                    self.jugador.energia += 40
                    print("🔋 Energía recargada.")

                elif op == "5":
                    self.batalla_jefe()

                elif op == "6":
                    self.ejecutando = False

            except Exception as e:
                print(f"⚠️ Error controlado: {e}")

        if not self.jugador.esta_vivo():
            print("\n💀 SISTEMA COLAPSADO. GAME OVER.")

