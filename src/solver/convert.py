# GeneralConverver class: auxiliar class that helps to return the desire input
#                         for the required classes.
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import collections
from readfiles import *

class GeneralConverter:
    def __init__(self):
        pass
        
    def convert_txt_file_to_string(self,txt_file):
        """ Convert a txt file into a string """
        txtreader = SudokuFileReader(txt_file)
        buffertxt = txtreader.reading_txt()
        if(txtreader.validate_size_txt()==81 and txtreader.validate_values_txt()):
            string = ''
            for x in buffertxt:
                if(x != '\n'):string += x
            return string
        else:
            print "Please insert a txt file with the correct dimensions"
            return "Please insert a txt file with the correct dimensions"

    def convert_csv_file_to_string(self,csv_file):
        """ Convert a csv file into a string """
        csvreader = SudokuFileReader(csv_file)
        buffercsv = csvreader.reading_csv()
        if(csvreader.validate_size_csv()==81 and csvreader.validate_values_csv()):
            string = ''
            for i in buffercsv:
                for j in i:
                    string += j
            return string
        else:
            print "Please insert a csv file with the correct dimensions"
            return "Please insert a csv file with the correct dimensions"


    def convert_dictionary_to_string(self,dictionary):
        """ Order and convert a dictionary into a string """
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        string = ''
        for k, v in ordered.iteritems():
            string += v
        return string

    def convert_txt_file_to_matrix(self,txt_file):
        """ Convert a txt file to a matrix of integers """
        txtreader = SudokuFileReader(txt_file)
        buffertxt = txtreader.reading_txt()
        M=[]
        for i in range(9):
            M.append([0]*9)
        i = 0
        j = 0
        try:
            for x in buffertxt:
                if(x != '\n'):
                    M[i][j] = int(x)
                    j += 1
                    if(j == 9):
                        i += 1
                        j = 0
        except ValueError:
            print "PLEASE INSERT A 9x9 MATRIZ in a TXT file"
            return False
        return M

    def convert_matrix_to_string(self,matrix):
        """ Convert a matrix to a string  """
        string = ''
        for i in matrix:
            for j in i:
                string += str(j)
        return string

    def convert_string_to_matrix(self, string):
        """ Convert a string to a matrix"""
        M=[]
        for i in range(9):
            M.append([0]*9)
        i = 0
        j = 0
        try:
            for x in string:
                M[i][j] = str(x)
                j += 1
                if(j == 9):
                    i += 1
                    j = 0
        except IndexError:
            print "PLEASE INSERT A 9x9 MATRIZ in a TXT file"
            return False
        return M

    def convert_string_to_matrix_int(self, string):
        """ Convert a string to a matrix"""
        M=[]
        for i in range(9):
            M.append([0]*9)
        i = 0
        j = 0
        try:
            for x in string:
                M[i][j] = int(x)
                j += 1
                if(j == 9):
                    i += 1
                    j = 0
        except IndexError:
            print "PLEASE INSERT A 9x9 MATRIZ in a TXT file"
            return False
        return M

    def convert_matrix_to_dict(self,matrix):
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.cross(self.rows, self.cols)
        dictionary = {}
        for x in self.squares:
            dictionary[x] = x
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        dicti = {}
        i = 0
        j = 0
        for x in ordered:
            dicti[x] = str(matrix[i][j])
            j += 1
            if(j==9):
                i += 1
                j = 0
        return dicti
            
    def cross(self, A, B):
        "Cross product of elements in A and elements in B."
        return [a+b for a in A for b in B]