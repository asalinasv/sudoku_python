from norvigalgorithm import *
from convert import GeneralConverter
import os
from display import *

class CommandLine:
    def __init__(self,string):
        self.string = string

    """Definitions for command line reading and solving"""

    def reading_command_line(self):
        self.commandline = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        if self.commandline != '':
            return self.commandline
        else:
            return False

    def validate_size_command_line(self):
        #commandline = self.reading_command_line()
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        b = 0
#        for x in self.commandline:
        for x in self.string:
            b += 1
        if b == 81:
            return b
        else:
            print "The inserted string does not have 81 characters"
            return False

    def validate_values_command_line(self):
        #commandline = self.reading_command_line()
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        valids = '1','2','3','4','5','6','7','8','9','0'
        #for x in self.commandline:
        for x in self.string:
            if x not in valids:
                print "Values in the string are not allowed"
                return False
        return True

    def solve_from_commandline(self):
        #a = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        if self.validate_size_command_line()==81 and self.validate_values_command_line():
            os.system('cls')
            norvig = NorvigAlgorithm()
            b = norvig.solve(self.string)
            if b:

                resstring = GeneralConverter().convert_dictionary_to_string(b)
                matrix = GeneralConverter().convert_string_to_matrix(resstring)
                SudokuDisplayer(matrix).displaysudoku()
                print "Sudoku has been resolved sucessfully"
                return matrix
            else:
                print "The sudoku is invalid, please insert a good one"
                return False
        else:
            return False