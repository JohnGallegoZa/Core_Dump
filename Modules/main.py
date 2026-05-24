import tkinter as tk
from tkinter import messagebox
from Engine import Engine
from exceptions import GameException


class CoreDumpGUI:
    def __init__(self, root):
        self.game = Engine()
        self.root = root

        self.root.title("Core-Dump: Advanced System Recovery")
        self.root.geometry("700x600")

        self.bg_dark = "#0a0f1d"
        self.bg_panel = "#111936"
        self.text_neon = "#00ffcc"
        self.text_alert = "#ff3366"
        self.text_gold = "#ffcc00"

        self.root.configure(bg=self.bg_dark)

        self.title_label = tk.Label(
            root, text="CORE-DUMP: SYSTEM RECOVERY",
            font=("Courier New", 16, "bold"), bg=self.bg_dark, fg=self.text_neon
        )
        self.title_label.pack(pady=12)

        self.status_frame = tk.LabelFrame(
            root, text="DIAGNÓSTICO EN TIEMPO REAL", font=("Courier New", 10, "bold"),
            bg=self.bg_panel, fg=self.text_neon, bd=2, relief="groove", padx=15, pady=10
        )
        self.status_frame.pack(fill="x", padx=20, pady=5)

        self.lbl_info_player = tk.Label(self.status_frame, text="", font=("Courier New", 11, "bold"), bg=self.bg_panel,
                                        fg="#ffffff")
        self.lbl_info_player.grid(row=0, column=0, columnspan=2, sticky="w", pady=2)

        tk.Label(self.status_frame, text="Integridad:", font=("Courier New", 10), bg=self.bg_panel, fg="#ffffff").grid(
            row=1, column=0, sticky="w")
        self.canvas_vida = tk.Canvas(self.status_frame, width=200, height=15, bg="#222", bd=0, highlightthickness=0)
        self.canvas_vida.grid(row=1, column=1, sticky="w", padx=10, pady=4)

        tk.Label(self.status_frame, text="Energía:", font=("Courier New", 10), bg=self.bg_panel, fg="#ffffff").grid(
            row=2, column=0, sticky="w")
        self.canvas_energia = tk.Canvas(self.status_frame, width=200, height=15, bg="#222", bd=0, highlightthickness=0)
        self.canvas_energia.grid(row=2, column=1, sticky="w", padx=10, pady=4)

        self.lbl_sector = tk.Label(self.status_frame, text="", font=("Courier New", 10, "italic"), bg=self.bg_panel,
                                   fg="#33ccff")
        self.lbl_sector.grid(row=3, column=0, columnspan=2, sticky="w", pady=4)

        self.lbl_boss = tk.Label(self.status_frame, text="", font=("Courier New", 11, "bold"), bg=self.bg_panel,
                                 fg=self.text_alert)
        self.lbl_boss.grid(row=4, column=0, columnspan=2, sticky="w", pady=2)

        self.txt_console = tk.Text(
            root, height=12, font=("Courier New", 11),
            bg="#050811", fg="#00ff66", wrap="word", state="disabled",
            bd=2, relief="solid", insertbackground="white"
        )
        self.txt_console.pack(fill="both", expand=True, padx=20, pady=10)

        self.btn_frame = tk.Frame(root, bg=self.bg_dark)
        self.btn_frame.pack(pady=15)

        self.crear_botones_estilizados()
        self.actualizar_pantalla()

        self.log_consola("[BOOT] Cargando subrutinas de recuperación...")
        self.log_consola("[READY] Sistema en línea. Destruye el malware antes de que colapse el núcleo.")

    def crear_botones_estilizados(self):
        acciones = [
            ("EXPLORAR RED (-5 En)", self.ejecutar_explorar, self.text_neon, self.bg_dark),
            ("COMPRAR PARCHE (35 Bits)", self.ejecutar_tienda, self.text_gold, self.bg_dark),
            ("REPARAR SECTOR", self.ejecutar_reparar, "#3399ff", "#ffffff"),
            ("INYECTAR ENERGIA (-15 Hp)", self.ejecutar_recargar, "#9933ff", "#ffffff"),
            ("PURGAR ENEMIGO (JEFE)", self.ejecutar_jefe, self.text_alert, "#ffffff")
        ]

        for i, (texto, comando, color_fg, color_bg_act) in enumerate(acciones):
            btn = tk.Button(
                self.btn_frame, text=texto, font=("Courier New", 9, "bold"),
                bg="#132342", fg=color_fg, activebackground=color_fg,
                activeforeground=color_bg_act, width=28, height=2, bd=2,
                relief="raised", cursor="hand2", command=comando
            )
            btn.grid(row=i // 2, column=i % 2, padx=8, pady=6)

    def log_consola(self, texto: str):
        self.txt_console.configure(state="normal")
        self.txt_console.insert(tk.END, texto + "\n")
        self.txt_console.see(tk.END)
        self.txt_console.configure(state="disabled")

    def dibujar_barra(self, canvas, valor_actual, valor_maximo, color_barra):
        canvas.delete("all")
        ancho_max = 200
        porcentaje = max(0.0, min(valor_actual / valor_maximo, 1.0))
        ancho_actual = ancho_max * porcentaje

        canvas.create_rectangle(0, 0, ancho_max, 15, fill="#1c1c1c", outline="")
        canvas.create_rectangle(0, 0, ancho_actual, 15, fill=color_barra, outline="")
        canvas.create_text(100, 7, text=f"{int(porcentaje * 100)}%", fill="#ffffff", font=("Courier New", 9, "bold"))

    def flash_pantalla(self, color_flash):
        original_bg = self.txt_console.cget("bg")
        self.txt_console.config(bg=color_flash)
        self.root.after(100, lambda: self.txt_console.config(bg=original_bg))

    def actualizar_pantalla(self):
        jugador = self.game.jugador
        jefe = self.game.jefe_final

        self.lbl_info_player.config(
            text=f"Usuario: {jugador.nombre} | Bits: {jugador.bits} | Inventario: [{len(jugador.morral)}] items")
        self.lbl_boss.config(text=jefe.obtener_reporte())

        color_vida = "#00ff66" if jugador.integridad > 40 else "#ff3366"
        self.dibujar_barra(self.canvas_vida, jugador.integridad, 100, color_vida)
        self.dibujar_barra(self.canvas_energia, jugador.energia, 100, "#33ccff")

        if self.game.nivel_actual < len(self.game.sectores):
            sec = self.game.sectores[self.game.nivel_actual]
            self.lbl_sector.config(text=f"SECTOR COMPROMETIDO: {sec.nombre} (Dificultad de cifrado: {sec.dificultad})")
        else:
            self.lbl_sector.config(text="TODOS LOS SECTORES REPARADOS. CORTAFUEGOS AL 100%. AISLANDO VIRUS...")

        if not jugador.esta_vivo():
            self.flash_pantalla("#ff0000")
            messagebox.showerror("CRITICAL COLLAPSE",
                                 "El sistema operativo sufrió un Kernel Panic masivo.\nPERDISTE EL JUEGO.")
            self.root.quit()

    def ejecutar_explorar(self):
        try:
            resultado = self.game.explorar()
            if "Error" in resultado:
                self.flash_pantalla("#441111")
            else:
                self.flash_pantalla("#113322")
            self.log_consola(resultado)
        except GameException as e:
            self.flash_pantalla("#441111")
            messagebox.showwarning("Advertencia de Red", str(e))
        finally:
            self.actualizar_pantalla()

    def ejecutar_tienda(self):
        try:
            resultado = self.game.comprar_parche()
            self.log_consola(resultado)
        except GameException as e:
            messagebox.showwarning("Error de Transacción", str(e))
        finally:
            self.actualizar_pantalla()

    def ejecutar_reparar(self):
        try:
            resultado = self.game.reparar_sector()
            self.flash_pantalla("#112244")
            self.log_consola(resultado)
        except GameException as e:
            messagebox.showwarning("Fallo de Desencriptación", str(e))
        finally:
            self.actualizar_pantalla()

    def ejecutar_recargar(self):
        try:
            resultado = self.game.recargar_sistema()
            self.log_consola(resultado)
        except GameException as e:
            self.flash_pantalla("#441111")
            messagebox.showwarning("Peligro de Sobrecarga", str(e))
        finally:
            self.actualizar_pantalla()

    def ejecutar_jefe(self):
        try:
            resultado = self.game.batalla_jefe()
            self.flash_pantalla("#ff3366")
            self.log_consola(resultado)
            if not self.game.ejecutando:
                messagebox.showinfo("VICTORIA DEL SISTEMA",
                                    "¡Felicidades Administrador!\nEl GIGA VIRUS fue purgado exitosamente del núcleo.")
                self.root.quit()
        except GameException as e:
            self.flash_pantalla("#441111")
            self.log_consola(f"[DAÑO DIRECTO] {str(e)}")
        finally:
            self.actualizar_pantalla()


if __name__ == "__main__":
    root = tk.Tk()
    app = CoreDumpGUI(root)
    root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# from Engine import Engine
# from models import Sector, Boss, Item
#
# class CoreDumpGUI:
#     def __init__(self, root):
#         self.game = Engine()
#         self.root = root
#         self.root.title(" Core-Dump: Advanced System Recovery ")
#         self.root.geometry("700x600")
#         self.root.configure(bg="#0a0f1d")
#
#
#         self.bg_dark = "#0a0f1d"
#         self.bg_panel = "#111936"
#         self.text_neon = "#00ffcc"
#         self.text_alert = "#ff3366"
#         self.text_gold = "#ffcc00"
#
#
#         self.title_label = tk.Label(
#             root, text=" CORE-DUMP: SYSTEM RECOVERY ",
#             font=("Courier New", 16, "bold"), bg=self.bg_dark, fg=self.text_neon
#         )
#         self.title_label.pack(pady=12)
#
#
#         self.status_frame = tk.LabelFrame(
#             root, text=" DIAGNÓSTICO EN TIEMPO REAL ", font=("Courier New", 10, "bold"),
#             bg=self.bg_panel, fg=self.text_neon, bd=2, relief="groove", padx=15, pady=10
#         )
#         self.status_frame.pack(fill="x", padx=20, pady=5)
#
#
#         self.lbl_info_player = tk.Label(self.status_frame, text="", font=("Courier New", 11, "bold"), bg=self.bg_panel, fg="#ffffff")
#         self.lbl_info_player.grid(row=0, column=0, columnspan=2, sticky="w", pady=2)
#
#
#         tk.Label(self.status_frame, text="Integridad:", font=("Courier New", 10), bg=self.bg_panel, fg="#ffffff").grid(row=1, column=0, sticky="w")
#         self.canvas_vida = tk.Canvas(self.status_frame, width=200, height=15, bg="#222", bd=0, highlightthickness=0)
#         self.canvas_vida.grid(row=1, column=1, sticky="w", padx=10, pady=4)
#
#         tk.Label(self.status_frame, text="Energía:", font=("Courier New", 10), bg=self.bg_panel, fg="#ffffff").grid(row=2, column=0, sticky="w")
#         self.canvas_energia = tk.Canvas(self.status_frame, width=200, height=15, bg="#222", bd=0, highlightthickness=0)
#         self.canvas_energia.grid(row=2, column=1, sticky="w", padx=10, pady=4)
#
#
#         self.lbl_sector = tk.Label(self.status_frame, text="", font=("Courier New", 10, "italic"), bg=self.bg_panel, fg="#33ccff")
#         self.lbl_sector.grid(row=3, column=0, columnspan=2, sticky="w", pady=4)
#
#         self.lbl_boss = tk.Label(self.status_frame, text="", font=("Courier New", 11, "bold"), bg=self.bg_panel, fg=self.text_alert)
#         self.lbl_boss.grid(row=4, column=0, columnspan=2, sticky="w", pady=2)
#
#
#         self.txt_console = tk.Text(
#             root, height=12, font=("Courier New", 10),
#             bg="#050811", fg="#00ff66", wrap="word", state="disabled",
#             bd=2, relief="solid", insertbackground="white"
#         )
#         self.txt_console.pack(fill="both", expand=True, padx=20, pady=10)
#
#
#         self.btn_frame = tk.Frame(root, bg=self.bg_dark)
#         self.btn_frame.pack(pady=15)
#
#         self.crear_botones_estilizados()
#         self.actualizar_pantalla()
#         self.log_consola("[BOOT] Cargando subrutinas de recuperación...")
#         self.log_consola("[READY] Sistema en línea. Destruye el malware antes de que colapse el núcleo.")
#
#     def crear_botones_estilizados(self):
#         acciones = [
#             ("EXPLORAR RED (-5 En)", self.ejecutar_explorar, "#00ffcc", "#0a0f1d"),
#             ("COMPRAR PARCHE (35 Bits)", self.ejecutar_tienda, "#ffcc00", "#0a0f1d"),
#             ("REPARAR SECTOR", self.ejecutar_reparar, "#3399ff", "#ffffff"),
#             ("INYECTAR ENERGÍA (-15 Hp)", self.ejecutar_recargar, "#9933ff", "#ffffff"),
#             ("PURGAR ENEMIGO (JEFE)", self.ejecutar_jefe, "#ff3366", "#ffffff"),
#         ]
#
#         for i, (texto, comando, color_fg, color_bg_act) in enumerate(acciones):
#             btn = tk.Button(
#                 self.btn_frame, text=texto, font=("Courier New", 10, "bold"),
#                 bg="#1a2342", fg=color_fg, activebackground=color_fg,
#                 activeforeground=color_bg_act, width=32, height=2, bd=2,
#                 relief="raised", cursor="hand2", command=comando
#             )
#
#             btn.grid(row=i // 2, column=i % 2, padx=8, pady=6)
#
#     def log_consola(self, texto: str):
#         self.txt_console.configure(state="normal")
#         self.txt_console.insert(tk.END, texto + "\n")
#         self.txt_console.see(tk.END)
#         self.txt_console.configure(state="disabled")
#
#     def dibujar_barra(self, canvas, valor_actual, valor_maximo, color_barra):
#         canvas.delete("all")
#         ancho_max = 200
#         porcentaje = max(0, min(valor_actual / valor_maximo, 1))
#         ancho_actual = ancho_max * porcentaje
#
#
#         canvas.create_rectangle(0, 0, ancho_max, 15, fill="#1c1c1c", outline="")
#
#         canvas.create_rectangle(0, 0, ancho_actual, 15, fill=color_barra, outline="")
#
#         canvas.create_text(100, 7, text=f"{int(porcentaje*100)}%", fill="#ffffff", font=("Courier New", 9, "bold"))
#
#     def flash_pantalla(self, color_flash):
#         original_bg = self.txt_console.cget("bg")
#         self.txt_console.config(bg=color_flash)
#         self.root.after(100, lambda: self.txt_console.config(bg=original_bg))
#
#     def actualizar_pantalla(self):
#         jugador = self.game.jugador
#         jefe = self.game.jefe_final
#
#         self.lbl_info_player.config(text=f"Usuario: {jugador.nombre}  |   Bits: {jugador.bits}  |   Inventario: {len(jugador.morral)} ítems")
#         self.lbl_boss.config(text=jefe.obtener_reporte())
#
#
#         color_vida = "#00ff66" if jugador.integridad > 40 else "#ff3336"
#         self.dibujar_barra(self.canvas_vida, jugador.integridad, 100, color_vida)
#         self.dibujar_barra(self.canvas_energia, jugador.energia, 100, "#00ccff")
#
#
#         if self.game.nivel_actual < len(self.game.sectores):
#             sec = self.game.sectores[self.game.nivel_actual]
#             self.lbl_sector.config(text=f" SECTOR COMPROMETIDO: {sec.nombre} (Dificultad de cifrado: {sec.dificultad})")
#         else:
#             self.lbl_sector.config(text=" ¡TODOS LOS SECTORES REPARADOS! CORTAFUEGOS AL 100%. AISLANDO VIRUS...")
#
#
#         if not jugador.esta_vivo():
#             self.flash_pantalla("#550000")
#             messagebox.showerror(" CRITICAL COLLAPSE ", "El sistema operativo sufrió un Kernel Panic masivo.\n¡PERDISTE EL JUEGO!")
#             self.root.quit()
#
#
#     def ejecutar_explorar(self):
#         resultado = self.game.explorar()
#         if "⚠️" in resultado:
#             self.flash_pantalla("#441111")
#         else:
#             self.flash_pantalla("#113322")
#         self.log_consola(resultado)
#         self.actualizar_pantalla()
#
#     def ejecutar_tienda(self):
#         resultado = self.game.comprar_parche()
#         self.log_consola(resultado)
#         self.actualizar_pantalla()
#
#     def ejecutar_reparar(self):
#         resultado = self.game.reparar_sector()
#         self.flash_pantalla("#112244")
#         self.log_consola(resultado)
#         self.actualizar_pantalla()
#
#     def ejecutar_recargar(self):
#         resultado = self.game.recargar_sistema()
#         self.log_consola(resultado)
#         self.actualizar_pantalla()
#
#     def ejecutar_jefe(self):
#         resultado = self.game.batalla_jefe()
#         self.flash_pantalla("#ff3366")
#         self.log_consola(resultado)
#         self.actualizar_pantalla()
#
#         if not self.game.ejecutando:
#             messagebox.showinfo(" VICTÓRIA DEL SISTEMA ", "¡Felicidades Administrador!\nEl GIGA_VIRUS fue purgado exitosamente del núcleo.")
#             self.root.quit()
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CoreDumpGUI(root)
#     root.mainloop()