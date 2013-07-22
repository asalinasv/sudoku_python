'''
    Created on Jul 22, 2013
    Class to Play sudoku based on main menu or generated
    @author: Ana Salinas
    Automation Class (Sudoku project) - 2013
'''
from generators import SudokuGenerator

class SudobuGame(object):

    def __init__(self):
        '''
        Constructor
        '''
    def create_sudoku_game(self):
        self.matrix = SudokuGenerator()
    
    def print_sudoku_game(self):
        pass
    
    def validate_editable_cells(self):
        pass
        
        