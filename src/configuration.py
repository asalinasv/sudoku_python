# Configuration Class , retrieve file name and settings for configuration file
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
from readconfiguration import ReadFile
class Configuration:
    config='Output_file','Default_alghoritm','Dificult_level'
    settings = {config[0]:'Txt', config[1]:'Norvig', config[2]:'Easier'}

    
    def __init__(self,config_file,default_settings):

        self.config_file_name=config_file
        self.settings=default_settings

    def modify_existing_settings(self,config_name,custom_value):
        exist=config_name
        self.settings[config_name]=custom_value

    def add_new_custom_setting(self,new_label,new_value):
        self.settings.update({new_label:new_value})
        self.config.append(new_value)
            
class StoreSetting:
   
    def __init__(self,config_file,settings):
        self.configuration=Configuration(config_file,settings)
        self.readfile=ReadFile(config_file)

    """'save_settings_config_file' method saves the settings values in the config file"""
    def save_txt_config_file(self):
        ln="\n"
        if self.readfile.file_exist()==True or self.readfile.file_exist()==False:
            f=open(self.readfile.config_file,"w")
                
            f.write(self.configuration.config[0]+":"+self.configuration.settings[self.configuration.config[0]]+ln+self.configuration.config[1]+":"+self.configuration.settings[self.configuration.config[1]]+ln+self.configuration.config[2]+":"+self.configuration.settings[self.configuration.config[2]]+ln)
            #f.write(read_setting_dic(self.configuration))
            f.close()
        return "File Created"

    
    """Preguntar"""
    def read_setting_dic(self,configuration_obj):
        for i in len(configuration_obj.config):
            cadena+=self.configuration.config[i]+":"+self.configuration.settings[self.configuration.config[i]]+ln
        return cadena

