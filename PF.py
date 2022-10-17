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
total_turnos = 1
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
sf = open(save_file, "a")


def instrucciones_menu():
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

    print("Bienvenido a conecta 4 por favor introduzca alguno de los siguiemntes numeros: \n"
          "1.Para cargar una nueva partida.\n"
          "2.Para cargar una partida existente.\n"
          "3.Para mostrar las estadísticas de la última partida.")

    flag_menu = int(input())

    while not 1 <= flag_menu <= 3:
        print("Entrada invalida, introduzca alguno de los numeros indicados")
        flag_menu = int(input())

    if flag_menu == 1:
        espacios_libres = 42
        flag_nueva = True
        row1 = 6
        row2 = 6
        row3 = 6
        row4 = 6
        row5 = 6
        row6 = 6
        row7 = 6
        espacios_libres = 42
        total_turnos = 1
    elif flag_menu == 2:
        flag_cargar = True
    elif flag_menu == 3:
        flag_estadisticas = True

    return flag_nueva, flag_cargar, flag_estadisticas


def Crear_tablero(flag, flag2, flag3):
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
        flag2 = False

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
        ficha = "\033[0;33;237m O \033[0;37;0m"
    else:
        ficha = "\033[0;31;237m O \033[0;37;0m"

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

    if movimiento == "GUARDAR":
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

    t += 1
    if t % 2 == 0:
        turno_activo = "ROJO"
        ultimo_turno = "AMARILLO"
    else:
        turno_activo = "AMARILLO"
        ultimo_turno = "ROJO"

    total_turnos = t
    return turno_activo, total_turnos


def Ganador(tablero):
    ficha_roja = "\033[0;31;237m O \033[0;37;0m"
    ficha_amarilla = "\033[0;33;237m O \033[0;37;0m"
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


while regresar_menu:
    ganadorflag = False
    instrucciones_menu()
    Crear_tablero(flag_nueva, flag_cargar, flag_estadisticas)
    flag_nueva = False
    flag_cargar = False
    flag_estadisticas = False
    while espacios_libres > 0 and ganadorflag == False:
        print("Turno del jugador: " + turno_activo + "\n")
        print("Movimiento (escriba GUARDAR si desea guardar y salir de la partida actual): ", end=" ")
        movimiento = input()
        Decision(Tablero, movimiento)
        print("\n")
        Tablero = Imprimir_Tablero(Tablero, columna, turno_activo)
        if guardarflag:
            guardarflag = False
            break
        cambiar_Jugador(total_turnos)
        Ganador(Tablero)
    if espacios_libres == 0:
        print("\nEMPATE\n")

    elif ganadorflag:
        print("Gano el jugador: " + ultimo_turno + "\n")
        regresar_menu = True
