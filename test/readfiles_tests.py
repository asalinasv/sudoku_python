import unittest
import csv
from readfiles import ReadFiles

class TestReadFiles(unittest.TestCase):
    def setUp(self):
        self.txtfile = "juego.txt"
        self.txtfile1 = "juego1.txt"
        self.csvfile = "juego.csv"
        self.readvalidtxt = ReadFiles("juego.txt")
        self.readinvalidtxt = ReadFiles("juego1.txt")
        self.readvalidcsv = ReadFiles("juego.csv")
        self.readinvalidcsv = ReadFiles("juego1.csv")
        self.invalidfile = ReadFiles("hola.png")
               
    def test_if_gettype_verifies_a_txt_file(self):
        expected = "TXT File"
        self.assertEqual(expected, self.readvalidtxt.gettype())

    def test_if_gettype_verifies_a_csv_file(self):
        expected = "CSV File"
        self.assertEqual(expected, self.readvalidcsv.gettype())

    def test_if_gettype_verifies_another_file_extension(self):
        expected = "invalid extension"
        self.assertEqual(expected, self.invalidfile.gettype())

    def test_if_solver_is_able_to_read_a_txt_file(self):
        f1 = open(self.txtfile,'r')
        expected = f1.read()
        self.assertEqual(expected, self.readvalidtxt.reading_txt())

    def test_if_txt_has_a_matrix_of_9x9(self):
        expected = 81
        self.assertEqual(expected,self.readvalidtxt.validate_size_txt())

    def test_if_alert_message_is_displayed_for_non_valid_dimentions_in_txt_file(self):
        expected = "The dimensions inserted are invalid"
        self.assertEqual(expected,self.readinvalidtxt.validate_size_txt())

    def test_if_txt_has_values_from_0_to_9(self):
        expected = True  # ??????
        self.assertEqual(expected, self.readvalidtxt.validate_values_txt())

    def test_if_alert_message_is_displayed_for_non_valid_values_in_txt_file(self):
        expected = "The values from txt files are invalid"
        self.assertEqual(expected,self.readinvalidtxt.validate_values_txt())

    def test_if_solver_is_able_to_read_a_csv_file(self):
        with open (self.csvfile,'rb') as csvfile:
            expected = list(csv.reader(csvfile))
        self.assertEqual(expected, self.readvalidcsv.reading_csv())

    def test_if_csv_has_a_matrix_of_9x9(self):
        expected = 81
        self.assertEqual(expected,self.readvalidcsv.validate_size_csv())

    def test_if_alert_message_is_displayed_for_non_valid_dimentions_in_csv_file(self):
        expected = "The dimensions inserted are invalid"
        self.assertEqual(expected,self.readinvalidcsv.validate_size_csv())

    def test_if_csv_has_values_from_0_to_9(self):
        expected = True
        self.assertEqual(expected,self.readvalidcsv.validate_values_csv())

    def test_if_alert_message_is_displayed_for_non_valid_values_in_csv_file(self):
        expected = "The values from csv files are invalid"
        self.assertEqual(expected,self.readinvalidcsv.validate_values_csv())



#def test_if_txt_sudoku_is_solved_correctly(self):
     #   f2 = open(self.presolution,'r')
      #  expected = f2.read()
       # f2.close()
       # self.assertEqual(expected, self.readsolve.solved_sudoku_txt(self.txtfile))

if __name__ == '__main__':
    unittest.main()


