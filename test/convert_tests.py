import unittest
from solver.convert import GeneralConverter
import os
class TestConvert(unittest.TestCase):
    def setUp(self):
        self.convert = GeneralConverter()
        self.validtxt = os.path.abspath("../src/Menu/EmptySudokus/juego.txt")
        self.invalidtxt = os.path.abspath("../src/Menu/EmptySudokus/juego1.txt")
        self.validcsv = os.path.abspath("../src/Menu/EmptySudokus/juego.csv")
        self.invalidcsv = os.path.abspath("../src/Menu/EmptySudokus/juego1.csv")
        self.dictionary = {'G7': '5', 'G6': '3', 'G5': '4', 'G4': '6', 'G3': '9',\
                            'G2': '8', 'G1': '2', 'G9': '1', 'G8': '7', 'C9': '6',\
                            'C8': '1', 'C3': '8', 'C2': '5', 'C1': '9', 'C7': '3',\
                            'C6': '4', 'C5': '2', 'C4': '7', 'E5': '8', 'E4': '5',\
                            'F1': '3', 'F2': '4', 'F3': '6', 'F4': '9', 'F5': '1',\
                            'F6': '2', 'F7': '7', 'F8': '5', 'F9': '8', 'B4': '1',\
                            'B5': '5', 'B6': '8', 'B7': '9', 'B1': '6', 'B2': '3',\
                            'B3': '2', 'B8': '4', 'B9': '7', 'I9': '3', 'I8': '9',\
                            'I1': '1', 'I3': '4', 'I2': '6', 'I5': '7', 'I4': '8',\
                            'I7': '2', 'I6': '5', 'A1': '4', 'A3': '7', 'A2': '1',\
                            'E9': '2', 'A4': '3', 'A7': '8', 'A6': '9', 'A9': '5',\
                            'A8': '2', 'E7': '4', 'E6': '6', 'E1': '7', 'E3': '1',\
                            'E2': '9', 'E8': '3', 'A5': '6', 'H8': '8', 'H9': '4',\
                            'H2': '7', 'H3': '3', 'H1': '5', 'H6': '1', 'H7': '6',\
                            'H4': '2', 'H5': '9', 'D8': '6', 'D9': '9', 'D6': '7',\
                            'D7': '1', 'D4': '4', 'D5': '3', 'D2': '2', 'D3': '5',\
                            'D1': '8'}
        self.matrix = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
                    [9, 0, 0, 3, 0, 5, 0, 0, 1], \
                    [0, 0, 1, 8, 0, 6, 4, 0, 0], \
                    [0, 0, 8, 1, 0, 2, 9, 0, 0], \
                    [7, 0, 0, 0, 0, 0, 0, 0, 8], \
                    [0, 0, 6, 7, 0, 8, 2, 0, 0], \
                    [0, 0, 2, 6, 0, 9, 5, 0, 0], \
                    [8, 0, 0, 2, 0, 3, 0, 0, 9], \
                    [0, 0, 5, 0, 1, 0, 3, 0, 0]]

        self.string = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        self.invalidstring = '11483921657967345821251876493548132976729564138136798245372689514814253769695417382'

