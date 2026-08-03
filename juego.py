from mapa import Mapa


class Juego:
    sondas_restantes: int = 20
    mapa: Mapa

    def __init__(self, sondas: int = 20, naufragos: int = 4, tamaño=5) -> None:
        self.sondas_restantes = sondas
        self.mapa = Mapa(naufragos=naufragos, tamaño=tamaño)

    def juego_ganado(self) -> bool | None:
        if self.mapa.naufragos_restantes() <= 0:
            return True
        elif not self.quedan_sondas_restantes():
            return False
        return None

    def quedan_sondas_restantes(self) -> bool:
        return self.sondas_restantes > 0

    def _consumir_sonda(self):
        self.sondas_restantes -= 1

    def intentar_rescate(self, x: int, y: int) -> bool | None:
        """
        Esta funcion lanza una sonda, consumiendola.
        Devuelve True si la sonda rescata a un naufrago, False si no rescata pero detecta uno, o None si no rescata ni detecta algo.
        """
        if x < 0 or x > 4:
            raise ValueError("Posicion invalida para x")
        if y < 0 or y > 4:
            raise ValueError("Posicion invalida para y")
        if not self.quedan_sondas_restantes():
            raise RuntimeError("No quedan más sondas")

        self._consumir_sonda()

        # Se encontró a un náufrago en esa posición. Lo rescatamos (removemos del mapa) y devolvemos True.
        if self.mapa.verificar_sonda(x, y):
            self.mapa.rescatar_naufrago(x, y)
            return True
        else:
            self.mapa.marcar_intento_sonda(x, y)

        naufrago_detectado = False
        # Buscamos naufragos con esa misma posicion vertical pero diferente pos. horizontal, y si hay uno, luego devolvemos False.
        ancho = 5
        for i in range(ancho):
            if x == i:
                continue
            if not naufrago_detectado and self.mapa.verificar_sonda(i, y):
                naufrago_detectado = True
            self.mapa.marcar_camino_sonda(i, y)
        # Buscamos naufragos con esa misma posicion horizontal pero diferente pos. vertical, y si hay uno, luego devolvemos false.
        alto = 5
        for i in range(alto):
            if y == i:
                continue
            if not naufrago_detectado and self.mapa.verificar_sonda(x, i):
                naufrago_detectado = True
            self.mapa.marcar_camino_sonda(x, i)

        if naufrago_detectado:
            self.mapa.marcar_avistamiento(x, y)
            return False

        return None
