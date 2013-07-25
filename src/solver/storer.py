# Storer Class , store sudoku game in txt or cvs file, receiving a list of list
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
from time import gmtime, strftime

class Storer:

    def __init__(self, matrix, file_name, extension):
        self.matrix_sudoku = matrix
        self.sudoku_file = file_name
        self.sudoku_extension = extension

    def verify_right_matrix(self):
        num_elements = len(self.matrix_sudoku)
        count = 0
        for i in range (num_elements):
            for j in range(len(self.matrix_sudoku[i])):
                if int(self.matrix_sudoku[i][j])>=0 and int(self.matrix_sudoku[i][j])<=9:
                    count +=1
        return count

    def save_matrix_to_file(self):
        if self.sudoku_extension != '':
            if self.file_already_exist() == False:
                f = open(self.sudoku_file + "." + self.sudoku_extension, 'w')
                f.write(self.return_cadena(self.sudoku_extension))
                f.close
                return "The file was created"
            else:
                f = open(self.sudoku_file +strftime("%Y%m%d%H%M%S", gmtime())+ "." + self.sudoku_extension, 'w')
                f.write(self.return_cadena(self.sudoku_extension))
                f.close 
                return "The file was created with the same name + datetime"

    def return_cadena(self, format_file):
        num_rows = len(self.matrix_sudoku)
        sudoku_string = ''
        if format_file == 'txt':
            for i in range(num_rows):
                for j in range (num_rows):
                    sudoku_string += self.matrix_sudoku[i][j]+" "
                sudoku_string +="\n"
            return sudoku_string
        if format_file == 'csv':
            for i in range(num_rows):
                for j in range (num_rows):
                    sudoku_string += self.matrix_sudoku[i][j]+", "
                sudoku_string +="\n"
            return sudoku_string
    
    def file_already_exist(self):
        try:
            f = open(self.sudoku_file + "." + self.sudoku_extension, 'r')
            return True

        except IOError:
            return False
