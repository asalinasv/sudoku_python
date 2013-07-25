# StoreSetting Class , retrieve file name and settings for configuration file
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest
import os
import sys
sys.path.append('../src/Configuration')

from Configuration.store_setting import StorerSetting


class TestStorerSettingClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.file_not_exist = ''
        self.settings03 = {'Output_file':'Csv', 'Default_alghoritm':'Norvig', 'Dificult_level':'Medium'}
        self.settings04 = {'Output_file':'Txt', 'Default_alghoritm':'Backtracking', 'Dificult_level':'Easier'}
        self.store = StorerSetting("config.ini", self.settings03)
        self.store2 = StorerSetting("pepito.ini", self.settings04)

    """def test_that_new_settings_are_stored_in_config_file(self):
        test01 = self.store.save_txt_config_file()
        self.assertEqual("File Created", test01)"""

        
    """def test_if_exist_config_file_it_is_overwritten(self):
        test01 = self.store3.save_txt_config_file()
        self.assertEqual("File Created", test01)"""

if __name__ == '__main__':
    unittest.main()