from dataclasses import replace
from functools import reduce

from modelos import Personaje, Enemigo


def crear_multiplicador(factor: float):
    def multiplicar(valor: int) -> int:
        return int(valor * factor)

    return multiplicar


def calcular_danio(ataque: int, defensa: int) -> int:
    return max(1, ataque - defensa)


def recibir_danio(personaje: Personaje, danio: int) -> Personaje:
    nueva_vida = max(0, personaje.vida - danio)
    return replace(personaje, vida=nueva_vida)


def curar_personaje(personaje: Personaje, cantidad: int) -> Personaje:
    nueva_vida = min(
        personaje.vida_maxima,
        personaje.vida + cantidad
    )
    return replace(personaje, vida=nueva_vida)


def procesar_accion(
    accion: str,
    jugador: Personaje,
    enemigo: Enemigo
) -> tuple[Personaje, Enemigo, str]:

    match accion:
        case "atacar":
            nuevo_enemigo = replace(
                enemigo,
                vida=max(0, enemigo.vida - jugador.ataque)
            )

            mensaje = (
                f"{jugador.nombre} infligió {jugador.ataque} "
                f"puntos de daño a {enemigo.nombre}."
            )

            if nuevo_enemigo.vida == 0 and enemigo.vida > 0:
                jugador = replace(
                    jugador,
                    experiencia=jugador.experiencia + enemigo.recompensa
                )
                mensaje += (
                    f" ¡Enemigo derrotado! "
                    f"Ganaste {enemigo.recompensa} de experiencia."
                )

            return jugador, nuevo_enemigo, mensaje

        case "curar":
            nuevo_jugador = curar_personaje(jugador, 25)

            if nuevo_jugador.vida == jugador.vida:
                mensaje = "Tu vida ya está al máximo."
            else:
                mensaje = f"{jugador.nombre} recuperó vida."

            return nuevo_jugador, enemigo, mensaje

        case _:
            return jugador, enemigo, "Acción no reconocida."


def filtrar_enemigos_derrotados(
    enemigos: tuple[Enemigo, ...]
) -> tuple[Enemigo, ...]:
    return tuple(filter(lambda enemigo: enemigo.vida == 0, enemigos))


def calcular_experiencia_total(
    enemigos: tuple[Enemigo, ...]
) -> int:
    return reduce(
        lambda total, enemigo: total + enemigo.recompensa,
        enemigos,
        0
    )


def obtener_nombres_enemigos(
    enemigos: tuple[Enemigo, ...]
) -> list[str]:
    return list(map(lambda enemigo: enemigo.nombre, enemigos))


def calcular_ataque_especial(ataque: int) -> int:
    multiplicador = crear_multiplicador(1.5)
    return multiplicador(ataque)


def buscar_enemigo(
    nombre: str,
    enemigos: tuple[Enemigo, ...]
) -> Enemigo | None:
    return next(
        (enemigo for enemigo in enemigos if enemigo.nombre == nombre),
        None
    )


def procesar_accion_imperativa(
    accion: str,
    jugador: Personaje,
    enemigo: Enemigo
) -> tuple[Personaje, Enemigo, str]:

    if accion == "atacar":
        vida_restante = enemigo.vida - jugador.ataque

        if vida_restante < 0:
            vida_restante = 0

        nuevo_enemigo = replace(enemigo, vida=vida_restante)

        return (
            jugador,
            nuevo_enemigo,
            f"{jugador.nombre} atacó a {enemigo.nombre}."
        )

    if accion == "curar":
        vida_restante = jugador.vida + 25

        if vida_restante > jugador.vida_maxima:
            vida_restante = jugador.vida_maxima

        nuevo_jugador = replace(jugador, vida=vida_restante)

        return nuevo_jugador, enemigo, "El jugador se ha curado."

    return jugador, enemigo, "Acción no reconocida."