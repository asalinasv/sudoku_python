""" Created on Jul 17, 2013 
    Generator Class , class and methods to generate sudokus based on difficult level
    @author: Ana Salinas
    Automation Class (Sudoku project) - 2013
"""
import os
import sys
sys.path.append('./src/Configuration')

from readconfiguration import FileReader
from random import randint
from solver.convert import GeneralConverter

class SudokuGenerator:
    '''
    Generator class will create new sudoku games, based on already stored files
    '''
    level = ''
    files = []
    script_dir = os.path.dirname(__file__) 
    path_easy = os.path.join(script_dir, "Sudoku_Levels/Easy/")
    path_medium = os.path.join(script_dir,'Sudoku_Levels/Medium/')
    path_hard = os.path.join(script_dir,'Sudoku_Levels/Hard/')
    
    def __init__(self,config_file):
        '''
        Constructor: define which is the difficult level set by the user at config.ini file
        '''
        self.readfile = FileReader(config_file)
        self.level = self.readfile.read_dificult_level().lower()
                        
    def retrieve_file_names(self):
        """
        retrieve_file_names method retrieves all file names stored based on difficult level
        """
        if not self.level:
            return "No Setting"
        
        else:
            if self.level.strip() == "easier":
                self.files = [f for f in os.listdir(self.path_easy) if f.endswith('.txt')]
                return self.files
                      
            elif self.level.strip() == "medium":
                
                self.files = [f for f in os.listdir(self.path_medium) if f.endswith('.txt')]
                return self.files
            
            elif self.level.strip() == "difficult":
                self.files = [f for f in os.listdir(self.path_hard) if f.endswith('.txt')]
                return self.files
            
            else:
                return "There is not Sudoku game for this difficult level"
    
    def select_file(self):
        """
        Select any file from the relevant difficult set in the configuration file and return a list
        """
        file_list = self.retrieve_file_names()
              
        if file_list != "No Setting":
            num_files = len(file_list)
            num_f = randint(0, num_files-1)
            return file_list[num_f]
        else: 
            return "No Setting"
       
    def read_file(self):
        """
        Read the selected file from the list to display
        """
        value = []
        files = self.select_file()
        converter = GeneralConverter()
        
        if files == 'No Setting':
            return files
        
        elif self.level.strip() == "easier":
            value = converter.convert_txt_file_to_string(self.path_easy+'/'+files)
  
        elif self.level.strip() == "medium":
            value = converter.convert_txt_file_to_string(self.path_medium+'/'+files)
            
        elif self.level.strip() == "difficult":
            value = converter.convert_txt_file_to_string(self.path_hard+'/'+files)
        if len(value) == 81:
            return converter.convert_string_to_matrix(value)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) 
    #path = os.path.join(script_dir, "../src/Configuration/config.ini")
    path = os.path.abspath("../Configuration/config.ini")
    #path = ("../Configuration/config.ini")
    print path
    var = SudokuGenerator(path)
    print var.read_file()
