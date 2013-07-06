# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Oscar Tapia"
__date__ ="$Jul 1, 2013 12:50:42 PM$"

import norvigm
import csv
import collections


""" Definitions for TXT file reading and solving"""
class Read_and_Solve:
    
    def __init__(self):
	pass

    def reading_txt(self, txt_file):
        f1 = open(txt_file,'r')
        r = f1.read()
        f1.close()
        return r

    def validate_size_txt(self, txt_file):
        r = self.reading_txt(txt_file)
        a = 0
        for x in r:
                if(x != '\n'):
                    a += 1
        return a

    def validate_values_txt(self,txt_file):
        r = self.reading_txt(txt_file)
        validos = '1','2','3','4','5','6','7','8','9','0','\n'
        for x in r:
                if x not in validos:
                    return False
        return True






    def solved_sudoku_txt(self,txt_file):
        a = self.reading_txt(txt_file)
        if(self.validate_size_txt(txt_file)==81 and self.validate_values_txt(txt_file)):
            cadena = ''
            for x in a:
                if(x != '\n'):
                    cadena += x
        resdict = norvigm.parse_grid(cadena)
        ordered = collections.OrderedDict(sorted(resdict.items()))



        cad = ''
        for k, v in ordered.iteritems():
            cad += v
        sudo = open('resolvedsudoku.txt','w')




        substringlist = [cad[i:i+9] for i in range(0, len(cad), 9)]
        for x in substringlist:
            sudo.write(x+'\n')
        sudo.close()
        suread = open('resolvedsudoku.txt','r')
        sudoread = suread.read()
        suread.close()
        return sudoread


    """Definitions for CSV file reading and solving"""

    def reading_csv(self,csv_file):
        with open(csv_file,'rb') as csvfile:
            reader = list(csv.reader(csvfile))
        return reader


    def validate_size_csv(self,csv_file):
        cs = self.reading_csv(csv_file)
        a = 0
        for row in cs:
            for column in row:
                a += 1
        return a

    def validate_values_csv(self,csv_file):
        cs = self.reading_csv(csv_file)
        validos = '1','2','3','4','5','6','7','8','9','0'
        for row in cs:
            for column in row:
                if column not in validos:
                    return False
        return True

    """Definitions for command line reading and solving"""

    def reading_command_line():
        if raw_input('Please insert a string with 81 characters to play the sudoku game : \n'):
            return True

    def validate_size_command_line():
        a = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        b = 0
        for x in a:
            b += 1
        print b
        return b

    def validate_values_command_line():
        a = raw_input('Please insert a string with 81 characters to play the sudoku game : \n')
        validos = '1','2','3','4','5','6','7','8','9','0'
        for x in a:
            if x not in validos:
                return False
        return True