### ******* Unittest for convert class *************

    def test_if_txt_file_is_converted_to_string(self):
        expected = type(self.validtxt)
        self.assertEqual(expected,type(self.convert.convert_txt_file_to_string(self.validtxt)))

    def test_if_string_from_txt_file_is_correct_converted(self):
        expected = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertEqual(expected,self.convert.convert_txt_file_to_string(self.validtxt))

    def test_if_txt_file_convert_display_a_friendly_message_for_invalid_input(self):
        expected = "Please insert a txt file with the correct dimensions"
        self.assertEqual(expected,self.convert.convert_txt_file_to_string(self.invalidtxt))

    def test_if_csv_file_is_converted_to_string(self):
        expected = type(self.validcsv)
        self.assertEqual(expected,type(self.convert.convert_csv_file_to_string(self.validcsv)))

    def test_if_string_from_csv_file_is_correct_converted(self):
        expected = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertEqual(expected,self.convert.convert_csv_file_to_string(self.validcsv))

    def test_if_csv_file_convert_display_a_friendly_message_for_invalid_input(self):
        expected = "Please insert a csv file with the correct dimensions"
        self.assertEqual(expected,self.convert.convert_csv_file_to_string(self.invalidcsv))

    def test_if_dictionary_is_converted_to_string(self):
        expected = '417369825632158947958724316825437169791586432346912758289643571573291684164875293'
        self.assertEqual(expected,self.convert.convert_dictionary_to_string(self.dictionary))

    def test_if_txt_file_is_converted_to_matrix(self):
        expected = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
                    [9, 0, 0, 3, 0, 5, 0, 0, 1], \
                    [0, 0, 1, 8, 0, 6, 4, 0, 0], \
                    [0, 0, 8, 1, 0, 2, 9, 0, 0], \
                    [7, 0, 0, 0, 0, 0, 0, 0, 8], \
                    [0, 0, 6, 7, 0, 8, 2, 0, 0], \
                    [0, 0, 2, 6, 0, 9, 5, 0, 0], \
                    [8, 0, 0, 2, 0, 3, 0, 0, 9], \
                    [0, 0, 5, 0, 1, 0, 3, 0, 0]]
        self.assertEqual(expected,self.convert.convert_txt_file_to_matrix(self.validtxt))

    def test_if_convert_txt_file_to_matrix_returns_frienly_message(self):
        expected = False
        self.assertEqual(expected,self.convert.convert_txt_file_to_matrix(self.invalidtxt))

    def test_if_matrix_is_converted_to_string_correctly(self):
        expected = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertEqual(expected,self.convert.convert_matrix_to_string(self.matrix))

    def test_if_string_is_converted_to_matrix_correctly(self):
        expected = [['4', '8', '3', '9', '2', '1', '6', '5', '7'], \
                    ['9', '6', '7', '3', '4', '5', '8', '2', '1'], \
                    ['2', '5', '1', '8', '7', '6', '4', '9', '3'], \
                    ['5', '4', '8', '1', '3', '2', '9', '7', '6'], \
                    ['7', '2', '9', '5', '6', '4', '1', '3', '8'], \
                    ['1', '3', '6', '7', '9', '8', '2', '4', '5'], \
                    ['3', '7', '2', '6', '8', '9', '5', '1', '4'], \
                    ['8', '1', '4', '2', '5', '3', '7', '6', '9'], \
                    ['6', '9', '5', '4', '1', '7', '3', '8', '2']]
        self.assertEqual(expected,self.convert.convert_string_to_matrix(self.string))

    def test_if_convert_string_to_matrix_returns_frienly_message_for_invalid_input(self):
        expected = False
        self.assertEqual(expected,self.convert.convert_string_to_matrix(self.invalidstring))
        
    def test_if_string_is_converted_to_matrix_of_integers_correctly(self):
        expected = [[4, 8, 3, 9, 2, 1, 6, 5, 7], [9, 6, 7, 3, 4, 5, 8, 2, 1], \
                    [2, 5, 1, 8, 7, 6, 4, 9, 3], [5, 4, 8, 1, 3, 2, 9, 7, 6], \
                    [7, 2, 9, 5, 6, 4, 1, 3, 8], [1, 3, 6, 7, 9, 8, 2, 4, 5], \
                    [3, 7, 2, 6, 8, 9, 5, 1, 4], [8, 1, 4, 2, 5, 3, 7, 6, 9], \
                    [6, 9, 5, 4, 1, 7, 3, 8, 2]]
        self.assertEqual(expected,self.convert.convert_string_to_matrix_int(self.string))

    def test_if_convert_string_to_matrix_of_integers_returns_frienly_message_for_invalid_input(self):
        expected = False
        self.assertEqual(expected,self.convert.convert_string_to_matrix_int(self.invalidstring))

    def test_if_convert_matrix_to_dictionary_is_working_correctly(self):
        expected = {'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0',\
                    'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9',\
                    'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0',\
                    'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0',\
                    'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0',\
                    'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0',\
                    'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0',\
                    'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0',\
                    'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0',\
                    'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0',\
                    'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8',\
                    'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9',\
                    'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0',\
                    'B8': '0', 'B9': '1', 'D1': '0'}
        self.assertEqual(expected,self.convert.convert_matrix_to_dict(self.matrix))


if __name__ == '__main__':
    unittest.main()
