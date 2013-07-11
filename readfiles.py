import csv

class ReadFiles:
    def __init__(self,file):
	self.file = file

    def gettype(self):
        if 'txt' in self.file:
            return "TXT File"
        if 'csv' in self.file:
            return "CSV File"
        else:
            return "invalid extension"

    """ Definitions for TXT file reading"""

    def reading_txt(self):
        f1 = open(self.file,'r')
        r = f1.read()
        f1.close()
        return r

    def validate_size_txt(self):
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
        r = self.reading_txt()
        validos = '1','2','3','4','5','6','7','8','9','0','\n'
        for x in r:
                if x not in validos:
                    print "The values from txt files are invalid"
                    return "The values from txt files are invalid"
        return True


    """Definitions for CSV file reading and solving"""

    def reading_csv(self):
        with open(self.file,'rb') as csvfile:
            reader = list(csv.reader(csvfile))
        return reader

    def validate_size_csv(self):
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
        cs = self.reading_csv()
        validos = '1','2','3','4','5','6','7','8','9','0'
        for row in cs:
            for column in row:
                if column not in validos:
                    print "The values from csv files are invalid"
                    return "The values from csv files are invalid"
        return True
