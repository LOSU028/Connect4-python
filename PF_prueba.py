import os 
global columna
global espacios_libres
global ganadorflag
global guardarflag
global turno_activo
global Tablero
global flag_nueva
global flag_cargar
global flag_estadisticas
global turnos_amarillo
global turnos_rojo
global row1
global row2
global row3
global row4
global row5
global row6
global row7

flag_nueva = False
flag_cargar = False
flag_estadisticas = False
ganadorflag = False
regresar_menu = True
ganador = False
espacios_libres = 42

row1 = 6
row2 = 6
row3 = 6
row4 = 6
row5 = 6
row6 = 6
row7 = 6
turno_activo = str

save_file = "Save_file_conecta4.txt"
statistics_file = "Statisitcs_file.txt"
sf = open(save_file, "a")


def instrucciones_menu():
    global turnos_amarillo
    global turnos_rojo
    global flag_nueva
    global flag_cargar
    global flag_estadisticas
    global espacios_libres
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    global total_turnos
    flag_menu = int

    print("Bienvenido a conecta 4 por favor introduzca alguno de los siguientes numeros: \n"
          "1.Para crear una nueva partida.\n"
          "2.Para cargar una partida existente.\n"
          "3.Para mostrar las estadísticas de la última partida concluida.")

    flag_menu = int(input())

    while not 1 <= flag_menu <= 3:
        print("Entrada invalida, introduzca alguno de los numeros indicados")
        flag_menu = int(input())

    if flag_menu == 1:
        os.system("cls")
        turnos_amarillo = 0
        turnos_rojo = 0
        espacios_libres = 42
        flag_nueva = True
        row1 = 6
        row2 = 6
        row3 = 6
        row4 = 6
        row5 = 6
        row6 = 6
        row7 = 6
        total_turnos = 1
    elif flag_menu == 2:
        os.system("cls")
        flag_cargar = True
    elif flag_menu == 3:
        os.system("cls")
        flag_estadisticas = True

    return flag_nueva, flag_cargar, flag_estadisticas


def Crear_tablero(flag, flag2):
    global Tablero
    global Filas
    global columnas
    global turno_activo
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    global espacios_libres
    global total_turnos
    global turnos_amarillo
    global turnos_rojo

    Filas = 6
    columnas = 7

    Tablero = [["   " for x in range(columnas)] for y in range(Filas)]

    if flag:
        turno_activo = "AMARILLO"
        for i in range(0, Filas):
            for j in range(0, columnas):
                print("|", Tablero[i][j], end=" ")
            print("|", "\n")
        return Tablero, turno_activo

    elif flag2:
        sf = open(save_file, "r+")
        lines = sf.readlines()
        tableroguardado = lines[0].split(",")
        turno_activo = str(lines[1]).strip("\n")
        row1 = int(lines[2])
        row2 = int(lines[3])
        row3 = int(lines[4])
        row4 = int(lines[5])
        row5 = int(lines[6])
        row6 = int(lines[7])
        row7 = int(lines[8])
        espacios_libres = int(lines[9])
        total_turnos = int(lines[10])
        turnos_amarillo = int(lines[11])
        turnos_rojo = int(lines[12])
        sf.close()
        c = 0
        for i in range(0, Filas):
            for j in range(0, columnas):
                Tablero[i][j] = tableroguardado[c]
                c += 1

        for i in range(0, Filas):
            for j in range(0, columnas):
                print("|", Tablero[i][j], end=" ")
            print("|", "\n")

        return Tablero, turno_activo


def Imprimir_Tablero(tablero, movimiento, turno):
    global total_turnos
    global espacios_libres
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7

    if turno == "AMARILLO":
        ficha = "\033[1;33;40m O \033[0;37;40m"
    else:
        ficha = "\033[1;31;40m O \033[0;37;40m"

    if movimiento == "GUARDAR":
        return tablero
    else:
        if movimiento == 1:
            tablero[row1 - 1][0] = ficha
            row1 -= 1
        elif movimiento == 2:
            tablero[row2 - 1][1] = ficha
            row2 -= 1
        elif movimiento == 3:
            tablero[row3 - 1][2] = ficha
            row3 -= 1
        elif movimiento == 4:
            tablero[row4 - 1][3] = ficha
            row4 -= 1
        elif movimiento == 5:
            tablero[row5 - 1][4] = ficha
            row5 -= 1
        elif movimiento == 6:
            tablero[row6 - 1][5] = ficha
            row6 -= 1
        elif movimiento == 7:
            tablero[row7 - 1][6] = ficha
            row7 -= 1
        os.system("cls")
        for i in range(0, 6):
            for j in range(0, 7):
                print("|", tablero[i][j], end=" ")
            print("|", "\n")
        espacios_libres -= 1

        return tablero


