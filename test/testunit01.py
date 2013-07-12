# Unit Test for Read configuration file by usign 2 clases Configuration and ReadConfiguration
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import unittest
from readconfiguration import ReadFile
from configuration import Configuration, StoreSetting

class TestReadFileClassAndMethods(unittest.TestCase):

    def setUp(self):
        self.read_file=ReadFile("config.ini",)
        self.out_put_file_not_exist=''
        self.file_empty=" "
        self.right_format="['Output_file:Txt']['Default_alghoritm:Backtracking']['Dificult_level:Easier']"
       
     
    def test_verify_config_file_exist(self):
        exist_file=self.read_file.file_exist()
        self.assertEqual(True,exist_file)
  
    def test_verify_config_file_is_empty(self):
        empty_file=self.read_file.file_is_empty()
        self.assertEqual(False,empty_file)

    def test_verify_config_file_has_right_format_settings_name(self):
        format_file_name=self.read_file.right_configuration_format()
        self.assertEqual(self.right_format,format_file_name)
    
    def test_verify_config_file_has_the_new_custom_values(self):
        custom_setting_file=self.read_file.file_exist()
        self.assertEqual(True,custom_setting_file)
    def test_an_error_is_raised_when_there_is_not_file(self):
        pass
    def test_an_error_is_raised_when_the_file_is_empty(self):
        pass

class TestConfigurationClassAndMethods(unittest.TestCase):
    def setUp(self):
        pass
    def test_configuration_file_has_Default_values(self):
        pass
    def test_an_existing_setting_is_modified(self):
        pass
    def test_all_existing_settings_are_modified(self):
        pass
    def test_all_existing_settings_are_left_by_default(self):
        pass
    def test_that_a_new_setting_is_added_to_setting_list(self):
        pass
    def test_no_changes_is_made_when_not_existent_seeting_is_being_modified(self):
        pass
    def test_that_when_custom_setting_value_is_empty_the_default_setting_remain_active(self):
        pass

class TestStoreSettingClassAndMethods(unittest.TestCase):
    def setUp(self):
        self.file_not_exist=''
        self.settings03 = {'Output_file':'Csv', 'Default_alghoritm':'Norvig', 'Dificult_level':'Medium'}
        self.settings04 = {'Output_file':'Txt', 'Default_alghoritm':'Backtracking', 'Dificult_level':'Easier'}
        self.store3=StoreSetting("config1.ini",self.settings03)
        self.store4=StoreSetting("config.ini",self.settings04)


    def test_that_new_setting_are_stored_in_config_file(self):
        test01=self.store3.save_txt_config_file()
        self.assertEqual("File Created",test01)

    def test_if_no_exist_config_file_a_new_one_is_created(self):
        test02=self.store4.save_txt_config_file()
        self.assertEqual("File Created",test02)
        
    def test_if_exist_config_file_it_is_overwritten(self):
        test01=self.store3.save_txt_config_file()
        self.assertEqual("File Created",test01)

if __name__ == '__main__':
    unittest.main()