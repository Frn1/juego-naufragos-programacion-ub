import random

import mapa


class Celda:
    # None cuando no paso ninguna sonda, False cuando la sonda pasó pero no empezó aca, True cuando la zona empezó ahí
    sonda_empezó_aca: None | bool = None
    # None si no habia un náufrago, False si el náufrago ya fue removido, True si el náufrago todavia sigue en el agua
    naufrago_en_agua: None | bool = None
    # None cuando no paso ninguna sonda, False si la sonda paso pero no detecto a nadie, True cuando la sonda detecto a alguien    naufrago_avistado: None | bool = None
    naufrago_avistado: None | bool = None

    def __str__(self) -> str:

        if self.naufrago_avistado == True:
            return "*"

        match self.naufrago_en_agua:
            case False:
                return "R"

        match self.sonda_empezó_aca:
            case True:
                return "x"
            case False:
                return "+"

        return "."


class Mapa:
    tamaño: int = 5

    def __init__(self, naufragos: int = 4, tamaño: int = 5):
        self.tamaño = tamaño
        if naufragos > self.tamaño * self.tamaño:
            raise ValueError(
                f"No puede haber mas de {self.tamaño * self.tamaño} naufragos"
            )
        self._crear_mapa_vacio()
        self._poner_naufragos(naufragos)

    def _crear_mapa_vacio(self):  # matriz solo 0
        self.mapa = [
            # Agregamos las celdas así, y no con * por que si no cada lista y cada Celda termina siendo el mismo objeto en lugar de objetos únicos
            [Celda() for columna in range(self.tamaño)]
            for fila in range(self.tamaño)
        ]

    def _poner_naufragos(self, cantidad):  # poner naufragos "1" randoms
        posiciones = random.sample(range(self.tamaño * self.tamaño), k=cantidad)
        for indice in posiciones:
            x = indice % self.tamaño  # columna
            y = indice // self.tamaño  # fila
            self.mapa[y][x].naufrago_en_agua = True

    def naufragos_restantes(self):
        cuenta = 0
        for fila in self.mapa:
            for celda in fila:
                if celda.naufrago_en_agua:
                    cuenta += 1
        return cuenta

    def verificar_sonda(self, x: int, y: int) -> bool:
        return self.mapa[y][x].naufrago_en_agua == True

    def rescatar_naufrago(self, x: int, y: int):
        self.mapa[y][x].naufrago_en_agua = False

    def marcar_camino_sonda(self, x: int, y: int):
        # Si es False o None
        if not self.mapa[y][x].sonda_empezó_aca:
            self.mapa[y][x].sonda_empezó_aca = False

    def marcar_intento_sonda(self, x: int, y: int):
        self.mapa[y][x].sonda_empezó_aca = True

    def marcar_avistamiento(self, x: int, y: int, detectado: bool):
        self.mapa[y][x].naufrago_avistado = detectado

    def limpiar_avistamientos(self):
        for fila in self.mapa:
            for celda in fila:
                celda.naufrago_avistado = None