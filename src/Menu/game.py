import os.path
# Game classes, Main module that call all the classes to play Sudoku
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Author: Ana Salinas# Automation Class (Sudoku project) - 2013
import os
import sys

sys.path.append('./src/Configuration')
sys.path.append('./src/Player/')
from Player.generators import *
from Player.generators import SudokuGenerator
from solver.solver import Solver
from solver.commandline import CommandLine
from solver.readfiles import *
from solver.convert import *

from Player.playing_sudoku import *
from Player.sudokusavepartialgame import *
from Configuration.readconfiguration import FileReader
from solver.storer import *
from Configuration.store_setting import StorerSetting
from Configuration.configuration import Configuration
from Player.sudokusavepartialgame import *
import time

class Welcome:
    
    def welcome(self):
        if not os.path.exists('EmptySudokus'):
            os.makedirs('EmptySudokus')
        if not os.path.exists('ResolvedSudokus'):
            os.makedirs('ResolvedSudokus')
        os.system('cls')
        print "******************Welcome to Sudoke game***********************\n"+\
                '\n'+"Please select an option to start:\n"
        print "1: Menu \n2: Exit"
        try:
            value = int(raw_input())
            if value == 1:
                return Menu().menu()
            if value == 2:
                return Exit().exit()
            else:
                print "Please insert a value from the list"
                return self.welcome()
        except ValueError:
            print "Please insert a value from the list"
            return self.welcome()

class Menu:
    path = os.path.abspath("../Configuration/config.ini")
    def menu(self):
        os.system('cls')
        print '***Menu***\nPlease select an option:\n\
                1: Resolve sudoku from file\n\
                2: Resolve sudoku from command line\n\
                3: Generate sudoku\n\
                4: Configure Settings\n\
                5: Play Sudoku\n\
                6: Back to Welcome\n\
                7: Exit'
        try:
            value = int(raw_input())
            if value == 1:
                return FileResolver().resolvefromfile()
            if value == 2:
                return CmdResolver().resolvefromcmd()
            if value == 3:
                return SudokuGeneratorGame().generatesudoku()
            if value == 4:
                return SettingsConfiguratorDisplay(self.path).configuresettings()
            if value == 5:
                SudokuGameSelection() #.SudokuGameSelection()
##                return SudokuGameSelection().SudokuGameSelection()            if value == 6:
                return Welcome().welcome()
            if value == 7:
                return Exit().exit()
            else:
                return self.menu()
        except ValueError:
            return self.menu()
            
class FileResolver():
    
    def resolvefromfile(self):
        os.system('cls')
        print "Please select a file to resolve a sudoku: \n"
        print "Available files to be resolved:"
        a = os.listdir('EmptySudokus')
        for i in a:
            print i
        print "\n\nOptions:\n1:Back to Menu\n2:Exit"
        print "\n\n\nHELP: Please copy the empty sudoku files in the "+\
                os.path.abspath("EmptySudokus")+" folder to be resolved"
        self.filer = raw_input('\n')
        if self.filer == '1':
            return Menu().menu()
        if self.filer == '2':
            return Exit().exit()
        else:
            if os.path.isfile('EmptySudokus\\'+self.filer):
                self.filer = os.path.abspath('EmptySudokus\\'+self.filer)
                return SudokuDisplayer().display(self.filer)
            else:
                return self.resolvefromfile()

class SudokuDisplayer:

    def display(self,file):
        os.system('cls')
        solv = Solver(file)
        if solv.solvesudoku()== False:
            return FileResolver().resolvefromfile()
        else:
            self.matrixtosave = solv.solvesudoku()
            return self.savesudoku(self.matrixtosave)
            
    def validateoption(self):
        print "\n\nOptions:\n1:Back to Menu\n2:Exit"
        self.option = raw_input('\n')
        if self.option == '1':
            return Menu().menu()
        if self.option == '2':
            return Exit().exit()
        else:
            return self.validateoption()

    def savesudoku(self,matrix):
        absolutepath = os.path.abspath("../Configuration/config.ini")
        self.readconf = FileReader(absolutepath)
        extension = self.readconf.read_output_file()
        extension = extension.lower()
        name = raw_input("Please insert a name to store the resolved sudoku file\n")
        store = Storer(matrix,name,extension)
        store.save_matrix_to_file()
        return self.validateoption()
        
class CmdResolver:

    def resolvefromcmd(self):
        os.system('cls')
        print "Options:\n1:Back to Menu\n2:Exit\n"
        print 'Please insert a string with 81 characters to play the sudoku game : \n'
        self.string = raw_input()
        if self.string == '1':
            return Menu().menu()
        if self.string == '2':
            return Exit().exit()
        else:
            cmd = CommandLine(self.string)
            if cmd.solve_from_commandline() == False:
                time.sleep(3.0)
                self.resolvefromcmd()
            else:
                raw_input('Press any key to insert other string')
                return self.resolvefromcmd()

class SudokuGeneratorGame:
    '''
    Created on Jul 22, 2013
    Class to link with Generator class and get the sudoku matrix based on dificult level
    @author: Ana Salinas
    Automation Class (Sudoku project) - 2013
    '''
    

    def generatesudoku(self):
        """
        method to generate sudoku and give the option to store the generator sudoku (matrix) or allow the user play 
        """
        path = os.path.abspath("../Configuration/config.ini")
        os.system('cls')
        print "\n\
               The 'Sudoku Game' will be generated based on the 'Difficult Level' set at configuration file "
        
        sudoku_game = SudokuGenerator(path)
        matrix = sudoku_game.read_file()

        if len(matrix)== 9:
            print "Sudoku game created properly "
            for i in range(9):
                print matrix[i]
            
            print "Please type 'save' to storer the sudoku game in a txt file\nPlease type 'play' to star a new game"
            value = raw_input()
                
        if value.lower() == "save":
            print "Type the name of the file to store a sudoku game"
            file_name = raw_input()
            store_sudoku = Storer(matrix,file_name,"txt")
            store_sudoku.save_matrix_to_file()
            
            return Menu().menu()
        elif value.lower() == "play":
             '''call to playing sudoku to start the game

             '''
             self.play = MenuPlay(matrix)
             self.play.menu()
             return
