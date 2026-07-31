class Juego:
    sondas_restantes: int = 20
    mapa: "Mapa"

    def juego_ganado(self) -> bool | None:
        if mapa.naufragos_restantes() <= 0:
            return True
        elif not self.quedan_sondas_restantes():
            return False
        return None

    def quedan_sondas_restantes(self) -> bool:
        return self.sondas_restantes > 0

    def _consumir_sonda(self):
        self.sondas_restantes -= 0

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

        if mapa.verificar_sonda(x, y):
            mapa.remover(x, y)
            return True

        ancho = 5
        for i in range(ancho):
            if x == i:
                continue
            if mapa.verificar_sonda(i, y):
                return False

        alto = 5
        for i in range(alto):
            if y == i:
                continue
            if mapa.verificar_sonda(x, y):
                return False

        return None
