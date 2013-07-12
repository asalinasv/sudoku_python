import unittest
from convert import GeneralConverter

class TestConvert(unittest.TestCase):
    def setUp(self):
        self.convert = GeneralConverter()
        self.validtxt = "juego.txt"
        self.invalidtxt = "juego1.txt"
        self.validcsv = "juego.csv"
        self.invalidcsv = "juego1.csv"

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
   
if __name__ == '__main__':
    unittest.main()
