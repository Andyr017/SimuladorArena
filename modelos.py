from dataclasses import dataclass


@dataclass(frozen=True)
class Personaje:
    nombre: str
    vida: int
    vida_maxima: int
    ataque: int
    experiencia: int = 0


@dataclass(frozen=True)
class Enemigo:
    nombre: str
    vida: int
    vida_maxima: int
    ataque: int
    recompensa: int