class SudokuGameSelection(object):
    """
    Class to allow user play a sudoku game from 
    1 = generated game or
    2 = load sudoku file
    """
    def __init__(self):
        os.system('cls')
        print '***Menu***\nPlease select an option:\n\
               1: Generate a sudoku game\n\
               2: Select a sudoku game from a existing file\n\
               3: Back to main menu\n'
        value = int(raw_input())
        if value == 1:
            return SudokuGeneratorGame().generatesudoku()
        if value == 2:
            self.open_existing_file()
        if value == 3:
            return Menu().menu()
        
    def select_existing_Sudoku(self):
        pass
    
    def select_sudoku_from_generator(self):
        pass
    
    def open_existing_file(self):
        self.display_file = FileDisplayer() # show the list of files
        self.display_file.list_files()
        self.convert = GeneralConverter()
        new_file = raw_input("Enter the name of new sudoku game: ")
        if os.path.isfile('EmptySudokus\\'+new_file): # validate when does not exist a file
            new_file = os.path.abspath('EmptySudokus\\'+new_file)
        else:
             print "The file does not exist"
             return self.open_existing_file()
        self.read_file = SudokuFileReader(new_file) # read the file
        type_file = self.read_file.gettype() #verify the type of file csv or txt

        if type_file == "TXT File":
           self.read_file.reading_txt()
           matrix_loaded = self.convert.convert_txt_file_to_matrix(new_file)
        elif type_file == "CSV File":
             self.read_file.reading_csv()
             string_file = self.convert.convert_csv_file_to_string(new_file)
             matrix_loaded = self.convert.convert_string_to_matrix_int(string_file)
        else:
             return #type_file

        self.play = MenuPlay(matrix_loaded) # Call to interactive game
        self.play.menu()




class FileDisplayer():
      def list_files(self):
           a = os.listdir('EmptySudokus')
           for i in a:
               print i
class SudokuGame:
    
    def __init__(self):
        '''
        Constructor
        '''
    def create_sudoku_game(self):
        self.matrix = SudokuGenerator()
    
    def play_sudoku(self,matrix):
        pass
    
    def print_sudoku_game(self):
        pass
    
    def validate_editable_cells(self):
        pass
        
class SettingsConfiguratorDisplay:
    legend = "\nThis is the current setting values of configuration file:\n"
    setting_menu = "\nPlease select the option to modify any value or leave by default\n"
    path = ("../Configuration/config.ini")
    
    read_file_setting = ""
    def __init__(self, config_file):
        self.read_file_setting = FileReader(self.path)
                
    def configuresettings(self):
        os.system('cls')
        print self.legend
        value_setting = self.read_file_setting.read_txt_file()
        
        for i in range(len(value_setting)):
                       print value_setting[i]
        self.sub_menu_setting()
        
    def sub_menu_setting(self):
        
        print self.setting_menu
        print '\
                1: Leave By default\n\
                2: Modify Setting Values\n\
                3: Back To Main Menu\n'
        
        value = int(raw_input())
        if value == 1:
            return Menu().menu()
        
        if value == 2:
            return SaveSetting().save_all_setting_in_file(self.path)
        
        if value == 3:
            return Menu().menu()
        

class SaveSetting:
    
    def save_setting_in_file(self, path):
        os.system('cls')
        print '\n\
               Insert the new output file format Txt, or Csv\n'
        value = int(raw_input()) 
    
    def save_all_setting_in_file(self, path):
        os.system('cls')
        flag = False
        
        while flag == False: 
            print 'Please Insert the Output_file:\n'
            output_file = str(raw_input())
            flag, message = self.validate_outputfile(output_file)
            print message
        
        flag = False  
        while flag == False:
            print 'Please Insert the Default_alghoritm:\n'
            default_algorithm = str(raw_input())
            flag, message = self.validate_default_algorithm(default_algorithm)
            print message
            
        flag = False
        while flag == False:
            print 'Please Insert the Dificult_level:\n'
            difficult_level = str(raw_input())
            flag, message = self.validate_difficult_level(difficult_level)
            print message
        
        settings_dic = ["Output_file:"+output_file, "Default_alghoritm:"+default_algorithm, "Dificult_level:"+difficult_level]
        
        save_setting = StorerSetting(path, settings_dic)
        save_setting.save_txt_config_file()
        return Menu().menu()

    def validate_outputfile(self, output):
        if output.lower() == "txt" or output.lower() == "csv":
            return True, ""
        else:
            return False, "The supported formats are: Txt or Csv, Please try again..."
        
    def validate_default_algorithm(self, default):
        if default.lower() == "norvig" or default.lower() == "backtracking" or default.lower() == "brute force":
            return True, ""
        else:
            return False, "The supported algorithms are: Norvig or BackTracking and Brute Force, Please try again..."
        
    def validate_difficult_level(self, difficult):
        if difficult.lower() == "easier" or difficult.lower() == "medium" or difficult.lower() == "difficult":
            return True, ""
        else:
            return False, "The supported algorithms are: Easier, Medium or Difficult Please try again..."
        
class Exit:

    def exit(self):
        os.system('cls')
        print "Thanks for using Sudoku Game"
        return

if __name__ == "__main__":
    game = Welcome()
    game.welcome()



