import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

from modelos import Personaje, Enemigo
from logica import (
    procesar_accion,
    calcular_ataque_especial,
    filtrar_enemigos_derrotados,
    calcular_experiencia_total,
    buscar_enemigo,
    obtener_nombres_enemigos
)


class ArenaApp:

    def __init__(self, ventana: ttk.Window):
        self.ventana = ventana
        self.ventana.title("Arena Funcional")
        self.ventana.geometry("850x650")
        self.ventana.minsize(750, 580)

        self.jugador = Personaje(
            nombre="Guerrero",
            vida=100,
            vida_maxima=100,
            ataque=20
        )

        self.enemigos = (
            Enemigo("Goblin", 60, 60, 10, 20),
            Enemigo("Orco", 100, 100, 15, 35),
            Enemigo("Dragón", 150, 150, 25, 60)
        )

        self.enemigo_actual = self.enemigos[0]
        self.historial = []

        self.construir_interfaz()
        self.actualizar_interfaz()

    def construir_interfaz(self):
        principal = ttk.Frame(self.ventana, padding=20)
        principal.pack(fill="both", expand=True)

        ttk.Label(
            principal,
            text="ARENA FUNCIONAL",
            font=("Segoe UI", 22, "bold"),
            bootstyle="info"
        ).pack(pady=(0, 15))

        paneles = ttk.Frame(principal)
        paneles.pack(fill="x")

        panel_jugador = ttk.Labelframe(
            paneles,
            text="Jugador",
            padding=15,
            bootstyle="success"
        )
        panel_jugador.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        panel_enemigo = ttk.Labelframe(
            paneles,
            text="Enemigo",
            padding=15,
            bootstyle="danger"
        )
        panel_enemigo.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        self.lbl_jugador = ttk.Label(
            panel_jugador,
            font=("Segoe UI", 13, "bold")
        )
        self.lbl_jugador.pack(anchor="w", pady=5)

        self.barra_jugador = ttk.Progressbar(
            panel_jugador,
            maximum=100,
            bootstyle="success-striped"
        )
        self.barra_jugador.pack(fill="x", pady=8)

        self.lbl_experiencia = ttk.Label(panel_jugador)
        self.lbl_experiencia.pack(anchor="w")

        self.lbl_enemigo = ttk.Label(
            panel_enemigo,
            font=("Segoe UI", 13, "bold")
        )
        self.lbl_enemigo.pack(anchor="w", pady=5)

        self.barra_enemigo = ttk.Progressbar(
            panel_enemigo,
            maximum=100,
            bootstyle="danger-striped"
        )
        self.barra_enemigo.pack(fill="x", pady=8)

        self.lbl_ataque = ttk.Label(panel_enemigo)
        self.lbl_ataque.pack(anchor="w")

        ttk.Label(
            principal,
            text="Selecciona un enemigo",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", pady=(20, 5))

        self.seleccion_enemigo = ttk.Combobox(
            principal,
            state="readonly",
            values=obtener_nombres_enemigos(self.enemigos)
        )
        self.seleccion_enemigo.pack(fill="x")
        self.seleccion_enemigo.current(0)
        self.seleccion_enemigo.bind(
            "<<ComboboxSelected>>",
            self.seleccionar_enemigo
        )

        botones = ttk.Frame(principal)
        botones.pack(fill="x", pady=15)

        ttk.Button(
            botones,
            text="Atacar",
            bootstyle="danger",
            command=lambda: self.ejecutar_accion("atacar")
        ).pack(side="left", expand=True, fill="x", padx=4)

        ttk.Button(
            botones,
            text="Curarse",
            bootstyle="success",
            command=lambda: self.ejecutar_accion("curar")
        ).pack(side="left", expand=True, fill="x", padx=4)

        ttk.Button(
            botones,
            text="Ataque especial",
            bootstyle="warning",
            command=self.ejecutar_ataque_especial
        ).pack(side="left", expand=True, fill="x", padx=4)

        ttk.Button(
            botones,
            text="Estadísticas",
            bootstyle="info",
            command=self.mostrar_estadisticas
        ).pack(side="left", expand=True, fill="x", padx=4)

        ttk.Label(
            principal,
            text="Historial de combate",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w")

        self.texto_historial = tk.Text(
            principal,
            height=9,
            state="disabled",
            wrap="word",
            font=("Consolas", 10)
        )
        self.texto_historial.pack(fill="both", expand=True, pady=5)

        ttk.Button(
            principal,
            text="Limpiar historial",
            bootstyle="secondary",
            command=self.limpiar_historial
        ).pack(anchor="e", pady=5)

    def seleccionar_enemigo(self, evento=None):
        nombre = self.seleccion_enemigo.get()
        enemigo = buscar_enemigo(nombre, self.enemigos)

        if enemigo is not None:
            self.enemigo_actual = enemigo
            self.registrar_evento(
                f"Has seleccionado a {enemigo.nombre}."
            )
            self.actualizar_interfaz()

    def ejecutar_accion(self, accion: str):
        if self.jugador.vida <= 0:
            messagebox.showwarning(
                "Combate terminado",
                "Tu personaje ha sido derrotado."
            )
            return

        if self.enemigo_actual.vida <= 0:
            messagebox.showwarning(
                "Enemigo derrotado",
                "Selecciona otro enemigo para continuar."
            )
            return

        self.jugador, enemigo, mensaje = procesar_accion(
            accion,
            self.jugador,
            self.enemigo_actual
        )

        self.enemigo_actual = enemigo

        self.enemigos = tuple(
            enemigo if elemento.nombre == enemigo.nombre else elemento
            for elemento in self.enemigos
        )

        self.registrar_evento(mensaje)

        if accion == "atacar" and self.enemigo_actual.vida > 0:
            self.jugador = self._recibir_ataque_enemigo()

        self.actualizar_interfaz()

    def _recibir_ataque_enemigo(self) -> Personaje:
        from logica import recibir_danio

        nuevo_jugador = recibir_danio(
            self.jugador,
            self.enemigo_actual.ataque
        )

        self.registrar_evento(
            f"{self.enemigo_actual.nombre} contraatacó. "
            f"Daño recibido: {self.enemigo_actual.ataque}."
        )

        return nuevo_jugador

    def ejecutar_ataque_especial(self):
        if self.jugador.vida <= 0 or self.enemigo_actual.vida <= 0:
            messagebox.showwarning(
                "Combate no disponible",
                "Necesitas un personaje vivo y un enemigo activo."
            )
            return

        danio = calcular_ataque_especial(self.jugador.ataque)

        nuevo_enemigo = Enemigo(
            nombre=self.enemigo_actual.nombre,
            vida=max(0, self.enemigo_actual.vida - danio),
            vida_maxima=self.enemigo_actual.vida_maxima,
            ataque=self.enemigo_actual.ataque,
            recompensa=self.enemigo_actual.recompensa
        )

        if nuevo_enemigo.vida == 0:
            self.jugador = Personaje(
                nombre=self.jugador.nombre,
                vida=self.jugador.vida,
                vida_maxima=self.jugador.vida_maxima,
                ataque=self.jugador.ataque,
                experiencia=(
                    self.jugador.experiencia
                    + self.enemigo_actual.recompensa
                )
            )

        self.enemigo_actual = nuevo_enemigo

        self.enemigos = tuple(
            nuevo_enemigo if elemento.nombre == nuevo_enemigo.nombre
            else elemento
            for elemento in self.enemigos
        )

        self.registrar_evento(
            f"Ataque especial: {danio} puntos de daño."
        )

        if nuevo_enemigo.vida > 0:
            self.jugador = self._recibir_ataque_enemigo()

        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        self.lbl_jugador.config(
            text=f"{self.jugador.nombre}: {self.jugador.vida}/"
                 f"{self.jugador.vida_maxima} HP"
        )

        self.barra_jugador.configure(
            maximum=self.jugador.vida_maxima,
            value=self.jugador.vida
        )

        self.lbl_experiencia.config(
            text=f"Experiencia: {self.jugador.experiencia}"
        )

        self.lbl_enemigo.config(
            text=f"{self.enemigo_actual.nombre}: "
                 f"{self.enemigo_actual.vida}/"
                 f"{self.enemigo_actual.vida_maxima} HP"
        )

        self.barra_enemigo.configure(
            maximum=self.enemigo_actual.vida_maxima,
            value=self.enemigo_actual.vida
        )

        self.lbl_ataque.config(
            text=f"Ataque: {self.enemigo_actual.ataque}"
        )

    def registrar_evento(self, mensaje: str):
        self.historial.append(mensaje)

        self.texto_historial.configure(state="normal")
        self.texto_historial.insert("end", f"• {mensaje}\n")
        self.texto_historial.see("end")
        self.texto_historial.configure(state="disabled")

    def limpiar_historial(self):
        self.historial = []
        self.texto_historial.configure(state="normal")
        self.texto_historial.delete("1.0", "end")
        self.texto_historial.configure(state="disabled")

    def mostrar_estadisticas(self):
        derrotados = filtrar_enemigos_derrotados(self.enemigos)
        recompensas = calcular_experiencia_total(derrotados)

        mensaje = (
            f"Experiencia del jugador: {self.jugador.experiencia}\n"
            f"Enemigos derrotados: {len(derrotados)}\n"
            f"Recompensas disponibles entre derrotados: {recompensas}\n"
            f"Eventos registrados: {len(self.historial)}"
        )

        messagebox.showinfo("Estadísticas", mensaje)