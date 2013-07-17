import sudokubacktrack
from convert import *
from norvigalgorithm import NorvigAlgorithm
from sudokubacktrack import *

class Solver(ReadFiles):
    def __init__(self,file):
        ReadFiles.__init__(self,file)
        self.convert = GeneralConverter()
        self.norvigalg = NorvigAlgorithm()

    def norvig_algorithm(self):
        if(self.gettype()== "TXT File"):
            if(self.validate_size_txt()==81 and self.validate_values_txt()):
                a = self.convert.convert_txt_file_to_string(self.file)
            else:
                print "Please insert the correct data and size in the txt file"
                return "Please insert the correct data and size in the txt file"
        if(self.gettype()== "CSV File"):
            if(self.validate_size_csv()==81 and self.validate_values_csv()):
                a = self.convert.convert_csv_file_to_string(self.file)
            else:
                print "Please insert the correct data and size in the csv file"
                return "Please insert the correct data and size in the csv file"
        if(self.gettype()== "invalid extension"):
            print "Please insert a valid dimension"
            return "invalid extension"
        resdict = self.norvigalg.solve(a)
        self.norvigalg.display(resdict)
        resstring = self.convert.convert_dictionary_to_string(resdict)
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

    def backtracking_algorithm(self):
        if(self.gettype()== "TXT File"):
            if(self.validate_size_txt()==81 and self.validate_values_txt()):
                a = self.convert.convert_txt_file_to_matrix(self.file)
            else:
                print "Please insert the correct data and size in the txt file"
                return "Please insert the correct data and size in the txt file"
        if(self.gettype()== "CSV File"):
            if(self.validate_size_csv()==81 and self.validate_values_csv()):
                a = self.convert.convert_csv_file_to_matrix(self.file)
            else:
                print "Please insert the correct data and size in the csv file"
                return "Please insert the correct data and size in the csv file"
        if(self.gettype()== "invalid extension"):
            print "Please insert a valid dimension"
            return "invalid extension"
        #print a
        sudokubacktrack = Backtracking(a,9)
        resmatrix = sudokubacktrack.solve_backtracking(a)
#        print resmatrix

        # resstring = self.convert.convert_dictionary_to_string(resdict)
        # need to be implemented in convert class, ,ethod to convert matrix to string
        return resmatrix

    def store_solution_in_txt_file_bt(self):
        sudo = open('resolvedsudokuisra.txt','w')
        mat = self.backtracking_algorithm()
        cad = self.convert.convert_matrix_to_string(mat)
        substringlist = [cad[i:i+9] for i in range(0, len(cad), 9)]
        for x in substringlist:
            sudo.write(x+'\n')
        sudo.close()
        suread = open('resolvedsudokuisra.txt','r')
        sudoread = suread.read()
        suread.close()
        return sudoread

#isra = Solver("juegoisra.txt")
#a = isra.backtracking_algorithm()
#isra.store_solution_in_txt_file_bt()
#print "Ajjj Isra, controla tu recursividad XD"
#print a
