# ReadConfiguration Class to read configuration file when this has is text file (.txt, .ini, .csv)
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
import os

class FileReader():
    config_file=''
 
    def __init__(self,config_file):
        self.config_file = config_file
     
    def get_name_label(self,config):
        """
        method to retrieve the name of the setting in config file
        """
        var = config.split(":")
        return var
          
    def read_output_file(self):
        """
        method to retrieve the output type
        """
        content = self.right_contain_of_the_ini_file()
       
        for i in range(len(content)):
            value = self.get_name_label(content[i])
            if value[0] == "Output_file":
                return value[1].strip()
                
                       
    def read_default_algorithm(self):
        """
        method to retrieve the name algorithm defiend on config file
        """
        content = self.right_contain_of_the_ini_file()
       
        for i in range(len(content)):
            value = self.get_name_label(content[i])
            if value[0] == "Default_alghoritm":
                return value[1].strip() 
    
    def read_dificult_level(self):
        """
        method to retrieve the difficult level in config file
        """
        content = self.right_contain_of_the_ini_file()
       
        for i in range(len(content)):
            value = self.get_name_label(content[i])
            if value[0] == "Dificult_level":
                return value[1].strip()
    
    def file_exist(self):
        """"
        'file_exist' method verifies that config file exist or not and raise an error it it does not exist
        """

        try:
            f=open(self.config_file,'r')
            f.read()
            f.close()
            return True
            
        except IOError:
       
            return IOError

    def file_is_empty(self):
        """
        file_is_empty method verifies that file is not empty
        """
        if self.file_exist()== True:
            f=open(self.config_file,'r')
             
            if f.read() == "":
                print f.read()
                print "is Empty"
                f.close()
                return True
            else:
                f.close()
                return False
                                     
    def right_configuration_extension(self):
        """
        This method verifies that file has the right extension
        """
        file_name=[]
    
        if self.file_exist():
            
            #Identify the file type, file_name has the name of the file [0] and [1] the extension
            file_name=self.config_file.split('.',1)
             
            if file_name[1]=='txt' or file_name[1]=='ini':# or file_name[1]=='csv':
                return True

            return False
                        
    def right_contain_of_the_ini_file(self):
        """
        Method to verify that contain of the configuration file has the right info
        """
        tag_name_setting = []
            
        if self.file_exist():
            if self.file_is_empty() == False:
                if self.right_configuration_extension() == True:
                    tag_name_setting = self.read_txt_file()
                
                    return tag_name_setting
            return "The File is empty"
        return "The file does not exist"
    
    def read_txt_file(self):
        """
        This method is to support read the plain text file and return a string with the contain on the file
        """
        f = open(self.config_file,'r')
        file_contain = f.readlines()
        f.close()
        
        return file_contain

if __name__ == "__main__":
    var = FileReader("config.ini")
    print var.right_contain_of_the_ini_file()
    print var.read_default_algorithm() 
