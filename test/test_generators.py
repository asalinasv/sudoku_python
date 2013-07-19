import unittest 
import os
import sys
sys.path.append('../src/Player')

from generators import SudokuGenerator


class TestGeneratorClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.error_message = 'There is not Sudoku game for this difficult level'
        self.error_message_empty = 'No Setting'
        self.generate_game_error = SudokuGenerator("config0.ini")
        self.generate_game_easy = SudokuGenerator("config.ini")
        self.generate_game_medium = SudokuGenerator("config1.ini")
        self.generate_game_hard = SudokuGenerator("config2.ini")
        self.generate_game_empty = SudokuGenerator("config_empty.ini")

    def test_that_a_easier_sudoku_game_is_created_when_conf_file_is_Set_with_Easier_level(self):
        value = self.generate_game_easy.read_file()
        self.assertEqual(9, len(value))

    def test_that_a_medium_sudoku_game_is_created_when_conf_file_is_Set_with_Medium_level(self):
        value = self.generate_game_medium.read_file()
        self.assertEqual(9, len(value))
    
    def test_that_a_difficult_sudoku_game_is_created_when_conf_file_is_Set_with_Difficult_level(self):
        value = self.generate_game_hard.read_file()
        self.assertEqual(9, len(value))
    
    def test_an_error_should_be_displayed_when_the_selected_difficul_level_does_not_exist(self):
        value = self.generate_game_error.retrieve_file_names()
        self.assertEqual(self.error_message, value)
    
    def test_an_error_should_be_displayed_when_there_the_difficult_level_is_empty(self):
        value = self.generate_game_empty.retrieve_file_names()
        self.assertEqual(self.error_message_empty, value)

    
if __name__ == '__main__':
    unittest.main()  
    