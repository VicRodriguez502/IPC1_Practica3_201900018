from re import X


class jugador():
    
    #CONSTRUCTOR PARA JUGADOR
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.puntos = 0
        self.mov = 0
    
    #ENCAPSULAMIENTO PARA PARAMETROS DE JUGADOR
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getPuntos(self):
        return self.puntos
    
    def getMov(self):
        return self.mov
    
    