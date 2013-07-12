import collections
from readfiles import *

class GeneralConverter:
    def __init__(self):
        pass
        
    def convert_txt_file_to_string(self,txt_file):
        txtreader = ReadFiles(txt_file)
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
        csvreader = ReadFiles(csv_file)
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
        ordered = collections.OrderedDict(sorted(dictionary.items()))
        string = ''
        for k, v in ordered.iteritems():
            string += v
        return string
