# Configuration Class , retrieve file name and settings for configuration file
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import sys
sys.path.append('./src/Configuration')

from Configuration.readconfiguration import FileReader

class Configuration:
   
    config =['Output_file','Default_algorithm','Difficult_level']
    #settings = {config[0]:'Txt', config[1]:'Norvig', config[2]:'Easier'}
    settings = []

    def __init__(self, config_file):
        self.config_setting = FileReader(config_file)
        self.settings = self.config_setting.right_contain_of_the_ini_file()


    def leave_default_value(self):
        self.config =['Output_file','Default_algorithm','Difficult_level']
        self.settings = {self.config[0]:'Txt', self.config[1]:'Norvig', self.config[2]:'Easier'}
        return self.settings

    def modify_existing_settings(self, custom_name, custom_value):
        if not custom_name:
            return self.settings
        
        elif self.exist_custom_name(custom_name) != False:
            pos = self.exist_custom_name(custom_name)
            self.settings[pos] = custom_name+":"+custom_value
            return self.settings
        else: 
            return False
            

    def add_new_custom_setting(self, new_label, new_value):
        self.settings.append(new_label+":"+new_value)
        self.config.append(new_value)
        return self.settings

    def exist_custom_name(self,custom_name):
        num_elements = len(self.config)
        i = 0
        while i < range(num_elements):
            if custom_name == self.config[i]:
                return i
            else:
                i += 1 
        return False
    
    