import collections
from readfiles import *

class Convert:
    def __init__(self):
        pass
        
    def txt_file_to_string(self,txt_file):
        leer = ReadFiles(txt_file)
        a = leer.reading_txt()
        if(leer.validate_size_txt()==81 and leer.validate_values_txt()):
            cadena = ''
            for x in a:
                if(x != '\n'):cadena += x
            return cadena
        else:
            print "Please insert a txt file with the correct dimensions"
            return "Please insert a txt file with the correct dimensions"

    def csv_file_to_string(self,csv_file):
        leercsv = ReadFiles(csv_file)
        leer = leercsv.reading_csv()
        if(leercsv.validate_size_csv()==81 and leercsv.validate_values_csv()):
            cadena = ''
            for i in leer:
                for j in i:
                    cadena += j
            return cadena
        else:
            print "Please insert a csv file with the correct dimensions"
            return "Please insert a csv file with the correct dimensions"


    def dictionary_to_string(self,dictionary):
        #resdict = norvigm.parse_grid(cadena)
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        cad = ''
        for k, v in ordered.iteritems():
            cad += v
        return cad

    #def
#convert = Convert()
#convert.csv_file_to_string("juego.csv")


#leer = ReadFiles(txt_file)

"""conver = Convert()
a = conver.txt_file_to_string("juego.txt")
b = {'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
c = conver.dictionary_to_string(b)
print c
print a
"""