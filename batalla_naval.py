#Ahora vamos a hacer el juego de batalla naval como proyecto final
#De acuerdo a los requisitos necesitamos primero crear las variables, en este caso
#son las de las matrices de los jugadores

table_player1 = []
table_player2 = []

#Ahora vamos a crear la funcion que crear las matrices de los jugadores
def show_matrix(matrix):
    for filas in matrix:
        print(filas)

def create_matrix():
    matrix = [[' ' for _ in range(10)] for _ in range(10)]
    show_matrix(matrix)
    return matrix
         
def put_ships(matrix):
    options_ships = ['D', 'S' , 'N']
    for opciones in range(len(options_ships)):
        print(opciones)
        pos_x = int(input(f"Digita la posicion x del barco {options_ships[opciones]}"))
        pos_y = int(input(f"Digita la posicion y del barco {options_ships[opciones]}"))
        matrix[pos_x][pos_y] = options_ships[opciones]

        pos2_x = int(input(f"Digita la posicion 2 x del barco {options_ships[opciones]}"))
        pos2_y = int(input(f"Digita la posicion 2 y del barco {options_ships[opciones]}"))
        matrix[pos2_x][pos2_y] = options_ships[opciones]

        if opciones == 0:
            if pos_x == pos2_x:
                matrix[pos2_x][pos2_y + 1] = options_ships[opciones]
            else:
                matrix[pos2_x + 1][pos2_y] = options_ships[opciones]
        elif opciones == 1:
            if pos_x == pos2_x:
                matrix[pos2_x][pos2_y + 1] = options_ships[opciones]
                matrix[pos2_x][pos2_y + 2] = options_ships[opciones]
            else:
                matrix[pos2_x + 1][pos2_y] = options_ships[opciones]
                matrix[pos2_x + 2][pos2_y] = options_ships[opciones]

    show_matrix(matrix)

def shot(matrix_opponent):
    pos_x = int(input("Ingrese la coordenada x"))
    pos_y = int(input("Ingrese la coordenada y"))
    if matrix_opponent[pos_x][pos_y] != ' ' or matrix_opponent[pos_x][pos_y] != 'O' or matrix_opponent[pos_x][pos_y] != 'X':
        matrix_opponent[pos_x][pos_y] = 'X'
        print("Impacto")
        return 1
    else:
        matrix_opponent[pos_x][pos_y] = 'O'
        print("Al Agua")
        return 0

def play_game():
    table_player1 = create_matrix()
    table_player2 = create_matrix()
    puntos_jugador1 = 0
    puntos_jugador2 = 0

    print("Posiciona tus barcos jugador 1")
    put_ships(table_player1)
    print("Posiciona tus barcos jugador 2")
    put_ships(table_player2)


    while True:
        print("Jugador 1: Dispara")
        puntos_jugador1 += shot(table_player2)
        show_matrix(table_player2)
        print("Jugador 2 : Dispara")
        puntos_jugador2 += shot(table_player1)
        show_matrix(table_player1)
        if puntos_jugador1 == 9:
            print("Ganado jugador 1")
            break
        elif puntos_jugador2 == 9:
            print("Ganador jugador 2")
            break
        
play_game()