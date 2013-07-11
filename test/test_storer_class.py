# TestStorerClassAndMEthods test all basic cases about Storer class
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest

from storer import Storer

class TestStorerClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.file_name = "testeo"
        self.extension_txt = "txt"
        self.extension_csv = "csv"
        self.matrix = ['9','3','8','4','7','5','1','6','2'],['1','4','6','9','3','2','7','5','8'],['7','5','2','8','6','1','9','4','3'],\
                      ['8','9','1','6','4','3','2','7','5'],['3','6','5','2','9','7','8','1','4'],['4','2','7','1','5','8','6','3','9'],\
                      ['5','8','3','7','2','6','4','9','1'],['2','7','9','3','1','4','5','8','6'],['6','1','4','5','8','9','3','2','7']
        self.store01 = Storer(self.matrix, self.file_name, self.extension_txt)
        self.store02 = Storer(self.matrix, self.file_name, self.extension_csv)

    def test_storer_receive_righ_number_of_elements_from_1_to_9_be_stored(self):
        num_elements = self.store01.verify_right_matrix()
        self.assertEqual (81, num_elements)

    def test_a_sudoku_solution_is_storer_in_txt_format(self):
        self.store01.save_matrix_to_file()
        self.assertTrue(self.file_exist(self.store01.sudoku_file,self.store01.sudoku_extension))

    def test_a_sudoku_solution_is_storer_in_csv_format(self):
        self.store02.save_matrix_to_file()
        self.assertTrue(self.file_exist(self.store02.sudoku_file,self.store02.sudoku_extension))
    
    def test_if_the_file_already_exist_an_alert_is_displayed(self):
        error = self.store02.save_matrix_to_file()
        self.assertEqual("File already exist", error)

    def file_exist(self, f_name, extension_file):
        """
        This def is auxiliar to verify that the new file was created properly.
        """
        try: 
            f=open(f_name+"."+extension_file,'r')
            f.read()
            f.close()
            return True
            
        except IOError:
            return IOError

if __name__ == '__main__':
  
    unittest.main()
    