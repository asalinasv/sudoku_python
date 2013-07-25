'''
Created on Jul 22, 2013
Class to get the right number to resolve a sudoku
@author: Ana Salinas
'''
import copy
from Configuration.readconfiguration import FileReader
from solver.norvigalgorithm import NorvigAlgorithm
from solver.solver import Solver

class HintsDisplayer:
    columns = ['A','B','C','D','E','F','G','H','I']

    def __init__(self, matrix):
        '''
        Constructor
        '''
        matrix_copy=copy.deepcopy(matrix)
        self.original_matrix = matrix_copy

        self.solve_matrix = Solver(file)
        matrix_aux = self.get_int_matrix(matrix)
        self.resolved_matrix_backtracking = self.solve_matrix.solve_sudoku_game_backtracking(matrix_aux)
        self.resolved_matrix = self.solve_matrix.solve_sudoku_game_norvig(self.original_matrix)

    def get_value_in_cell(self, position):
        if len(position) > 2:
            print "Error"
        else:
            #cell = position.split(':')
            column = position[0]
            row = position[1]
            column = self.get_column_number(column)
            return self.resolved_matrix[int(row)-1][int(column)]

    def get_column_number(self, col):
        for i in range(9):
            if self.columns[i] == col.upper():
                return i

    def get_int_matrix(self, str_matrix):
        backtrack_matrix = []
        for i in range(9):
            backtrack_matrix.append([0]*9)

        for k in range(9):
            for l in range(9):
                backtrack_matrix[k][l] = int(str_matrix[k][l])

        return backtrack_matrix