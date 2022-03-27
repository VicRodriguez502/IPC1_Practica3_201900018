class jugador():
    def __init__(self):
        self.posx = -1
        self.posy = -1
        self.puntos = 0
        self.movimientos = 0

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def getMovimientos(self):
        return self.movimientos

    def getPuntos(self):
        return self.puntos

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def addMovimiento(self):
        self.movimientos = self.movimientos + 1

    def addPuntos(self):
        self.puntos = self.puntos + 5