# ReadConfiguration Class to read configuration file when this has is text file (.txt, .ini, .csv)
# Author: Ana Salinas
# Automation Class (Sudoku project) - 2013
class ReadFile():
    config_file=''


    def __init__(self,config_file):
        self.config_file=config_file

    """file_exist' method verifies that config file exist or not and raise an error it it does not exist"""
    def file_exist(self):
        try:
            f=open(self.config_file,'r')
            f.read()
            return True
            f.close()
        except IOError:
       
            return False

    def file_is_empty(self):
        if self.file_exist()==True:
            f=open(self.config_file,'r')
             
            if f.read()==" ":
                return True
            else:
                return False
                                
            f.close()
     

    """read_config_file method read the config file to recover configruation values"""
  

    def right_configuration_format(self):

        tag_name_setting=[]
        tag_name_values=[]
        file_name=[]
    
        if self.file_exist():
            if self.file_is_empty()==False:
                #Identify the file type, file_name has the name of the file [0] and [1] the extension
                file_name=self.config_file.split('.',1)
               
                if file_name[1]=='txt' or file_name[1]=='ini' or file_name[1]=='csv':
                    tag_name_setting=self.read_txt_file()
                    
                if file_name[1]=='xml':
                    tag_name_setting=self.read_xml_file()
        return tag_name_setting
                    
    
    def read_txt_file(self):
        f=open(self.config_file,'r')
        file_contain=''
        file_tag_name=''
  
        for l in f.readlines():
            file_contain+=str(l.strip().split("\t"))
        f.close()

        for i in range(0,len(file_contain)):
            file_tag_name+=str(file_contain[i])

 
        return file_tag_name
