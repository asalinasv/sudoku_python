# Unit Test for Configuration class
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest
import os
import sys
sys.path.append('../src/Configuration')

from Configuration.configuration import Configuration


class TestConfigurationClassAndMethods(unittest.TestCase):
    def setUp(self):
        self.file_name = "config.ini"
       
        #default settings of configuration file
        self.settings01 = {'Default_algorithm': 'Norvig', 'Difficult_level': 'Easier', 'Output_file': 'Txt'}
        {'Default_algorithm': 'Norvig', 'Difficult_level': 'Easier', 'Output_file': 'Txt'}

        self.config01 = Configuration("config.ini")

        self.settings02 = {'Output_file':'csv', 'Default_alghoritm':'Norvig', 'Dificult_level':'Easier'}
        self.config02 = Configuration("config.ini")
        
        self.settings03 = ['Output_file:Txt\n','Default_alghoritm:Backtracking\n','Dificult_level:Easier\n']
        self.config03 = Configuration("config.ini")

        self.settings04 = ['Output_file:Txt\n', 'Default_alghoritm:Backtracking\n', 'Dificult_level:Easier\n','CustomX:ValueX']
        self.config04 = Configuration("config.ini")

    def test_configuration_file_has_Default_values(self):
        configsetting = self.config01.leave_default_value()
        self.assertEqual(self.settings01, configsetting)

    def test_an_existing_setting_is_properly_modified(self):
        configsetting = self.config02.modify_existing_settings("Difficult_level", "Easier")
        self.assertEqual(self.config02.settings, configsetting)
        
    def test_that_a_new_setting_is_added_to_setting_list(self):
        new_parameter = self.config04.add_new_custom_setting("CustomX", "ValueX")
        self.assertEqual(self.settings04, new_parameter)
        
    def test_all_existing_settings_are_modified(self):
        configsetting = Configuration("config.ini")
        self.assertEqual(self.settings03, configsetting.settings)

    def test_all_existing_settings_are_left_by_default(self):
        self.assertEqual(self.settings01, self.config01.leave_default_value())

    def test_no_changes_is_made_when_not_existent_seeting_is_being_modified(self):
        configsetting = self.config02.modify_existing_settings("Anything", "csv")
        self.assertFalse(self.config02.settings)

    def test_that_when_custom_setting_value_is_empty_the_default_setting_remain_active(self):
        configsetting = self.config02.modify_existing_settings("", "csv")
        self.assertEqual(configsetting, self.config02.settings)

if __name__ == '__main__':
    unittest.main()