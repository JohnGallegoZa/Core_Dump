# import random
# from item import Item
# from player import Player
# from boss import Boss
#
# class Engine:
#     def __init__(self):
#         self.jugador = Player("Admin_User")
#         self.sectores = [
#             {"nombre": "Kernel_Core", "dificultad": 25},
#             {"nombre": "Firewall_Node", "dificultad": 50}
#         ]
#         self.jefe_final = Boss("GIGA_VIRUS", 100)
#         self.nivel_actual : int  = 0
#         self.ejecutando = True
#
#     # ==========================================================
#     # FUNCIONALIDAD 1 (JOHN GALLEGO): SISTEMA DE ECONOMÍA (TIENDA)
#     # ==========================================================
#     def tienda(self):
#         print("\n TIENDA DE SISTEMA ")
#         parche_pro = Item("Parche_Ultra", 70, 35)
#         print(f"1. Comprar {parche_pro.nombre} (35 Bits)")
#         op = input("Seleccione: ")
#         if op == "1" and self.jugador.bits >= 35:
#             self.jugador.bits -= 35
#             self.jugador.morral.append(parche_pro) # SE USÓ MORRAL
#             print(" Compra exitosa.")
#         else:
#             print("Saldo insuficiente, debes conseguir mas bits")
#
#     # ==========================================================
#     # FUNCIONALIDAD 2 (SAMUEL MARROQUÍN): MECÁNICA DE COMBATE FINAL
#     # ==========================================================
#     def batalla_jefe(self):
#         print(f"\n COMBATIENDO AL JEFE: {self.jefe_final.nombre}")
#         if not self.jugador.morral: # SE USÓ MORRAL
#             print(" Sin herramientas. Recibiste daños directos.")
#             self.jugador._integridad -= 20
#             return
#
#         ataque = self.jugador.morral.pop(0) # SE USÓ MORRAL
#         self.jefe_final.recibir_danio(ataque.potencia)
#
#         if self.jefe_final.escudo <= 0:
#             print(" ¡SISTEMA RECUPERADO! HAS GANADO.")
#             self.ejecutando = False
#         else:
#             print(f" Escudo restante: {self.jefe_final.escudo}")
#             self.jugador._integridad -= 20
#
#     def jugar(self):
#         print(" CORE-DUMP: SYSTEM RECOVERY INICIADO ")
#
#         while self.ejecutando and self.jugador.esta_vivo():
#             print(f"\n{self.jugador.obtener_reporte()}")
#             print("\n COMANDOS:")
#             print("1. Explorar (-5 Energía)")
#             print("2. Reparar sector")
#             print("3. Tienda")
#             print("4. Recargar (-15 vida, +40 energía)")
#             print("5. Combatir Jefe")
#             print("6. Terminar juego")
#
#             try:
#                 op = input("\nSeleccione acción: ")
#
#                 # ==========================================================
#                 # FUNCIONALIDAD 3 (CAMILA PRADILLA): EXPLORACIÓN Y RECURSOS
#                 # ==========================================================
#                 if op == "1":
#                     self.jugador.energia -= 5
#                     if random.random() > 0.4:
#                         bits = random.randint(20, 40)
#                         self.jugador.bits += bits
#                         print(f" Bits encontrados: {bits}")
#                     else:
#                         print(" Error detectado: -10 Integridad")
#                         self.jugador._integridad -= 10
#
#                 elif op == "2":
#                     if self.nivel_actual < len(self.sectores) and self.jugador.morral: # SE USÓ MORRAL
#                         parche = self.jugador.morral.pop(0) # SE USÓ MORRAL
#                         if parche.potencia >= self.sectores[self.nivel_actual]["dificultad"]:
#                             print(f" Sector {self.sectores[self.nivel_actual]['nombre']} reparado.")
#                             self.nivel_actual += 1
#                         else:
#                             print(" Potencia insuficiente.")
#                     else:
#                         print(" Morral vacío o sectores ya reparados.") # SE CAMBIÓ TEXTO A MORRAL
#
#                 elif op == "3":
#                     self.tienda()
#
#                 elif op == "4":
#                     self.jugador._integridad -= 15
#                     self.jugador.energia += 40
#                     print(" Energía recargada.")
#
#                 elif op == "5":
#                     self.batalla_jefe()
#
#                 elif op == "6":
#                     self.ejecutando = False
#
#             except Exception as e:
#                 print(f" Error controlado: {e}")
#
#         if not self.jugador.esta_vivo():
#             print("\n SISTEMA COLAPSADO. PERDISTE EL JUEGO .")
#
# if __name__ == "__main__":
#     Engine().jugar()


import random
from item import Item
from player import Player
from boss import Boss

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
        print("\n TIENDA DE SISTEMA ")
        parche_pro = Item("Parche_Ultra", 70, 35)
        print(f"1. Comprar {parche_pro.nombre} (35 Bits)")
        op = input("Seleccione: ")
        if op == "1" and self.jugador.bits >= 35:
            self.jugador.bits -= 35
            self.jugador.morral.append(parche_pro)
            print(" Compra exitosa.")
        else:
            print("Saldo insuficiente, debes conseguir mas bits")

    def batalla_jefe(self):
        print(f"\n COMBATIENDO AL JEFE: {self.jefe_final.nombre}")
        if not self.jugador.morral:
            print(" Sin herramientas. Recibiste daños directos.")
            self.jugador.integridad -= 20
            return

        ataque = self.jugador.morral.pop(0)
        self.jefe_final.recibir_danio(ataque.potencia)

        if self.jefe_final.escudo <= 0:
            print(" ¡SISTEMA RECUPERADO! HAS GANADO.")
            self.ejecutando = False
        else:
            print(f" Escudo restante: {self.jefe_final.escudo}")
            self.jugador.integridad -= 20

    def jugar(self):
        print(" CORE-DUMP: SYSTEM INICIADO ")

        while self.ejecutando and self.jugador.esta_vivo():
            print(f"\n{self.jugador.obtener_reporte()}")
            print("\n COMANDOS:")
            print("1. Explorar (-5 Energía)")
            print("2. Reparar sector")
            print("3. Tienda")
            print("4. Recargar (-15 vida, +40 energía)")
            print("5. Combatir Jefe")
            print("6. Terminar juego")

            try:
                op = input("\nSeleccione acción: ")

                if op == "1":
                    self.jugador.energia -= 5
                    if random.random() > 0.4:
                        bits = random.randint(20, 40)
                        self.jugador.bits += bits
                        print(f" Bits encontrados: {bits}")
                    else:
                        print(" Error detectado: -10 Integridad")
                        self.jugador.integridad -= 10

                elif op == "2":
                    if self.nivel_actual < len(self.sectores) and self.jugador.morral:
                        parche = self.jugador.morral.pop(0)
                        if parche.potencia >= self.sectores[self.nivel_actual]["dificultad"]:
                            print(f" Sector {self.sectores[self.nivel_actual]['nombre']} reparado.")
                            self.nivel_actual += 1
                        else:
                            print(" Potencia insuficiente.")
                    else:
                        print(" Morral vacío o sectores ya reparados.")

                elif op == "3":
                    self.tienda()

                elif op == "4":
                    self.jugador.integridad -= 15
                    self.jugador.energia += 40
                    print(" Energía recargada.")

                elif op == "5":
                    self.batalla_jefe()

                elif op == "6":
                    self.ejecutando = False

            except Exception as e:
                print(f" Error controlado: {e}")

        if not self.jugador.esta_vivo():
            print("\n SISTEMA COLAPSADO. PERDISTE EL JUEGO .")

if __name__ == "__main__":
    Engine().jugar()