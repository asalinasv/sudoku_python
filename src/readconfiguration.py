# ReadConfiguration Class to read configuration file when this has is text file (.txt, .ini, .csv)
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
class FileReader():
    config_file=''

    def __init__(self,config_file):
        self.config_file=config_file

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
        if self.file_exist()==True:
            f=open(self.config_file,'r')
             
            if f.read()=="":
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
                    tag_name_setting=self.read_txt_file()
                    
                    return tag_name_setting
                

    def read_txt_file(self):
        """
        This method is to support read the plain text file and return a string with the contain on the file
        """
        f=open(self.config_file,'r')
        file_contain=''
        file_tag_name=''
  
        for l in f.readlines():
            file_contain+=str(l.strip().split("\t"))
        f.close()

        for i in range(0,len(file_contain)):
            file_tag_name+=str(file_contain[i])
 
        return file_tag_name