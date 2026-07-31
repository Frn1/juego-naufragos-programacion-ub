from juego import Juego


def input_int(
    mensaje: str,
    mensaje_error: str = "Eso no es un valor válido, por favor vuelve a intentar.",
    valores_validos: None | range = None,
) -> int:
    while True:
        entrada = input(mensaje)
        if not entrada.isnumeric():
            print(mensaje_error)
            continue
        entrada_int = int(entrada)
        if valores_validos is not None and entrada_int not in valores_validos:
            print(mensaje_error)
            continue
        return entrada_int


def imprimit_numeros_horizontales(juego: Juego):
    print("  ", end="")
    for x in range(juego.mapa.tamaño):
        print(f"{x: >2}", end="")
    print()


def imprimir_pared_horizontal(juego: Juego):
    print("  +", end="")
    for x in range(juego.mapa.tamaño):
        print("--", end="")
    print("+")


def imprimir_filas(juego: Juego):
    for y in range(juego.mapa.tamaño):
        print(f"{y: >2}|", end="")
        for celda in juego.mapa.mapa[y]:
            print(f"{celda} ", end="")
        print("|")


def imprimir_tablero(juego: Juego):
    imprimit_numeros_horizontales(juego)
    imprimir_pared_horizontal(juego)
    imprimir_filas(juego)
    imprimir_pared_horizontal(juego)


if __name__ == "__main__":
    juego = Juego(naufragos=1)
    while (ganó := juego.juego_ganado()) is None:
        imprimir_tablero(juego)

        naufragos_restantes = juego.mapa.naufragos_restantes()
        print(
            f"Te quedan {juego.sondas_restantes} sonda{'' if juego.sondas_restantes == 1 else 's'} y {naufragos_restantes} naufrago{'' if naufragos_restantes == 1 else 's'}"
        )

        pos_x = input_int("Introduce la posicion horizontal en el tablero de 0 a 4: ")
        pos_y = input_int("Introduce la posicion vertical en el tablero de 0 a 4: ")

        resultado_rescate = juego.intentar_rescate(pos_x, pos_y)
        if resultado_rescate:
            print("¡Encontraste y rescataste un náufrago!")
        elif resultado_rescate is not None:
            print("¡Se detectó al menos un náufrago en alguna direccion ortogonal!")
        else:
            print("No se detectó nada...")

    print("-" * 40)
    imprimir_tablero(juego)
    if ganó:
        print("No quedan más naufragos, ¡ganaste!")
    else:
        naufragos_restantes = juego.mapa.naufragos_restantes()
        print(
            f"Perdiste... Fallaste en rescatar {naufragos_restantes} naufrago{'' if naufragos_restantes == 1 else 's'}"
        )
