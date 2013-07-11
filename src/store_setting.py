# StoreSetting Class , retrieve file name and settings for configuration file
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
from readconfiguration import FileReader
from configuration import Configuration

class StorerSetting:
   
    def __init__(self, config_file, settings):
        self.configuration = Configuration(config_file, settings)
        self.readfile = FileReader(config_file)

    """'save_settings_config_file' method saves the settings values in the config file"""

    def read_setting_dic(self, configuration_obj):
        num = len(configuration_obj.settings)
        cadena = ''
        ln = "\n"
        for i in range(num):
            cadena += self.configuration.config[i]+":"+self.configuration.settings[self.configuration.config[i]]+ln
        return cadena

    def save_txt_config_file(self):
     
        if self.readfile.file_exist() == True or self.readfile.file_exist() == False:
            f = open(self.readfile.config_file,"w")
                
            #f.write(self.configuration.config[0]+":"+self.configuration.settings[self.configuration.config[0]]+ln+self.configuration.config[1]+":"+self.configuration.settings[self.configuration.config[1]]+ln+self.configuration.config[2]+":"+self.configuration.settings[self.configuration.config[2]]+ln)
            f.write(self.read_setting_dic(self.configuration))
            f.close()
        return "File Created"