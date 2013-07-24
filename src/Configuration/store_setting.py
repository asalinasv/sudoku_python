# StoreSetting Class , retrieve file name and settings for configuration file
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
from readconfiguration import FileReader
from configuration import Configuration
import os

class StorerSetting:
   
    def __init__(self, config_file, settings):
        self.configuration = Configuration(config_file)
        self.readfile = FileReader(config_file)
        self.storer_setting = settings

    """'save_settings_config_file' method saves the settings values in the config file"""

    def read_setting_dic(self, configuration_obj):
        num = len(configuration_obj.settings)
        cadena = ''
        ln = "\n"
        for i in range(num):
            cadena += self.configuration.settings[i]
        return cadena

    def save_txt_config_file(self):
     
        if self.readfile.file_exist() == True or self.readfile.file_exist() == False:
            f = open(self.readfile.config_file,"w")
            f.write(self.storer_setting[0]+"\n"+self.storer_setting[1]+"\n"+self.storer_setting[2])
            f.close()
        return "File Created"
    
if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) 
    path = os.path.abspath("../Configuration/config.ini")
    seting = ['Output_file:Txt\n','Default_alghoritm:Backtracking\n','Dificult_level:Easier\n']
    var = StorerSetting(path, seting)
    print var.save_txt_config_file()