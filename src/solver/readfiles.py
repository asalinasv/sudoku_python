import os.path
# SudokuFileReader class, read inputs for sudoku from csv and txt
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
#Automation Class (Sudoku project) - 2013
import csv
import os

class SudokuFileReader:
    def __init__(self,file):
	self.file = file

    def gettype(self):
        """ Returns the type of the file that is being read """
        if 'txt' in self.file:
            return "TXT File"
        if 'csv' in self.file:
            return "CSV File"
        else:
            return "invalid extension"

    """ Definitions for TXT file reading"""

    def reading_txt(self):
        """ Read the data from the txt file """
        f1 = open(self.file,'r')
        r = f1.read()
        f1.close()
        return r
                
    def validate_size_txt(self):
        """ Validate if the txt file contains 81 characters """
        r = self.reading_txt()
        a = 0
        for x in r:
            if(x != '\n'):
                a += 1
        if a == 81:
            return a
        else:
            print "The dimensions inserted are invalid for txt"
            return "The dimensions inserted are invalid"

    def validate_values_txt(self):
        """ Validate if the txt has values between 0 and 9 """
        r = self.reading_txt()
        validos = '1','2','3','4','5','6','7','8','9','0','\n'
        for x in r:
                if x not in validos:
                    print "The values from txt files are invalid"
                    return False
        return True

    """Definitions for CSV file reading """

    def reading_csv(self):
        """ Read the data from the csv file """
        with open(self.file,'rb') as csvfile:
            reader = list(csv.reader(csvfile))
        return reader

    def validate_size_csv(self):
        """ Validate if the csv file contains 81 characters """
        cs = self.reading_csv()
        a = 0
        for row in cs:
            for column in row:
                a += 1
        if a==81:
            return a
        else:
            print "The dimensions inserted are invalid for csv"
            return "The dimensions inserted are invalid"

    def validate_values_csv(self):
        """ Validate if the csv has values between 0 and 9 """
        cs = self.reading_csv()
        validos = '1','2','3','4','5','6','7','8','9','0'
        for row in cs:
            for column in row:
                if column not in validos:
                    print "The values from csv files are invalid"
                    return "The values from csv files are invalid"
        return True

#sud = SudokuFileReader("juego.txt")
#sud.reading_txt()