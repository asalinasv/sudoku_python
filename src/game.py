import cmd
# Game classes, Main module that call all the classes to play Sudoku
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import os
import sys
from Player.generators import SudokuGenerator
sys.path.append('./src/Configuration')
sys.path.append('./src/Player')

from solver import *
from commandline import *
from readconfiguration import FileReader
from storer import *
from store_setting import StorerSetting
from configuration import Configuration


class Welcome:
    
    def welcome(self):
        os.system('cls')
        print "Welcome to Sudoke game" +'\n'+"Please select an option to start"
        print "1: Menu \n2: Exit"
        value = int(raw_input())
        if value == 1:
            return Menu().menu()
        if value == 2:
            return Exit().exit()
        else:
            print "Please insert a value from the list"
            return self.welcome()

class Menu:
    
    def menu(self):
        os.system('cls')
        print '***Menu***\nPlease select an option:\n\
                1: Resolve sudoku from file\n\
                2: Resolve sudoku from command line\n\
                3: Generate sudoku\n\
                4: Configure Settings\n\
                5: Back to Welcome\n\
                6: Exit'
        value = int(raw_input())
        if value == 1:
            return FileResolver().resolvefromfile()
        if value == 2:
            return CmdResolver().resolvefromcmd()
        if value == 3:
            return SudokuGeneratorGame().generatesudoku()
        if value == 4:
            return SettingsConfiguratorDisplay("config.ini").configuresettings()
        if value == 5:
            return Welcome().welcome()
        if value == 6:
            return Exit().exit()
            
class FileResolver():
    
    def __init__(self):
        self.exit = Exit()
        
    def resolvefromfile(self):
        os.system('cls')
        print "Please insert the name of the file to resolve\n\
                or type 'exit' to exit"
        self.filer = raw_input()
        if self.filer == 'exit':
            self.exit.exit()
        else:
            return SudokuDisplayer().display(self.filer)

class SudokuDisplayer:

    def display(self,file):
        os.system('cls')
        print "Sudoku has been resolved sucessfully\n\n\n"
        solv = Solver(file)
        solv.solvesudoku()
        return
        
class CmdResolver:

    def resolvefromcmd(self):
        os.system('cls')
        cmd = CommandLine()
        cmd.solve_from_commandline()
        return

class SudokuGeneratorGame:
    '''
    Created on Jul 22, 2013
    Class to Play sudoku based on main menu or generated
    @author: Ana Salinas
    Automation Class (Sudoku project) - 2013
    '''
    path = ("../Configuration/config.ini")
    
    def generatesudoku(self):
        os.system('cls')
        print "\n\
               The 'Sudoku Game' will be generated based on the 'Difficult Level' set at configuration file "
        
        sudoku_game = SudokuGenerator(self.path)
        sudoku_game.read_file()
        return



class SudobuGame(object):

    def __init__(self):
        '''
        Constructor
        '''
    def create_sudoku_game(self):
        self.matrix = SudokuGenerator()
    
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
        
        if value == 6:
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
            
        while flag == False:
            print 'Please Insert the Default_alghoritm:\n'
            default_algorithm = str(raw_input())
            flag, message = self.validate_default_algorithm(default_algorithm)
            print message
        
        while flag == False:
            print 'Please Insert the Dificult_level:\n'
            difficult_level = str(raw_input())
            flag, message = self.validate_difficult_level(difficult_level)
            print message
        
        settings_dic = {"Output_file":output_file, "Default_alghoritm":default_algorithm, "Dificult_level":difficult_level}
        
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
            return False, "The supported algorithms are: Norvig or BackTracking and Brute Force, Please try again..."
        
class Exit:

    def exit(self):
        os.system('cls')
        print "Thanks for using Sudoku Game"
        return

if __name__ == "__main__":
    game = Welcome()
    game.welcome()

