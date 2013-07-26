# CommandLine class: Class that handles the sudoku game from console
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import os
from norvigalgorithm import *
from convert import GeneralConverter
from display import *

class CommandLine:
    def __init__(self,string):
        self.string = string

    def reading_command_line(self):
        """Read a value from command line"""
        self.commandline = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        if self.commandline != '':
            return self.commandline
        else:
            return False

    def validate_size_command_line(self):
        """Validate if the string inserted has 81 characters"""
        b = 0
        for x in self.string:
            b += 1
        if b == 81:
            return b
        else:
            print "The inserted string does not have 81 characters"
            return False

    def validate_values_command_line(self):
        """Validate if the string inserted has valid values"""
        valids = '1','2','3','4','5','6','7','8','9','0'
        for x in self.string:
            if x not in valids:
                print "Values in the string are not allowed"
                return False
        return True

    def solve_from_commandline(self):
        """Solves and display on screen the sudoku game resolved"""
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