'''
Created on Jul 22, 2013

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
        self.resolved_matrix_backtracking = self.solve_matrix.solve_sudoku_game_backtracking(self.original_matrix)
        self.resolved_matrix = self.solve_matrix.solve_sudoku_game_norvig(self.original_matrix)

    def get_value_in_cell(self, position):
        if len(position) > 3:
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

    def display_all_hints(self, matrix):
        pass

    def print_matrix(self, ma):
        for i in range(9):
           print ma[i]


if __name__=="__main__":
##    game = ['4','0','0','0','0','1','6','5','0'],\
##         ['0','0','7','0','4','0','0','0','1'],\
##         ['0','5','0','8','0','6','0','0','3'],\
##         ['5','4','8','0','3','0','9','7','0'],\
##         ['0','0','0','0','0','4','0','0','8'],\
##         ['1','0','0','7','0','0','2','0','0'],\
##         ['0','7','0','0','0','0','0','0','4'],\
##         ['0','0','0','2','0','0','0','6','0'],\
##         ['6','0','5','0','1','0','3','0','0']
##    file = "Sudoku_Levels/Easy/Easy_1.txt"
##    var = HintsDisplayer(game)
##    print var.get_value_in_cell("I9")

    """
    print "To get a hint you should type 'Hint' to get a hint at that position"
    value = raw_input()

    while value.lower() == "hint":
        print "Select the position to get hint, for example 'A:2'"
        position = raw_input()
        num_cell = var.get_value_in_cell(position)

        if num_cell == "Error":
            print "Select the position to get hint, for example 'A:2'"
            position = int(raw_input())
        print num_cell
        hint = "any"
    """

