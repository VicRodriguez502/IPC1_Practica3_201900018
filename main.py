#IMPORTACIONES 
import random
from comida import Comida
from jugador import jugador


#******************************************************************************************************************************
#TODO RELACIONADO CON EL MENU.
#MÉTODO PARA EL MENU DE JUEGO.
def menu(jugadores):
    while True:
        print("『PACMAN ★ IPC1 ★  2022』")
        print("✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        print("1.         Iniciar Juego")
        print("2.   Tabla de Posiciones")
        print("3.                 Salir")
        print("✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        num = int(input("Escoge tu opción: "))
        if (num == 1):
            Inicio(jugadores)

        elif(num == 2):
            Posiciones(jugadores)

        elif(num == 3):
            break 

#****************************************************************************************************************
#TODO LO RELACIONADO CON EL INICIO DEL JUEGO
#MÉTODO PARA INICIAR JUEGO
def Inicio(jugadores):
    name = input("Ingrese su Nombre: ")
    jugadores.nombre = name
    comidassol = random.randint(1,int(10*10*0.4))
    comidita = []
    crearComida(comidita, comidassol)
    
    JugadorAl(jugadores, comidita)

    matriz = Tablero(comidita, jugadores)
    GenerarTablero(matriz)
    
    movimientos(jugadores, comidita)

#***************************************************************************************************************
#TODO LO RELACIONADO CON LA TABLA DE POSICIONES
#MÉTODO PARA LA TABLA DE POSICIONES
def Posiciones(jugadores):
    Primerlugar = -1
    segundolugar = 0
    tercerlugar = 1
    
    if jugadores == -1:
        print("1. {0} - {1} MOVIIENTOS {2} PUNTOS". format (jugadores.nombre, jugadores.movimientos, jugadores.puntos))
    elif jugadores == 0:
        print("2. {0} - {1} MOVIIENTOS {2} PUNTOS". format (jugadores.nombre, jugadores.movimientos, jugadores.puntos))  
    elif jugadores == 1:
        print("3. {0} - {1} MOVIIENTOS {2} PUNTOS". format (jugadores.nombre, jugadores.movimientos, jugadores.puntos))  



#***************************************************************************************************************
#TODO RELACIONADO CON LOS MOVIMIENTOS
#MÉTODO PARA LA LÓGICA DE LOS MOVIMIENTOS DEL JUEGO 
def movimientos(jugadores, comidita):
    while True:
        movimiento = input("Movimiento: ")
        if str(movimiento) == "a" or str(movimiento) == "4":
            Izquierda(jugadores, comidita)
            print(" - JUGADOR: {0} - PUNTOS: {1} - MOVIMIMENTOS: {2}".format(jugadores.nombre,jugadores.getPuntos(), jugadores.getMovimientos()))
            matriz = Tablero(comidita, jugadores)
            GenerarTablero(matriz)
            if jugadores.getPuntos() == 40 or HabraComidas(comidita):
                break
        elif str(movimiento) == "d" or str(movimiento) == "6":
            Derecha(jugadores, comidita)
            print(" - JUGADOR: {0} - PUNTOS: {1} - MOVIMIMENTOS: {2}".format(jugadores.nombre,jugadores.getPuntos(), jugadores.getMovimientos()))
            matriz = Tablero(comidita, jugadores)
            GenerarTablero(matriz)
            if jugadores.getPuntos() == 40 or HabraComidas(comidita):
                break 
        elif str(movimiento) == "w" or str(movimiento) == "8":
            Arriba(jugadores, comidita)
            print(" - JUGADOR: {0} - PUNTOS: {1} - MOVIMIMENTOS: {2}".format(jugadores.nombre,jugadores.getPuntos(), jugadores.getMovimientos()))
            matriz = Tablero(comidita, jugadores)
            GenerarTablero(matriz)
            if jugadores.getPuntos() == 40 or HabraComidas(comidita):
                break
        elif str(movimiento) == "s" or str(movimiento) == "5":
            Abajo(jugadores, comidita)
            print(" - JUGADOR: {0} - PUNTOS: {1} - MOVIMIMENTOS: {2}".format(jugadores.nombre,jugadores.getPuntos(), jugadores.getMovimientos()))
            matriz = Tablero(comidita, jugadores)
            GenerarTablero(matriz)
            if jugadores.getPuntos() == 40 or HabraComidas(comidita):
                break 
            

#MÉTODO PARA LA POSICIÓN ALEATORIA DEL JUGADOR  
def JugadorAl(jugadores, comidita):
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        
        Ocupado = False
        for c in comidita:
            
            try:
                if c.getPosX() == x and c.PosY() == y:
                    Ocupado = True
            except Exception as e:
                pass
                
        if not Ocupado:
            jugadores.setPosX(x)
            jugadores.setPosY(y)
            break

#MÉTODO PARA MOVERSE A LA  IZQUIERDA
def Izquierda(jugadores, comidita):    
    x = jugadores.getPosX() 
    y = jugadores.getPosY() - 1
    
    if y >= 0:
        jugadores.setPosX(int(x))
        jugadores.setPosY(int(y))
        m = sigComida(jugadores, comidita)
        jugadores.addMovimiento()

#MÉTODO PARA MOVERSE A LA DERECHA 
def Derecha(jugadores, comidita):    
    x = jugadores.getPosX() 
    y = jugadores.getPosY() + 1
    
    if y >= 0:
        jugadores.setPosX(int(x))
        jugadores.setPosY(int(y))
        m = sigComida(jugadores, comidita)
        jugadores.addMovimiento()

#MÉTODO PARA MOVERSE PARA ARRIBA 
def Arriba(jugadores, comidita):    
    x = jugadores.getPosX() - 1
    y = jugadores.getPosY() 
    
    if x >= 0:
        jugadores.setPosX(int(x))
        jugadores.setPosY(int(y))
        m = sigComida(jugadores, comidita)
        jugadores.addMovimiento()

#MÉTODO PARA MOVERSE PARA ABAJO
def Abajo(jugadores, comidita):    
    x = jugadores.getPosX() + 1
    y = jugadores.getPosY() 
    
    if x >= 0:
        jugadores.setPosX(int(x))
        jugadores.setPosY(int(y))
        m = sigComida(jugadores, comidita)
        jugadores.addMovimiento()


#***************************************************************************************************************    
#TODO LO RELACIONADO CON LA COMIDA 
#METODO PARA CREAR LA COMIDA EN POSICIONES ALEATORIAS
def crearComida(comidita, comidas: int):
    index = 0
    while index < comidas:##iterar mientras index sea menor a comida
        posxcgenerada = random.randint(0,9)
        posycgenerada = random.randint(0,9)
        Ocupado = False
        for cbusqueda in comidita:
            if cbusqueda.getPosX() == posxcgenerada and cbusqueda.getPosY() == posycgenerada:
                Ocupado = True
        
        if not Ocupado:
            ccreada = Comida(posxcgenerada, posycgenerada)
            comidita.append(ccreada)
            index = index + 1
            
#MÉTODO PARA VALIDAD SI HAY COMIDA EN LA SIGUIENTE CASILLA            
def sigComida(jugadores, comidita):
    for comida in comidita:
        if jugadores.getPosX() == comida.getPosX() and jugadores.getPosY() == comida.getPosY():
            comida.setEat()
            jugadores.addPuntos()
            return True
    return False

#MÉTODO PARA VALIDAD SI AUN HAY COMIDA
def HabraComidas(comidita):
    for comida in comidita:
        if not comida.isComido():
            return False
    return True


#***************************************************************************************************************
#Todo lo RELACIONADO CON EL TABLERO 
#MÉTODOS PARA EL USO DEL  TABLERO 
def GenerarTablero(matriz):
    for fila in matriz:
        print("\t| {0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} | ".format(fila))
        
#MÉTODO PARA MOSTRAR EL TABLERO EN LA PANTALLA
def Tablero(comidita, jugadores):

    matriz = [
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "]
    ]
    
    for comida in comidita:
        if not comida.isComido():
            matriz[comida.getPosX()][comida.getPosY()] = "@"
    
    matriz[jugadores.getPosX()][jugadores.getPosY()] = "C"
    return matriz


#****************************************************************************************************************
#TODO LO RELACIONADO PARA EMPEZAR EL JUEGO
##LLAMAR MÉTODO MENU PARA INICIAR EL JUEGO
jugadores = jugador()
menu(jugadores)