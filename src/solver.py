from convert import *
from norvigalgorithm import NorvigAlgorithm

class Solver(ReadFiles):
    def __init__(self,file):
        ReadFiles.__init__(self,file)
        self.convert = Convert()
        self.norvigalg = NorvigAlgorithm()

    def norvig_algorithm(self):
        if(self.gettype()== "TXT File"):
            if(self.validate_size_txt()==81 and self.validate_values_txt()):
                a = self.convert.txt_file_to_string(self.file)
            else:
                print "Please insert the correct data and size in the txt file"
                return "Please insert the correct data and size in the txt file"
        if(self.gettype()== "CSV File"):
            if(self.validate_size_csv()==81 and self.validate_values_csv()):
                a = self.convert.csv_file_to_string(self.file)
            else:
                print "Please insert the correct data and size in the csv file"
                return "Please insert the correct data and size in the csv file"
        if(self.gettype()== "invalid extension"):
            print "Please insert a valid dimension"
            return "invalid extension"
        resdict = self.norvigalg.parse_grid(a)
        self.norvigalg.display(resdict)
        resstring = self.convert.dictionary_to_string(resdict)
        return resstring
        
    def store_solution_in_txt_file(self):
        sudo = open('resolvedsudoku.txt','w')
        cad = self.norvig_algorithm()
        substringlist = [cad[i:i+9] for i in range(0, len(cad), 9)]
        for x in substringlist:
            sudo.write(x+'\n')
        sudo.close()
        suread = open('resolvedsudoku.txt','r')
        sudoread = suread.read()
        suread.close()
        return sudoread