def Decision(tablero, movimiento):
    global guardarflag
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    global columna

    guardarflag = False

    while movimiento != "GUARDAR" and not 1 <= int(movimiento) <= 7:
        print("Movimiento inválido, por favor escoja un columna en rango 1-7 o escoja GUARDAR: ", end="")
        movimiento = input()

    if movimiento == "GUARDAR":
        os.system("cls")
        sf = open(save_file, "a")
        sf.truncate(0)
        for i in range(0, Filas):
            for j in range(0, columnas):
                sf.write(tablero[i][j])
                sf.write(",")
        sf.write("\n")
        sf.write(turno_activo)
        sf.write("\n")
        sf.write(str(row1))
        sf.write("\n")
        sf.write(str(row2))
        sf.write("\n")
        sf.write(str(row3))
        sf.write("\n")
        sf.write(str(row4))
        sf.write("\n")
        sf.write(str(row5))
        sf.write("\n")
        sf.write(str(row6))
        sf.write("\n")
        sf.write(str(row7))
        sf.write("\n")
        sf.write(str(espacios_libres))
        sf.write("\n")
        sf.write(str(total_turnos))
        sf.write("\n")
        sf.write(str(turnos_amarillo))
        sf.write("\n")
        sf.write(str(turnos_rojo))
        sf.close()
        guardarflag = True
        columna = "GUARDAR"
        return guardarflag, tablero, columna

    elif 1 <= int(movimiento) <= 7:
        while row1 <= 0 and int(movimiento) == 1:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        while row2 <= 0 and int(movimiento) == 2:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        while row3 <= 0 and int(movimiento) == 3:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        while row4 <= 0 and int(movimiento) == 4:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        while row5 <= 0 and int(movimiento) == 5:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        while row6 <= 0 and int(movimiento) == 6:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        while row7 <= 0 and int(movimiento) == 7:
            print("Movimiento inválido, por favor escoja una columna con espacios disponibles: ", end="")
            movimiento = int(input())
        columna = int(movimiento)
        return columna


def cambiar_Jugador(t):
    global turno_activo
    global total_turnos
    global ultimo_turno
    global turnos_amarillo
    global turnos_rojo

    t += 1
    if t % 2 == 0:
        turno_activo = "ROJO"
        ultimo_turno = "AMARILLO"
        turnos_amarillo += 1
    else:
        turno_activo = "AMARILLO"
        ultimo_turno = "ROJO"
        turnos_rojo += 1

    total_turnos = t
    return turno_activo, total_turnos


def cargar_estadisticas():
    global turnos_amarillo
    global turnos_rojo
    global total_turnos
    global ultimo_ganador

    turnos_amarillo = int(linesstf[0])
    turnos_rojo = int(linesstf[1])
    total_turnos = int(linesstf[2])
    ultimo_ganador = linesstf[3].strip("\n")

    print("\nTurnos del jugador amarillo: " + str(turnos_amarillo))
    print("Turnos del jugador rojo: " + str(turnos_rojo))
    print("Turnos totales de la partida: " + str(total_turnos))
    print("Ganador de la partida: " + ultimo_ganador)
    print("Total de partidas terminadas: " + str(partidas_terminadas) + "\n")


