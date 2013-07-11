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
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        cad = ''
        for k, v in ordered.iteritems():
            cad += v
        return cad
