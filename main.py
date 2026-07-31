from juego import Juego

def input_int(mensaje: str, mensaje_error: str = "Eso no es un valor válido, por favor vuelve a intentar.", valores_validos: None | range = None) -> int:
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


if __name__ == "__main__":
    juego = Juego()
    while (ganó := juego.juego_ganado()) is None:
        print("(TODO: Tablero)")

        print()
        print(f"Te quedan {juego.sondas_restantes} sonda{'s' if juego.sondas_restantes == 1 else ''}")

        pos_x = input_int("Introduce la posicion horizontal en el tablero de 0 a 4: ")
        pos_y = input_int("Introduce la posicion vertical en el tablero de 0 a 4: ")

        resultado_rescate = juego.intentar_rescate(pos_x, pos_y)
        if resultado_rescate:
            print("¡Encontraste y rescataste un náufrago!")
        elif resultado_rescate is not None:
            print("¡Se detectó al menos un náufrago en alguna direccion ortogonal!")
        else:
            print("No se detectó nada...")
    if ganó:
        print("¡Ganaste! Muy bien")
    else:
        naufragos_restantes = juego.mapa.naufragos_restantes()
        print(f"Perdiste... Fallaste en rescatar {naufragos_restantes} naufrago{'s' if naufragos_restantes == 1 else ''}")
