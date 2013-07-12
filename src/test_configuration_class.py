# Unit Test for Configuration class
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest
from configuration import Configuration


class TestConfigurationClassAndMethods(unittest.TestCase):
    def setUp(self):
        self.file_name = "config.ini"
       
        #default settings of configuration file
        self.settings01 = {'Output_file':'Txt', 'Default_alghoritm':'Norvig', 'Dificult_level':'Easier'}
        self.config01 = Configuration("config.ini", self.settings01)

        self.settings02 = {'Output_file':'csv', 'Default_alghoritm':'Norvig', 'Dificult_level':'Easier'}
        self.config02 = Configuration("config.ini", self.settings02)
        
        self.settings03 = {'Output_file':'txt', 'Default_alghoritm':'Backtracking', 'Dificult_level':'Dificult'}
        self.config03 = Configuration("config.ini", self.settings03)

        self.settings04 = {'Output_file':'txt', 'Default_alghoritm':'Backtracking', 'Dificult_level':'Dificult','CustomX':'ValueX'}
        self.config04 = Configuration("config.ini", self.settings03)

    def test_configuration_file_has_Default_values(self):
        configsetting = self.config01.leave_default_value()
        self.assertEqual(self.settings01, configsetting)

    def test_an_existing_setting_is_properly_modified(self):
        configsetting = self.config02.modify_existing_settings("Output_file", "csv")
        self.assertEqual(self.config02.settings, configsetting)
        
    def test_all_existing_settings_are_modified(self):
        configsetting = Configuration("config.ini", self.settings03)
        self.assertEqual(self.settings03, configsetting.settings)

    def test_all_existing_settings_are_left_by_default(self):
        self.assertEqual(self.settings01, self.config01.leave_default_value())

    def test_that_a_new_setting_is_added_to_setting_list(self):
        new_parameter = self.config04.add_new_custom_setting("CustomX", "ValueX")
        self.assertEqual(self.settings04, new_parameter)

    def test_no_changes_is_made_when_not_existent_seeting_is_being_modified(self):
        configsetting = self.config02.modify_existing_settings("Output_fileX", "csv")
        self.assertNotEqual(configsetting, self.config02.settings)

    def test_that_when_custom_setting_value_is_empty_the_default_setting_remain_active(self):
        configsetting = self.config02.modify_existing_settings(" ", "csv")
        self.assertEqual(configsetting, self.config02.settings)

if __name__ == '__main__':
    unittest.main()