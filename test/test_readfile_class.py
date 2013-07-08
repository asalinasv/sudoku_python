# Unit Test for Read configuration file by usign 2 clases Configuration and ReadConfiguration
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest
from readconfiguration import ReadFile

class TestReadFileClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.read_file = ReadFile("config.ini",)
        self.out_put_file_not_exist = ''
        self.file_empty = " "
        self.right_format = "['Output_file:Txt']['Default_alghoritm:Backtracking']['Dificult_level:Easier']"
     
    def test_verify_config_file_exist(self):
        exist_file = self.read_file.file_exist()
        self.assertEqual(True, exist_file)
  
    def test_verify_config_file_is_empty(self):
        empty_file = self.read_file.file_is_empty()
        self.assertEqual(False,empty_file)

    def test_verify_config_file_has_right_format_settings_name(self):
        format_file_name = self.read_file.right_configuration_format()
        self.assertEqual(self.right_format, format_file_name)
    
    def test_verify_config_file_has_the_new_custom_values(self):
        custom_setting_file = self.read_file.file_exist()
        self.assertEqual(True, custom_setting_file)

    def test_an_error_is_raised_when_there_is_not_file(self):
        pass

    def test_an_error_is_raised_when_the_file_is_empty(self):
        pass
        
    def test_just_right_extension_file_is_read(self):
        pass

if __name__ == '__main__':
    unittest.main()