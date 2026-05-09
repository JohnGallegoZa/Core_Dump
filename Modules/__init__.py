import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random

class BossBattleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("⚔️ BETA: Combate contra el Jefe – Derrota al Guardián Oscuro ⚔️")
        self.root.geometry("780x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        # --- Atributos del jugador ---
        self.player_max_hp = 100
        self.player_hp = 100
        self.player_attack_min = 15
        self.player_attack_max = 25

        # --- Atributos del jefe ---
        self.boss_max_hp = 220
        self.boss_hp = 220
        self.boss_attack_min = 12
        self.boss_attack_max = 20

        # --- Habilidades especiales ---
        self.special_uses = 3      # Golpe feroz
        self.heal_uses = 3         # Curaciones
        self.game_active = True

        # --- Configuración UI ---
        self.setup_ui()
        self.update_all()

    def setup_ui(self):
        # Estilos
        self.root.option_add("*Font", "Consolas 10")
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#1e1e2f")
        estilo.configure("TLabel", background="#1e1e2f", foreground="#f0f0f0")
        estilo.configure("TButton", font=("Consolas", 10, "bold"), padding=6)
        estilo.map("TButton",
                   background=[("active", "#3c6e47"), ("disabled", "#4a4a5a")],
                   foreground=[("active", "white"), ("disabled", "#a0a0a0")])

        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Panel izquierdo (Jefe y su arte) ---
        left_panel = ttk.Frame(main_frame, relief=tk.RIDGE, borderwidth=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Canvas para dibujo del jefe
        self.boss_canvas = tk.Canvas(left_panel, width=300, height=180, bg="#2a2a3a", highlightthickness=0)
        self.boss_canvas.pack(pady=15, padx=10)
        # Dibujar al jefe (estilo pixelart simple)
        self.boss_canvas.create_oval(70, 40, 230, 160, fill="#3a1f0a", outline="#b97f44", width=3)
        self.boss_canvas.create_text(150, 100, text="👾 GUARDIÁN\n   OSCURO", font=("Consolas", 16, "bold"), fill="#ffcc88", justify="center")
        self.boss_canvas.create_text(150, 150, text="💀 LVL. BOSS 💀", font=("Consolas", 9), fill="#dd6666")

        # Barra de vida del jefe
        ttk.Label(left_panel, text="VIDA DEL JEFE", font=("Consolas", 11, "bold"), foreground="#ffaa66").pack(pady=(10, 0))
        self.boss_hp_bar = ttk.Progressbar(left_panel, length=280, mode='determinate', style="TProgressbar")
        self.boss_hp_bar.pack(pady=5)
        self.boss_hp_label = ttk.Label(left_panel, text="", font=("Consolas", 10))
        self.boss_hp_label.pack()

        # --- Panel derecho (Jugador y acciones) ---
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Info del jugador
        player_frame = ttk.LabelFrame(right_panel, text="⚔️ HÉROE ⚔️", padding=10)
        player_frame.pack(fill=tk.X, pady=5)
        self.player_hp_bar = ttk.Progressbar(player_frame, length=300, mode='determinate', style="TProgressbar")
        self.player_hp_bar.pack(pady=5)
        self.player_hp_label = ttk.Label(player_frame, text="", font=("Consolas", 10))
        self.player_hp_label.pack()

        # Contadores de habilidades
        stats_frame = ttk.Frame(right_panel)
        stats_frame.pack(fill=tk.X, pady=10)
        self.special_label = ttk.Label(stats_frame, text="💢 Golpe Feroz: 3", font=("Consolas", 10, "bold"), foreground="#ffaa66")
        self.special_label.pack(side=tk.LEFT, padx=10)
        self.heal_label = ttk.Label(stats_frame, text="❤️ Curación: 3", font=("Consolas", 10, "bold"), foreground="#88ffaa")
        self.heal_label.pack(side=tk.RIGHT, padx=10)

        # Botones de combate
        button_frame = ttk.Frame(right_panel)
        button_frame.pack(pady=15)
        self.attack_btn = ttk.Button(button_frame, text="⚔️ ATAQUE NORMAL", command=self.player_attack, width=18)
        self.attack_btn.grid(row=0, column=0, padx=5, pady=5)
        self.special_btn = ttk.Button(button_frame, text="💢 GOLPE FEROZ", command=self.player_special, width=18)
        self.special_btn.grid(row=0, column=1, padx=5, pady=5)
        self.heal_btn = ttk.Button(button_frame, text="❤️ CURARSE", command=self.player_heal, width=18)
        self.heal_btn.grid(row=1, column=0, padx=5, pady=5)
        self.reset_btn = ttk.Button(button_frame, text="🔄 REINICIAR BATALLA", command=self.reset_game, width=38)
        self.reset_btn.grid(row=1, column=1, padx=5, pady=5)

        # Registro de combate (log)
        log_frame = ttk.LabelFrame(right_panel, text="📜 REGISTRO DE COMBATE", padding=5)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.log_area = scrolledtext.ScrolledText(log_frame, height=12, width=55, bg="#0a0a12", fg="#dddddd",
                                                   font=("Consolas", 9), wrap=tk.WORD, relief=tk.FLAT)
        self.log_area.pack(fill=tk.BOTH, expand=True)
        self.log_area.config(state=tk.DISABLED)

    # --- Actualización de la interfaz ---
    def update_all(self):
        # Actualizar barras de vida
        boss_percent = (self.boss_hp / self.boss_max_hp) * 100
        self.boss_hp_bar['value'] = boss_percent
        self.boss_hp_label.config(text=f"{self.boss_hp}/{self.boss_max_hp} HP")

        player_percent = (self.player_hp / self.player_max_hp) * 100
        self.player_hp_bar['value'] = player_percent
        self.player_hp_label.config(text=f"{self.player_hp}/{self.player_max_hp} HP")

        # Actualizar contadores y estado de botones
        self.special_label.config(text=f"💢 Golpe Feroz: {self.special_uses}")
        self.heal_label.config(text=f"❤️ Curación: {self.heal_uses}")

        if not self.game_active:
            self.attack_btn.config(state=tk.DISABLED)
            self.special_btn.config(state=tk.DISABLED)
            self.heal_btn.config(state=tk.DISABLED)
        else:
            self.attack_btn.config(state=tk.NORMAL)
            self.special_btn.config(state=tk.NORMAL if self.special_uses > 0 else tk.DISABLED)
            self.heal_btn.config(state=tk.NORMAL if self.heal_uses > 0 and self.player_hp < self.player_max_hp else tk.DISABLED)

    def add_log(self, message):
        """Añadir mensaje al registro de combate"""
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, f"> {message}\n")
        self.log_area.see(tk.END)
        self.log_area.config(state=tk.DISABLED)

    # --- Mecánicas del juego ---
    def boss_turn(self):
        """El jefe contraataca si sigue vivo y el juego activo"""
        if not self.game_active or self.boss_hp <= 0 or self.player_hp <= 0:
            return
        damage = random.randint(self.boss_attack_min, self.boss_attack_max)
        self.player_hp = max(0, self.player_hp - damage)
        self.add_log(f"😈 ¡El Guardián Oscuro te golpea por {damage} de daño!")
        self.update_all()
        if self.player_hp <= 0:
            self.game_active = False
            self.add_log("💀 ¡HAS SIDO DERROTADO! El jefe ruge victorioso... 💀")
            self.update_all()
            return
        self.update_all()

    def check_victory(self):
        """Comprobar si el jefe ha sido vencido"""
        if self.boss_hp <= 0:
            self.game_active = False
            self.add_log("✨ ¡VICTORIA! Derrotaste al Guardián Oscuro ✨")
            self.add_log("🏆 El pueblo te aclama como héroe. ¡Felicidades! 🏆")
            self.update_all()
            return True
        return False

    def player_attack(self):
        if not self.game_active:
            return
        # Ataque normal
        damage = random.randint(self.player_attack_min, self.player_attack_max)
        self.boss_hp = max(0, self.boss_hp - damage)
        self.add_log(f"⚔️ Atacas con fiereza y causas {damage} de daño al jefe.")
        self.update_all()
        if self.check_victory():
            return
        # Turno del jefe después del ataque (si sigue vivo)
        if self.game_active and self.boss_hp > 0 and self.player_hp > 0:
            self.boss_turn()
        self.update_all()

    def player_special(self):
        if not self.game_active:
            return
        if self.special_uses <= 0:
            self.add_log("❌ ¡No te queda energía para el Golpe Feroz! ❌")
            return
        damage = random.randint(30, 45)
        self.boss_hp = max(0, self.boss_hp - damage)
        self.special_uses -= 1
        self.add_log(f"💢 ¡GOLPE FEROZ! Asestas un devastador ataque de {damage} daño.")
        self.update_all()
        if self.check_victory():
            return
        if self.game_active and self.boss_hp > 0 and self.player_hp > 0:
            self.boss_turn()
        self.update_all()

    def player_heal(self):
        if not self.game_active:
            return
        if self.heal_uses <= 0:
            self.add_log("❌ ¡No te quedan curaciones! ❌")
            return
        if self.player_hp >= self.player_max_hp:
            self.add_log("❌ Ya tienes la vida al máximo. No puedes curarte ahora.")
            return
        heal_amount = random.randint(20, 30)
        self.player_hp = min(self.player_max_hp, self.player_hp + heal_amount)
        self.heal_uses -= 1
        self.add_log(f"❤️ Usas una poción y recuperas {heal_amount} puntos de vida.")
        self.update_all()
        # El jefe contraataca después de la curación
        if self.game_active and self.boss_hp > 0 and self.player_hp > 0:
            self.boss_turn()
        self.update_all()

    def reset_game(self):
        """Reiniciar completamente la batalla"""
        self.player_hp = self.player_max_hp
        self.boss_hp = self.boss_max_hp
        self.special_uses = 3
        self.heal_uses = 3
        self.game_active = True

        # Limpiar registro
        self.log_area.config(state=tk.NORMAL)
        self.log_area.delete(1.0, tk.END)
        self.log_area.config(state=tk.DISABLED)
        self.add_log("⚔️ ¡BATALLA REINICIADA! Enfréntate de nuevo al Guardián Oscuro ⚔️")
        self.update_all()
        # Efecto visual en el canvas del jefe (parpadeo)
        self.boss_canvas.itemconfig(1, fill="#3a1f0a")  # color restaurado

#
# --- Punto de entrada ----
if __name__ == "__main__":
    root = tk.Tk()
    game = BossBattleGame(root)
    root.mainloop()