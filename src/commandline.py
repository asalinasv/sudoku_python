from norvigalgorithm import *
from convert import GeneralConverter

class CommandLine:
    def __init__(self):
        self.commandline = ''

    """Definitions for command line reading and solving"""

    def reading_command_line(self):
        #commandline = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        if self.commandline != '':
            return self.commandline
        else:
            return False

    def validate_size_command_line(self):
        #commandline = self.reading_command_line()
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        b = 0
        for x in self.commandline:
            b += 1
        print b
        if b == 81:
            return b
        else:
            print "The inserted string does not have 81 characters"
            return "The inserted string does not have 81 characters"

    def validate_values_command_line(self):
        #commandline = self.reading_command_line()
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        valids = '1','2','3','4','5','6','7','8','9','0'
        for x in self.commandline:
            if x not in valids:
                print "Values in the string are not allowed"
                print x
                return "Values in the string are not allowed"
        return True

    def solve_from_commandline(self):
        #a = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        #commandline = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        norvig = NorvigAlgorithm()
        b = norvig.solve(self.commandline)
        print norvig.display(b)
        generalconv = GeneralConverter()
        cad = generalconv.convert_dictionary_to_string(b)
        return cad


#com = CommandLine()
#com.solve_from_commandline()
#com.validate_size_command_line()
#com.validate_values_command_line()