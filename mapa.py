import mapa


import random
class Mapa:
    def crearMatriz0(self): #matriz solo 0
        self.mapa0 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    def ponerNaufragos(self, cantidad): #poner naufragos "1" randoms
        posiciones = random.sample(range(25), cantidad)
        for pos in posiciones:
            r = pos // 5  #fila
            c = pos % 5  #columna
            self.mapa0[r][c] = 1

    def mostrarMapa(self):
        for fila in self.mapa0:
            print(fila)

if __name__ == '__main__':
    mapa = Mapa()
    mapa.crearMatriz0()
    mapa.ponerNaufragos(4)
    mapa.mostrarMapa()
