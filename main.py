import ttkbootstrap as ttk

from interfaz import ArenaApp


def main() -> None:
    ventana = ttk.Window(
        title="Arena Funcional",
        themename="darkly"
    )

    ArenaApp(ventana)

    ventana.mainloop()


if __name__ == "__main__":
    main()