def Ganador(tablero):
    ficha_roja = "\033[1;33;40m O \033[0;37;40m"
    ficha_amarilla = "\033[1;31;40m O \033[0;37;40m"
    global ganadorflag

    '''Columna'''
    for i in range(3):
        for j in range(6):
            if ((tablero[i][j] == ficha_amarilla and tablero[i + 1][j] == ficha_amarilla) and (
                    tablero[i][j] == ficha_amarilla and tablero[i + 2][j] == ficha_amarilla) and (
                        tablero[i][j] == ficha_amarilla and tablero[i + 3][j] == ficha_amarilla)) or (
                    (tablero[i][j] == ficha_roja and tablero[i + 1][j] == ficha_roja) and (
                    tablero[i][j] == ficha_roja and tablero[i + 2][j] == ficha_roja) and (
                            tablero[i][j] == ficha_roja and tablero[i + 3][j] == ficha_roja)):
                ganadorflag = True
                return ganadorflag

    '''Fila'''
    for i in range(6):
        for j in range(4):
            if ((tablero[i][j] == ficha_amarilla and tablero[i][j + 1] == ficha_amarilla) and (
                    tablero[i][j] == ficha_amarilla and tablero[i][j + 2] == ficha_amarilla) and (
                        tablero[i][j] == ficha_amarilla and tablero[i][j + 3] == ficha_amarilla)) or (
                    (tablero[i][j] == ficha_roja and tablero[i][j + 1] == ficha_roja) and (
                    tablero[i][j] == ficha_roja and tablero[i][j + 2] == ficha_roja) and (
                            tablero[i][j] == ficha_roja and tablero[i][j + 3] == ficha_roja)):
                ganadorflag = True
                return ganadorflag

    '''Diagonal derecha'''
    for i in range(3):
        for j in range(6, 2, -1):
            if ((tablero[i][j] == ficha_amarilla and tablero[i + 1][j - 1] == ficha_amarilla) and (
                    tablero[i][j] == ficha_amarilla and tablero[i + 2][j - 2] == ficha_amarilla) and (
                        tablero[i][j] == ficha_amarilla and tablero[i + 3][j - 3] == ficha_amarilla)) or (
                    (tablero[i][j] == ficha_roja and tablero[i + 1][j - 1] == ficha_roja) and (
                    tablero[i][j] == ficha_roja and tablero[i + 2][j - 2] == ficha_roja) and (
                            tablero[i][j] == ficha_roja and tablero[i + 3][j - 3] == ficha_roja)):
                ganadorflag = True
                return ganadorflag

    '''Diagonal izquierda'''
    for i in range(3):
        for j in range(4):
            if ((tablero[i][j] == ficha_amarilla and tablero[i + 1][j + 1] == ficha_amarilla) and (
                    tablero[i][j] == ficha_amarilla and tablero[i + 2][j + 2] == ficha_amarilla) and (
                        tablero[i][j] == ficha_amarilla and tablero[i + 3][j + 3] == ficha_amarilla)) or (
                    (tablero[i][j] == ficha_roja and tablero[i + 1][j + 1] == ficha_roja) and (
                    tablero[i][j] == ficha_roja and tablero[i + 2][j + 2] == ficha_roja) and (
                            tablero[i][j] == ficha_roja and tablero[i + 3][j + 3] == ficha_roja)):
                ganadorflag = True
                return ganadorflag


stf = open(statistics_file, "a")
stf.close()
stf = open(statistics_file, "r+")
linesstf = stf.readlines()
if linesstf == []:
    partidas_terminadas = 0
else:
    partidas_terminadas = int(linesstf[4])
stf.close()
while regresar_menu:
    ganadorflag = False
    instrucciones_menu()
    sf = open(save_file, "r+")
    lines = sf.readlines()
    if flag_cargar and lines == []:
        print("No se han guardado partidas todavía.")
        flag_cargar = False
        sf.close()
    else:
        Crear_tablero(flag_nueva, flag_cargar)
        if flag_estadisticas:
            stf = open(statistics_file, "r+")
            linesstf = stf.readlines()
            if linesstf == []:
                print("No hay partidas terminadas registradas.")
            else:
                cargar_estadisticas()
            stf.close()
            flag_nueva = False
            flag_cargar = False
            flag_estadisticas = False
        else:
            flag_nueva = False
            flag_cargar = False
            flag_estadisticas = False
            while espacios_libres > 0 and ganadorflag == False:
                print("Turno del jugador: " + turno_activo + "\n")
                print("Movimiento (escriba GUARDAR si desea guardar y salir de la partida actual): ", end=" ")
                movimiento = input()
                movimiento = movimiento.upper()
                Decision(Tablero, movimiento)
                print("\n")
                Tablero = Imprimir_Tablero(Tablero, columna, turno_activo)
                if guardarflag:
                    guardarflag = False
                    break
                cambiar_Jugador(total_turnos)
                Ganador(Tablero)
            if espacios_libres == 0:
                partidas_terminadas += 1
                print("\nEMPATE\n")
                stf = open(statistics_file, "a")
                partidas_terminadas += 1
                stf.truncate(0)
                stf.write(str(turnos_amarillo))
                stf.write("\n")
                stf.write(str(turnos_rojo))
                stf.write("\n")
                stf.write(str(total_turnos - 1))
                stf.write("\n")
                stf.write("Ninguno, fue un empate")
                stf.write("\n")
                stf.write(str(partidas_terminadas))
                stf.close()

            elif ganadorflag:
                print("Gano el jugador: " + ultimo_turno + "\n")
                stf = open(statistics_file, "a")
                partidas_terminadas += 1
                stf.truncate(0)
                stf.write(str(turnos_amarillo))
                stf.write("\n")
                stf.write(str(turnos_rojo))
                stf.write("\n")
                stf.write(str(total_turnos - 1))
                stf.write("\n")
                stf.write(ultimo_turno)
                stf.write("\n")
                stf.write(str(partidas_terminadas))
                stf.close()
                regresar_menu = True