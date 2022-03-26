
jugadores = [] #Variable global para lista de jugadores 

#MÉTODO PARA EL MENU DE JUEGO
def menu():
    while True:
        print("『PACMAN ★ IPC1 ★  2022』")
        print("✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        print("1.         Iniciar Juego")
        print("2.   Tabla de Posiciones")
        print("3.                 Salir")
        print("✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
        num = int(input("Escoge tu opción: "))
        if (num == 1):
            juego()

        elif(num == 2):
            pass

        elif(num == 3):
            break 

#MÉTODO PARA EL JUEGO 
def juego():
    name = input("Ingrese su Nombre: ")
    comidarestante = int(5*5*0.4)
    comidaobtenida = 0
    paredes = int(5*5*0.3)
    movimientos = 0
    print("Comida Restante: " +str(comidarestante))
    print("Comida Obtenida: " +str(comidaobtenida))
    print("Paredes: " +str(paredes))
    print("Movimientos" +str(movimientos))

#MÉTODO PARA EL TABLERO 
def tablero():
    matriz = []
for i in range(5): 
    for j in range(5):
        print(" |", end = "") #vacio "" 
    print("")


##LLAMAR MÉTODO MENU PARA INICIAR EL JUEGO
menu()