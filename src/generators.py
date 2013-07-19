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


class SudokuGenerator:
    '''
    Generator class will create new sudoku games, based on already stored files
    '''
    level = ''
    files = []
    path_easy = os.path.realpath('Sudoku_Levels/Easy/') #os.path.abspath('Sudoku_Levels/Easy/')
    path_medium = 'Sudoku_Levels/Medium/'
    path_hard = 'Sudoku_Levels/Hard/'
    
    def __init__(self,config_file):
        '''
        Constructor: define which is the difficult level set by the user at config.ini file
        '''
        self.readfile = FileReader(config_file)
        self.level = self.readfile.read_dificult_level()
        
    def retrieve_file_names(self):
        """
        retrieve_file_names method retrieves all file names stored based on difficult level
        """

        if self.level.strip()== "Easier":
            self.files = [f for f in os.listdir(self.path_easy) if f.endswith('.txt')]
            return self.files
                  
        elif self.level.strip()== "Medium":
            self.files = [f for f in os.listdir(self.path_medium) if f.endswith('.txt')]
            return self.files
        
        elif self.level.strip()== "Difficult":
            self.files = [f for f in os.listdir(self.path_hard) if f.endswith('.txt')]
            return self.files
        
        else:
            return "There is not Sudoku game for this difficult level"
    
    def select_file(self):
        file_list = self.retrieve_file_names()
        num_files = len(file_list)
        num_f = randint(0, num_files-1)
        return file_list[num_f]
       
    def read_file(self):
        
        value = []
        files = self.select_file()
        if self.level.strip() == "Easier":
            f=open(self.path_easy+'/'+files,'r')
            value = f.readlines()
            f.close()
        if len(value) == 9:
            return value
        
if __name__ == "__main__":
  
    var = SudokuGenerator("config.ini")
    matrix = var.read_file()
    
    print matrix