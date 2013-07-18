import cmd
# Game classes, Main module that call all the classes to play Sudoku
# Author: Oscar Walker Tapia Merida - oscar.tapia@jalasoft.com
# Automation Class (Sudoku project) - 2013

import os
from solver import *
from commandline import *
from readconfiguration import *
from storer import *

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
            return SudokuGenerator().generatesudoku()
        if value == 4:
            return SettingsConfigurator().configuresettings()
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

class SudokuGenerator:

    def generatesudoku(self):
        os.system('cls')
        print "\n\n ********** Under construction ****************"
        return

class SettingsConfigurator:

    def configuresettings(self):
        os.system('cls')
        print "*** Under COnstruction ***"
        return


class Exit:

    def exit(self):
        os.system('cls')
        print "Thanks for using Sudoku Game"
        return

if __name__ == "__main__":
    game = Welcome()
    game.welcome()
