# ESTUDIANTE: IGLESIAS ROCABADO DANIELA
# CU: 35-4780

#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""


HUMANO = -1
COMPUTADOR = +1
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def evaluate(estado):
    """
    Función de evaluación heurística del estado.
     : parametro: estado, estado actual del tablero
     : devuelve: +1 si COMPUTADOR gana; -1 si el HUMANO gana; 0 en caso de empate
    """
    if wins(estado, COMPUTADOR):
        score = +1
    elif wins(estado, HUMANO):
        score = -1
    else:
        score = 0

    return score


def wins(estado, player):
    """
    Esta funcion verifica si un jugador especifico gana. Posibilidades:
    * Tres filas    [X X X] or [O O O]
    * Tres columnas    [X X X] or [O O O]
    * Dos diagonales [X X X] or [O O O]
    :parametro estado, el estado del tablero actual
    :parametro player: un HUMANOo o un COMPUTADORutador
    :devuelve: True si un jugador gana
    """
    win_state = [
        #PRIMERA FILA
        [estado[0][0], estado[0][1], estado[0][2]],
        [estado[0][1], estado[0][2], estado[0][3]],
        #SEUNDA FILA
        [estado[1][0], estado[1][1], estado[1][2]],
        [estado[1][1], estado[1][2], estado[1][3]],
        #TERCERA FILA
        [estado[2][0], estado[2][1], estado[2][2]],
        [estado[2][1], estado[2][2], estado[2][3]],
        #CUARTA FILA
        [estado[3][0], estado[3][1], estado[3][2]],
        [estado[3][1], estado[3][2], estado[3][3]],
        #PRIMERA COLUMNA
        [estado[0][0], estado[1][0], estado[2][0]],
        [estado[1][0], estado[2][0], estado[3][0]],
        #SEGUNDA COLUMNA
        [estado[0][1], estado[1][1], estado[2][1]],
        [estado[1][1], estado[2][1], estado[3][1]],
        #TERCERA COLUMNA
        [estado[0][2], estado[1][2], estado[2][2]],
        [estado[1][2], estado[2][2], estado[3][2]],
        #CUARTA COLUMNA
        [estado[0][3], estado[1][3], estado[2][3]],
        [estado[1][3], estado[2][3], estado[3][3]],
        #DIAGONALES
        [estado[0][0], estado[1][1], estado[2][2]],
        [estado[1][1], estado[2][2], estado[3][3]],
        [estado[1][0], estado[2][1], estado[3][2]],
        [estado[0][1], estado[1][2], estado[2][3]],

        [estado[0][3], estado[1][2], estado[2][1]],
        [estado[1][2], estado[2][1], estado[3][0]],
        [estado[0][2], estado[1][1], estado[2][0]],
        [estado[1][3], estado[2][2], estado[3][1]]
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(estado):
    """
    Esa funcion verifica si el HUMANOo o el COMPUTADORutador gana
    :parametro estado, estado del tablero actual
    :devuelve: True si el HUMANOo o el COMPUTADORutador gana
    """
    return wins(estado, HUMANO) or wins(estado, COMPUTADOR)


def empty_cells(estado):
    """
    Cada celda vacía se agregará a la lista de celdas
    :parametro estado, estado de tablero actual
    :devuelve, una lista de las celdas vacias
    """
    cells = []

    for x, fila in enumerate(estado):
        for y, cell in enumerate(fila):
            if cell == 0:
                cells.append([x, y])
    return cells

def valid_move(x, y):
    """
    Un movimiento es válido si la celda elegida está vacía
    :parametro x, coordenada X
    :parametro y, coordenada Y
    :devuelve: True si la posicion del tablero[x][y] esta vacia
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False

def set_move(x, y, player):
    """
    Establece un movimiento en el tablero, si las coordenadas son validas
    :parametro x, coordenada X
    :parametro y, coordenada Y
    :parametro player, jugador actual
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(estado, depth, player):
    """
    Funcion IA que elige la mejor movida
    AI function that choice the best move
    :param estado:
    :parametro estado, estado actual en el tablero
    :param depth, indice del nodo en el arbol (0 <= depth <= 9), pero nunca nueve.
    :param player, un HUMANOo o un COMPUTADORutador
    :devuelve, una lista con [la mejor fila, la mejor columna, el mejor score]
    """
    if player == COMPUTADOR:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(estado):
        score = evaluate(estado)
        return [-1, -1, score]

    for cell in empty_cells(estado):
        x, y = cell[0], cell[1]
        estado[x][y] = player
        score = minimax(estado, depth - 1, -player)
        estado[x][y] = 0
        score[0], score[1] = x, y

        if player == COMPUTADOR:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(estado, c_choice, h_choice):
    """
    Print the board on console
    :param estado: current estado of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '--------------------'

    print('\n' + str_line)
    for fila in estado:
        for cell in fila:
            symbol = chars[cell]
            print(f'| {symbol} |', end = '')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Juega COMPUTADORA [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 16:
        x = choice([0, 1, 2, 3])
        y = choice([0, 1, 2, 3])
    else:
        move = minimax(board, depth, COMPUTADOR)
        x, y = move[0], move[1]

    set_move(x, y, COMPUTADOR)
    time.sleep(1)

def HUMANO_turn(c_choice, h_choice):
    """
    The HUMANO plays choosing a valid move.
    :param c_choice: COMPUTADORuter's choice X or O
    :param h_choice: HUMANO's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3],
        5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3],
        9: [2, 0], 10: [2, 1], 11: [2, 2], 12: [2, 3],
        13: [3, 0], 14: [3, 1], 15: [3, 2], 16: [3, 3]
    }

    clean()
    print(f'TURNO HUMANO [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 16:
        try:
            move = int(input('Elija una casilla (1..16): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMANO)

            if not can_move:
                print('Mal Movimiento')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Adios')
            exit()
        except (KeyError, ValueError):
            print('Elección incorrecta')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if HUMANO is the first

    # HUMANO chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Escoja "X" o "O"\nElegido: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Adios')
            exit()
        except (KeyError, ValueError):
            print('Mala eleccion')

    # Setting COMPUTADORuter's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # HUMANO may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('Primero en empezar?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Adios')
            exit()
        except (KeyError, ValueError):
            print('Mala eleccion')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        HUMANO_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMANO):
        clean()
        print(f'HUMANO turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('Ganaste!')
    elif wins(board, COMPUTADOR):
        clean()
        print(f'TURNO COMPUTADORA [{c_choice}]')
        render(board, c_choice, h_choice)
        print('PERDISTE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('EMPATE!')

    exit()


if __name__ == '__main__':
    main()