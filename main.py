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
            pass

        elif(num == 3):
            break 

#****************************************************************************************************************
#TODO LO RELACIONADO CON EL INICIO DEL JUEGO
#MÉTODO PARA INICIAR JUEGO
def Inicio(jugadores):
    name = input("Ingrese su Nombre: ")

    ### --- definir las comidas
    comidas_solicitadas = 15
    lista_comidas = []
    crearListaComidas(lista_comidas, comidas_solicitadas)

    jugadores.setPosX(0)
    jugadores.setPosY(0)

    ### inicializar el tablero de juego
    tablero = Tablero(lista_comidas, jugadores)
    GenerarTablero(tablero)
    
    ## logica de juego
    movimientos(jugadores, lista_comidas)
    ## setear tabla posiciones
    #--- unicamente 3 lugares


#****************************************************************************************************************
#TODO RELACIONADO CON LOS MOVIMIENTOS
def movimientos(jugadores, lista_comidas):
    while True:
        movimiento = input("Movimiento: ")
        posx_jug = movimiento.split(",")[0]
        posy_jug = movimiento.split(",")[1]
        jugadores.setPosX(int(posx_jug))
        jugadores.setPosY(int(posy_jug))
        movimiento = siguienteHayComida(jugadores, lista_comidas)
        if movimiento:
            jugadores.addMovimiento()
        print(" - JUGADOR - PUNTOS: {0} - MOVIMIMENTOS: {0}".format(jugadores.getPuntos(), jugadores.getMovimientos()))
        matriz = Tablero(lista_comidas, jugadores)
        GenerarTablero(matriz)
        if jugadores.getPuntos() > 15 or aunHayComidas(lista_comidas):
            break    

#*****************************************************************************************************************    
#TODO LO RELACIONADO CON LA COMIDA 
def crearListaComidas(lista_comida, comidas: int):
    index = 0
    while index < comidas:##iterar mientras index sea menor a comida
        posx_comida_generada = random.randint(0,9)
        posy_comida_generada = random.randint(0,9)
        estaOcupado = False
        for comidas_busqueda in lista_comida:
            if comidas_busqueda.getPosX() == posx_comida_generada and comidas_busqueda.getPosY() == posy_comida_generada:
                estaOcupado = True
        
        if not estaOcupado:
            comida_creada = Comida(posx_comida_generada, posy_comida_generada)
            lista_comida.append(comida_creada)
            index = index + 1

def siguienteHayComida(jugadores, lista_comida):
    for comida in lista_comida:
        if jugadores.getPosX() == comida.getPosX() and jugadores.getPosY() == comida.getPosY():
            comida.setEat()
            jugadores.addPuntos()
            return True
    return False

def aunHayComidas(lista_comidas):
    for comida in lista_comidas:
        if not comida.isComido():
            return False
    return True


#*****************************************************************************************************************
#Todo lo RELACIONADO CON EL TABLERO 
#MÉTODOS PARA EL USO DEL  TABLERO 
def GenerarTablero(matriz):
    for fila in matriz:
        print("\t| {0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} | ".format(fila))

def Tablero(lista_comida, jugadores):

    matriz = [
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "]
    ]
    
    for comida in lista_comida:
        if not comida.isComido():
            matriz[comida.getPosX()][comida.getPosY()] = "@"
    
    matriz[jugadores.getPosX()][jugadores.getPosY()] = "C"
    return matriz


#**********************************************************************************************************************
#TODO LO RELACIONADO PARA EMPEZAR EL JUEGO
##LLAMAR MÉTODO MENU PARA INICIAR EL JUEGO
jugadores = jugador()
menu(jugadores)