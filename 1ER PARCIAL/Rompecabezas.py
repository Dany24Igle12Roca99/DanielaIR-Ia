from busquedas_02 import aestrella, ProblemaBusqueda


OBJETIVO = '''a-b-c-d
e-f-g-h
i-j-k-x'''

INICIAL = '''a-c-f-d
i-e-x-b
j-g-k-h'''


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(filas, element_to_find):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       DEvuelve una tupla: fila, columna'''
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)
for numero in 'abcefghijkx':
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)


class EigthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
        filas = string_to_list(estado)
        fila_e, columna_e = find_location(filas, 'x')

        acciones = []
        if fila_e > 0:
            acciones.append(filas[fila_e - 1][columna_e])
        if fila_e < 2:
            acciones.append(filas[fila_e + 1][columna_e])
        if columna_e > 0:
            acciones.append(filas[fila_e][columna_e - 1])
        if columna_e < 3:
            acciones.append(filas[fila_e][columna_e + 1])

        return acciones

    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        fila_e, columna_e = find_location(filas, 'x')
        fila_n, columna_n = find_location(filas, accion)

        filas[fila_e][columna_e], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_e][columna_e]

        return list_to_string(filas)

    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion. 
        '''
        return 1

    # def heuristica(self, estado):
    #     '''Devuelve una estimacion de la distancia
    #     de un estado a otro, utilizando la distancia manhattan.
    #     '''
    #     filas = string_to_list(estado)
    #
    #     distancia = 0
    #
    #     for numero in 'abcefghijkx':
    #         fila_n, columna_n = find_location(filas, numero)
    #         fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]
    #
    #         distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)
    #
    #     return distancia

    def heurisica(self,estado):
        filas = string_to_list(estado)

        distancia = 0

        for numero in 'abcdefghijkx':
            fila_n, columna_n = find_location(filas, numero)
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]
            if fila_n != fila_n_objetivo and columna_n != col_n_goal:
                distancia += 1
        return distancia


resultado = aestrella(EigthPuzzleProblem(INICIAL))
it = 0

for accion, estado in resultado.camino():
    print('Move numero', accion)
    it += 1
    print('nro de movimientos', it)
    print(estado)


