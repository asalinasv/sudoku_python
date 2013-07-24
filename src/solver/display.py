# SudokuDisplayer class: class that displays the sudokus in screen.
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013
from convert import *
class SudokuDisplayer:
    def __init__(self,matrix):
        self.matrix = matrix
        self.conv = GeneralConverter()

    def displaysudoku(self):
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.cross(self.rows, self.cols)
        a = self.conv.convert_matrix_to_dict(self.matrix)
        return self.display(a)

    def cross(self, A, B):
        "Cross product of elements in A and elements in B."
        return [a+b for a in A for b in B]

    def display(self,values):
        "Display these values as a 2-D grid."
        row_number = 0
        if values==False:
            print "Norvig algorithm is receiving an input different of 81 characters"
            return False
        else:
            print "\tA-B-C--D-E-F--G-H-I"
            width = 1+max(len(values[s]) for s in self.squares)
            line = '+'.join(['-'*(width*3)]*3)
            for r in self.rows:
                row_number += 1
                print str(row_number) + "|", '\t',
                print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                              for c in self.cols)
                if r in 'CF':
                    print '\t' + line
            print
            return True

