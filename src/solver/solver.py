# Solver class, read inputs for sudoku from csv and txt
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import time
from convert import *
from norvigalgorithm import NorvigAlgorithm
from sudokubacktrack import *
from Configuration.readconfiguration import *
from display import *

class Solver(SudokuFileReader):
    def __init__(self,file):
        SudokuFileReader.__init__(self,file)
        self.convert = GeneralConverter()
        self.norvigalg = NorvigAlgorithm()
        absolutepath = os.path.abspath("../Configuration/config.ini")
        self.readconf = FileReader(absolutepath)

    def solvesudoku(self):
        """Solves the Sudoku based in the configuration file settings"""
        print self.readconf.read_default_algorithm()
        if(self.readconf.read_default_algorithm() == 'Norvig'):
           return self.solve_using_norvig_algorithm()
        if(self.readconf.read_default_algorithm() == 'Backtracking'):
            return self.solve_using_backtracking_algorithm()
        else:
            print "The algorithm specified in the configuration file is invalid\
                    \n Please set a valid algorithm"
            return False
        
    def solve_using_norvig_algorithm(self):
        """ Calls the norvigalgorithm class to solve the specified file """
        if(self.gettype()== "TXT File"):
            if(self.validate_size_txt()==81 and self.validate_values_txt()):
                a = self.convert.convert_txt_file_to_string(self.file)
            else:
                print "\n\nPlease insert the correct data and size in the "+self.file+" file\
                        \n  Or specify another file"
                time.sleep(7.0)
                return False
        if(self.gettype()== "CSV File"):
            if(self.validate_size_csv()==81 and self.validate_values_csv()):
                a = self.convert.convert_csv_file_to_string(self.file)
            else:
                print "\n\nPlease insert the correct data and size in the "+self.file+" file\
                        \n  Or specify another file"
                time.sleep(7.0)
                return False
        if(self.gettype()== "invalid extension"):
            print "Please insert a valid dimension"
            return "invalid extension"
        resdict = self.norvigalg.solve(a)
        print "Sudoku has been resolved successfully\n\n"
        print "Sudoku solved using Norvig Algorithm\n\n"
        resstring = self.convert.convert_dictionary_to_string(resdict)
        matrix = self.convert.convert_string_to_matrix(resstring)
        SudokuDisplayer(matrix).displaysudoku()
        return matrix

    def solve_using_backtracking_algorithm(self):
        """ Calls the backtracking class to solve the specified file """
        if(self.gettype()== "TXT File"):
            if(self.validate_size_txt()==81 and self.validate_values_txt()):
                a = self.convert.convert_txt_file_to_matrix(self.file)
            else:
                print "\n\nPlease insert the correct data and size in the "+self.file+" file\
                        \n  Or specify another file"
                time.sleep(7.0)
                return False
        if(self.gettype()== "CSV File"):
            if(self.validate_size_csv()==81 and self.validate_values_csv()):
                b = self.convert.convert_csv_file_to_string(self.file)
                a = self.convert.convert_string_to_matrix_int(b)
            else:
                print "\n\nPlease insert the correct data and size in the "+self.file+" file\
                        \n  Or specify another file"
                time.sleep(7.0)
                return False
        if(self.gettype()== "invalid extension"):
            print "Please insert a valid dimension"
            return "invalid extension"
        sudokubacktrack = Backtracking(a,9)
        resmatrix = sudokubacktrack.solve_backtracking(a)
        print "Sudoku has been resolved successfully\n\n"
        print "Sudoku solved using Backtracking Algorithm\n\n"
        a = self.convert.convert_matrix_to_string(resmatrix)
        matrixstr = self.convert.convert_string_to_matrix(a)
        SudokuDisplayer(matrixstr).displaysudoku()
        return matrixstr

    def solve_sudoku_game_backtracking(self, matrix):
        """
        @author: Ana Salinas
        method added to link solver with hintsdiplayer methods
        """
        if len(matrix)<9 or len(matrix)>9:
            return "Invalid matrix"
        else:
            sudokubacktrack = Backtracking(matrix, 9)
            resolved_matrix = sudokubacktrack.solve_backtracking(matrix)
                
        return resolved_matrix

    def solve_sudoku_game_norvig(self, matrix):
        """
        @author: Ana Salinas
        method added to link solver with hintsdiplayer methods
        """
        if len(matrix)<9 or len(matrix)>9:
            return "Invalid matrix"
        else:
            a = self.convert.convert_matrix_to_string(matrix)
            resdict = self.norvigalg.solve(a)
            resstring = self.convert.convert_dictionary_to_string(resdict)
            #return resstring
            resolved_matrix = self.convert.convert_string_to_matrix(resstring)
            
        return resolved_matrix