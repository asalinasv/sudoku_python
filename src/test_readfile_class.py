# Unit Test for Read configuration file by usign 2 clases Configuration and ReadConfiguration
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest
from readconfiguration import FileReader

class TestFileReaderClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.read_file = FileReader("config.ini")
        self.read_file1 = FileReader("config_empty.ini")
        self.read_file2 = FileReader("config_no_rigth_format.ini")
        self.read_file01 = FileReader("anything.ini")
        self.read_file02 = FileReader("anything.xls")
        self.out_put_file_not_exist = ''
        self.file_empty = " "
        self.right_format = "['Output_file:Txt']['Default_alghoritm:Backtracking']['Dificult_level:Easier']"
     
    def test_verify_config_file_exist(self):
        exist_file = self.read_file.file_exist()
        self.assertEqual(True, exist_file)
  
    def test_verify_config_file_is_empty(self):
        empty_file = self.read_file.file_is_empty()
        self.assertEqual(False, empty_file)

    def test_when_config_file_is_empty_return_True(self):
        empty_file = self.read_file1.file_is_empty()
        self.assertEqual(True, empty_file)

    def test_verify_config_file_has_right_extension_ini(self):
        format_file_name = self.read_file.right_configuration_extension()
        self.assertTrue(format_file_name)
    
    def test_verify_config_file_has_the_new_custom_values(self):
        custom_setting_file = self.read_file.file_exist()
        self.assertEqual(True, custom_setting_file)

    def test_just_right_extension_file_is_read(self):
        self.assertTrue(self.read_file.right_configuration_extension())

    def test_that_a_no_defined_extension_file_is_not_taken_into_account(self):
        self.assertFalse(self.read_file02.right_configuration_extension())

    def test_that_config_file_has_the_right_info_according_to_defiened_format(self):
        read0=self.read_file.right_contain_of_the_ini_file()
        self.assertEqual(read0,self.right_format)

    def test_an_error_is_raised_when_there_is_not_file(self):
        read01=self.read_file01.file_exist()
        self.failureException(read01)

    


if __name__ == '__main__':
    unittest.main()