class Comida():
    
    def __init__(self, posx, posy): ##Init sirve para el constructor
        self.posx = posx ##EL SELF ES IGUAL A THIS
        self.posy = posy                   
        self.isEat = False

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def isComido(self):
        return self.isEat

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def setEat(self):
        self.isEat = True